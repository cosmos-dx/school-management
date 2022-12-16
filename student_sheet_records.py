#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import os
from rmsdatepicker import RmsDate, RmsDatePicker
from  datetime import datetime
import shutil
from class_query import STU_INFO, SHEET_REC
from rmsvalidators import *

class SheetRecords(Frame):
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
        self.bg = 'SystemButtonFace'
        lb_fg_bg = {'font': ['Courier', self.ftsz, 'bold'], 'bg':'#b0e0e6', 'fg': 'black'} 
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

        self.fro = RMS_LABEL(self.master, text="From :", **lfntfg_bgg)
        self.fro.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w') 
        self.from_ = RmsDate(self.master, self.master, self, width=12, **efnt_fgbg)
        self.from_.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')

        self.to = RMS_LABEL(self.master, text="To :", **lfntfg_bgg)
        self.to.grid(row=wrow, column=7, rowspan=1, columnspan=1, sticky='w') 
        self.to_ = RmsDate(self.master, self.master, self, width=12, **efnt_fgbg)
        self.to_.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        
        self.studid = None
        self.class_entry_stx = RMS_LABEL(self.master, text='Class Name :', **lfntfg_bgg)
        self.class_entry_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w') 
        self.class_entry_cb = RMSCombobox(self.master, values=Clist, state='readonly', width=6, **combx_fnt)       
        self.class_entry_cb.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.class_entry_cb.current(3)
        
        self.class_sec_stx = RMS_LABEL(self.master, text="Class Section :", **lfntfg_bgg)
        self.class_sec_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w') 
        self.section_tx = RMS_ENTRY(self.master, textvariable=StringVar(), width=5, **efnt_fg_bg)
        self.section_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        self.section_tx.SetValue('A')

        self.ss = False
        self.namevar = StringVar()
        self.namevar.trace('w', lambda nm, idx, mode, var=self.namevar:
                          self.Student_Name_Text(var))
        self.stu_name_stx = RMS_LABEL(self.master, text="Student's Name :", **lfntfg_bgg)
        self.stu_name_stx.grid(row=wrow, column=7, rowspan=1, columnspan=1, sticky='w')
        self.stu_name_tx = RMS_ENTRY(self.master, textvariable=self.namevar, **efnt_fg_bg)
        self.stu_name_tx.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        rows = 11
        colconf = {0:{'idname':'name','text':'Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},}
            
        self.snlc = RMSLBN(self.master, self, True, rows, colconf, **efnt_fg_bg)
        self.snlcpos = {'row':wrow-2, 'column':8,'columnspan':8,'rowspan':10, 'sticky':'w'}

        gbd, gbg, gfg, gfont,wd = 1, 'white', 'blue', ('Courier', self.ftsz, 'normal'),6
        ### Month name must be given in 3 Char Format further used in key value format
        ### {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUNE', 7: 'JULY', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC', 13: 'H-Yrly', 14: 'Annual'}
        self.gcolconf = {0:{'vcmd':'AN','idname':'0','text':'','width':1,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           1:{'vcmd':'AN','idname':'sheetdate','text':'Date','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',}, 
           2:{'vcmd':'AN','idname':'name','text':'Name','width':12,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           3:{'vcmd':'F','idname':'hindi','text':'HINDI','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           4:{'vcmd':'F','idname':'english','text':'ENG.','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           5:{'vcmd':'F','idname':'science','text':'SCNC','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           6:{'vcmd':'AN','idname':'math','text':'MATH','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           7:{'vcmd':'F','idname':'sport','text':'SPORT','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           8:{'vcmd':'F','idname':'chem','text':'CHEM','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           9:{'vcmd':'F','idname':'phys','text':'PHY','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           10:{'vcmd':'F','idname':'bio','text':'BIO','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           11:{'vcmd':'AN','idname':'civic','text':'CIVIC','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           12:{'vcmd':'AN','idname':'civic','text':'CIVIC','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           13:{'vcmd':'AN','idname':'hist','text':'HIST','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           14:{'vcmd':'AN','idname':'geo','text':'GEO','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',}, 
           15:{'vcmd':'AN','idname':'comm','text':'Comm','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           16:{'vcmd':'AN','idname':'sact','text':'Sc.Act','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           17:{'vcmd':'AN','idname':'sport','text':'SPORT','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           18:{'vcmd':'AN','idname':'other','text':'OTHER','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',},
           19:{'vcmd':'AN','idname':'comp','text':'COMP.','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',}, 
           20:{'vcmd':'F','idname':'attend','text':'ATTEND.','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',}, 
           21:{'vcmd':'AN','idname':'total','text':'TOTAL','width':wd,'bd':gbd,'bg':gbg,'fg':gfg, 'font':gfont, 'relief':'raised',}, }
        
        self.rowfillcount = 0
        rows = 10
        coln = 13 ##len(colconf)
        sbar = {'vsb':{'row':wrow,'column':coln,'rowspan':rows,'columnspan':1,'sticky':'ns',},
                'hsb':{'row':sum([rows,1]),'column':0,'rowspan':rows,'columnspan':rows,'sticky':'we',},
                'cnv':{'row':wrow,'column':0,'rowspan':rows,'columnspan':coln,'sticky':'news',},}
                   
        grid_fg_bg = {'sbar': sbar} 
        self.grid = RMSGRID(self.master, self, wrow, rows, 0, self.gcolconf, True, **grid_fg_bg)
        wrow += rows
        
        self.close = RMS_BUTTON(self.master, text='Close', bd=3,
                                command=self.OnClose, **bfnt_fg_bg) 
        self.close.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        
        btmwg_fg_bg = {'font': ['Courier New', self.ftsz, 'bold'], 'bg': 'SystemButtonFace', 'fg': 'blue'}
        self.kuddp = RMS_LABEL(self.master, text='0', width=12, **btmwg_fg_bg)
        self.kuddp.grid(row=wrow, column=1,)
        self.kuddisplay = RMS_LABEL(self.master, text='0', width=12, **btmwg_fg_bg)
        self.kuddisplay.grid(row=wrow, column=2,)
        wrow += 1
        self.status = RMS_LABEL(self.master, text='', **lfnt_fg_bg)
        self.status.grid(row=wrow, column=1, rowspan=1, columnspan=15)
        wrow += 2

        self.sqry = STU_INFO()
        self.shqry = SHEET_REC()
        #self.class_entry_cb.bind('<<ComboboxSelected>>', self.OnClass_entry_cb)
        
        for r in range(wrow):
            self.master.rowconfigure(r, weight=1)
        for r in range(15):
            self.master.columnconfigure(r, weight=1)
        self.stu_name_tx.bind('<Key>', self.student_name_tx_key)
        
        #self.RefreshEntryBG(self.class_entry_cb, self.class_entry_cb)
        self.wdfiddict = {self.snlc:'snlc', self.grid:'grid',}

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

    def SNLCShow(self):
        if not self.snlcdata:
            self.snlc.Hide()
            return 
        self.snlc.grid(self.snlcpos)
        self.snlc.lift(aboveThis=None)

    def SNLC_SEARCH(self, text):
        self.snlc.DeleteAllItems()
        Act = '0' ## 0 for Active Students in School
        Out = '1' ## 1 for OUT Students in School
        val = self.class_entry_cb.GetValue()
        try:
            key_val = Combox_Val(self, val)
        except KeyError:
            mess = RMSMBX(self, text="\n Select Student Class \n Than Search start searching...!!\n", info=True,
              textclr='blue', bg='yellow')
            self.student_name_tx.SetValue('')
            return
        section = self.section_tx.GetValue().strip()
        if section == '':
            mess = RMSMBX(self, text="\n Select Student Section \n Than Search start searching...!!\n", info=True,
              textclr='blue', bg='yellow')
            self.section_tx.SetFocus()
            return
        
        ##Act = '0' ## 0 for Active Students in School
        ##Out = '1' ## 1 for OUT Students in School
        textlist = '00', '00', text, self.fyear, 'ledgerID', text, key_val, section, '0'
        self.snlcdata = self.snlc.SETDATA(self.sqry.Student_Data_Fill, textlist, 'name')
        self.studid = str(self.snlcdata['esid'])
        self.SNLCShow()
        
    def Student_Name_Text(self, var):
        text = var.get()
        var.set(text)
        if self.ss:
            self.snlc.Clear()
            self.SNLC_SEARCH(text)

    def student_name_tx_key(self, event):
        key = event.keysym
        text = self.stu_name_tx.GetValue() 
        self.ss = True ### search start
        try:
            self.snlcdata, kidx = self.snlc.KeyMove(key, 'name')     
            self.KUDDP(kidx, self.snlc)          
        except Exception as err :
            kidx = 0
        
        if key in ['Return', 'Tab']:
            if not text:
                return
            self.ss = False ### search stop
            
            if not self.snlcdata:
                self.RefreshEntryBG(self.stu_name_tx, self.stu_name_tx)
                return
            self.studid = str(self.snlcdata['esid'])
            self.DataFill(data=self.snlcdata)
            self.snlc.Hide()
            
            
    def KUDDP(self, kidx, wdg):
        snkidx = sum([kidx, wdg.datavarlimit])
        self.kuddp.SetLabel(snkidx)

    def DataFill(self, data=None):
        if not data:
            return
        fdate = datetime.strptime(self.from_.GetValue(), "%d/%m/%Y").strftime("%Y-%m-%d")
        tdate = datetime.strptime(self.to_.GetValue(), "%d/%m/%Y").strftime("%Y-%m-%d")
        rows = self.shqry.SheetDictRec(self.studid, fdate, tdate)  ## dict rows
        self.stu_name_tx.SetValue(data['name'])
        self.grid.SetCellValue(self.rowfillcount, 2, data['name'], bg='yellow')
        for k,v in self.gcolconf.items():
            try:
                self.grid.SetCellValue(self.rowfillcount, k, str(rows[0][v['idname']]), fg='black')
                self.grid.SetCellValue(self.rowfillcount, 0, '***')
            except KeyError:
                pass
        self.rowfillcount += 1
        
    def GetLCSelectData(self, ridx, data, evtname):
        row, col, wdg = ridx
        if evtname == 'Return':
            wdgname = self.wdfiddict[wdg]
            if wdgname == 'snlc':
                getrowdata = data[row]
                if getrowdata:
                    self.studid = str(getrowdata['esid'])
                    self.DataFill(data=self.snlcdata)
                    self.snlc.Hide()
            if wdgname == 'grid':
                getrowdata = data[row]
                print ('grid action student_sheet_records.py line 282')
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
"""                
def main():
    import config
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
            'exp_alert':90,'estifilter':False,'sdc':'1','mysoft':'1','mysoftval':'1',
            'compbool':True, 'config':cofdic}
    buttonidx = 1
    parent = None
    sptag = 'Student Performance Entry'
    spnum = 1
    whxy = (sw, sh-70, 0, 0)
    app = SheetRecords(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()
"""
