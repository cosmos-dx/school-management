#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import subprocess
import config
from student_sheet_print import Sheet_Print
from class_query import STU_INFO, EMP_INFO, SHEET_REC
from rmss_config import kdwnf
from rmsvalidators import *
from rmsdatepicker import RmsDate, RmsDatePicker
from  datetime import datetime
import string
import config
import rmss_config


def ValueDist1(dist):
    if dist <= 5:
        fare = int(config.Configuration().FARE_MODE1()[1])
        value = 1
    if dist > 5 and dist <= 10:
        fare = int(config.Configuration().FARE_MODE1()[2])
        value = 2
    if dist > 10 and dist <= 15:
        fare = int(config.Configuration().FARE_MODE1()[3])
        value = 3
    if dist > 15:
        fare = int(config.Configuration().FARE_MODE1()[4])
        value = 4
    newval = value * fare
    return newval

def ValueDist2(dist):
    if dist <= 5:
        fare = int(config.Configuration().FARE_MODE2()[1])
        value = 1
    if dist > 5 and dist <= 10:
        fare = int(config.Configuration().FARE_MODE2()[2])
        value = 2
    if dist > 10 and dist <= 15:
        fare = int(config.Configuration().FARE_MODE2()[3])
        value = 3
    if dist > 15:
        fare = int(config.Configuration().FARE_MODE2()[4])
        value = 4
    newval = value * fare
    return newval

def ValueDist3(dist):
    if dist <= 5:
        fare = int(config.Configuration().FARE_MODE3()[1])
        value = 1
    if dist > 5 and dist <= 10:
        fare = int(config.Configuration().FARE_MODE3()[2])
        value = 2
    if dist > 10 and dist <= 15:
        fare = int(config.Configuration().FARE_MODE3()[3])
        value = 3
    if dist > 15:
        fare = int(config.Configuration().FARE_MODE3()[4])
        value = 4
    newval = value * fare
    return newval

class StudentPerformance(Frame):
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
       
        self.editbv = BooleanVar()
        self.edit_update = RMSChkBut(self.master, text='- Edit',
                         variable=self.editbv, **chk_fg_bg)
        self.edit_update.grid(row=wrow, column=10, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        
        self.cbc_dic = {'':0,'YES':1,'NO':2}
        self.cbc_dic_rv = {0:'NO',1:'YES',2:'NO'}
        
        try:
            _con_ = config.Configuration()
            fare1 = _con_.FARE_MODE1()
            fare2 = _con_.FARE_MODE2()
            fare3 = _con_.FARE_MODE3()
            self.cc_dic = {'SELF':0,fare1[0]:1,fare2[0]:2,fare3[0]:3}
            self.cc_dic_rv = {0:'SELF',1:fare1[0],2:fare2[0],3:fare3[0]}
            self.late_fee_date = int(_con_.LATE_FEE_DATE())
        except:
            self.cc_dic = {'SELF':0,'RIKSHAW':1,'AUTO':2,'BUS':3}
            self.cc_dic_rv = {0:'SELF',1:'RIKSHAW',2:'AUTO',3:'BUS'}
            self.late_fee_date = 15
        ############################################################
        self.supid = None
        self.studid = None
        self.transid = None
        self.prymid = None
        self.proid = None
        self.txtID = None
        self.teacid = None
        self.sheetid = None
        self.upd = ''
        self.editonly = False
        self.class_entry_stx = RMS_LABEL(self.master, text='Class Name :', **lfntfg_bgg)
        self.class_entry_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e') 
        self.class_entry_cb = RMSCombobox(self.master, values=Clist, state='readonly', width=6, **combx_fnt)       
        self.class_entry_cb.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.class_entry_cb.current(3)
        
        self.class_sec_stx = RMS_LABEL(self.master, text="Class Section :", **lfntfg_bgg)
        self.class_sec_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e') 
        self.section_tx = RMS_ENTRY(self.master, textvariable=StringVar(), width=5, **efnt_fg_bg)
        self.section_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        self.section_tx.SetValue('A')
        
        wrow += 1
        self.fdate_stx = RMS_LABEL(self.master, text="Date :", **lfntfg_bgg)
        self.fdate_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e') 
        self.fdate_tx = RmsDate(self.master, self.master, self, width=12, **efnt_fgbg)
        self.fdate_tx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.fdate_tx.SetValue(self.today)
        self.date_check_tx = ''
        wrow += 1
        
        self.ptxrows = None
        self.ss = False
        self.namevar = StringVar()
        self.namevar.trace('w', lambda nm, idx, mode, var=self.namevar:
                          self.Student_Name_Text(var))
        self.student_name_stx = RMS_LABEL(self.master, text="Student's Name :", **lfntfg_bgg)
        self.student_name_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e') 
        self.student_name_tx = RMS_ENTRY(self.master, textvariable=self.namevar, **efnt_fg_bg)
        self.student_name_tx.grid(row=wrow, column=2, rowspan=1, columnspan=2, sticky='w')
        self.student_marksheet_stx = RMS_LABEL(self.master, text="", **lfntfg_bgg)
        self.student_marksheet_stx.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        
        self.tc = False
        self.tcnamevar = StringVar()
        self.tcnamevar.trace('w', lambda nm, idx, mode, var=self.tcnamevar:
                          self.Teacher_Name_Text(var))
        self.class_teach_stx = RMS_LABEL(self.master, text="Class Teacher :", **lfntfg_bgg)
        self.class_teach_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e') 
        self.class_teach_tx = RMS_ENTRY(self.master, textvariable=self.tcnamevar, **efnt_fg_bg)
        self.class_teach_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        
        wrow += 1
        rows = 11
        colconf = {0:{'idname':'name','text':'Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
            1:{'idname':'gname','text':'G.Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
            2:{'idname':'add1','text':'Address','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
           }
        
        self.snlc = RMSLBN(self.master, self, True, rows, colconf, **efnt_fg_bg)
        self.snlcpos = {'row':wrow-1, 'column':1, 'columnspan':10, 'rowspan':10, 'sticky':'w'}

        colconf = {0:{'idname':'name','text':'Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},}
        self.tclc = RMSLBN(self.master, self, True, rows, colconf, **efnt_fg_bg)
        self.tclcpos = {'row':wrow-1, 'column':5, 'columnspan':10, 'rowspan':10, 'sticky':'w'}
        wrow += 1

        self.father_name_stx = RMS_LABEL(self.master, text="Guardian's Name :", **lfntfg_bgg)
        self.father_name_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e') 
        self.father_name_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.father_name_tx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')

        self.add_stx = RMS_LABEL(self.master, text="Address :", **lfntfg_bgg)
        self.add_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e') 
        self.add_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.add_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        self.phone_stx = RMS_LABEL(self.master, text="Phone No :", **lfntfg_bgg)
        self.phone_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e') 
        self.phone_tx = NUM_ENTRY(self.master, width=20, **efnt_fg_bg)
        self.phone_tx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        self.hindi_stx = RMS_LABEL(self.master, text='hindi', **lfntfg_bgg)
        self.hindi_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.hindi_tx = FLOAT_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.hindi_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        
        self.english_stx = RMS_LABEL(self.master, text='english', **lfntfg_bgg)
        self.english_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.english_tx = FLOAT_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.english_tx.grid(row=wrow, column=5, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.science_stx= RMS_LABEL(self.master, text='science', **lfntfg_bgg)
        self.science_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.science_tx = FLOAT_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.science_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        
        self.math_stx = RMS_LABEL(self.master, text='math', **lfntfg_bgg)
        self.math_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.math_tx = FLOAT_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.math_tx.grid(row=wrow, column=5, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.sstd_stx = RMS_LABEL(self.master, text='sstd', **lfntfg_bgg)
        self.sstd_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.sstd_tx = FLOAT_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.sstd_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
       
        self.comp_stx = RMS_LABEL(self.master, text='compstx', **lfntfg_bgg)
        self.comp_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.comp_tx = FLOAT_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.comp_tx.grid(row=wrow, column=5, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.bio_stx = RMS_LABEL(self.master, text='biostx', **lfntfg_bgg)
        self.bio_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.bio_tx = FLOAT_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.bio_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        
        self.chem_stx = RMS_LABEL(self.master, text='chemstx', **lfntfg_bgg)
        self.chem_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.chem_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.chem_tx.grid(row=wrow, column=5, rowspan=1, columnspan=4, sticky='w')
        wrow += 1
        
        self.phys_stx = RMS_LABEL(self.master, text='phystx', **lfntfg_bgg)
        self.phys_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.phys_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.phys_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')

        self.sans_stx = RMS_LABEL(self.master, text="sansstx", **lfntfg_bgg)
        self.sans_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.sans_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.sans_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        self.civic_stx = RMS_LABEL(self.master, text='civic', **lfntfg_bgg)
        self.civic_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.civic_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.civic_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')

        self.hist_stx = RMS_LABEL(self.master, text="histstx", **lfntfg_bgg)
        self.hist_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.hist_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.hist_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        self.geog_stx = RMS_LABEL(self.master, text='geog', **lfntfg_bgg)
        self.geog_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.geog_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.geog_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')

        self.comm_stx = RMS_LABEL(self.master, text="commstx", **lfntfg_bgg)
        self.comm_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.comm_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.comm_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        self.sact_stx = RMS_LABEL(self.master, text='sact_stx', **lfntfg_bgg)
        self.sact_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.sact_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.sact_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')

        self.sport_stx = RMS_LABEL(self.master, text="sport_stx", **lfntfg_bgg)
        self.sport_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.sport_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.sport_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        self.other_stx = RMS_LABEL(self.master, text='other_stx', **lfntfg_bgg)
        self.other_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.other_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.other_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')

        self.attend_stx = RMS_LABEL(self.master, text="attend_stx", **lfntfg_bgg)
        self.attend_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.attend_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.attend_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        self.max_mks_ps_ =  RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.max_mks_ps_.SetValue('Max Marks/Subjects :')
        self.max_mks_ps_.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.max_mks_ps =  RMS_ENTRY(self.master, width=10, textvariable=StringVar(), **efnt_fg_bg)
        self.max_mks_ps.SetValue('500')
        self.max_mks_ps.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        
        self.max_mks_tx_ = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg) 
        self.max_mks_tx_.SetValue('Annual Maximum Marks :')
        self.max_mks_tx_.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        self.max_mks_tx = RMS_ENTRY(self.master, width=10, textvariable=StringVar(), **efnt_fg_bg) 
        self.max_mks_tx.SetValue(' ')
        self.max_mks_tx.grid(row=wrow, column=6, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        
        self.close = RMS_BUTTON(self.master, text='Close', bd=3,
                                command=self.OnClose, **bfnt_fg_bg) 
        self.close.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.save = RMS_BUTTON(self.master, text='Save', bd=3,
                                command=self.OnSave, **bfnt_fg_bg)
        self.save.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.update = RMS_BUTTON(self.master, text='Update', bd=3,
                                command=self.OnUpdate, **bfnt_fg_bg)
        self.update.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        self.upgrade = RMS_BUTTON(self.master, text='UpGrade', bd=3,
                                command=self.OnUpgrade, **bfnt_fg_bg)
        self.upgrade.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w')
        self.delete = RMS_BUTTON(self.master, text='Delete', bd=3,
                                command=self.OnDelete, **bfnt_fg_bg)
        self.update.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        self.reset = RMS_BUTTON(self.master, text='Reset', bd=3,
                                command=self.OnReset, **bfnt_fg_bg) 
        self.reset.grid(row=wrow, column=6, rowspan=1, columnspan=1, sticky='w')
        self.prnt = RMS_BUTTON(self.master, text='Print', bd=3,
                                command=self.OnPDF_Print, **bfnt_fg_bg) 
        self.prnt.grid(row=wrow, column=7, rowspan=1, columnspan=1, sticky='w')

        self.annualbv = BooleanVar()
        self.annual_cb = RMSChkBut(self.master, text='- Annual',
                         variable=self.annualbv, **chk_fg_bg)
        self.annual_cb.grid(row=wrow, column=10, rowspan=1, columnspan=1, sticky='w')
        
        wrow += 1
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
        self.eqry = EMP_INFO()
        self.shqry = SHEET_REC()
        self.class_entry_cb.bind('<<ComboboxSelected>>', self.OnClass_entry_cb)
       
        self.father_name_tx.bind('<Key>', self.Father_tx_Key_Enter)
        self.phone_tx.bind('<Key>', self.Phone_tx_Key_Enter)
        self.add_tx.bind('<Key>', self.Add_tx_Key_Enter)
        self.student_name_tx.bind('<Key>', self.student_name_tx_key)
        self.class_teach_tx.bind('<Key>', self.teacher_name_key)
        self.hindi_tx.bind('<Key>', self.First_entry_Text_Enter) 
        self.english_tx.bind('<Key>', self.Second_entry_Text_Enter)
        self.science_tx.bind('<Key>', self.Third_entry_Text_Enter)
        self.math_tx.bind('<Key>', self.Fourth_entry_Text_Enter)
        self.sstd_tx.bind('<Key>', self.Fifth_entry_Text_Enter)
        self.comp_tx.bind('<Key>', self.Sixth_entry_Text_Enter) 
        self.bio_tx.bind('<Key>', self.Seventh_entry_Text_Enter)
        self.chem_tx.bind('<Key>', self.Eighth_entry_Text_Enter)
        self.phys_tx.bind('<Key>', self.Ninth_entry_Text_Enter)

        self.sans_tx.bind('<Key>', self.KeyText10)
        self.civic_tx.bind('<Key>', self.KeyText11)
        self.hist_tx.bind('<Key>', self.KeyText12)
        self.geog_tx.bind('<Key>', self.KeyText13)
        self.comm_tx.bind('<Key>', self.KeyText14)
        self.sact_tx.bind('<Key>', self.KeyText15)
        self.sport_tx.bind('<Key>', self.KeyText16)
        self.other_tx.bind('<Key>', self.KeyText17)
        self.attend_tx.bind('<Key>', self.KeyText18)
        
        self.save.bind('<Key>', self.Onsave_key)
        for r in range(wrow):
            self.master.rowconfigure(r, weight=1)
        for r in range(15):
            self.master.columnconfigure(r, weight=1)
        self.save.Disable()
        self.update.Disable()
        self.upgrade.Disable()
        self.delete.Disable()
        self.RefreshEntryBG(self.class_entry_cb, self.class_entry_cb)
        self.Set_Subjects()
        self.wdfiddict = {self.snlc:'snlc', self.tclc:'tclc',}
        
    def Set_Subjects(self):
        try:
            cls_val = Combox_Val(self, self.class_entry_cb.GetValue().strip())
        except :
            RMSMBX(self, text="\n Class Not Selected \n Select Class  !!\n")
            return
        if int(cls_val) > 5  :
            subj = self.rscr['config']['subjecthigh'] 
        else :
            subj = self.rscr['config']['subjectlow'] 
        if int(cls_val) > 50  :
            subj = self.rscr['config']['subjectlow']         
        ###################################################################################
        self.hindi_stx.SetLabel(str(subj[0])+":")
        
        self.english_stx.SetLabel(str(subj[1])+":")
        
        self.science_stx.SetLabel(str(subj[2])+":")
        
        self.math_stx.SetLabel(str(subj[3])+":")
        
        ###################################################################################
        self.sstd_stx.SetLabel(str(subj[4])+":")
        
        self.comp_stx.SetLabel(str(subj[5])+":")
        
        self.bio_stx.SetLabel(str(subj[6])+":")
        
        #################################################################################################
        self.chem_stx.SetLabel(str(subj[7])+":")
        
        #################################################################################################
        self.phys_stx.SetLabel(str(subj[8])+":")
       
        #################################################################################################
        self.sans_stx.SetLabel(str(subj[9])+":")
        
        #################################################################################################
        self.civic_stx.SetLabel(str(subj[10])+":")
        
        self.hist_stx.SetLabel(str(subj[11])+":")
        
        self.geog_stx.SetLabel(str(subj[12])+":")
        
        self.comm_stx.SetLabel(str(subj[13])+":")
        
        self.sact_stx.SetLabel(str(subj[14])+":")
        
        self.sport_stx.SetLabel(str(subj[15])+":")
        
        self.other_stx.SetLabel(str(subj[16])+":")
        
        self.attend_stx.SetLabel(str(subj[17])+":")
        
    def Father_tx_Key_Enter(self, event=None):
        self.NextFocus(event, self.father_name_tx, self.phone_tx)
        
    def Phone_tx_Key_Enter(self, event=None):
        self.NextFocus(event, self.phone_tx, self.add_tx)
        
    def Add_tx_Key_Enter(self, event=None):
        self.NextFocus(event, self.add_tx, self.hindi_tx)
        
    def First_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.hindi_tx, self.english_tx)

    def Second_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.english_tx, self.science_tx)

    def Third_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.science_tx, self.math_tx)

    def Fourth_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.math_tx, self.sstd_tx)

    def Fifth_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.sstd_tx, self.comp_tx)
   
    def Sixth_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.comp_tx, self.bio_tx)
        
    def Seventh_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.bio_tx, self.chem_tx)

    def Eighth_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.chem_tx, self.phys_tx)

    def Ninth_entry_Text_Enter(self, event=None):
        self.NextFocus(event, self.phys_tx, self.sans_tx)

    def KeyText10(self, event=None):
        self.NextFocus(event, self.sans_tx, self.civic_tx)
    def KeyText11(self, event=None):
        self.NextFocus(event, self.civic_tx, self.hist_tx)
    def KeyText12(self, event=None):
        self.NextFocus(event, self.hist_tx, self.geog_tx)
    def KeyText13(self, event=None):
        self.NextFocus(event, self.geog_tx, self.comm_tx)
    def KeyText14(self, event=None):
        self.NextFocus(event, self.comm_tx, self.sact_tx)
    def KeyText15(self, event=None):
        self.NextFocus(event, self.sact_tx, self.sport_tx)
    def KeyText16(self, event=None):
        self.NextFocus(event, self.sport_tx, self.other_tx)
    def KeyText17(self, event=None):
        self.NextFocus(event, self.other_tx, self.attend_tx)
    def KeyText18(self, event=None):
        self.NextFocus(event, self.attend_tx, self.save)
        
    def NextFocus(self, event, currwdg, nxtwdg):
        text = currwdg.GetValue()
        if event.keysym in ['Return', 'Tab']:
            if text.strip() == '':
                return
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

    def SNLCShow(self):
        if not self.snlcdata:
            self.snlc.Hide()
            return 
        self.snlc.grid(self.snlcpos)
        self.snlc.lift(aboveThis=None)

    def TCLCShow(self):
        if not self.tclcdata:
            self.tclc.Hide()
            return 
        self.tclc.grid(self.tclcpos)
        self.tclc.lift(aboveThis=None)
        
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

    def Teacher_Name_Text(self, var):
        text = var.get()
        var.set(text)
        if self.tc:
            self.tclc.DeleteAllItems()
            textlist = '00', '00', text, self.fyear, 'T', 
            self.tclcdata = self.tclc.SETDATA(self.eqry.Emp, textlist, 'name')  
            self.teacid = str(self.snlcdata['esid'])
            self.TCLCShow()
            
    def KUDDP(self, kidx, wdg):
        snkidx = sum([kidx, wdg.datavarlimit])
        self.kuddp.SetLabel(snkidx)
        ##srn_len = len(wdg.itemlc_dict)

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
                    self.save.Enable()
                    self.CheckMarkSheetStatus()
                    
            if wdgname == 'tclc':
                getrowdata = data[row]
                if getrowdata:
                    self.teacid = str(getrowdata['esid'])
                    self.class_teach_tx.SetValue(self.tclcdata['name'])
                    self.tclc.Hide()
                    
    def DataFill(self, data=None):
        if data:
            d = data
        else:
            d = self.snlcdata
        
        self.ss = False
        self.txtID = d['lid']
        self.student_name_tx.SetValue(d['name'])
        if d['doa']:
            try:
                doa = datetime.strptime(str(d['doa']), "%Y-%m-%d").strftime("%d/%m/%Y")
                self.doa.SetValue(doa)
            except :
                pass
        if d['dob']:
            try:
                dob = datetime.strptime(str(d['dob']), "%Y-%m-%d").strftime("%d/%m/%Y")
                self.dob.SetValue(dob)
            except :
                pass
        if d['dot']:
            try:
                dot = datetime.strptime(str(d['dot']), "%Y-%m-%d").strftime("%d/%m/%Y")
                self.dot.SetValue(dot)
            except:
                pass
        
        self.section_tx.SetValue(d['section']) 
        #self.section_tx.SetValue(d['section']) 
        self.father_name_tx.SetValue(d['gname'])    
        self.add_tx.SetValue(d['add1'])
        #self.add2_tx.SetValue(d['add2'])
        #self.conv_dist_tx.SetValue(d['distance'])
        self.phone_tx.SetValue(d['phone'])
        
    def student_name_tx_key(self, event=None):
        key = event.keysym
        self.save.Enable()
        text = self.student_name_tx.GetValue() 
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
                self.RefreshEntryBG(self.student_name_tx, self.class_teach_tx)
                return
            self.DataFill(data=self.snlcdata)
            self.snlc.Hide()
            self.save.Enable()
            self.studid = str(self.snlcdata['esid'])
            self.CheckMarkSheetStatus()
            self.RefreshEntryBG(self.student_name_tx, self.class_teach_tx)
            
    def CheckMarkSheetStatus(self):
        if self.Getting_TrnasID_For_UPDATE(self.studid, self.fdate_tx.GetValue()):
            self.student_marksheet_stx['fg']='blue'
            self.student_marksheet_stx.SetValue('Data Already Exists !')
            session_start = self.rscr['config']['session'] ###conf.SESSION()
            mkrslt = self.MARKSHEET_QUERY(session_start)
            self.FillSheetData(mkrslt)
        else:
            self.student_marksheet_stx['fg']='red'
            self.student_marksheet_stx.SetValue('Enter Data !')
            self.sheetid = None

    def FillSheetData(self, dd):
        d = dd[0]
        self.hindi_tx.SetValue(d['hindi'])
        self.english_tx.SetValue(d['english'])
        self.science_tx.SetValue(d['science'])
        self.math_tx.SetValue(d['math'])
        self.sstd_tx.SetValue(d['sstd'])
        self.comp_tx.SetValue(d['comp'])
        self.bio_tx.SetValue(d['bio'])
        self.chem_tx.SetValue(d['chem'])
        self.phys_tx.SetValue(d['phys'])
        self.sans_tx.SetValue(d['sans'])
        self.civic_tx.SetValue(d['civic'])
        self.hist_tx.SetValue(d['hist'])
        self.geog_tx.SetValue(d['geog'])
        self.comm_tx.SetValue(d['comm'])
        self.sact_tx.SetValue(d['sact'])
        self.sport_tx.SetValue(d['sport'])
        self.other_tx.SetValue(d['other'])
        self.attend_tx.SetValue(d['attend'])
        dpdate = str(d['sheetdate'])#datetime.strptime(str(d['sheetdate']), "%Y-%m-%d").strftime("%d/%m/%Y")
        self.fdate_tx.SetValue(dpdate)
        
    def teacher_name_key(self, event=None):
        key = event.keysym
        self.save.Enable()
        self.tc = True ### search start
        try:
            self.tclcdata, kidx = self.tclc.KeyMove(key, 'name')     
            self.KUDDP(kidx, self.tclc)          
        except Exception as err :
            kidx = 0
        
        if key in ['Return', 'Tab']:
            self.tc = False ### search stop
            if not self.tclcdata:
                self.RefreshEntryBG(self.student_name_tx, self.student_name_tx)
                return
            self.class_teach_tx.SetValue(self.tclcdata['name'])
            self.tclc.Hide()
            self.save.Enable()
            self.teacid = str(self.tclcdata['esid'])
            self.RefreshEntryBG(self.student_name_tx, self.hindi_tx)


    def Check_Date(self):
        date = self.date_tx.GetValue()
        if date == '':
            RMSMBX(self,text="\n DATE IS EMPTY \n ENTER DATE\n", info=True,
                  textclr='red', bg='yellow')
            self.date_tx.SetFocus()
            
    def OnClass_entry_cb(self, event):
        self.Set_Subjects()
        self.RefreshEntryBG(self.class_entry_cb, self.student_name_tx)
        
    def Onsave_key(self, event):
        if event.keysym in ['Return',]:
            self.OnSave()
            
        if event.keysym in ['Left',]:
            self.close.SetFocus()
        if event.keysym in ['Right',]:
            self.reset.SetFocus()

    def Category_Val(self, cat):
        try:
            str_type = {'A':'0','B':'1','C':'2','D':'3','E':'4','F':'5','G':'6','H':'7','I':'8','J':'9'}
            cat_val = str_type[cat]
            return cat_val
        except :
            self.section_tx.SetValue('A')
            
    def Getting_TrnasID_For_UPDATE(self, stid, date_):
        spdate = str(date_).split('/')
        month = int(spdate[1])
        day = int(spdate[0])
        year = str(spdate[2])
        frmd = str('01')+'/'+str(month)+'/'+str(year)
        fdd = datetime.strptime(str(frmd), "%d/%m/%Y").strftime("%Y-%m-%d")
        tdd = datetime.strptime(str(date_), "%d/%m/%Y").strftime("%Y-%m-%d")
        row = self.shqry.Get_TrnasID(stid, fdd, tdd)
        self.sheetid = None
        if row is not None:
            sheet_upid = row[0]
            self.sheetid = row[0]
        else:
            sheet_upid = 0
      
        return sheet_upid
    
    def OnSave(self):
        val = self.class_entry_cb.GetValue()
        key_val = Combox_Val(self, val)
        classid = key_val
        cat = self.section_tx.GetValue()
        cat_val = self.Category_Val(cat)
        sec = cat_val                       # column name = category in sheet TABLE
        date_ = self.fdate_tx.GetValue()
        fdtx = self.fdate_tx.GetValue()
        try:
            fdate = datetime.strptime(str(fdtx), "%d/%m/%Y").strftime("%Y-%m-%d")
            check = True
        except ValueError:
            check = False
            self.fdate_tx.SetFocus()
            self.save.Disable()
        student_name = self.student_name_tx.GetValue().strip()
        teacher_name = self.class_teach_tx.GetValue().strip()
        stid = str(self.studid)
        tcid = self.teacid
        
        hindi = self.hindi_tx.GetValue().strip()
        eng = self.english_tx.GetValue().strip()
        science = self.science_tx.GetValue().strip()
        math = self.math_tx.GetValue().strip()
        sstd = self.sstd_tx.GetValue().strip()
        comp = self.comp_tx.GetValue().strip()
        bio = self.bio_tx.GetValue().strip()
        chem = self.chem_tx.GetValue().strip()
        phy = self.phys_tx.GetValue().strip()
        sans = self.sans_tx.GetValue().strip()
        civic = self.civic_tx.GetValue().strip()
        hist = self.hist_tx.GetValue().strip()
        geo = self.geog_tx.GetValue().strip()
        comm = self.comm_tx.GetValue().strip()
        sact = self.sact_tx.GetValue().strip()
        sport = self.sport_tx.GetValue().strip()
        other = self.other_tx.GetValue().strip()
        attend = self.attend_tx.GetValue().strip()
        edit_update = self.edit_update.GetValue()
        upd_id = self.upd
        
        if check == True:
            
            mess = RMSMBX(self.master, text="\nSAVE Record ?? \n Confirm !", info=False, pos=(500,350),
                      size=(220, 130),textclr='blue', bg='white')
            fyear = self.fyear
            if mess.result:
                if sec == "" or student_name == ""\
                        or teacher_name == "" or fdate =="" :
                        self.section_tx.SetFocus()
                        self.save.Disable()
                        RMSMBX(self, text="\n Some Fields Are Empty \n Can't Save !\n", info=True,
                          textclr='red', bg='yellow')
                        return
                else:
                    if edit_update == True:
                        upargs = tcid,classid,sec,fdate,hindi,eng,science,math,sstd,comp,bio,\
                                 chem,phy,sans,civic,hist,geo,comm,sact,sport,other,attend,upd_id
                        self.shqry.SheetUpdate(upargs)
                        self.OnPDF_Print()
                        self.ButtonAfterSave()                       
                    else:
                        sheet_upid = self.Getting_TrnasID_For_UPDATE(stid, date_)
                        if sheet_upid == 0:
                            args = (stid,tcid,classid,sec,fdate,hindi,eng,science,math,sstd,comp,bio,
                                   chem,phy,sans,civic,hist,geo,comm,sact,sport,other,attend, fyear)
                            self.shqry.SheetInsert(args)
                            self.OnPDF_Print()
                        else:
                            RMSMBX(self, text="\n Record Already Exist \n of this Month !\n", info=True,
                              textclr='blue', bg='yellow')
                            return
                        self.ButtonAfterSave()         
            else:
                self.close.SetFocus()

    def ButtonAfterSave(self):
        self.save.Disable()
        self.upgrade.Disable()
        self.update.Disable()
        self.delete.Disable()
        self.shqry = SHEET_REC()  ### refreshing class
        self.eqry = EMP_INFO()
        
    def OnDelete(self):
        mess = RMSMBX(self.master, text="\nARE YOU SURE ?? \n DELETE THIS !", info=False, pos=(500,350),
                      size=(220, 130),textclr='red', bg='yellow')
        if mess.result:
            try:
                del_val = self.txtID.GetValue().strip()
                ####Product_Delete(del_val)
                RMSMBX(self, text="\n Not Prepared Yet!!\n", info=True)
                self.Clear_Text()
            except IndexError:
                RMSMBX(self, text="\n Error Found \n Can't Delete\n Try Again Later!!\n", info=True)
               
        self.ButtonAfterSave()
        self.Clear_Text()
        
        self.class_entry_cb.SetFocus()

    def OnUpgrade(self, event=None):
        ##Upgrade_Class().Show()
        RMSMBX(self, text="\n Not Prepared Yet!!\n", info=True)

    def MARKSHEET_QUERY(self,session_start,listdata=False):
        date = self.fdate_tx.GetValue()
        tdate = datetime.strptime(str(date), "%d/%m/%Y").strftime("%Y-%m-%d")
        ttd = str(tdate).split('-')
        if len(session_start) < 2:
                session_start = "%02d" % int(session_start)
        nfdate = '%s-%s-01'%(ttd[0],session_start)
        if ttd[1] < '04':
            nmd = int(ttd[0])-1
            fdate = '%s-%s-01'%(nmd,session_start)
        else:
            
            fdate = nfdate
        stid = self.studid
        if listdata:
            rows = self.shqry.Sheetrec(stid, fdate, tdate)  ## list rows  
        else:
            rows = self.shqry.SheetDictRec(stid, fdate, tdate)  ## dict rows
        return rows
    
    def OnPDF_Print(self):
        self.class_entry_cb.Enable()
        conf = config.Configuration()
        import platform
        ur = platform.uname()[1]
        
        try:
            val1,val2 = config.config_mydb().READ_LICENCE()[0].decode('hex'),config.config_mydb().READ_LICENCE()[1].decode('hex')
            licence_val = val1+val2
        except:
            licence_val = ''
        lic_codes = [platform.uname()[1]+'_DemO_',platform.uname()[1]+'_OnE_',platform.uname()[1]+'_TwO_'
                     ,platform.uname()[1]+'_ThreE_',platform.uname()[1]+'_FouR_']
       
        ifvxtest = True
        if ifvxtest == False:
            return 
        else:
            otest = self.rscr['config']['outoff'] ###conf.OUTOFF_LIST()
            mnth, hlfy, annl = otest[0],otest[1],otest[2]
            session_start = self.rscr['config']['session'] ###conf.SESSION()
            mkrslt = self.MARKSHEET_QUERY(session_start, listdata=True)
            hyanm = self.rscr['config']['an_hy_montn'] ###conf.ANNUAL_HY_MONTH()
            #HY_AN_key = config.MONTHS_HEADINGS()
            #
            #hfyrly = HY_AN_key[int(hyanm[0])]
            #annualy = HY_AN_key[int(hyanm[1])]
            
            try:
                hfyval, annualy = int(hyanm[0]),int(hyanm[1])
                if hfyval > 12 :
                   hfyval = 10
                if annualy > 12 :
                   annualy = 3 
            except:
                hfyval, annualy = 10, 3
            #hfyval = 8 
            
            #hfyval = 10
            """
            if str(hfyrly) ==  'OCTOBER':
                hfyval = 10
            if str(hfyrly) ==  'NOVEMBER':
                hfyval = 11
            if str(hfyrly) ==  'DECEMBER':
                hfyval = 12
            """
            whxy = (self.rscr['sw'], self.rscr['sh']-70, 0, 0)
            self.shpr = Sheet_Print(self.master, 'Sheet Print', 1, 1, self, whxy, rscr=self.rscr)
            

            hindi_stx = self.hindi_stx.GetLabel().strip()
            english_stx = self.english_stx.GetLabel().strip()
            science_stx = self.science_stx.GetLabel().strip()
            math_stx = self.math_stx.GetLabel().strip()
            sstd_stx = self.sstd_stx.GetLabel().strip()
            comp_stx = self.comp_stx.GetLabel().strip()
            bio_stx = self.bio_stx.GetLabel().strip()
            chem_stx = self.chem_stx.GetLabel().strip()
            phys_stx = self.phys_stx.GetLabel().strip()
            sans_stx = self.sans_stx.GetLabel().strip()
            civic_stx = self.civic_stx.GetLabel().strip()
            hist_stx = self.hist_stx.GetLabel().strip()
            geog_stx = self.geog_stx.GetLabel().strip()
            comm_stx = self.comm_stx.GetLabel().strip()
            sact_stx = self.sact_stx.GetLabel().strip()
            sport_stx = self.sport_stx.GetLabel().strip()
            other_stx = self.other_stx.GetLabel().strip()
            attend_stx = self.attend_stx.GetLabel().strip()
            max_mks = self.max_mks_tx.GetValue().strip()
            self.shpr.max_mks_ps_.SetValue(str(self.max_mks_ps_.GetValue().strip()))
            self.shpr.max_mks_ps.SetValue(str(self.max_mks_ps.GetValue().strip()))
            self.shpr.max_mks_tx_.SetValue(str(self.max_mks_tx_.GetValue().strip()))
            self.shpr.max_mks_tx.SetValue(str(self.max_mks_tx.GetValue().strip()))
            #self.shpr.date_range.SetValue(str(self.date_range.GetValue().strip()))
            #self.shpr.date_partition.SetValue(str(self.date_partition.GetValue().strip()))
            #scolSize = [30,50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
            rowLabels = [hindi_stx, english_stx, science_stx, math_stx, sstd_stx, comp_stx,
                         bio_stx, chem_stx, phys_stx, sans_stx, civic_stx, hist_stx, geog_stx,
                         comm_stx, sact_stx, sport_stx, other_stx, attend_stx]
            for row in range(18):
                self.shpr.grid.SetRowLabelValue(row, rowLabels[row])
            #    #self.shpr.grid.SetColSize(row, scolSize[row])           
            self.shpr.name_tx.SetValue(str(self.student_name_tx.GetValue().strip()))
            self.shpr.father_tx.SetValue(str(self.father_name_tx.GetValue().strip()))
            
            self.shpr.class_tx.SetValue(str(self.class_entry_cb.GetValue().strip())) 
            self.shpr.class_sec_tx.SetValue(str(self.section_tx.GetValue().strip()))
            self.shpr.teacher_tx.SetValue(str(self.class_teach_tx.GetValue().strip()))
            self.shpr.date_tx.SetValue(str(self.fdate_tx.GetValue()))
            self.shpr.phone_tx.SetValue(str(self.phone_tx.GetValue()))
            self.shpr.studid = self.studid
            self.shpr.grid.ClearGrid()
            gr_row =  self.shpr.grid.GetNumberRows()
            gr_col =  self.shpr.grid.GetNumberCols()

            for i in range(gr_row):
                for j in range(gr_col):
                    self.shpr.SetCellValue(i,j,str('0.0'))
                    
            ##from config import MONTHS_HEADINGS, REVERSE_MONTHS_HEADINGS
            ##rvmkey = REVERSE_MONTHS_HEADINGS()
            ##mkey = MONTHS_HEADINGS()
            
            rvmkey = rvmkey = self.rscr['config']['rvmonthhead']
            mkey = self.rscr['config']['monthhead'] 
            ##print rvmkey
            rmlist = []
            for cl in range(14):
                colval = self.shpr.grid.GetColLabelValue(cl)
                rmlist.append(colval)
            
            for i in range( len(mkrslt)):
                mthvalue = int(str(mkrslt[i][18]).split('-')[1])
                listidx = rmlist.index(mkey[int(mthvalue)])
                for j in range(0,18):
                    try:
                        self.shpr.grid.SetCellValue(j, listidx, str(format("%.1f" % float(mkrslt[i][j]))))    
                    except ValueError:
                        self.shpr.grid.SetCellValue(j, listidx, '0') 
            gr_row =  self.shpr.grid.GetNumberRows()
            gr_col =  self.shpr.grid.GetNumberCols()

            for all_row in range(0,gr_row):
                #try:
                    gbv0 = self.shpr.grid.GetCellValue(all_row, 0)
                    gbv1 = self.shpr.grid.GetCellValue(all_row, 1)
                    gbv2 = self.shpr.grid.GetCellValue(all_row, 2)
                    gbv3 = self.shpr.grid.GetCellValue(all_row, 3)
                    gbv4 = self.shpr.grid.GetCellValue(all_row, 4)
                    gbv5 = self.shpr.grid.GetCellValue(all_row, 5)
                    gbv6 = self.shpr.grid.GetCellValue(all_row, 6)
                    gbv7 = self.shpr.grid.GetCellValue(all_row, 7)
                    gbv8 = self.shpr.grid.GetCellValue(all_row, 8)
                    gbv9 = self.shpr.grid.GetCellValue(all_row, 9)
                    gbv10 = self.shpr.grid.GetCellValue(all_row, 10)
                    gbv11 = self.shpr.grid.GetCellValue(all_row, 11)

                    if hfyval == 9:
                        gbvalhy = float(gbv0)+float(gbv1)+float(gbv2)+float(gbv3)+float(gbv4)+float(gbv5)
                        self.shpr.grid.SetCellValue(all_row, 12, str(gbvalhy))
                        gbvalan = float(gbvalhy)+float(gbv6)+float(gbv7)+float(gbv8)+float(gbv9)+float(gbv10)+float(gbv11)
                        self.shpr.grid.SetCellValue(all_row, 13, str(gbvalan))
                    if hfyval == 10:
                        gbvalhy = float(gbv0)+float(gbv1)+float(gbv2)+float(gbv3)+float(gbv4)+float(gbv5)+float(gbv6)
                        self.shpr.grid.SetCellValue(all_row, 12, str(gbvalhy))
                        gbvalan = float(gbvalhy)+float(gbv7)+float(gbv8)+float(gbv9)+float(gbv10)+float(gbv11)
                        self.shpr.grid.SetCellValue(all_row, 13, str(gbvalan))
                    if hfyval == 11:
                        gbvalhy = float(gbv0)+float(gbv1)+float(gbv2)+float(gbv3)+float(gbv4)+float(gbv5)+float(gbv6)+float(gbv7)
                        self.shpr.grid.SetCellValue(all_row, 12, str(gbvalhy))
                        gbvalan = float(gbvalhy)+float(gbv8)+float(gbv9)+float(gbv10)+float(gbv11)
                        self.shpr.grid.SetCellValue(all_row, 13, str(gbvalan))
                    if hfyval == 12:
                        gbvalhy = float(gbv0)+float(gbv1)+float(gbv2)+float(gbv3)+float(gbv4)+float(gbv5)+float(gbv6)+float(gbv7)+float(gbv8)
                        self.shpr.grid.SetCellValue(all_row, 12, str(gbvalhy))
                        gbvalan = float(gbvalhy)+float(gbv9)+float(gbv10)+float(gbv11)
                        self.shpr.grid.SetCellValue(all_row, 13, str(gbvalan))
                    
            
            for i in range(gr_row):
                for j in range(gr_col):
                    try:
                        if float(self.shpr.grid.GetCellValue(i,j)) == 0.0 :
                            #print (self.shpr.grid.GetCellValue(i,j))
                            self.shpr.SetCellTextColour(i,j,(wx.WHITE))
                            #self.shpr.grid.SetCellTextColour(i,2,(wx.WHITE))
                        else:
                            pass
                    except ValueError:
                        pass
            
            if self.annual_cb.GetValue() == False:
                for i in range(gr_row):
                    self.shpr.grid.SetCellValue(i,13,('an-2828'))
        
    def check_val(self):
        name = self.student_name_tx.GetValue().upper().strip()
        ftn = self.father_name_tx.GetValue().upper().strip()
        
        add1 = self.add_tx.GetValue().strip()
        phone = self.phone_tx.GetValue().strip()
        
        self.check = True
        if name == '' :
            RMSMBX(self, text="\nName is Empty \n     Check Again !! \n", info=True, textclr='red', bg='white')
            self.name_tx.SetFocus()
            self.delete.Disable()
            self.save.Disable()
            self.check = False
        if ftn == '' :
            RMSMBX(self, text="\nGuardian Name is Empty \n     Check Again !! \n", info=True, textclr='red', bg='white')
            self.father_tx.SetFocus()
            self.delete.Disable()
            self.save.Disable()
            self.check = False
        if add1 == '' :
            RMSMBX(self, text="\nAddress 1 is Empty \n     Check Again !! \n", info=True, textclr='red', bg='white')
            self.add1_tx.SetFocus()
            self.delete.Disable()
            self.save.Disable()
            self.check = False
        if phone == '' :
            RMSMBX(self, text="\nPhone No. is  Empty \n     Check Again !! \n", info=True, textclr='red', bg='white')
            self.phone_tx.SetFocus()
            self.delete.Disable()
            self.save.Disable()
            self.check = False
        else:
            self.check = True
        return self.check
    
    def OnUpdate(self):
        fdtx = self.fdate_tx.GetValue()
        try:
            fdate = datetime.strptime(str(fdtx), "%d/%m/%Y").strftime("%Y-%m-%d")
            check = True
        except ValueError:
            check = False
            self.fdate_tx.SetFocus()
        check = self.edit_update.GetValue()
        if check == True:
            try:
                val = self.class_entry_cb.GetValue()
                key_val = Combox_Val(self, val)
                classid = key_val
                cat = self.section_tx.GetValue()
                cat_val = self.Category_Val(cat)
                sec = cat_val                       # column name = category in sheet TABLE
                stid = self.studid
                tcid = self.teacid
                hindi = self.hindi_tx.GetValue().strip()
                eng = self.english_tx.GetValue().strip()
                science = self.science_tx.GetValue().strip()
                math = self.math_tx.GetValue().strip()
                sstd = self.sstd_tx.GetValue().strip()
                comp = self.comp_tx.GetValue().strip()
                bio = self.bio_tx.GetValue().strip()
                chem = self.chem_tx.GetValue().strip()
                phy = self.phys_tx.GetValue().strip()
                sans = self.sans_tx.GetValue().strip()
                civic = self.civic_tx.GetValue().strip()
                hist = self.hist_tx.GetValue().strip()
                geo = self.geog_tx.GetValue().strip()
                comm = self.comm_tx.GetValue().strip()
                sact = self.sact_tx.GetValue().strip()
                sport = self.sport_tx.GetValue().strip()
                other = self.other_tx.GetValue().strip()
                attend = self.attend_tx.GetValue().strip()
                upd_id = self.upd.GetValue().strip()
                upargs = (tcid,classid,sec,fdate,hindi,eng,science,math,sstd,
                          comp,bio,chem,phy,sans,civic,hist,geo,comm,sact,
                          sport,other,attend,upd_id)
                self.shqry.SheetUpdate(upargs)
                self.Clear_Text()
                self.ButtonAfterSave()        
            except IndexError:
                RMSMBX(self, text="\nError Found \n     Check Again !! \n",
                       info=True, textclr='red', bg='white')
                return
            self.delete.Disable()
            self.update.Disable()
            self.save.Disable()
            self.phys_tx.SetValue("")
            
        else:
            self.sstd_tx.SetFocus()
    
    def OnReset(self):
        self.Clear_Text()
        self.save.Disable()
        self.class_entry_cb.SetFocus()
        self.five_fee_tx.SetValue('0')

    def Clear_Text(self):
        self.txtID = None
        self.supid = None
        self.upd = ''
        self.prymid = None
        self.edit_update.SetValue(False)
        self.father_name_tx.SetValue("")
        self.add_tx.SetValue("")
        self.phone_tx.SetValue("")
        self.hindi_tx.SetValue("0")
        self.english_tx.SetValue('0')
        self.science_tx.SetValue('0')
        self.math_tx.SetValue('0')
        self.sstd_tx.SetValue('0')
        self.comp_tx.SetValue('0')
        self.bio_tx.SetValue('0')
        self.chem_tx.SetValue('0')
        self.phys_tx.SetValue('0')
        self.sans_tx.SetValue('0')
        self.civic_tx.SetValue('0')
        self.hist_tx.SetValue('0')
        self.geog_tx.SetValue('0')
        self.comm_tx.SetValue('0')
        self.sact_tx.SetValue('0')
        self.sport_tx.SetValue('0')
        self.other_tx.SetValue('0')
        self.attend_tx.SetValue('0')
        self.edit_update.SetValue(False)
        self.save.Disable()
        self.update.Disable()
        self.delete.Disable()
        
    def Clear_Student_Fileds(self):
        self.student_name_tx.SetValue("")
        self.prymid = None
        self.supid = None
        self.father_name_tx.SetValue("")
        self.add_tx.SetValue("")
        self.phone_tx.SetValue("")
        self.father_name_tx.Show()
        self.conv_tx.Show()
        self.one_fee_tx.Show()
        self.phone_tx.Show()
        self.add_tx.Show()
        
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
    app = StudentPerformance(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()
"""
