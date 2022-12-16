#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

from reportlab.platypus.paragraph import *
from reportlab.platypus.doctemplate import *
from reportlab.platypus.tables import *
from reportlab.lib.colors import *
###import shutil
import string
import num2word
import subprocess
import config
from class_query import FEERECEIPT, CLASS_SELECT, STU_INFO
from rmss_config import kdwnf
from rmsvalidators import *
from class_query import CLASS_SELECT
from rmsdatepicker import RmsDate, RmsDatePicker
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

class FeeReceipt(Frame):
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
        lb_fg_bg = {'font': ['Courier', self.ftsz, 'bold'], 'bg': '#b0e0e6', 'fg': 'black'} 
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
       
        self.receipt_stx = RMS_LABEL(self.master, text="Receipt No :", **lfntfg_bgg)
        self.receipt_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.receipt_tx = RMS_LABEL(self.master, text='', **lfntfg_bgg)
        self.receipt_tx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        
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
        self.upd = ''
        self.editonly = False
        self.class_entry_stx = RMS_LABEL(self.master, text='Class Name :', **lfntfg_bgg)
        self.class_entry_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e') 
        self.class_entry_cb = RMSCombobox(self.master, values=Clist, state='readonly', width=6, **combx_fnt)       
        self.class_entry_cb.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')

        self.class_sec_stx = RMS_LABEL(self.master, text="Class Section :", **lfntfg_bgg)
        self.class_sec_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e') 
        self.section_tx = RMS_ENTRY(self.master, textvariable=StringVar(), width=5, **efnt_fg_bg)
        self.section_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        self.section_tx.SetValue('A')
        
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
    
        self.date_stx = RMS_LABEL(self.master, text="Date :", **lfntfg_bgg)
        self.date_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e') 
        self.date_tx = RmsDate(self.master, self.master, self, width=12, **efnt_fgbg)
        self.date_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        ###self.date_tx.SetValue(self.today)
        wrow += 1
        rows = 11
        colconf = {0:{'idname':'name','text':'Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
            1:{'idname':'gname','text':'G.Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
            2:{'idname':'add1','text':'Address','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
           }
        
        self.snlc = RMSLBN(self.master, self, True, rows, colconf, **efnt_fg_bg)
        self.snlcpos = {'row':wrow-2, 'column':1, 'columnspan':10, 'rowspan':10, 'sticky':'w'}

        self.info_stx = RMS_LABEL(self.master, text="", **lfntfg_bgg)
        self.info_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.info_stx1 = RMS_LABEL(self.master, text="", **lfntfg_bgg)
        self.info_stx1.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        wrow += 1
        
        FEEH =  config.Configuration().FEE_HEADINGS()
        self.conv_stx = RMS_LABEL(self.master, text="Convinence :", **lfntfg_bgg)
        self.conv_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e') 
        self.conv_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.conv_tx.grid(row=wrow, column=2, rowspan=1, columnspan=2, sticky='w')

        self.father_name_stx = RMS_LABEL(self.master, text="Guardian's Name :", **lfntfg_bgg)
        self.father_name_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e') 
        self.father_name_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.father_name_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        self.phone_stx = RMS_LABEL(self.master, text="Phone No :", **lfntfg_bgg)
        self.phone_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e') 
        self.phone_tx = NUM_ENTRY(self.master, width=20, **efnt_fg_bg)
        self.phone_tx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        
        self.add_stx = RMS_LABEL(self.master, text="Address :", **lfntfg_bgg)
        self.add_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e') 
        self.add_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.add_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        FEEH =  config.Configuration().FEE_HEADINGS()
        
        self.one_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[0])+ ":"), **lfntfg_bgg)
        self.one_fee_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.one_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        #self.one_fee_tx = RMS_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.one_fee_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        
        self.two_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[1])+ ":"), **lfntfg_bgg)
        self.two_fee_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.two_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.two_fee_tx.grid(row=wrow, column=5, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.three_fee_stx= RMS_LABEL(self.master, text=(str(FEEH[2])+ ":"), **lfntfg_bgg)
        self.three_fee_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.three_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.three_fee_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        
        self.four_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[3])+ ":"), **lfntfg_bgg)
        self.four_fee_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.four_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.four_fee_tx.grid(row=wrow, column=5, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.five_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[4])+ ":"), **lfntfg_bgg)
        self.five_fee_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.five_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.five_fee_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
       
        self.six_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[5])+ ":"), **lfntfg_bgg)
        self.six_fee_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.six_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.six_fee_tx.grid(row=wrow, column=5, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.seven_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[6])+ ":"), **lfntfg_bgg)
        self.seven_fee_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.seven_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.seven_fee_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        
        self.eight_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[7])+ ":"), **lfntfg_bgg)
        self.eight_fee_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.eight_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.eight_fee_tx.grid(row=wrow, column=5, rowspan=1, columnspan=4, sticky='w')
        wrow += 1
        
        self.nine_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[8])+ ":"), **lfntfg_bgg)
        self.nine_fee_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='e')
        self.nine_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.nine_fee_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')

        self.total_fee_stx = RMS_LABEL(self.master, text="Total Fee", **lfntfg_bgg)
        self.total_fee_stx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='e')
        self.total_fee_tx = RMS_LABEL(self.master, **lfntfg_bgg)
        self.total_fee_tx.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='e')
        
        wrow += 1

        self.close = RMS_BUTTON(self.master, text='Close', bd=3,
                                command=self.OnClose, **bfnt_fg_bg) 
        self.close.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.save = RMS_BUTTON(self.master, text='Save', bd=3,
                                command=self.OnSave, **bfnt_fg_bg)
        self.save.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        
        self.delete = RMS_BUTTON(self.master, text='Delete', bd=3,
                                command=self.OnDelete, **bfnt_fg_bg)
        self.delete.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        self.reset = RMS_BUTTON(self.master, text='Reset', bd=3,
                                command=self.OnReset, **bfnt_fg_bg) 
        self.reset.grid(row=wrow, column=6, rowspan=1, columnspan=1, sticky='w')
        self.prnt = RMS_BUTTON(self.master, text='Print', bd=3,
                                command=self.OnPDF_Print, **bfnt_fg_bg) 
        self.prnt.grid(row=wrow, column=7, rowspan=1, columnspan=1, sticky='w')
         
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
        
        feelst = [self.one_fee_tx, self.two_fee_tx,self.three_fee_tx,self.four_fee_tx,
                self.five_fee_tx,self.six_fee_tx,self.seven_fee_tx, self.eight_fee_tx,
                        self.nine_fee_tx,]
        self.getfeewdgdict = {}
        self.getfeerecdict = {}
        fcount = 1
        for i in range(len(feelst)):
            svar = feelst[i].GetStrVar()
            svar.trace('w', lambda nm, idx, mode, var=svar:
                self.totalcal(var))
            self.getfeewdgdict[str(svar)]=fcount
            fcount += 1
            
        self.clqry = CLASS_SELECT()
        self.frqry = FEERECEIPT()
        self.sqry = STU_INFO() 
        self.class_entry_cb.bind('<<ComboboxSelected>>', self.OnClass_entry_cb)
        self.conv_tx.bind('<Key>', self.Conv_tx_Key_Enter) 
        self.father_name_tx.bind('<Key>', self.Father_tx_Key_Enter)
        self.phone_tx.bind('<Key>', self.Phone_tx_Key_Enter)
        self.add_tx.bind('<Key>', self.Add_tx_Key_Enter)
        self.student_name_tx.bind('<Key>', self.student_name_tx_key)
        
        self.save.bind('<Key>', self.Onsave_key)
        for r in range(wrow):
            self.master.rowconfigure(r, weight=1)
        for r in range(15):
            self.master.columnconfigure(r, weight=1)
        self.save.Disable()
       
        self.delete.Disable()
        self.RefreshEntryBG(self.class_entry_cb, self.class_entry_cb)
        self.Receipt_No_Entery()
        
    def totalcal(self,var):
        wdgnum = self.getfeewdgdict[str(var)]
        
        text = var.get()
        StatusDP(self.status, '', 'blue')
        self.total_fee_tx.SetValue('0')
        if text:
            try:
                ftext = int(text)
                self.getfeerecdict[wdgnum]=ftext
            except Exception :
                StatusDP(self.status, 'Inccorect Format Given, Give Number Only', 'red')
                return
            self.total_fee_tx.SetValue(str(
                sum([v for k,v in self.getfeerecdict.items()])))
        else:
            StatusDP(self.status, 'Empty Fields Not Allowed, Give Number Only', 'red')
            
    def Conv_tx_Key_Enter(self, event=None):
        self.NextFocus(event, self.conv_tx, self.father_name_tx)
        
    def Father_tx_Key_Enter(self, event=None):
        self.NextFocus(event, self.father_name_tx, self.phone_tx)
        
    def Phone_tx_Key_Enter(self, event=None):
        self.NextFocus(event, self.phone_tx, self.add_tx)
        
    def Add_tx_Key_Enter(self, event=None):
        self.NextFocus(event, self.add_tx, self.one_fee_tx)
        
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

    def GetLCSelectData(self, ridx, data, evtname):
        r,c,wdg = ridx
        self.snlcdata = data[r]
        self.OnStudentNameEnter()
        self.snlc.Hide()
        
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

    def Receipt_No_Entery(self):
        brow = self.frqry.Rnum('0')  ### ac_type = '0'
        try:
            brw = brow[0]+1
            r_bil = "%04d" % brw
            nword = 'R-'
            recpt = str(nword)+str(r_bil)
            self.receipt_tx.SetValue(str(recpt))
        except TypeError:
            brw = 1
            r_bil = "%04d" % brw
            nword = 'R-'
            recpt = str(nword)+str(r_bil)
            self.receipt_tx.SetValue(str(recpt))

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
        self.SNLCShow()
        
    def Student_Name_Text(self, var):
        text = var.get()
        var.set(text)
        if self.ss:
            self.snlc.Clear()
            self.SNLC_SEARCH(text)

    def KUDDP(self, kidx, wdg):
        snkidx = sum([kidx, wdg.datavarlimit])
        self.kuddp.SetLabel(snkidx)
        ##srn_len = len(wdg.itemlc_dict)

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
        self.ss = True ### search start
        try:
            self.snlcdata, kidx = self.snlc.KeyMove(key, 'name')     
            self.KUDDP(kidx, self.snlc)          
        except Exception as err :
            kidx = 0
        
        if key in ['Return', 'Tab']:
            self.OnStudentNameEnter()
            
    def OnStudentNameEnter(self, ):
        self.ss = False ### search stop
        if not self.snlcdata:
            self.RefreshEntryBG(self.student_name_tx, self.one_fee_tx)
            return
        self.DataFill(data=self.snlcdata)
        self.snlc.Hide()
        self.OnSnlcData(self.snlcdata)
        self.RefreshEntryBG(self.student_name_tx, self.one_fee_tx)
        
    def IdSearchSetVal(self, stid):
        row = STU_INFO().IdSearch(stid) ### from rmss_dates.py
        self.studid = str(row[0])
        self.student_name_tx.ChangeValue(str(row[1]))
        self.father_name_tx.SetValue(str(row[2]))
        self.add_tx.SetValue(str(row[3]))
        self.phone_tx.SetValue(str(row[5]))
        self.six_fee_stx.SetLabel('By '+str(self.cc_dic_rv[int(row[12])])+' Less Than '+str(row[13])+' '+'Km')
        if int(row[12]) == 0:
            newval = 0
        if int(row[12]) == 1:
            newval = ValueDist1(int(row[13]))
        if int(row[12]) == 2:
            try:
                newval = ValueDist2(int(row[13]))
            except :
                newval = 0
        if int(row[12]) == 3:
            newval = ValueDist3(int(row[13]))
        self.six_fee_tx.SetValue(str(newval))
        self.conv_tx.SetValue(str(self.cbc_dic_rv[int(row[14])]))
        
    def OnSnlcData(self, d):
        edit_update = self.edit_update.GetValue()
        stid = str(d['lid'])
        try:
            date = int(self.date_tx.GetValue().split('/')[0])
        except :
            date = 1
        if date > self.late_fee_date :
            self.four_fee_stx.SetLabel('LATE FEE')
            self.four_fee_stx.fg('red')
        else:
            self.four_fee_stx.SetLabel('Late Fee')
            self.four_fee_stx.fg('black')

        date = self.date_tx.GetValue()
        ndt = str(date).split('/')
        day = '01'
        mm,yy = ndt[1], ndt[2]
        tdat = str(day)+'/'+str(mm)+'/'+str(yy)
        fdate = datetime.strptime(str(tdat), "%d/%m/%Y").strftime("%Y-%m-%d")
        tdate = datetime.strptime(str(date), "%d/%m/%Y").strftime("%Y-%m-%d")
        self.IdSearchSetVal(stid)
        
        if edit_update == True:
            row = self.frqry.OnFeeEdit(stid, fdate, tdate)  
            if row == []:
                self.studid = None
                self.father_name_tx.ChangeValue(str(''))
                self.add_tx.SetValue(str(''))
                self.phone_tx.ChangeValue(str(''))
                self.conv_tx.ChangeValue(str(''))
            else:
                try:
                    self.one_fee_tx.SetValue(str(row[1]))
                    self.two_fee_tx.SetValue(str(row[2]))
                    self.three_fee_tx.SetValue(str(row[3]))
                    self.four_fee_tx.SetValue(str(row[4]))
                    self.five_fee_tx.SetValue(str(row[5]))
                    self.six_fee_tx.SetValue(str(row[6]))
                    self.seven_fee_tx.SetValue(str(row[7]))
                    self.eight_fee_tx.SetValue(str(row[8]))
                    self.nine_fee_tx.SetValue(str(row[9]))
                    rowdate = datetime.strptime(str(row[10]), "%Y-%m-%d" ).strftime("%d/%m/%Y")
                    self.date_tx.SetValue(str(rowdate))
                    self.transid = str(row[11]) 
                except TypeError:
                    self.conv_tx.Hide()
                    self.phone_tx.Hide()
                    return
        else:
            
            trid = self.Getting_TrnasID_For_UPDATE(stid, date)
            self.info_stx.SetLabel('')
            self.info_stx1.SetLabel('')
            if trid != 0:
                self.info_stx.SetLabel('Fee Received')
                self.info_stx.fg('green')
            else:
                self.info_stx.SetLabel('PENDING')
                self.info_stx.fg('red')
                
    def Check_Date(self):
        date = self.date_tx.GetValue()
        if date == '':
            RMSMBX(self,text="\n DATE IS EMPTY \n ENTER DATE\n", info=True,
                  textclr='red', bg='yellow')
            self.date_tx.SetFocus()
            
    def OnClass_entry_cb(self, event):
        val = self.class_entry_cb.GetValue()
        key_val = Combox_Val(self, val)
        row = self.clqry.Select(key_val)
        sec, addf, tutf, mainf, latef, other = row[0], row[1], row[2], row[3], row[4], row[5]
        conv, examf, fee3, fee4 = row[6], row[7], row[8], row[9]
        self.one_fee_tx.SetValue(str(addf))
        self.two_fee_tx.SetValue(str(tutf ))
        self.three_fee_tx.SetValue(str(mainf ))
        self.four_fee_tx.SetValue(str(latef ))
        self.five_fee_tx.SetValue(str( other))
        self.six_fee_tx.SetValue(str(conv ))
        self.seven_fee_tx.SetValue(str(examf ))
        self.eight_fee_tx.SetValue(str(fee3 ))
        self.nine_fee_tx.SetValue(str(fee4 ))
        total=sum([row[i] for i in range(1, len(row))])
        self.total_fee_tx.SetValue(str(total))
        #self.Total_Fee()
        self.RefreshEntryBG(self.class_entry_cb, self.student_name_tx)

    def Total_Fee(self):
        one = self.getfeerecdict[1] ###self.one_fee_tx.GetValue().strip()
        two = self.getfeerecdict[2] ###self.two_fee_tx.GetValue().strip()
        three = self.getfeerecdict[3] ###self.three_fee_tx.GetValue().strip()
        four = self.getfeerecdict[4] ###self.four_fee_tx.GetValue().strip()
        five = self.getfeerecdict[5] ###self.five_fee_tx.GetValue().strip()
        six = self.getfeerecdict[6] ###self.six_fee_tx.GetValue().strip()
        seven = self.getfeerecdict[7] ###self.seven_fee_tx.GetValue().strip()
        eight = self.getfeerecdict[8] ###self.eight_fee_tx.GetValue().strip()
        nine = self.getfeerecdict[9] ###self.nine_fee_tx.GetValue().strip()
        totval = 0
        
        try:
            totval = sum([float(one),float(two),float(three),
                        float(four),float(five),float(six),
                        float(seven),float(eight),float(nine)])
        except (Exception):
            pass
        self.total_fee_tx.SetValue(str(int(totval)))
        return totval
    
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
        except KeyboardInterrupt :
            #self.class_sec_tx.SetFocus()
            self.section_tx.SetValue('A')
            
    def Save_Records(self, args, fyear):
        deb = str(self.Total_Fee())
        self.frqry.FeeInsert(args, deb, fyear)
        self.Receipt_No_Entery()
        
    def Update_Records(self, upargs, trans_upid):
        deb = self.Total_Fee()
        self.frqry.FeeUpdate(deb, upargs, trans_upid, )
        
    def Getting_TrnasID_For_UPDATE(self, ledid, date_):
        fyear = self.fyear
        try:
            spdate = str(date_).split('/')
            month = int(spdate[1])
            day = int(spdate[0])
            year = str(spdate[2])
            frmd = str('01')+'/'+str(month)+'/'+str(year)
            fdd = datetime.strptime(str(frmd), "%d/%m/%Y").strftime("%Y-%m-%d")
            tdd = datetime.strptime(str(date_), "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            return None
        rows = self.frqry.CheckTransFee(fyear, ledid, fdd, tdd)
        if rows is not None:
            trans_upid = rows[0]
        else:
            trans_upid = 0
        
        return trans_upid
    
    def OnSave(self):
        
        edit_update = self.edit_update.GetValue()
        trandid = self.transid  ## Gettinf transid from Getting_TrnasID_For_UPDATE(ledid, date_) function
    
        mess = RMSMBX(self.master, text="\nSAVE Record ?? \n Confirm !", info=False, pos=(500,350),
                      size=(220, 130),textclr='blue', bg='white')
        if mess.result:
            self.save.SetFocus()
            one = self.getfeerecdict[1] ##self.one_fee_tx.GetValue().strip()
            seven = self.getfeerecdict[7] ##self.seven_fee_tx.GetValue().strip()
            eight = self.getfeerecdict[8] ##self.eight_fee_tx.GetValue().strip()
            nine = self.getfeerecdict[9] ##self.nine_fee_tx.GetValue().strip()
            
            if one == "" or seven == "" or eight == "" or nine =="" :
                RMSMBX(self, text="\n Some Fields Are Empty \n Can't Save  !!\n", info=True,textclr='red', bg='yellow')
                return
            else:
                val = self.class_entry_cb.GetValue()
                date_ = self.date_tx.GetValue()
                date = datetime.strptime(str(date_), "%d/%m/%Y").strftime("%Y-%m-%d")
                key_val = Combox_Val(self, val)
                classid = key_val
                cat = self.section_tx.GetValue()
                
                cat_val = self.Category_Val(cat)
                sec = cat_val
                ledid = self.studid
                prym = self.prymid
                two = self.getfeerecdict[2] ###self.two_fee_tx.GetValue().strip()
                three = self.getfeerecdict[3] ###self.three_fee_tx.GetValue().strip()
                four = self.getfeerecdict[4] ###self.four_fee_tx.GetValue().strip()
                five = self.getfeerecdict[5] ###self.five_fee_tx.GetValue().strip()
                six = self.getfeerecdict[6] ###self.six_fee_tx.GetValue().strip()

                #fyear = FYEAR_RETURN(self) ## from rmss_dates.py
                fyear = self.fyear
                
                if edit_update == False:
                    args = ledid,classid, one, two, three, four, five, six, seven, eight, nine, date, fyear
                    trans_upid = self.Getting_TrnasID_For_UPDATE(ledid, date_)
                    if trans_upid == 0:
                        self.Save_Records(args, fyear)
                    else:
                        RMSMBX(self, text="\n Fees Record Already Exist \n of this Month  !!\n", info=True,textclr='blue', bg='yellow')
                else:
                    if self.edit_update.GetValue() == True:
                    #if self.editonly.GetValue().strip()== '':
                        trans_upid = self.Getting_TrnasID_For_UPDATE(ledid, date_)
                        trans_upid = self.transid
                    else:
                        trans_upid = self.transid
                    upargs = classid, one, two, three, four, five, six, seven, eight, nine, date, trans_upid
                    self.Update_Records(upargs, trans_upid)
                
                self.class_entry_cb.SetFocus()
                self.delete.Disable()
               
                self.save.Disable()
                #self.Clear_Text()
                
            self.info_stx.SetLabel('')
            self.info_stx1.SetLabel('')
            self.four_fee_stx.SetLabel('Late Fee:')
            self.four_fee_stx.fg('black')
            self.OnPDF_Print()
            self.frqry = FEERECEIPT()
            
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
               
        self.delete.Disable()
       
        self.save.Disable()
        self.Clear_Text()
        self.frqry = FEERECEIPT()
        self.class_entry_cb.SetFocus()
        
    def OnPDF_Print(self):
        from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
        from reportlab.lib.pagesizes import letter, A6
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        import os, platform
        from reportlab.platypus import SimpleDocTemplate, Image
        from rmss_config import OWNER_DETAILS
        
        WORK_OS = platform.system()   
        conf = config.Configuration()
        if WORK_OS == 'Linux':
            PP_EXPORT = conf.EXPORT_PATH()
            export_path = "%s/Student_Fee_Receipt.pdf"%PP_EXPORT
        if WORK_OS == 'Windows':
            export_path = "%s/Student_Fee_Receipt.pdf"%rmss_config.PP_EXPORT
        else:
            export_path = "%s/Student_Fee_Receipt.pdf"%rmss_config.PP_EXPORT
        #export_path = "%s/Student_Fee_Receipt.pdf"%rmss_config.PP_EXPORT
        #export_path = '/home/sunil/Desktop/Rms_User_Files/Report_Multi_Product_Customer.pdf' # FOR LINUX
        #export_path = "/Users/Sunil/Desktop/Rms_User_Files/Report_Multi_Product_Customer.pdf" # FOR WINDOWS 
        #export_result = wx.MessageBox(
        #       " WANT TO EXPORT ??  ",
        #       "Export Confirmation !", wx.YES_NO |wx.ICON_EXCLAMATION)
        doc = SimpleDocTemplate("%s"%export_path,pagesize=A6,
                        rightMargin=20,leftMargin=20,
                        topMargin=30,bottomMargin=10)
        Story=[]
        ############################################################
        repo_text = "REPORT FROM ==>"
        
        phone = self.phone_tx.GetValue()
        owner, o_add1, o_add2, pphone = OWNER_DETAILS()
        #owner, o_add1, o_add2, pphone = rmss_config.OWNER_DETAILS()
        #tot_stx = self.cvalue_stx.GetLabel()
        #tot = self.cvalue.GetValue()
        #vat = self.svalue.GetValue()
        #sat = self.cvalue.GetValue()
        ###########################################################
        rcpt_stx = self.receipt_stx.GetLabel().strip()
        class_stx = self.class_entry_stx.GetLabel()
        name_stx = self.student_name_stx.GetLabel()
        fatherstx = self.father_name_stx.GetLabel()
        phonestx = self.phone_stx.GetLabel()
        phone = self.phone_stx.GetLabel()
        one_stx = self.one_fee_stx.GetLabel()
        two_stx = self.two_fee_stx.GetLabel()
        three_stx = self.three_fee_stx.GetLabel()
        four_stx = self.four_fee_stx.GetLabel()
        five_stx = self.five_fee_stx.GetLabel()
        six_stx = self.six_fee_stx.GetLabel()
        seven_stx = self.seven_fee_stx.GetLabel()
        eight_stx = self.eight_fee_stx.GetLabel()
        nine_stx = self.nine_fee_stx.GetLabel()
        tot_stx = self.total_fee_stx.GetLabel()
        ################################################################################################
        date = self.date_tx.GetValue()
        rcpt_tx = self.receipt_tx.GetValue().strip()
        class_tx = self.class_entry_cb.GetValue().strip()
        csec = self.section_tx.GetValue().strip()
        name_tx = self.student_name_tx.GetValue().strip()
        father = self.father_name_tx.GetValue().strip()
        phone = self.phone_tx.GetValue().strip()
        one = self.getfeerecdict[1] ###self.one_fee_tx.GetValue().strip()
        two = self.getfeerecdict[2] ###self.two_fee_tx.GetValue().strip()
        three = self.getfeerecdict[3] ###self.three_fee_tx.GetValue().strip()
        four = self.getfeerecdict[4] ###self.four_fee_tx.GetValue().strip()
        five = self.getfeerecdict[5] ###self.five_fee_tx.GetValue().strip()
        six = self.getfeerecdict[6] ###self.six_fee_tx.GetValue().strip()
        seven = self.getfeerecdict[7] ###self.seven_fee_tx.GetValue().strip()
        eight = self.getfeerecdict[8] ###self.eight_fee_tx.GetValue().strip()
        nine = self.getfeerecdict[9] ###self.nine_fee_tx.GetValue().strip()
        tot = self.total_fee_tx.GetValue().strip()
        cls_det = str(class_stx)+''+str(class_tx)+'-'+str(csec)
        
        val = self.class_entry_cb.GetValue()
        try:
            key_val = Combox_Val(self, val)
        except :
            RMSMBX(self, text="\n Nothing To Print \n Select Name and\n Try Again !!\n", info=True)   
            return
        export_result = True
        if export_result == True:
            try:
                num_word = num2word.to_card(float(tot))
                #I = PhotoImage(file="mylogo.jpg") 
                I = Image('bitmaps/mylogo.jpg')
                I.drawHeight = 0.50*inch*I.drawHeight / I.drawWidth
                I.drawWidth = 0.50*inch
                #im = Image.open("/School_RMS/ATP.gif")
                styles=getSampleStyleSheet()
                #styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY)) # (name='Center', alignment=TA_CENTER)
                styles.add(ParagraphStyle( name="ParagraphTitle", fontSize=3, alignment=TA_JUSTIFY, fontName="Courier"))
                ptitl_ = "FEE RECEIPT"
                ptitle = ('<para align=center spaceb=3><font size=6>  %s </font></para>' % (ptitl_))
                
                Story.append(Paragraph(ptitle, styles["Normal"]))
                
                ptext1 = ('<para align=center spaceb=3><font size=11> %s </font></para>' % (owner))
                
                Story.append(Paragraph(ptext1, styles["Normal"]))
                Story.append(Spacer(1, 5))
                
                p0 = I,str(o_add1),str(' ')
                p1 = ' ', str(o_add2+','+pphone),str(' ')
                p2 = str('%s%s'%(rcpt_stx,rcpt_tx)),' ',str('Date : %s'%date)
                pitem0 = [p0,p1,p2]
                t0 = Table(pitem0, colWidths=[50,130,50],rowHeights=[15,10,10])
                t0.setStyle(TableStyle([
                ('FONTSIZE',(0,0),(-1,-1),6),
                ('TEXTFONT',(0,0),(-1,-1),'Courier-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]))
                
                Story.append(t0)
                Story.append(Spacer(1, -11))
                
                ################################################################################################
                static_sp = 58 * "-"
                ptext_body_static_line_0 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                Story.append(Paragraph(ptext_body_static_line_0, styles["Normal"]))
                Story.append(Spacer(1, 0))
                
                ptext_body_static_line_1 = ('''<para align=center spaceb=3><font size=7><font name=Courier>
                 %s <font name=Courier-Bold> %s  </font>%s </font></font></para>''' % (name_stx,name_tx,cls_det))
                Story.append(Paragraph(ptext_body_static_line_1, styles["Normal"]))
                Story.append(Spacer(1, -4))
                
                ptext_body_static_line_3 = ('''<para align=center spaceb=3><font size=7><font name=Courier>
                                %s<font name=Courier-Bold> %s  </font>Phone : %s </font></font></para>''' % (fatherstx,father,phone))                                                             
                Story.append(Paragraph(ptext_body_static_line_3, styles["Normal"]))
                Story.append(Spacer(1, 5))

                #ptext_body_static_line_4 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                #Story.append(Paragraph(ptext_body_static_line_4, styles["Normal"]))
                #Story.append(Spacer(1, -1))
                rdet = 'S.No','PARTICULARS','AMOUNTS'
                pitem1 = [rdet]
                t1 = Table(pitem1, colWidths=[25,165,45],rowHeights=[12])
                t1.setStyle(TableStyle([
                ('FONTSIZE',(0,0),(-1,-1),7),
                ('TEXTFONT',(0,0),(-1,-1),'Courier-Bold'),
                ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                #('BOX', (0,0), (-1,-1), 0.25, colors.Color(0.9,0.9,0.9)), for light white color
                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                ('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
                #('ALIGN', (0,0), (-1,-1), 'CENTER')]))
                Story.append(t1)
                Story.append(Spacer(1, 5))
                
                fp1 = str('1'),str(one_stx),str(one)
                fp2 = str('2'),str(two_stx),str(two)
                fp3 = str('3'),str(three_stx),str(three)
                fp4 = str('4'),str(four_stx),str(four)
                fp5 = str('5'),str(five_stx),str(five)
                fp6 = str('6'),str(six_stx),str(six)
                fp7 = str('7'),str(seven_stx),str(seven)
                
                pitem2 = [fp1,fp2,fp3,fp4,fp5,fp6,fp7]
                t2 = Table(pitem2, colWidths=[25,170,40],rowHeights=[15,15,15,15,15,15,15])
                t2.setStyle(TableStyle([
                ('FONTSIZE',(0,0),(-1,-1),7),
                ('FONTNAME',(0,0),(-1,-1),'Courier-Bold'),
                #('BOX', (0,0), (-1,-1), 0.25, colors.black),
                #('INNERGRID', (0,0), (-1,0), 0.25, colors.black)
                ]))
                Story.append(t2)
                Story.append(Spacer(1, 10))

                ptext_body_static_line_5 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                Story.append(Paragraph(ptext_body_static_line_5, styles["Normal"]))
                Story.append(Spacer(1, -7))
                
                ptext_total = '''<para align=right spaceb=3><font size=7><font name=Courier>
                                %s = </font><font name=Courier-Bold><font size=9> %s</font>
                                </font></font><font size=7><font name=Courier>/-</font></font></para>''' % (tot_stx,tot)
                Story.append(Paragraph(ptext_total, styles["Normal"]))
                Story.append(Spacer(1, -1))

                ptext_body_static_line_6 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                Story.append(Paragraph(ptext_body_static_line_6, styles["Normal"]))
                Story.append(Spacer(1, 0))
                
                ptext_total_w = '''<para align=left spaceb=3><font size=6><font name=Courier>
                                 Rs:<font name=Courier-Bold> %s Only </font></font></font></para>''' % (num_word)
                Story.append(Paragraph(ptext_total_w, styles["Normal"]))
                Story.append(Spacer(1, -1))

                ptext_auth = '''<para align=right spaceb=3><font size=6><font name=Courier>
                                 <font name=Courier-Bold> Authorize Signatory </font></font></font></para>''' 
                Story.append(Paragraph(ptext_auth, styles["Normal"]))
                Story.append(Spacer(1, 1))

                ptext_auth_gap = '''<para align=right spaceb=3><font size=6><font name=Courier>
                                 <font name=Courier-Bold>  </font></font></font></para>''' 
                Story.append(Paragraph(ptext_auth_gap, styles["Normal"]))
                Story.append(Spacer(1, -4))
                
                ptext_auth_1 = '''<para align=right spaceb=3><font size=6><font name=Courier>
                                 <font name=Courier-Bold> __________________ </font></font></font></para>''' 
                Story.append(Paragraph(ptext_auth_1, styles["Normal"]))
                Story.append(Spacer(1, -4))

                ptext_body_static_line_7 = ('<font size=7><font name=Courier> %s </font></font>' % (static_sp))
                Story.append(Paragraph(ptext_body_static_line_7, styles["Normal"]))
                Story.append(Spacer(1, -4))
                
                bott_sg = "+++ DEVELOPED By RMS Deoria 9935188831 +++"
                ptext_sign = ('<para align=left spaceb=3><font size=5><font name=Courier-Bold> %s </font></font></para>' % (bott_sg))
                Story.append(Paragraph(ptext_sign, styles["Normal"]))
                Story.append(Spacer(1, -1))
                doc.build(Story)
                #wx.MessageBox("File EXPORTED AS 'Rms_User_Files/User_Report'","SUCESSES !! ",wx.ICON_INFORMATION)
            except (IOError,ValueError)as e: 
                wx.MessageBox("ERROR %s"%e, "Export File Already OPEN or Nothing to Print", wx.ICON_INFORMATION)
                self.add.SetFocus()
            if WORK_OS == 'Linux':
                subprocess.call(['xdg-open',export_path])
            if WORK_OS == 'Windows':
                exppath = 'start %s'%export_path
                dc = subprocess.Popen(exppath,shell=True)
                dc.wait()
            else:
                #subprocess.call(['start',export_path])
                exppath = 'start %s'%export_path
                dc = subprocess.Popen(exppath,shell=True)
                dc.wait()
                #os.system('start %s'%export_path)

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
        self.conv_tx.SetValue("")        
        self.one_fee_tx.SetValue('0')
        self.two_fee_tx.SetValue('0')
        self.three_fee_tx.SetValue('0')
        self.four_fee_tx.SetValue('0')
        self.five_fee_tx.SetValue('0')
        self.six_fee_tx.SetValue('0')
        self.seven_fee_tx.SetValue('0')
        self.eight_fee_tx.SetValue('0')
        self.nine_fee_tx.SetValue('0')      
        self.five_fee_tx.SetValue('0')
        self.six_fee_tx.SetValue('0')        
        self.total_fee_tx.SetValue('0')
        self.save.Disable()
        self.getfeerecdict = {} 
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
    
    rscr = {'sw':sw, 'sh':sh, 'font':fontd,'sysfontnum':int(sysfontnum), 'ownerdict':ownerdict, 'mycalendar':mycalendar,
            'fyear':'0', 'daterange':['2000-01-01','2021-03-31'],
            'daterange':{'fy':'fy6','dbfrm':'2021-04-01','frm':'01/04/2021','tod':'31/03/2022','partnum':'','dbtod':'2022-03-31'},
            'ledgerid':'0','itemid':'0','transid':'0','spid':'0','csid':'0','csname':'',
            'rmspath':rmspath,'rmsicon':rmsicon, 'pardir': rmspath, 'prpath':prpath,'taxinfo':taxinfo,'printerinfo': printerinfo,
            'TABLENUM':'','today':today, 'today_db_format':today_db_f,'tax1':'0', 'tax2':'0',
            'the_time':'', 'itemidlist':[], 'spidlist':[],'renderlist':[],
            'taxinvoice':True,'stkmess':'YES','decimalval':'2','last_esti_no':None, 'last_sale_bill_no':None,
            'exp_alert':90,'estifilter':False, }
    buttonidx = 1
    parent = None
    sptag = 'FEES RECEIPTS'
    spnum = 1
    whxy = (sw, sh-70, 0, 0)
    app = FeeReceipt(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()

"""
