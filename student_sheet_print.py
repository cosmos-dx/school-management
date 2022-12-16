#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

from rmsvalidators import *
import config
import rmss_config
from config import MONTHS_HEADINGS
import subprocess
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter,landscape, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus.flowables import Image, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.platypus.paragraph import Paragraph

from PyPDF2 import PdfFileWriter, PdfFileReader
from io import StringIO
from reportlab.pdfgen import canvas
import os, platform
        
class Sheet_Print(Frame):
    def __init__(self, parent, sptag, spnum, buttonidx, gpar, whxy, **kw):
    
        Frame.__init__(self, parent)
        self.rscr = kw['rscr']
        self.ftsz = int(self.rscr['sysfontnum'])
        self.spnum = spnum
        self.sptag = sptag
        self.gpar = gpar
        self.whxy = whxy
        self.buttonidx = buttonidx
        self.fyear = self.rscr['fyear']
        self.today = self.rscr['today']
        self.daterange = self.rscr['daterange']
        self.leftpadd = 20 ### padding for left side of Frame
        self.kdk = -1
        try:
            self.master.iconbitmap(self.rscr['rmsicon'])
        except Exception as err:
            StatusDP(self.status, 'Error Found [%s]'%str(err), 'red')
        self.initUI()
        
    def initUI(self):
        self.master.title(self.sptag.title())
        wminwidth = 12
        wmaxcolumn = 15
        wmaxrows = 20
        wrow = 1
        self.tcount = 0
        lfnt_fg_bg = {'font': ['Calibri', self.ftsz, 'normal'], 'bg': 'SystemButtonFace', 'fg': 'black'}
        lfntfg_bgg = {'font': ['Calibri', sum([self.ftsz,2]), 'normal'],'bg': 'SystemButtonFace', 'fg':'blue'}
        bfnt_fg_bg = {'font':['Times New Roman Bold',self.ftsz,'bold'],'bg':'OliveDrab1','fg':'black'} ###self.rscr['font']['button']
        combx_fnt = {'font': ['Courier', self.ftsz, 'bold'],}
        chk_fg_bg = {'font': ['Calibri', self.ftsz, 'normal'], 'bg': 'SystemButtonFace', 'fg': 'black','relief':'raised'}
        efnt_fgbg = {'font': ['Courier', self.ftsz, 'bold'], 'bg':'#b0e0e6', 'fg': 'black'}
        efnt_fg_bg = {'font':['Courier',self.ftsz,'bold'],'bg':'#b0e0e6','fg':'black','bd':2}
        
        if self.whxy:
            self.master.geometry('%dx%d+%d+%d' % self.whxy)
        else:
            self.master.geometry('%dx%d+%d+%d' % (wsw, wsh, xpos, ypos))
        
        self.top = RMS_LABEL(self.master, text=self.sptag.title(), **lfntfg_bgg)
        self.top.grid(row=wrow, column=0, rowspan=1, columnspan=11, sticky='nwes')
        wrow += 1
        
        conf = config.Configuration()
        session_start = conf.SESSION()
        mval = int(session_start)-1
        ####mkey =  {1:'JANUARY',2:'FEBRUARY',3:'MARCH',4:'APRIL',5:'MAY',6:'JUNE',7:'JULY',8:'AUGUST',9:'SEPTEMBER',10:'OCTOBER',11:'NOVEMBER',12:'DECEMBER'}
        
        mkey = MONTHS_HEADINGS()
        mlist = []
        for s in range(int(14)):
            dicint =  s+1
            mval = mval +1
            if mval < 13:
                months =  mkey[mval]
            else:
                nmval = mval - 12
                months =  mkey[nmval]
            if dicint > 12 :
                months = mkey[dicint]
            mlist.append(months)

        self.headmrg = int(conf.HEAD_MARGIN())
        self.footmrg = int(conf.FOOT_MARGIN())
        self.leftmrg = int(conf.LEFT_MARGIN())
        self.rightmrg = int(conf.RIGHT_MARGIN())
        self.extndmrg = int(conf.EXTEND_MARGIN())
        self.topMargin = int(self.extndmrg)*int(self.headmrg)

        self.name_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.name_tx.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w')
        self.phone_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.phone_tx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.class_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.class_tx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.date_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.date_tx.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        self.studid = ''
        wrow += 1
        self.father_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.father_tx.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w')
        self.teacher_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.teacher_tx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.class_sec_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.class_sec_tx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.remark_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.remark_tx.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        gbd, gbg, gfg, gfont,wd = 1, 'white', 'blue', ('Courier', self.ftsz, 'normal'),8
        ### Month name must be given in 3 Char Format further used in key value format
        ### {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUNE', 7: 'JULY', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC', 13: 'H-Yrly', 14: 'Annual'}
        gcolconf = {0:{'vcmd':'F','idname':'0','text':'','width':1,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           1:{'vcmd':'F','idname':'1','text':'APR','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',}, 
           2:{'vcmd':'F','idname':'1','text':'MAY','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           3:{'vcmd':'F','idname':'2','text':'JUNE','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           4:{'vcmd':'F','idname':'3','text':'JULY','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           5:{'vcmd':'F','idname':'4','text':'AUG','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           6:{'vcmd':'AN','idname':'5','text':'SEP','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           7:{'vcmd':'F','idname':'6','text':'OCT','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           8:{'vcmd':'F','idname':'7','text':'NOV','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           9:{'vcmd':'F','idname':'8','text':'DEC','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           10:{'vcmd':'F','idname':'9','text':'JAN','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           11:{'vcmd':'F','idname':'10','text':'FEB','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           12:{'vcmd':'AN','idname':'11','text':'MAR','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           13:{'vcmd':'AN','idname':'12','text':'H-Yrly','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           14:{'vcmd':'AN','idname':'13','text':'Annual','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},}
        
        rows = 20
        coln = 13 ##len(colconf)
        sbar = {'vsb':{'row':wrow,'column':coln,'rowspan':rows,'columnspan':1,'sticky':'ns',},
                'hsb':{'row':sum([rows,1]),'column':0,'rowspan':rows,'columnspan':rows,'sticky':'we',},
                'cnv':{'row':wrow,'column':0,'rowspan':rows,'columnspan':coln,'sticky':'news',},}
                   
        grid_fg_bg = {'sbar': sbar} 
        self.grid = RMSGRID(self.master, self, wrow, rows, 0, gcolconf, True, srn_width=12, **grid_fg_bg)
        wrow += rows
        
        self.hz_gp = RMS_LABEL(self.master, **lfntfg_bgg)
        self.hz_gp1 = RMS_LABEL(self.master, **lfntfg_bgg)
        self.hy_tot = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.hy_tot.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w')
        self.an_tot = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.an_tot.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')

        self.max_mks_ps_ = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.max_mks_ps_.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.max_mks_ps = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.max_mks_ps.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        self.max_mks_tx_ = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.max_mks_tx_.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w')
        self.max_mks_tx = RMS_ENTRY(self.master, **efnt_fg_bg)
        self.max_mks_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        

        wrow += 1
        self.ok = RMS_BUTTON(self.master, text='PRINT', bd=3,
                                command=self.OnPrint, **bfnt_fg_bg) 
        self.ok.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.close = RMS_BUTTON(self.master, text='Close', bd=3,
                                command=self.OnClose, **bfnt_fg_bg) 
        self.close.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        self.status = RMS_LABEL(self.master, text='', **lfnt_fg_bg)
        self.status.grid(row=wrow, column=1, rowspan=1, columnspan=15)
        wrow += 4
        
        for r in range(wrow):
            self.master.rowconfigure(r, weight=1)
        for r in range(15):
            self.master.columnconfigure(r, weight=1)
        self.name_tx.bind('<Key>', self.name_enter)
        self.remark_tx.bind('<Key>', self.remark_enter)
        self.remark_tx.bind("<FocusIn>", self.remark_set_focus)
        self.remark_tx.bind("<FocusOut>", self.remark_kill_focus)
        #self.RefreshEntryBG(self.class_entry_cb, self.class_entry_cb)
        
    def name_enter(self, event):
        self.remark_tx.SetFocus()
        event.Skip()
    def remark_enter(self, event):
        self.ok.SetFocus()
        self.hy_an_tot()
    def remark_set_focus(self, event):
        self.hy_an_tot()
    def remark_kill_focus(self, event):
        self.hy_an_tot()
    def NextFocus(self, event, currwdg, nxtwdg):
        text = currwdg.GetValue()
        if event.keysym in ['Return', 'Tab']:
            if text.strip() == '':
                return
            self.Total_Fee()
            self.RefreshEntryBG(currwdg, nxtwdg)
        if event.keysym in ['Escape','End']:
            self.RefreshEntryBG(currwdg, self.class_entry_cb)
            
    def ResetAllEntry(self, resetcolor = 'white'):
        for k, v in self.widdict.items():
            try:
                k['bg'] = resetcolor
            except:
                pass
            
    def RefreshEntryBG(self, curentry, nextentry, resetcolor='white', mycolor='yellow', f=True):
        self.lastactiveentry = curentry
        if f:
            try:
                self.lastactiveentry['bg'] = resetcolor
            except:
                pass
            try:
                nextentry['bg'] = mycolor
            except:
                pass
            nextentry.SetFocus()
        else:
            self.ResetAllEntry(resetcolor=resetcolor)
            curentry['bg'] = mycolor

    def GetLCSelectData(self, ridx, data, evtname):
        row, col, wdg = ridx
        if evtname == 'Return':
            print ('Sheet_Print , key inputs line 213')
    def OnClose(self, event=None):
        self.click = True
        mess = RMSMBX(self.master, text="\nWANT to EXIT ??\n", info=False, pos=(500,350),
                          size=(220, 130),textclr='white', bg='black')
        if mess.result:
            self.master.destroy()
            try:
                self.gpar.btnlst[self.buttonidx]['state']='normal'
                self.gpar.btnlst[self.buttonidx]['relief']='raised'
            except Exception as err:
                pass
        else:
            self.master.focus()
            if event:
                event.widget.focus()

    def OnPrint(self, event=None):
        self.ok.SetLabel('Wait..!')
        conf = config.Configuration()
        otest = self.rscr['config']['outoff'] ###conf.OUTOFF_LIST()
        
        mnth, hlfy, annl = otest[0],otest[1],otest[2]
        hyanm = conf.ANNUAL_HY_MONTH()
        #hfyrly, annualy = hyanm[0],hyanm[1]
        HY_AN_key = self.rscr['config']['monthhead'] ###config.MONTHS_HEADINGS()  
        hfyrly = HY_AN_key[int(hyanm[0])]
        annualy = HY_AN_key[int(hyanm[1])]
            
        slogan = self.rscr['config']['monthhead'] ###conf.SLOGAN()
        pdf_style = self.rscr['config']['pdfs1'] ### conf.PRINT_PDF_STYLE()
        #cls_val = Combox_Val(self, self.class_tx.GetValue().strip())
        cls_val = 1
        if int(cls_val) > 5:
            ROWHT = [25]
            row = int(self.rscr['config']['subjectrowhigh']) ###int(conf.SUBJECTS_ROW_HIGHER())
            fntsize = int(self.rscr['config']['fontsize_h']) ###int(conf.HEIGHER_CLASS_FONT_SIZE())
            rgapsize = 0
        else:
            ROWHT = [40]
            row = int(self.rscr['config']['subjectrowlow']) ###int(conf.SUBJECTS_ROW_LOWER())
            fntsize = int(self.rscr['config']['fontsize_l']) ###int(conf.LOWER_CLASS_FONT_SIZE())
            rgapsize = 10
        if int(cls_val) > 50  :
            ROWHT = [40]
            row = int(self.rscr['config']['subjectrowlow']) ###int(conf.SUBJECTS_ROW_LOWER())
            fntsize = int(self.rscr['config']['fontsize_l']) ###int(conf.LOWER_CLASS_FONT_SIZE())
            rgapsize = 10
        
        if pdf_style == '1':
            self.OnPrint_Style_1(event,mnth, hlfy, annl, hfyrly, annualy)
        if pdf_style == '2':
            self.OnPrint_Style_2(event,mnth, hlfy, annl, hfyrly, annualy, ROWHT, row, fntsize, rgapsize)
        self.ok.SetLabel('Printing')

    def COL_HEADING_VALUES(self):
        rdet = []
        rdet.append('Subjects')
        for cl in range(14):  ### Actual Col is 14 , SUBJECT (col) + '' (Blank Col) Total = 16
            colval = self.grid.GetColLabelValue(cl)
            rdet.append(colval)
        rdet.append('')
        return rdet
    def PDF_HEADING1(self, SimpleDocTemplate, A4, getSampleStyleSheet, ParagraphStyle, Paragraph, Spacer, StringIO, TA_JUSTIFY,fntsize, rgapsize):
        from rmss_config import OWNER_DETAILS
        packet = StringIO()
        #doc = SimpleDocTemplate(packet,pagesize=A4,
        #                    rightMargin=0,leftMargin=4,
        #                    topMargin=150,bottomMargin=10)
        ##print self.headmrg,self.footmrg, self.leftmrg,self.rightmrg , self.extndmrg
        doc = SimpleDocTemplate(packet,pagesize=A4,
                                rightMargin=self.rightmrg,leftMargin=self.leftmrg,
                                topMargin=self.topMargin,bottomMargin=self.footmrg)
        Story=[]
        
        
        dtsess = self.rscr['daterange']
        
        dtsesf, dtsest = dtsess[0], dtsess[1]
        dtfm = str(dtsesf).split('-')[0]
        dtto = str(dtsest).split('-')[0]
        yrsession = str(dtfm)+'-'+str(dtto)
        
        phone = self.phone_tx.GetValue()
        owner, o_add1, o_add2, pphone = OWNER_DETAILS()
        #try:
        static_sp = 135 * "-"
        blank_space0 = '&nbsp'*122
        blank_space0_1 = '&nbsp'*85
        blank_space1 = '&nbsp'*2
        ptitl_ = "MARK SHEET %s (%s)" %(blank_space1, yrsession)       
        #I = Image('mylogo.jpg')
        #I.drawHeight = 1.30*inch*I.drawHeight / I.drawWidth
        #I.drawWidth = 1.70*inch
        ##im = Image.open("/School_RMS/ATP.gif")
        styles=getSampleStyleSheet()
        ##styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY)) # (name='Center', alignment=TA_CENTER)
        styles.add(ParagraphStyle( name="Justify", fontSize=3, alignment=TA_JUSTIFY, fontName="Courier"))
        phonetl = ('<para align=center ><font size=%s> %s </font></para>' % (str(fntsize+2),pphone))
        Story.append(Paragraph(phonetl, styles["Normal"]))
        Story.append(Spacer(1, (1+rgapsize)))
        ptitle = ('<para align=center ><font size=%s>  %s </font></para>' % (str(fntsize+2), ptitl_))
        Story.append(Paragraph(ptitle, styles["Normal"]))
        Story.append(Spacer(1, (-1+rgapsize)))
        
        ################################################################################################
        product_table = []
        
        COLWDTH = [50,0,35,35,35,35,35,35,35,35,35,35,35,40,40,40,30]
        #except (IOError,ValueError), e: 
        #    wx.MessageBox("ERROR %s"%e, "Export File Already OPEN or Nothing to Print", wx.ICON_INFORMATION)
        #    return
        return  packet, doc, Story, styles, product_table, COLWDTH, static_sp, blank_space0, blank_space0_1, blank_space1, ptitl_
    
    def PDF_BODY1(self,static_sp,Story,Paragraph,styles,Spacer,blank_space1,Table,colors,COLWDTH,ROWHT,TableStyle,product_table,row,fntsize, rgapsize):
        date = self.date_tx.GetValue()
        cls_det = self.class_tx.GetValue()+'-'+self.class_sec_tx.GetValue().strip()
        fatherstx =  "Father's Name :"
        father = self.father_tx.GetValue()
        name_stx = "Student's Name :"
        name_tx = self.name_tx.GetValue()
        phone = self.phone_tx.GetValue()
        teacher = self.teacher_tx.GetValue()
        studid = self.studid
        std_perf = self.remark_tx.GetValue()
        
        ptext_body_static_line_0 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
        Story.append(Paragraph(ptext_body_static_line_0, styles["Normal"]))
        Story.append(Spacer(1, -8))
    
        ptext_body_static_line_1 = ('''<para align=left spaceb=3><font size=10><font name=Courier>
         %s %s <font name=Courier-Bold> %s , </font><font name=Courier>
         %s, %s </font><font name=Courier-Bold> %s </font>Phone : %s </font></font></para>
         ''' % (blank_space1,name_stx,name_tx,cls_det,fatherstx,father,phone))
        Story.append(Paragraph(ptext_body_static_line_1, styles["Normal"]))
        Story.append(Spacer(0, (5+rgapsize)))
        ##rdet = 'SUBJECTS','April','May','June','July','August','Sept.','Oct.','Nov.','Dec.',\
        ##       'Jan.','Feb.','Mar.','H-Yrly','Annual',''
        ##pitem1 = [rdet]
        pitem1 = [self.COL_HEADING_VALUES()]
        ##pitem1 = [['Subjects', '', 'APR', 'MAY', 'JUNE', 'JULY', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'JAN', 'FEB', 'MAR', 'H-Yrly', 'ANNN']]
        t1 = Table(pitem1, colWidths=COLWDTH,
                       rowHeights=ROWHT,style=None)
        t1.setStyle(TableStyle([
            ('FONTSIZE',(0,0),(-1,-1),fntsize),
            ('TEXTFONT',(0,0),(-1,-1),'Courier-Bold'),
            ('BOX', (0,0), (14,0), 0.25, colors.black), ### IN RIGHT TUPEL LEFT int is for boxes black colour 
            #('BOX', (0,1), (-1,1), 0.25, colors.white),
            ('INNERGRID', (0,0), (14,0), 0.25, colors.black),
            #('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('ALIGN', (0,0), (-1,-1), 'LEFT')]))
        Story.append(t1)
        Story.append(Spacer(0, (0.5+rgapsize)))
        
        for r in range(0, row):   
            item = []
            item.append(self.grid.GetRowLabelValue(r))
            item.append(self.grid.GetCellValue(r, 0))
            item.append(self.grid.GetCellValue(r, 1))
            item.append(self.grid.GetCellValue(r, 2))
            item.append(self.grid.GetCellValue(r, 3))
            item.append(self.grid.GetCellValue(r, 4))
            item.append(self.grid.GetCellValue(r, 5))
            item.append(self.grid.GetCellValue(r, 6))
            item.append(self.grid.GetCellValue(r, 7))
            item.append(self.grid.GetCellValue(r, 8))
            item.append(self.grid.GetCellValue(r, 9))
            item.append(self.grid.GetCellValue(r, 10))
            item.append(self.grid.GetCellValue(r, 11))
            item.append(self.grid.GetCellValue(r, 12))
            item.append(self.grid.GetCellValue(r, 13))
            item.append('')
            product_table.append(item)
            for n, i in enumerate(item):
                if i == '0.00':
                    item[n] = ''
                if i == '0.0':
                    item[n] = ''
        return product_table

    def ProductTable(self,static_sp,Story,Paragraph,styles,Spacer,blank_space1,Table,colors,COLWDTH,ROWHT,TableStyle,product_table,i,fntsize,rgapsize):
        #for i in range(len(product_table)):
                
                try:
                    pitem2 = [product_table[i]]
                    t2 = Table(pitem2, colWidths=COLWDTH,rowHeights=ROWHT)
                    t2.setStyle(TableStyle([
                    ('FONTSIZE',(0,0),(-1,-1),fntsize),
                    ('FONTNAME',(0,0),(-1,-1),'Courier-Bold'),
                    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ('FONTSIZE',(0,18), (-1,-1),fntsize),
                    ('FONTNAME', (0,18), (-1,-1), 'Courier'),
                    #('TEXTCOLOR',(0,18), (-1,-2),colors.green),
                    #('TEXTCOLOR',(0,19), (-1,-1),colors.red),
                    ('FONTSIZE',(0,19), (-1,-1),(fntsize+1)),
                    ('FONTNAME',(0,19), (-1,-1),'Courier-Bold'),
                    #('INNERGRID', (0,0), (-1,0), 0.25, colors.black)
                    ]))
                except IndexError:
                        pass
                Story.append(t2)        
                Story.append(Spacer(0.001, (0.001+rgapsize)))
                return Story
    def PDF_BOTTOM1(self, Story, Paragraph, styles, Spacer, static_sp, mnth, hlfy, annl, hfyrly, annualy, bott_sg,fntsize,rgapsize):
            blank_space2 = '&nbsp'*120
            blank_space3 = '&nbsp'*30
            ptext_body_static_line_5 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
            Story.append(Paragraph(ptext_body_static_line_5, styles["Normal"]))
            Story.append(Spacer(1, -1))
            
            hy_tot = self.hy_tot.GetValue()
            ann_tot = self.an_tot.GetValue()
            #hy_tot,ann_tot = 222,444
            ptext_6 = ('''<font size=6><font name=Courier>%s<font size=11><font name=Courier-Bold>%s</font></font>
                        &nbsp  &nbsp <font size=11><font name=Courier-Bold>%s</font>
                        </font></font></font>''' % (blank_space2,hy_tot,ann_tot))
            Story.append(Paragraph(ptext_6, styles["Normal"]))
            Story.append(Spacer(1, (1+rgapsize)))
            anval = (self.max_mks_ps_.GetValue())+" "+(self.max_mks_ps.GetValue())+" ; "+(self.max_mks_tx_.GetValue())+" "+(self.max_mks_tx.GetValue())
            ptext_6_1 = ('''<font size=6><font name=Courier>%s<font size=11><font name=Courier-Bold> %s </font></font>
                        <font size=11><font name=Courier-Bold></font>
                        </font></font></font>''' % (blank_space3, anval))
            Story.append(Paragraph(ptext_6_1, styles["Normal"]))
            #Story.append(Spacer(1, (1+rgapsize)))
            ptext_body_static_line_6 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
            Story.append(Paragraph(ptext_body_static_line_6, styles["Normal"]))
            Story.append(Spacer(1, -4))
            ptext_total_w = '''<para align=left spaceb=3><font size=7><font name=Courier>
                             MAXIMUM MARKS FOR MONTHLY TEST = [<font name=Courier-Bold>%s</font>], HALF YEARLY = [<font name=Courier-Bold>%s</font>],
                             ANNUAL = [<font name=Courier-Bold>%s</font>]
                             HALF YEARLY EXAM. MONTH = <font name=Courier-Bold> %s
                             </font> ANNUAL EXAM MONTH = <font name=Courier-Bold> %s </font>
                             </font></font></para>''' % (mnth, hlfy, annl, hfyrly, annualy)
            Story.append(Paragraph(ptext_total_w, styles["Normal"]))
            Story.append(Spacer(1, (-4+rgapsize)))

            ptext_total_w1 = '''<para align=left spaceb=3><font size=7><font name=Courier>
                             OVERALL PERFORMANCE OF STUDENT : ,
                             <font name=Courier-Bold> %s </font></font></font></para>''' % (self.remark_tx.GetValue())
            Story.append(Paragraph(ptext_total_w1, styles["Normal"]))
            Story.append(Spacer(1, (-4+rgapsize)))
           
            ptext_body_static_line_7 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
            Story.append(Paragraph(ptext_body_static_line_7, styles["Normal"]))
            Story.append(Spacer(1, -7))
            
            ptext_sign = ('<para align=left spaceb=3><font size=7><font name=Courier-Bold> %s </font></font></para>' % (bott_sg))
            Story.append(Paragraph(ptext_sign, styles["Normal"]))
            Story.append(Spacer(1, -5))
            
            return Story
        
    def OnPrint_Style_2(self,event,mnth, hlfy, annl, hfyrly, annualy, ROWHT, row, fntsize,rgapsize):
            
        WORK_OS = platform.system()
        self.ok.SetLabel('Wait..2!')
        self.hy_an_tot()

        
        if WORK_OS == 'Linux':
            #PP_EXPORT = conf.EXPORT_PATH()
            export_path = "%s/Student_Mark_Sheet.pdf"%rmss_config.PP_EXPORT
        else:
            export_path = "%s\Student_Mark_Sheet.pdf"%rmss_config.PP_EXPORT
        
        
        packet, doc, Story, styles, product_table, COLWDTH, static_sp, blank_space0, blank_space0_1, blank_space1, ptitl_ = \
                self.PDF_HEADING1(SimpleDocTemplate, A4, getSampleStyleSheet, ParagraphStyle, Paragraph, Spacer, StringIO, TA_JUSTIFY,fntsize,rgapsize)
        #cls_val = Combox_Val(self, self.class_tx.GetValue().strip())
        cls_val = 1
        try:
            product_table = self.PDF_BODY1(static_sp,Story,Paragraph,styles,Spacer,blank_space1,Table,colors,COLWDTH,ROWHT,TableStyle,product_table,row, fntsize, rgapsize)
            for i in range(len(product_table)):
                Story = self.ProductTable(static_sp,Story,Paragraph,styles,Spacer,blank_space1,Table,colors,COLWDTH,ROWHT,TableStyle,product_table, i, fntsize,rgapsize)
            
            self.ok.SetLabel('Printing!')
            bott_sg = "+++ DEVELOPED By RMS Deoria 9935188831, 9795116531 +++"
            Story = self.PDF_BOTTOM1( Story, Paragraph, styles, Spacer, static_sp,mnth, hlfy, annl, hfyrly, annualy, bott_sg,fntsize,rgapsize)
            
            
            doc.build(Story)
            packet.seek(0)
            
            new_pdf = PdfFileReader(packet)
            existing_pdf = PdfFileReader(file("sspdfbase.pdf", "rb"))
            output = PdfFileWriter()
            page = existing_pdf.getPage(0)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            
            outputStream = file("%s"%export_path, "wb")
            output.write(outputStream)
            outputStream.close()
        except (IOError,ValueError) as e: 
            StatusDP(self.status, 'Error Found [%s]'%str(e), fg='red')
            return
        if WORK_OS == 'Linux':
            subprocess.call(['xdg-open',export_path])
        else:
            exppath = 'start %s'%export_path
            dc = subprocess.Popen(exppath,shell=True)
            self.ok.SetLabel('Done.. !')
            dc.wait()
            self.master.destroy()

    def hy_an_tot(self):
        scolsum = 0
        ccolsum = 0
        row = self.grid.GetNumberRows()
        #cols = self.grid.GetNumberCols()
        for ro in range(row):
            for co in range(12,13):
                try:    
                    colv = self.grid.GetCellValue(ro, 12)
                    scolsum = (float(scolsum)) + (float(colv))
                    #scolsum = format("%.2f" % scolsum)
                    self.hy_tot.SetValue(str(scolsum))
                except ValueError :
                    hy_tot = 0.00
                    self.hy_tot.SetValue(str('0.00'))
                try:
                    colvt = self.grid.GetCellValue(ro, 13)
                    ccolsum = (float(ccolsum)) + (float(colvt))
                    self.an_tot.SetValue(str(ccolsum))
                except ValueError :
                    ann_tot = 0.00
                    self.an_tot.SetValue(str('0.00'))
                    
    def OnPrint_Style_1(self,event,mnth, hlfy, annl, hfyrly, annualy):
        
        
        WORK_OS = platform.system()
        
        self.hy_an_tot()
        row = self.grid.GetNumberRows()
        date = self.date_tx.GetValue()
        cls_det = self.class_tx.GetValue()
        fatherstx =  "Father's Name :"
        father = self.father_tx.GetValue()
        name_stx = "Student's Name :"
        name_tx = self.name_tx.GetValue()
        
        teacher = self.teacher_tx.GetValue()
        studid = self.studid
        std_perf = self.remark_tx.GetValue()
        conf = config.Configuration()
        otest = conf.OUTOFF_LIST()
        mnth, hlfy, annl = otest[0],otest[1],otest[2]
        hyanm = conf.ANNUAL_HY_MONTH()
        hfyrly, annualy = hyanm[0],hyanm[1]
        slogan = conf.SLOGAN()
        if WORK_OS == 'Linux':
            PP_EXPORT = conf.EXPORT_PATH()
            export_path = "%s/Student_Fee_Receipt.pdf"%PP_EXPORT
        else:
            export_path = "%s/Student_Fee_Receipt.pdf"%rmss_config.PP_EXPORT
        doc = SimpleDocTemplate("%s"%export_path,pagesize=landscape(letter),
                            rightMargin=40,leftMargin=40,
                            topMargin=30,bottomMargin=10)
        Story=[]
        
        phone = self.phone_tx.GetValue()
        owner, o_add1, o_add2, pphone = OWNER_DETAILS()
        try:
                    
            I = Image('mylogo.jpg')
            I.drawHeight = 1.30*inch*I.drawHeight / I.drawWidth
            I.drawWidth = 1.70*inch
            #im = Image.open("/School_RMS/ATP.gif")
            styles=getSampleStyleSheet()
            #styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY)) # (name='Center', alignment=TA_CENTER)
            styles.add(ParagraphStyle( name="ParagraphTitle", fontSize=3, alignment=TA_JUSTIFY, fontName="Courier"))
            ptitl_ = "MARK SHEET"
            ptitle = ('<para align=center spaceb=3><font size=6>  %s </font></para>' % (ptitl_))
            ptext1 = ('<para align=center spaceb=3><font size=12><font name=Courier-Bold> %s </font></font></para>' % (owner))
            
            p0 = I,str(o_add1),str(' ')
            p1 = ' ', str(o_add2+','+pphone),str(' ')
            p2 = str(slogan),' ',str('Date : %s'%date)
            pitem0 = [p0,p1,p2]
            t0 = Table(pitem0, colWidths=[150,150,150],rowHeights=[18,12,8])
            cls_val = Combox_Val(self, cls_det)
            if int(cls_val) > 5:
                t0.setStyle(TableStyle([
                ('FONTSIZE',(0,0),(-1,-1),8),
                ('TEXTFONT',(0,0),(-1,-1),'Courier-Bold'),
                #('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]))
                
                Story.append(Paragraph(ptitle, styles["Normal"]))
                Story.append(Paragraph(ptext1, styles["Normal"]))
                #Story.append()
                
                Story.append(t0)
                Story.append(Spacer(1, -8))
                
                ################################################################################################
                static_sp = 165 * "-"
                ptext_body_static_line_0 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                Story.append(Paragraph(ptext_body_static_line_0, styles["Normal"]))
                Story.append(Spacer(1, -8))
                
                ptext_body_static_line_1 = ('''<para align=center spaceb=3><font size=8><font name=Courier>
                 %s <font name=Courier-Bold> %s , </font><font name=Courier>%s, %s </font><font name=Courier-Bold> %s </font>Phone : %s </font></font></para>
                 ''' % (name_stx,name_tx,cls_det,fatherstx,father,phone))
                Story.append(Paragraph(ptext_body_static_line_1, styles["Normal"]))
                Story.append(Spacer(1, 5))
                
                #rdet = 'SUBJECTS','April','May','June','July','August','Sept.','Oct.','Nov.','Dec.','Jan.','Feb.','Mar.','H-Yrly','Annual'
                #pitem1 = [rdet]
                pitem1 = [self.COL_HEADING_VALUES()]
                t1 = Table(pitem1, colWidths=[100,40,40,40,40,40,40,40,40,40,40,40,40,50,50],rowHeights=[20])
                t1.setStyle(TableStyle([
                ('FONTSIZE',(0,0),(-1,-1),9),
                ('TEXTFONT',(0,0),(-1,-1),'Courier-Bold'),
                ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]))
                
                Story.append(t1)
                Story.append(Spacer(1, 0.5))
                product_table = []
                for r in range(0, row):
                    item = []
                    #item.append('|'+self.grid.GetColLabelValue(self, col))
                    item.append(str(self.grid.GetRowLabelValue(r)))
                    item.append(self.grid.GetCellValue(r, 0))
                    item.append(self.grid.GetCellValue(r, 1))
                    item.append(self.grid.GetCellValue(r, 2))
                    item.append(self.grid.GetCellValue(r, 3))
                    item.append(self.grid.GetCellValue(r, 4))
                    item.append(self.grid.GetCellValue(r, 5))
                    item.append(self.grid.GetCellValue(r, 6))
                    item.append(self.grid.GetCellValue(r, 7))
                    item.append(self.grid.GetCellValue(r, 8))
                    item.append(self.grid.GetCellValue(r, 9))
                    item.append(self.grid.GetCellValue(r, 10))
                    item.append(self.grid.GetCellValue(r, 11))
                    item.append(self.grid.GetCellValue(r, 12))
                    item.append(self.grid.GetCellValue(r, 13))
                    item.append('0.011')
                    product_table.append(item)
                    for n, i in enumerate(item):
                        if i == '0.00':
                            item[n] = ''
                        if i == '0.0':
                            item[n] = ''
                for i in range(len(product_table)):
                    try:
                        pitem2 = [product_table[i]]
                        t2 = Table(pitem2, colWidths=[90,0,40,40,40,40,40,40,40,40,40,40,40,50,50,50],rowHeights=[20])
                        t2.setStyle(TableStyle([
                        ('FONTSIZE',(0,0),(-1,-1),9),
                        ('FONTNAME',(0,0),(-1,-1),'Courier-Bold'),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                        ('FONTSIZE',(0,18), (-1,-1),7),
                        ('FONTNAME', (0,18), (-1,-1), 'Courier'),
                        #('TEXTCOLOR',(0,18), (-1,-2),colors.green),
                        #('TEXTCOLOR',(0,19), (-1,-1),colors.red),
                        ('FONTSIZE',(0,19), (-1,-1),9),
                        ('FONTNAME',(0,19), (-1,-1),'Courier-Bold'),
                        #('INNERGRID', (0,0), (-1,0), 0.25, colors.black)
                        ]))
                    except IndexError:
                            pass
                    Story.append(t2)        
                    Story.append(Spacer(0.001, 0.001))
                    
                straight_line = 110 * "_"
                ptext_body_static_line_5 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                Story.append(Paragraph(ptext_body_static_line_5, styles["Normal"]))
                Story.append(Spacer(1, -1))
            else:
                t0.setStyle(TableStyle([
                ('FONTSIZE',(0,0),(-1,-1),8),
                ('TEXTFONT',(0,0),(-1,-1),'Courier-Bold'),
                #('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]))
                
                Story.append(Paragraph(ptitle, styles["Normal"]))
                Story.append(Paragraph(ptext1, styles["Normal"]))
                #Story.append()
                
                Story.append(t0)
                Story.append(Spacer(1, 10))
                
                ################################################################################################
                static_sp = 165 * "-"
                ptext_body_static_line_0 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                Story.append(Paragraph(ptext_body_static_line_0, styles["Normal"]))
                Story.append(Spacer(1, 5))
                
                ptext_body_static_line_1 = ('''<para align=center spaceb=3><font size=8><font name=Courier>
                 %s <font name=Courier-Bold> %s , </font><font name=Courier>%s, %s </font><font name=Courier-Bold> %s </font>Phone : %s </font></font></para>
                 ''' % (name_stx,name_tx,cls_det,fatherstx,father,phone))
                Story.append(Paragraph(ptext_body_static_line_1, styles["Normal"]))
                Story.append(Spacer(1, 5))
                
                #rdet = 'SUBJECTS','April','May','June','July','August','Sept.','Oct.','Nov.','Dec.','Jan.','Feb.','Mar.','H-Yrly','Annual'
                #pitem1 = [rdet]
                pitem1 = [self.COL_HEADING_VALUES()]
                t1 = Table(pitem1, colWidths=[90,0,40,40,40,40,40,40,40,40,40,40,40,50,50,50],rowHeights=[35])
                t1.setStyle(TableStyle([
                ('FONTSIZE',(0,0),(-1,-1),9),
                ('TEXTFONT',(0,0),(-1,-1),'Courier-Bold'),
                ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]))
                
                Story.append(t1)
                Story.append(Spacer(1, 5))
                product_table = []
                for r in range(0, 7):
                    item = []
                    #item.append('|'+self.grid.GetColLabelValue(self, col))
                    item.append(str(self.grid.GetRowLabelValue(r)))
                    item.append(self.grid.GetCellValue(r, 0))
                    item.append(self.grid.GetCellValue(r, 1))
                    item.append(self.grid.GetCellValue(r, 2))
                    item.append(self.grid.GetCellValue(r, 3))
                    item.append(self.grid.GetCellValue(r, 4))
                    item.append(self.grid.GetCellValue(r, 5))
                    item.append(self.grid.GetCellValue(r, 6))
                    item.append(self.grid.GetCellValue(r, 7))
                    item.append(self.grid.GetCellValue(r, 8))
                    item.append(self.grid.GetCellValue(r, 9))
                    item.append(self.grid.GetCellValue(r, 10))
                    item.append(self.grid.GetCellValue(r, 11))
                    item.append(self.grid.GetCellValue(r, 12))
                    item.append(self.grid.GetCellValue(r, 13))
                    item.append('0.012')
                    product_table.append(item)
                    for n, i in enumerate(item):
                        if i == '0.00':
                            item[n] = ''
                        if i == '0.0':
                            item[n] = ''
                for i in range(len(product_table)):
                    try:
                        pitem2 = [product_table[i]]
                        t2 = Table(pitem2, colWidths=[100,40,40,40,40,40,40,40,40,40,40,40,40,50,50],rowHeights=[40])
                        t2.setStyle(TableStyle([
                        ('FONTSIZE',(0,0),(-1,-1),9),
                        ('FONTNAME',(0,0),(-1,-1),'Courier-Bold'),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                        ('FONTSIZE',(0,18), (-1,-1),7),
                        ('FONTNAME', (0,18), (-1,-1), 'Courier'),
                        #('TEXTCOLOR',(0,18), (-1,-2),colors.green),
                        #('TEXTCOLOR',(0,19), (-1,-1),colors.red),
                        ('FONTSIZE',(0,19), (-1,-1),9),
                        ('FONTNAME',(0,19), (-1,-1),'Courier-Bold'),
                        #('INNERGRID', (0,0), (-1,0), 0.25, colors.black)
                        ]))
                    except IndexError:
                            pass
                    Story.append(t2)        
                    Story.append(Spacer(0.001, 5))
                
                ptext_body_static_line_5 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                Story.append(Paragraph(ptext_body_static_line_5, styles["Normal"]))
                Story.append(Spacer(1, -1))
            blank_space2 = '&nbsp'*105    
            straight_line = 110 * "_"
            hy_tot = self.hy_tot.GetValue()
            ann_tot = self.an_tot.GetValue()
            #hy_tot,ann_tot = 222,444
            ptext_6 = ('''<font size=9><font name=Courier>%s<font size=11><font name=Courier-Bold>%s</font></font>
                        &nbsp &nbsp &nbsp<font size=11><font name=Courier-Bold>%s</font>
                        </font></font></font>''' % (blank_space2,hy_tot,ann_tot))
            Story.append(Paragraph(ptext_6, styles["Normal"]))
            Story.append(Spacer(1, 2))
            ptext_body_static_line_6 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
            Story.append(Paragraph(ptext_body_static_line_6, styles["Normal"]))
            Story.append(Spacer(1, -4))
            ptext_total_w = '''<para align=left spaceb=3><font size=7><font name=Courier>
                             MAXIMUM MARKS FOR MONTHLY TEST = [<font name=Courier-Bold>%s</font>], HALF YEARLY = [<font name=Courier-Bold>%s</font>],
                             ANNUAL = [<font name=Courier-Bold>%s</font>]
                             HALF YEARLY EXAM. MONTH = <font name=Courier-Bold> %s
                             </font> ANNUAL EXAM MONTH = <font name=Courier-Bold> %s </font>
                             </font></font></para>''' % (mnth, hlfy, annl, hfyrly, annualy)
            Story.append(Paragraph(ptext_total_w, styles["Normal"]))
            Story.append(Spacer(1, -4))

            ptext_total_w1 = '''<para align=left spaceb=3><font size=7><font name=Courier>
                             OVERALL PERFORMANCE OF STUDENT : ,
                             <font name=Courier-Bold> %s </font></font></font></para>''' % (std_perf)
            Story.append(Paragraph(ptext_total_w1, styles["Normal"]))
            Story.append(Spacer(1, -4))
           
            ptext_body_static_line_7 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
            Story.append(Paragraph(ptext_body_static_line_7, styles["Normal"]))
            Story.append(Spacer(1, -4))
            
            bott_sg = "+++ DEVELOPED By RMS Deoria 9935188831, 9795116531 +++"
            ptext_sign = ('<para align=left spaceb=3><font size=6><font name=Courier-Bold> %s </font></font></para>' % (bott_sg))
            Story.append(Paragraph(ptext_sign, styles["Normal"]))
            Story.append(Spacer(1, 5))
            doc.build(Story)
        except (IOError,ValueError)as e: 
            StatusDP(self.status, 'Error Found [%s]'%str(e), fg='red')
        if WORK_OS == 'Linux':
            subprocess.call(['xdg-open',export_path])
        else:
            #subprocess.call(['start',export_path])
            exppath = 'start %s'%export_path
            dc = subprocess.Popen(exppath,shell=True)
            dc.wait()
            #os.system('start %s'%export_path)
        self.master.destroy()
     
def main():
    root = Tk()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    #"Calibri Bold", "Calibri", "Arial", "Arial Bold", "Times New Roman", "Times New Roman Bold"
    sysfontnum = 12  ### Default is given Upate Later/User Given 
    entryfont = "Calibri Bold"
    subentryfont = "Calibri"
    fontd = {"calb":"Calibri Bold", "cal":"Calibri", "arl":"Arial", "arlb":"Arial Bold",
                 "tnr":"Times New Roman", "tnrb":"Times New Roman Bold", "entryfont":{'font': (entryfont, sysfontnum)},
                 "subentryfont":{'font': (subentryfont, sysfontnum)}}
    today = time.strftime('%d/%m/%Y', time.localtime(time.time()))
    today_db_f = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    
    mycalendar = (('fy0', today_db_f, today_db_f, u''),)
    rmspath = os.path.dirname(os.path.realpath(__file__))
    pdir = os.path.dirname(rmspath)
    
    rmsicon = os.path.join(rmspath, 'my_icon.ico')
    ostd = {'pageline':60, 'net_colm':'Y','party_bal':'N','stockist_list':'Y',
                'page_size':'4','default_trade':0,'bill_series':'S'}
    own = {'name':'RMS SOFT','add1':'http://www.rmssoft.co.in','add2':'','phone':'','reg':'', 'gstin':'','statu1':'','statu2':'','statu3':'','statu4':''}
    otlst = {'others':'/True', 'stockist_det':''}
    opdfsett = {'vat':4, 'vat1':4, 'sat':1, 'cst':2}
    ownerdict = {'billseries':'S', 'demochk':45, 'ownerinfo':{'owner':own, 'othersett':ostd, 'otlst':otlst, 'opdfsett':opdfsett},
                 'errorlist':[]}
    prpath = {}
    printerinfo = {'printer':{'pport':'USB001','pname':'myprinter'},'shareprinter':{'sprinter':'myprinter','sport':'LPT1','sname':'tvs'}}
    taxinfo = {'taxinfo':{'tax1name':'CGST', 'tax2name':'SGST','tax1lst':[], 'tax2lst':[], 'taxpayer':True},}
    conf = config.Configuration()
    cofdic ={'fare1':conf.FARE_MODE1(),'fare2':conf.FARE_MODE2(),
              'fare3':conf.FARE_MODE3(),'latefee':conf.LATE_FEE_DATE(),'an_hy_montn':conf.ANNUAL_HY_MONTH(),
              'headmargin':conf.HEAD_MARGIN(),'footmargin':conf.FOOT_MARGIN(),'leftmargin':conf.LEFT_MARGIN(),
              'rightmargin':conf.RIGHT_MARGIN(),'extendmargin':conf.EXTEND_MARGIN(),'subjecthigh':conf.SUBJECTS_HIGHER(),
              'subjectlow':conf.SUBJECTS_LOWER(),'subjectrowhigh':conf.SUBJECTS_ROW_HIGHER(), 'subjectrowlow':conf.SUBJECTS_ROW_LOWER(),   
              'fontsize_h':conf.HEIGHER_CLASS_FONT_SIZE(),'fontsize_l':conf.LOWER_CLASS_FONT_SIZE(),'outoff':conf.OUTOFF_LIST(),
              'session':conf.SESSION(),'feehead':conf.FEE_HEADINGS(),'pdfs1':conf.PRINT_PDF_STYLE(),
              'exportpath':conf.EXPORT_PATH(),'slogan':conf.SLOGAN(),
              'monthhead':config.MONTHS_HEADINGS(),'rvmonthhead':config.REVERSE_MONTHS_HEADINGS(),}
    rscr = {'sw':sw, 'sh':sh, 'font':fontd,'sysfontnum':int(sysfontnum), 'ownerdict':ownerdict, 'mycalendar':mycalendar,
            'fyear':'0', 'daterange':['2000-01-01','2021-03-31'],
           
            'ledgerid':'0','itemid':'0','transid':'0','spid':'0','csid':'0','csname':'',
            'rmspath':rmspath,'rmsicon':rmsicon, 'pardir': rmspath, 'prpath':prpath,'taxinfo':taxinfo,'printerinfo': printerinfo,
            'TABLENUM':'','today':today, 'today_db_format':today_db_f,'tax1':'0', 'tax2':'0',
            'the_time':'', 'itemidlist':[], 'spidlist':[],'renderlist':[],
            'taxinvoice':True,'stkmess':'YES','decimalval':'2','last_esti_no':None, 'last_sale_bill_no':None,
            'exp_alert':90,'estifilter':False, 'sdc':'1','mysoft':'1','mysoftval':'1',
            'compbool':True,'config':cofdic}
    buttonidx = 1
    parent = None
    sptag = 'Sheet Print'
    spnum = 1
    whxy = (sw, sh-70, 0, 0)
    app = Sheet_Print(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()

