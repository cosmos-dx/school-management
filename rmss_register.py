#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import os
from rmsdatepicker import RmsDate, RmsDatePicker
from  datetime import datetime
import shutil
from xlwt import *
from class_query import STU_INFO, EMP_INFO, REG_REC
from rmsvalidators import *
import rmss_config

class rmss_register(Frame):
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
        self.todaydbf = self.rscr['today_db_format']
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
        combx_fnt = {'font': ['Courier', self.ftsz, 'normal'],}
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
        self.fro.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w') 
        self.from_ = RmsDate(self.master, self.master, self, width=12, **efnt_fgbg)
        self.from_.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')

        self.to = RMS_LABEL(self.master, text="To :", **lfntfg_bgg)
        self.to.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w') 
        self.to_ = RmsDate(self.master, self.master, self, width=12, **efnt_fgbg)
        self.to_.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')

        self.ss = False
        self.namevar = StringVar()
        self.namevar.trace('w', lambda nm, idx, mode, var=self.namevar:
                          self.Name_Text(var))
        self.search_stx = RMS_LABEL(self.master, text="Search Name :", **lfntfg_bgg)
        self.search_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w') 
        self.search_tx = RMS_ENTRY(self.master, textvariable=self.namevar, **efnt_fg_bg)
        self.search_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')

        self.snhidebv = BooleanVar()
        self.snhidecb = RMSChkBut(self.master, text='- Hide List',
                    command=self.ON_SNHide, variable=self.snhidebv, **chk_fg_bg)
        self.snhidecb.grid(row=wrow, column=6, rowspan=1, columnspan=1, sticky='w')
        
        wrow += 1

        self.select_stx = RMS_LABEL(self.master, text='SELECT :', **lfntfg_bgg)
        self.select_stx.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w')
        slcdata = ["TEACHER","STUDENT","OTHER",]
        self.select_tx = RMSCombobox(self.master, values=slcdata, state='readonly', width=12, **combx_fnt)
        self.select_tx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')

        self.class_entry_cb = RMSCombobox(self.master, values=Clist, state='readonly', width=6, **combx_fnt)       
        self.class_entry_cb.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.class_entry_cb.current(3)

        Slist = ['A','B', 'C', 'D', 'E', 'F', 'G','H','I','J','K']
        self.section_cb = RMSCombobox(self.master, values=Slist, state='readonly', width=6, **combx_fnt)       
        self.section_cb.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        self.section_cb.current(0)
        
        self.studid = None
        self.stid = ''
  
        wrow += 1

        self.search = RMS_BUTTON(self.master, text='Start', bd=3,
                                command=self.OnStart, **bfnt_fg_bg) 
        self.search.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w')
        self.ok = RMS_BUTTON(self.master, text='Mark _', bd=3,
                                command=self.OnSave, **bfnt_fg_bg)
        self.ok.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')

        self.section_tx = RMS_ENTRY(self.master, textvariable=StringVar(), width=5, **efnt_fg_bg)
        self.section_tx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.section_tx.SetValue('A')
                
        wrow += 1
        self.st_search = RMS_BUTTON(self.master, text='Search', bd=3,
                                command=self.ON_ST_Search, **bfnt_fg_bg) 
        self.st_search.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w')
        self.close_reg = RMS_BUTTON(self.master, text='Close Register', bd=3,
                                command=self.OnCLOSE_REGISTER, **bfnt_fg_bg)
        self.close_reg.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')

        self.scxbbv = BooleanVar()
        self.scxb = RMSChkBut(self.master, text='- Old Records',
                    command=self.ON_Cxb, variable=self.scxbbv, **chk_fg_bg)
        self.scxb.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        
        wrow += 1
        rows = 11
        colconf = {0:{'idname':'name','text':'Name','width':25,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
                   1:{'idname':'gname','text':'G.Name','width':20,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
                   2:{'idname':'add1','text':'Address','width':25,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
                   3:{'idname':'section','text':'S/D','width':5,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},}
            
        self.snlc = RMSLBN(self.master, self, True, rows, colconf, **efnt_fg_bg)
        self.snlcpos = {'row':wrow-3, 'column':1,'columnspan':18,'rowspan':10, 'sticky':'ne'}

        colconf = {0:{'idname':'name','text':'Name','width':20,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
                   1:{'idname':'gname','text':'G.Name','width':15,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
                   2:{'idname':'section','text':'S/D','width':5,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},}
        self.search_lc = RMSLBN(self.master, self, True, 8, colconf, **efnt_fg_bg)
        self.searchlcpos = {'row':sum([wrow,5]), 'column':1,'columnspan':18,'rowspan':10, 'sticky':'se'}
        
        self.rowfillcount = 0
        rows = 10
        coln = 13 ##len(colconf)
        
        #self.grid = RMSGRID(self.master, self, wrow, rows, 0, self.gcolconf, True, **grid_fg_bg)
        lbfont = ('Courier New', sum([self.ftsz, 1]), 'bold')
        gbd, gbg, gfg, wd = 2, '#b0e0e6', 'black', 9
        self.gcolconf = {
        0:{'idname':'sno','text':'S.N','width':5,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},
        1:{'idname':'lid','text':'ID','width':wd,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'sunken','wrow':wrow},
        2:{'idname':'daytime','text':'DayTime','width':11,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'sunken','wrow':wrow},
        3:{'idname':'desg','text':'DESG','width':wd,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'sunken','wrow':wrow},
        4:{'idname':'name','text':'NAME','width':20,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'sunken','wrow':wrow},
        5:{'idname':'gname','text':'G.NAME','width':20,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'sunken','wrow':wrow},
        6:{'idname':'phone','text':'CONTACT','width':11,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'sunken','wrow':wrow},
        7:{'idname':'section','text':'A/P','width':wd,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'sunken','wrow':wrow},
          }
       
        header, rows = True, 10
        self.st_lc = RMSLBN(self.master, self, header, rows, self.gcolconf, **lb_fg_bg)
        self.lcdata = None
        self.st_lc.grid(row=wrow, column=0, rowspan=1, columnspan=12, sticky='w')
        
        wrow += rows
        btmwg_fg_bg = {'font': ['Courier New', self.ftsz, 'bold'], 'bg': 'SystemButtonFace', 'fg': 'blue'}
        self.report_stx = RMS_LABEL(self.master, text="EXPORT XLS", **btmwg_fg_bg)
        self.report_stx.grid(row=wrow, column=0,)
        self.report_gst = RMS_BUTTON(self.master, text='Given Stud. List', bd=3,
                                command=self.ON_GSXLS, **bfnt_fg_bg) 
        self.report_gst.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        
        self.report_ast = RMS_BUTTON(self.master, text='ALL Stud. Record', bd=3,
                                command=self.ON_ASXLS, **bfnt_fg_bg) 
        self.report_ast.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.report_atr = RMS_BUTTON(self.master, text='ALL Emp. Record', bd=3,
                                command=self.ON_ATXLS, **bfnt_fg_bg) 
        self.report_atr.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        self.close = RMS_BUTTON(self.master, text='Close', bd=3,
                                command=self.OnClose, **bfnt_fg_bg) 
        self.close.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        
        self.kuddp = RMS_LABEL(self.master, text='0', width=12, **btmwg_fg_bg)
        self.kuddp.grid(row=wrow, column=1,)
        self.kuddisplay = RMS_LABEL(self.master, text='0', width=12, **btmwg_fg_bg)
        self.kuddisplay.grid(row=wrow, column=2,)
        wrow += 1
        self.status = RMS_LABEL(self.master, text='', **lfnt_fg_bg)
        self.status.grid(row=wrow, column=1, rowspan=1, columnspan=15)
        wrow += 10

        self.sqry = STU_INFO()
        self.tqry = EMP_INFO()
        self.regqry = REG_REC()
        for r in range(wrow):
            self.master.rowconfigure(r, weight=1)
        for r in range(25):
            self.master.columnconfigure(r, weight=1)
        self.search_tx.bind('<Key>', self.Name_tx_key)
        self.class_entry_cb.bind('<<ComboboxSelected>>', self.OnClass_entry_cb)
        self.section_cb.bind('<<ComboboxSelected>>', self.Section_CB)
        self.select_tx.bind('<<ComboboxSelected>>', self.OnSelectcb)
        self.wdfiddict = {self.snlc:'snlc', self.st_lc:'stlc',self.search_lc:'search_lc'}
        self.srlist = set()
        self.student_rows = None
        self.student_ids = None
        self.scxb_rows = None
        self.scxb_ids = None
        self.snlcdata = None
        self.teacher_rows = None
        self.teacher_ids = None
        self.tcxb_rows = None
        self.tcxb_ids = None
        self.DISABLE_()
        
    def DISABLE_(self):
        self.search_tx.Disable()
        self.select_tx.Disable()
        self.class_entry_cb.Disable()
        self.section_cb.Disable()
        self.ok.Disable()
        self.close_reg.Disable()
    def ENABLE_(self):
        self.search_tx.Enable()
        self.select_tx.Enable()
        self.class_entry_cb.Enable()
        self.section_cb.Enable()
        self.ok.Enable()
        self.close_reg.Enable()
        
    def SetDateRange(self):
        month = self.month_cb.GetValue()
        mnum  =(self.Mkey_rv[self.month_cb.GetValue()])
        yyyy = self.from_.GetValue().split('/')[2]
        fdt = '/'.join(['01', '%02d'%mnum, yyyy])
        if month == 'FEB':
            tdt = '/'.join(['28', '%02d'%mnum, yyyy])
        else:
            tdt = '/'.join(['30', '%02d'%mnum, yyyy])
        self.from_.SetValue(fdt)
        self.to_.SetValue(tdt)

    def OnSelectcb(self, event):
        value = self.select_tx.GetValue()
        self.ss = False
        self.search_tx.SetValue('')
        self.ss = True
        self.stid = ''
        self.srlist = set()
        self.STUDENT_DATAS_QUERY()
        if value == "STUDENT":
            self.SNLC_SEARCH('')
        if self.select_tx.GetValue().strip() == "TEACHER":
            self.close_reg.Enable()
            self.ok.SetLabel('Mark Present')
            self.ok.fg('black')
        else:
            self.close_reg.Disable()
            self.ok.SetLabel('Mark Absent')
            self.ok.fg('red')
        if self.select_tx.GetValue().strip() == "OTHER":
            self.close_reg.Enable()
            self.ok.SetLabel('Mark Present')
            self.ok.fg('black')
        self.search_lc.DeleteAllItems()
        self.search_lc.Hide()
        
    def OnClass_entry_cb(self, event):
        self.STUDENT_DATAS_QUERY()

    def Section_CB(self, event):
        self.STUDENT_DATAS_QUERY()
        
    def DATE_GET_VALUE(self):
        frmval = self.from_.GetValue()
        toval = self.to_.GetValue()
        frmsp = str(frmval).split('/')
        tosp = str(toval).split('/')
        fmdd , fmmm, fmyy = frmsp[0], frmsp[1], frmsp[2]
        todd , tomm, toyy = tosp[0], tosp[1], tosp[2]
        dicval = self.Mkey_rv[self.month_cb.GetValue()]
        
        session_start = int(self.rscr['config']['session'])
        if int(dicval) < int(session_start):
            dtyy = int(toyy)    
        else:
            dtyy = int(toyy) - 1
        dfrm , dtod = str(dtyy)+'-'+str(dicval)+'-'+str('01'), str(dtyy)+'-'+str(dicval)+'-'+str('31')
        return dfrm , dtod
     
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

    def SNLC_SHOW(self):
        if not self.snlcdata:
            self.snlc.Hide()
            return 
        self.snlc.grid(self.snlcpos)
        self.snlc.lift(aboveThis=None)
        
    def SEARCHLC_SHOW(self):
        self.search_lc.grid(self.searchlcpos)
        self.search_lc.lift(aboveThis=None)
        
    def SNLC_HIDE(self):
        self.snlc.Hide()
        
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
        select = self.select_tx.GetValue().strip()
        if select == "STUDENT" : 
            textlist = '00', '00', text, self.fyear, 'ledgerID', text, key_val, section, '0'
            self.snlcdata = self.snlc.SETDATA(self.sqry.Student_Data_Fill, textlist, 'name')
        elif select == "TEACHER" :
            textlist = '00', '00', text, self.fyear, 'T'
            self.snlcdata = self.snlc.SETDATA(self.tqry.Emp, textlist, 'name')
        elif select == "OTHER" :
            textlist = '00', '00', text, self.fyear, 'O'
            self.snlcdata = self.snlc.SETDATA(self.tqry.Emp, textlist, 'name')
        else:
            self.studid = None
            self.snlc.DeleteAllItems()
            self.snlc.Hide()
            return
        if self.snlcdata:
            self.studid = str(self.snlcdata['esid'])
            self.SNLC_SHOW()
        
    def Name_Text(self, var):
        text = var.get()
        var.set(text)
        if self.ss:
            self.snlc.Clear()
            self.SNLC_SEARCH(text)
            
    def Name_tx_key(self, event):
        key = event.keysym
        text = self.search_tx.GetValue() 
        self.ss = True ### search start
        try:
            self.snlcdata, kidx = self.snlc.KeyMove(key, 'name')     
            self.KUDDP(kidx, self.snlc)          
        except Exception as err :
            kidx = 0
        if self.snlcdata:
            self.studid = str(self.snlcdata['esid'])
            
        if key in ['Return', 'Tab']:
            if not text:
                return
            self.ss = False ### search stop
            
            if not self.snlcdata:
                self.RefreshEntryBG(self.search_tx, self.search_tx)
                return
            self.studid = str(self.snlcdata['esid'])
            self.search_tx.SetValue(self.snlcdata['name'])
            self.snlc.Hide()
            
            
    def KUDDP(self, kidx, wdg):
        snkidx = sum([kidx, wdg.datavarlimit])
        self.kuddp.SetLabel(snkidx)

    def SNLCKEYMOVE(self, wdgname, wdg, row, col, data):
        if wdgname == 'snlc':
            try:
                self.snlcdata = data[row]
            except KeyError:
                return
            if self.snlcdata:
                self.studid = str(self.snlcdata['esid'])
                self.ST_LC_FILL_DATA(esid=self.studid)
                
    def GetLCSelectData(self, ridx, data, evtname):
        row, col, wdg = ridx
        wdgname = self.wdfiddict[wdg]
        if evtname == 'Return':
            self.SNLCKEYMOVE(wdgname, wdg, row, col, data)
            rowdata = data[row]
            self.FilltoNextLC(row, rowdata)
        if evtname in ['Down','Up']:
            self.SNLCKEYMOVE(wdgname, wdg, row, col, data)

    def FilltoNextLC(self, row, data):
        self.SEARCHLC_SHOW()
        if not data:
            data = self.snlc.itemlc_dict[row]
        del self.snlc.itemlc_dict[row]
        resetdata = self.snlc.itemlc_dict
        self.snlc.ReSetData(resetdata)
        self.search_lc.SetUniqueStringItem(0, 'esid', data)
        self.srlist.add(str(data['esid']))
       
    def ON_SNHide(self):
        self.snlc.Hide()
        self.search_lc.Hide()
        
    def ON_Cxb(self):
        self.stid = ''
        self.srlist = set()
        self.search_lc.DeleteAllItems()
        self.close_reg.Disable()
        self.ok.Disable()
        
    def OnStart(self):
        self.snlc.DeleteAllItems()
        self.ENABLE_()    
        self.ST_LC_FILL_DATA()
        self.scxb.SetValue(False)
        
    def ON_ST_Search(self):
        if self.scxb.GetValue() == True:
            frm, tod, fyear, key_val = self.DATE_RANGE_RETURN()
            self.ST_LC_FILL_DATA_SCXB(frm, tod, key_val)  
        else:
            self.ST_LC_FILL_DATA()
       
    def ST_LC_FILL_DATA_SCXB(self, frm, tod, key_val):
        date_  =  self.todaydbf
        index = 0
        select = self.select_tx.GetValue().strip()
        self.st_lc.DeleteAllItems()
        if select == "STUDENT" : 
            format = '%d/%m/%Y %h:%i:%s'
            if not self.studid :
                textlist = frm, tod, self.studid, self.fyear, ''               
            else: ###
                textlist = frm, tod, None, self.fyear, ''
            self.stlcdata = self.st_lc.SETDATA(self.regqry.Stud_Reg_Search_By_Date, textlist, 'name')
            
            self.scxb_ids = []
            for k,v  in self.stlcdata.items():
                self.scxb_ids.append(v['lid'])
            
        if select == "TEACHER":
            if not self.studid :
                textlist = frm, tod, self.studid, self.fyear, 'T'
            else:
                textlist = frm, tod, None, self.fyear, 'T'
            self.stlcdata = self.st_lc.SETDATA(self.regqry.Emp_Reg_Search_By_Date, textlist, 'name')
        if select == "OTHER":
            if not self.studid :
                textlist = frm, tod, self.studid, self.fyear, 'O'
            else:
                textlist = frm, tod, None, self.fyear, 'O'
            self.stlcdata = self.st_lc.SETDATA(self.regqry.Emp_Reg_Search_By_Date, textlist, 'name')
            
    def ST_LC_FILL_DATA(self, esid=None):
        date_  =  self.todaydbf
        format = '%d/%m/%Y'
        if self.select_tx.GetValue().strip() == "STUDENT" :
            textlist = '00', '00', date_, self.fyear, esid
            self.stlcdata = self.st_lc.SETDATA(self.regqry.CheckStudentRegister, textlist, 'name')
            
        if self.select_tx.GetValue().strip() == "TEACHER":
            textlist = '00', '00', date_, self.fyear, esid, 'T'
            self.stlcdata = self.st_lc.SETDATA(self.regqry.CheckTeacherRegister, textlist, 'name')
            
        if self.select_tx.GetValue().strip() == "OTHER" :
            textlist = '00', '00', date_, self.fyear, esid, 'O'
            self.stlcdata = self.st_lc.SETDATA(self.regqry.CheckTeacherRegister, textlist, 'name')
            
    def OnCLOSE_REGISTER(self):
        self.SNLC_HIDE()
        time_ = datetime.now().strftime("%d/%m/%Y  %H:%M:%S") 
        date_  =  self.todaydbf
        mdate = str(date_)+' '+str(time_).split(' ')[1]
        intdate  =  ''.join(str(date_).split('-'))
        select = self.select_tx.GetValue().strip()
        desg = 'T'
        check = self.regqry.GetEmpID(date_)
        fyear = self.fyear
        if check == None:
            self.close_reg.SetLabel('Not Allowed')
        else:
            try:
                mess = RMSMBX(self, text="\n Are you Sure ? \n Want to Close Register\n For Today !\n", info=False,
                  textclr='black', bg='yellow')
                if mess.result == False:
                    return
                if select == "TEACHER":###,"OTHER"]:
                    Atend, Static, desg = 'A', '2017-01-30', 'T'
                elif select == "OTHER":
                    Atend, Static, desg = 'A', '2017-01-30', 'O'
                else:
                    ### Student Query not accepted here
                    return
                rows, emp_rows = self.regqry.Check_Save_Data_Teacher(Atend, date_, date_, desg)
                emplist = []
                for e in emp_rows:
                    emplist.append(e[0])
                eprstlist = []
                for r in rows:
                    eprstlist.append(r[0])
                val = [x for x in emplist if x not in eprstlist ]    
                for r in val: 
                    iddate = str(r)+str(intdate)
                    Attend = 'A'
                    args = r, Attend, mdate, iddate, self.fyear
                    self.regqry.EmrInsert(args,)
            except :
                self.snlc.Hide()
                
        self.search.Disable()
        self.DISABLE_()
        self.close_reg.Disable()
        self.sqry = STU_INFO()
        self.tqry = EMP_INFO()
        self.regqry = REG_REC()
        
    def STUDENT_DATAS_QUERY(self):
        select = self.select_tx.GetValue().strip()
        sval = self.search_tx.GetValue().strip()
        if select == "STUDENT" : 
            self.SNLC_SEARCH('')
        else:
            desg = 'T'
            self.snlc.DeleteAllItems()
            if select == "TEACHER" :
                desg = 'T'
            else:
                desg = 'O'           
            textlist = '00', '00', sval, self.fyear, desg
            self.snlcdata = self.snlc.SETDATA(self.tqry.Emp, textlist, 'name')
            self.SNLC_SHOW()
               
    def DATE_RANGE_RETURN(self):
        get01 = self.from_.GetValue()
        get02 = self.to_.GetValue()
        try:
            frm = datetime.strptime(str(get01), "%d/%m/%Y").strftime("%Y-%m-%d")
            tod = datetime.strptime(str(get02), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print ('rms_register.py error on line 552')
            return None
        fyear = self.fyear
        val = self.class_entry_cb.GetValue()
        key_val = Combox_Val(self, val)
        return frm, tod, fyear, key_val
     
    def OnSave(self):
        self.SNLC_HIDE()
       
        frm, tod, fyear, key_val = self.DATE_RANGE_RETURN()
        time_ = datetime.now().strftime("%d/%m/%Y  %H:%M:%S") 
        date_  =  self.todaydbf
        mdate = str(date_)+' '+str(time_).split(' ')[1]
        intdate  = ''.join(str(date_).split('-'))
        fyear = self.fyear
       
        try:
            if self.select_tx.GetValue().strip() == "STUDENT" : 
               
                for r in self.srlist:
                    iddate = ''.join([str(r),str(intdate)])
                    args = r, mdate.strip(), iddate, self.fyear
                    self.regqry.StrInsert(args,)
            else:
                if not self.srlist :
                    RMSMBX(self, text="\n No Name Selected \n To MARK Present \n", info=True,
                      textclr='red', bg='yellow')
                    return
                
                for r in self.srlist:
                    iddate = ''.join([str(r),str(intdate)])
                    Attend = 'P'
                    args = r, Attend, mdate.strip(), iddate, self.fyear
                    self.regqry.EmrInsert(args,)
                    
        except :
            self.snlc.Hide()
            self.search_lc.Hide()
        self.search.Disable()
        self.DISABLE_()
        if self.select_tx.GetValue().strip() == "TEACHER":
            self.close_reg.Enable()
        self.sqry = STU_INFO()
        self.tqry = EMP_INFO()
        self.regqry = REG_REC()
        
    def ON_GSXLS(self):
        
        rmh = 'ID','Date Time', 'CLASS', 'STUDENT NAME','PARENT NAME',\
                'PHONE ','','',\
                '','',  ''
        a,b,c,d,e,f,g,h,i,j,k,l = 10,10,10,10,10,10,10,10,10,10,10,10
        xone,xtwo,xthr,xfou,xfiv,xsix,xsev,xeig,xnin,xten,xelev, xtwel = [],[],[],[],[],[],[],[],[],[],[],[]
        col_count = self.st_lc.GetItemCount()
        for ro in range(0, col_count):
            xone.append(str(self.st_lc.GetItem(ro, 0).GetText()))
            xtwo.append(str(self.st_lc.GetItem(ro, 1).GetText()))
            xthr.append(str(self.st_lc.GetItem(ro, 2).GetText())+'-'+str(self.st_lc.GetItem(ro, 3).GetText()))
            xfou.append(str(self.st_lc.GetItem(ro, 4).GetText()))
            xfiv.append(str(self.st_lc.GetItem(ro, 5).GetText()))
            xsix.append(str(self.st_lc.GetItem(ro, 6).GetText()))
            
        roW = a,b,c,d,e,f,g,h,i,j,k,l                                       # Cell Gaps after Header, Cells for Middle Data 
        roH = xone,xtwo,xthr,xfou,xfiv,xsix,xsev,xeig,xnin,xten,xelev, xtwel         # LIST for data appended , Middle Data
        FontS = 10,3000,500,4000,4000,1000,1000,1000,1000,1000,1000,1000         # Cell Width for Coloumns
        if self.select_tx.GetValue().strip() == "TEACHER":
            ptitl_ = "TODAYS's EMPLOYEE ATTENDENCE"
            f_name = 'ATTENDENCE_EMPLOYEES_XLS_REPORT'
            repo_text = 'EMPLOYEE_XLS_REPORT'
        else:
            ptitl_ = "TODAYS's ABSENT STUDENTS"
            f_name = 'ABSENT_STUDENTS_XLS_REPORT'
            repo_text = 'STUDENT_XLS_REPORT'
        bt_val = '','','','','','',''   ## Bottom Values in xls file
        self.REPORT_XLS(f_name,ptitl_, repo_text, rmh,bt_val,roW,roH,FontS)
           
    def ON_ASXLS(self):
        rmh = 'ID','CLASS','STUDENT NAME','PARENT NAME',\
                'ADDRESS 1','PHONE 1',\
                'PHONE 2','email','Admission Date', 'DATE OF BIRTH', 'Remark'
        a,b,c,d,e,f,g,h,i,j,k,l = 10,10,10,10,10,10,10,10,10,10,10,10
        xone,xtwo,xthr,xfou,xfiv,xsix,xsev,xeig,xnin,xten,xelev, xtwel = [],[],[],[],[],[],[],[],[],[],[],[]
        regqry = REG_REC()
        status = '0' ### status = '0' Registered ; '1' Pass out
        all_strows = regqry.StuExport(status)
    
        for r in all_strows:
            xone.append(str(r[0]))
            try:
                key_val = Combox_Val_Reverse(str(r[1]))
            except:
                key_val = ''
            xtwo.append(str(key_val)+'-'+str(r[2]))
            xthr.append(str(r[3]))
            xfou.append(str(r[4]))
            xfiv.append(str(r[5]+'; '+r[6]))
            try:
                xsix.append(int(r[7]))
            except:
                xsix.append(str(r[7]))
            try:
                xsev.append(int(r[8]))
            except:
                xsev.append(str(r[8]))
            xeig.append(str(r[9]))
            xnin.append(str(r[10]))
            xten.append(str(r[11]))
            xelev.append(str(r[12]))
        
        roW = a,b,c,d,e,f,g,h,i,j,k,l                                       # Cell Gaps after Header, Cells for Middle Data 
        roH = xone,xtwo,xthr,xfou,xfiv,xsix,xsev,xeig,xnin,xten,xelev, xtwel         # LIST for data appended , Middle Data
        FontS = 10,100,2500,2500,2000,700,400,400,1000,1000,1000,1000         # Cell Width for Coloumns
        ptitl_ = 'STUDENT DATA'
        f_name = 'STUDENT_XLS_REPORT'
        repo_text = 'STUDENT_XLS_REPORT'
        bt_val = '','','','','','',''   ## Bottom Values in xls file
        self.REPORT_XLS(f_name,ptitl_, repo_text, rmh,bt_val,roW,roH,FontS)
       
    def ON_ATXLS(self):
        rmh = 'ID','Desig.','EMPLOYEE NAME','PARENT NAME',\
                'ADDRESS 1','PHONE 1',\
                'PHONE 2','email','JOIN Date', 'DATE OF BIRTH', 'Remark'
        a,b,c,d,e,f,g,h,i,j,k,l = 10,10,10,10,10,10,10,10,10,10,10,10
        xone,xtwo,xthr,xfou,xfiv,xsix,xsev,xeig,xnin,xten,xelev, xtwel = [],[],[],[],[],[],[],[],[],[],[],[]
        regqry = REG_REC()
        status = '0' ### status = '0' Registered ; '1' Pass out
        emp_rows = regqry.EmpExport(status)
        for r in emp_rows:
            xone.append(str(r[0]))
            xtwo.append(str(r[1]))
            xthr.append(str(r[2]))
            xfou.append(str(r[3]))
            xfiv.append(str(r[4]+'; '+r[5]))
            try:
                xsix.append(int(r[6]))
            except:
                xsix.append(str(r[6]))
            try:
                xsev.append(int(r[7]))
            except:
                xsev.append(str(r[7]))
            xeig.append(str(r[8]))
            xnin.append(str(r[9]))
            xten.append(str(r[10]))
            xelev.append(str(r[11]))
        
        roW = a,b,c,d,e,f,g,h,i,j,k,l                                       # Cell Gaps after Header, Cells for Middle Data 
        roH = xone,xtwo,xthr,xfou,xfiv,xsix,xsev,xeig,xnin,xten,xelev, xtwel         # LIST for data appended , Middle Data
        FontS = 10,100,2500,2500,2000,700,400,400,1000,1000,1000,1000         # Cell Width for Coloumns
        ptitl_ = 'EMPLOYEE DATA'
        f_name = 'EMPLOYEE_XLS_REPORT'
        repo_text = 'EMPLOYEE_XLS_REPORT'
        bt_val = '','','','','','',''   ## Bottom Values in xls file
        self.REPORT_XLS(f_name,ptitl_, repo_text, rmh,bt_val,roW,roH,FontS)
        
    def REPORT_XLS(self,f_name,ptitl_, repo_text, rmh,bt_val,roW,roH,FontS):
        import subprocess
        from rmss_config import OWNER_DETAILS
        #repo_text = 'STUDENT_XLS_REPORT'
        export_path = "%s/%s.xls"%(rmss_config.PP_EXPORT, f_name)
        owner, o_add1, o_add2, pphone = OWNER_DETAILS()
        
        #prty_0, prty_1,prty_2 = prty_d
        ##############################################
        hdf,fonth,fonthb,font0,font1 = Font(),Font(),Font(),Font(),Font()
        hdf.name,fonth.name,fonthb.name,font0.name,font1.name = 'Courier-Bold','Arial','Arial','Arial','Times New Roman'
        hdf.bold,fonth.bold,fonthb.bold,font0.bold,font1.bold = True,True,True,True,True
        hstyl,styleh,stylehb,style0,style1 = XFStyle(),XFStyle(),XFStyle(),XFStyle(),XFStyle()
        hstyl.font = hdf
        styleh.font = fonth
        styleh.font.height = 20 * 22
        stylehb.font = fonthb
        style0.font = font0
        style1.font = font1
        hdf.colour_index = 62
        hdf.outline = True
        fonth.colour_index = 30
        fonth.outline = True
        fonthb.colour_index = 30
        fonthb.outline = True
        font0.colour_index = 62
        font0.outline = True
        borders = Borders()
        borders.left = 22
        #style0.borders = borders
        ###############################################
        book = Workbook(encoding="utf-8")

        sheet1 = book.add_sheet("Sheet 1")
        sheet1.protect = True
        
        sheet1.write(1, 3, str(ptitl_),hstyl)
        sheet1.write_merge(2, 3, 2, 4,str(owner),styleh)
        sheet1.write_merge(4, 4, 2, 4, str(o_add1),stylehb)
        sheet1.write_merge(5, 5, 2, 4, str(o_add2),stylehb)
        sheet1.write_merge(6, 6, 2, 4,str(pphone).strip(),stylehb)
        sheet1.write_merge(7, 7, 2, 4, str('---').strip(),stylehb)
        sheet1.write_merge(8, 8, 2, 4, str("%s  "%(repo_text)),stylehb)

        ##sheet1.write_merge(4, 5, 5, 7, str(prty_0),style0)
        ##sheet1.write_merge(6, 7, 5, 7, str(prty_1),style0)
        ##sheet1.write_merge(8, 8, 5, 7, str(prty_2),style0)
        
        one,two,thr,fou,fiv,six,sev,eig,nin,ten,ele = rmh
        sheet1.write(10, 1, str(one),hstyl)
        sheet1.write(10, 2, str(two),hstyl)
        sheet1.write(10, 3, str(thr),hstyl)
        sheet1.write(10, 4, str(fou),hstyl)
        sheet1.write(10, 5, str(fiv),hstyl)
        sheet1.write(10, 6, str(six),hstyl)
        sheet1.write(10, 7, str(sev),hstyl)
        sheet1.write(10, 8, str(eig),hstyl)
        sheet1.write(10, 9, str(nin),hstyl)
        sheet1.write(10, 10, str(ten),hstyl)
        a,b,c,d,e,f,g,h,i,j,k,l = roW
        xone,xtwo,xthr,xfou,xfiv,xsix,xsev,xeig,xnin,xten,xelev,xtwel = roH
        
        try:
            dfmt = 'M/D/YY'
            tfmt = ' '
            c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12 = FontS
            for n in xone:
                style = XFStyle()
                style.num_format_str = dfmt
                a = a+1
                sheet1.write(a, 1, n, style)
                sheet1.col(1).width = 0x0d00 + c1
            for n in xtwo :
                b = b+1
                sheet1.write(b, 2, n)
                sheet1.col(2).width = 0x0d00 + c2
            
            for n in xthr :
                c = c+1
                sheet1.write(c, 3, str(n).strip())
                sheet1.col(3).width = 0x0d00 + c3
            for n in xfou:
                d = d+1
                sheet1.write(d, 4, n)
                sheet1.col(4).width = 0x0d00 + c4
            for n in xfiv:
                e = e+1
                sheet1.write(e, 5, n)
                sheet1.col(5).width = 0x0d00 + c5
            for n in xsix:
                f = f+1
                sheet1.write(f, 6, n)
                sheet1.col(6).width = 0x0d00 + c6
            for n in xsev:
                g = g+1
                sheet1.write(g, 7, n)
                sheet1.col(7).width = 0x0d00 + c7
            for n in xeig:
                h = h+1
                sheet1.write(h, 8, n)
                sheet1.col(8).width = 0x0d00 + c8
            for n in xnin:
                i = i+1
                sheet1.write(i, 9, n)
                sheet1.col(9).width = 0x0d00 + c9
            for n in xten:
                j = j+1
                sheet1.write(j, 10, n)
                sheet1.col(10).width = 0x0d00 + c10

            book.save("%s"%export_path)
            RMSMBX(self, text="\n EXPORTED in FOLDER Named \n Rms_User_Files\n", info=True,
              textclr='red', bg='yellow')
            exppath = 'start %s'%export_path
            subprocess.Popen(exppath,shell=True)
        except IOError as e: 
            RMSMBX(self, text="\n Error Found \n [%s]\n"%str(e), info=True,
              textclr='red', bg='yellow')
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
    sptag = 'Register Entry'
    spnum = 1
    whxy = (sw, sh-70, 0, 0)
    app = rmss_register(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()
"""
