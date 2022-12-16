#!/usr/bin/python
# -*- coding: UTF-8 -*-
#

from class_query import STU_INFO, EMP_INFO, AC_INS_UPD
from rmsvalidators import *
from rmsdatepicker import RmsDate, RmsDatePicker
import config
from datetime import datetime

class student_teacher_ac(Frame):
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
        self.master.title(self.sptag[self.spnum].title())
        wminwidth = 12
        wmaxcolumn = 15
        wmaxrows = 20
        wrow = 1
        self.tcount = 0
        lfnt_fg_bg = {'font': ['Calibri', self.ftsz, 'normal'], 'bg': 'SystemButtonFace', 'fg': 'black'}
        lfntfg_bgg = {'font': ['Calibri', sum([self.ftsz,2]), 'normal'],'bg': 'SystemButtonFace', 'fg':'blue'}
        lb_fg_bg = {'font': ['Courier', self.ftsz, 'bold'], 'bg': '#b0e0e6', 'fg': 'black'} 
        
        botm_fg_bg = {'font':[lfnt_fg_bg['font'][0], sum([int(lfnt_fg_bg['font'][1]),1]), 'bold'],
                      'bg':lfnt_fg_bg['bg'], 'fg':lfnt_fg_bg['fg']}
        btwd = 12
        tot_fg_bg = {'font':[lfnt_fg_bg['font'][0], sum([int(lfnt_fg_bg['font'][1]),11]), 'bold'],
                      'bg':lfnt_fg_bg['bg'], 'fg':lfnt_fg_bg['fg']}
        efnt_fgbg = {'font': ['Courier', self.ftsz, 'bold'], 'bg':'#b0e0e6', 'fg': 'black'}
        efnt_fg_bg = {'font':['Courier',self.ftsz,'bold'],'bg':'#b0e0e6','fg':'black','bd':2}
        bfnt_fg_bg = {'font':['Times New Roman Bold',self.ftsz,'bold'],'bg':'OliveDrab1','fg':'black'} ###self.rscr['font']['button']
        bfnt_fg_bg2 = {'font':['Times New Roman Bold',self.ftsz,'bold'],'fg':'black'} ###self.rscr['font']['button']
        combx_fnt = {'font': ['Courier', self.ftsz, 'bold'],}
        chk_fg_bg = {'font': ['Calibri', self.ftsz, 'normal'], 'bg': 'SystemButtonFace', 'fg': 'black','relief':'raised'}
        if self.whxy:
            self.master.geometry('%dx%d+%d+%d' % self.whxy)
        else:
            self.master.geometry('%dx%d+%d+%d' % (wsw, wsh, xpos, ypos))

        try:
            _con_ = config.Configuration()
            fare1 = _con_.FARE_MODE1()
            fare2 = _con_.FARE_MODE2()
            fare3 = _con_.FARE_MODE3()
            self.cc_dic = {'SELF':0,fare1[0]:1,fare2[0]:2,fare3[0]:3}
            self.cc_dic_rv = {0:'SELF',1:fare1[0],2:fare2[0],3:fare3[0]}
            Conv_CB = ['SELF', fare1[0],fare2[0],fare3[0]]
        except:
            self.cc_dic = {'SELF':0,'RIKSHAW':1,'AUTO':2,'BUS':3}
            self.cc_dic_rv = {0:'SELF',1:'RIKSHAW',2:'AUTO',3:'BUS'}
            Conv_CB = ['SELF','RIKSHAW','AUTO','BUS']
        self.cbc_dic = {'YES':1,'NO':2}
        self.cbc_dic_rv = {1:'YES',2:'NO'}
        Conv_Bool_CB = ['NO','YES']
        self.sqry = STU_INFO() 
        self.tqry = EMP_INFO()
        self.qryiu = AC_INS_UPD()
        
        self.top = RMS_LABEL(self.master, text="".join(['Open ',
                    self.sptag[self.spnum].title(),"'s Account "]), **lfntfg_bgg)
        self.top.grid(row=wrow, column=0, rowspan=1, columnspan=15, sticky='nwes')
        wrow += 1

        self.txtID = None
        self.upd = None
        self.ac_type_tx = self.sptag[self.spnum]
        
        self.name_stx = RMS_LABEL(self.master, text="Name :", **lfnt_fg_bg)
        self.name_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')

        self.ptxrows = None
        self.ss = False
        self.namevar = StringVar()
        self.namevar.trace('w', lambda nm, idx, mode, var=self.namevar:
                          self.name_tx_text(var))
        self.name_tx = RMS_ENTRY(self.master, textvariable=self.namevar, **efnt_fg_bg)
        self.name_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        
        Clist = ['Prep','L.K.G', 'U.K.G', 'I', 'II', 'III', 'IV','V','VI','VII','VIII','IX','X','XI','XII']
        self.class_entry_cb  = RMSCombobox(self.master, values=Clist, state='readonly', width=6, **combx_fnt)
        if self.ac_type_tx == 'student':
            self.class_entry_cb.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w')
        
            self.section_stx = RMS_LABEL(self.master, text="Section :", **lfnt_fg_bg)
            self.section_stx.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='e')
            self.section_tx = RMS_ENTRY(self.master, textvariable=StringVar(), width=5, **efnt_fg_bg)
            self.section_tx.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w')
        elif self.ac_type_tx == 'teacher':
            self.section_tx = RMS_ENTRY(self.master, textvariable=StringVar(), width=5, **efnt_fg_bg)
            #self.section_tx.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w')
            self.section_tx.SetValue('T')
        else:
            self.section_tx = RMS_ENTRY(self.master, textvariable=StringVar(), width=5, **efnt_fg_bg)
            #self.section_tx.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w')
            self.section_tx.SetValue('O')
        rows = 11
        colconf = {0:{'idname':'name','text':'Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
            1:{'idname':'gname','text':'G.Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
            2:{'idname':'add1','text':'Address','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},
           }
        
        self.snlc = RMSLBN(self.master, self, True, rows, colconf, **efnt_fg_bg)
        self.snlcpos = {'row':wrow-1, 'column':1, 'columnspan':15, 'rowspan':10, 'sticky':'w'}
        wrow += 1
        self.doa_stx = RMS_LABEL(self.master, text="Date of Admission :", **lfnt_fg_bg)
        self.doa_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.doa = RmsDate(self.master, self.master, self, width=10, **efnt_fgbg)
        self.doa.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.dot_stx = RMS_LABEL(self.master, text="Date of Transfer:", **lfnt_fg_bg)
        self.dot_stx.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='e')
        self.dot = RmsDate(self.master, self.master, self, width=10, **efnt_fgbg)
        self.dot.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w')        
        wrow += 1
        
        self.dob_stx = RMS_LABEL(self.master, text="Date of Birth :", **lfnt_fg_bg)
        self.dob_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        #self.dob = RmsDate(self.master, self.master, self, width=10, **efnt_fgbg)
        self.dob = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.dob.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.transferbv = BooleanVar()
        self.transfer = RMSChkBut(self.master, text='- Transfering',
                        command=self.OnCB_Trans, variable=self.transferbv, **chk_fg_bg)
        
        self.transfer.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w') 
        wrow += 1
        self.father_stx = RMS_LABEL(self.master, text="Father's Name :", **lfnt_fg_bg)
        self.father_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.father_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.father_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        self.conv_bool_stx = RMS_LABEL(self.master, text="Conv. Mode :", **lfnt_fg_bg)
        self.conv_bool_stx.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='e')
        self.conv_bool_cb = RMSCombobox(self.master, values=Conv_Bool_CB, state='readonly', width=5, **combx_fnt)
        self.conv_bool_cb.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w')
        self.conv_bool_cb.current(0)
        ##self.conv_bool_cb.bind('<Key>', self.Onconv_bool_cbKey)
        wrow += 1
        self.add1_stx = RMS_LABEL(self.master, text="Address 1 :", **lfnt_fg_bg)
        self.add1_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.add1_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.add1_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        wrow += 1
        self.add2_stx = RMS_LABEL(self.master, text="Address 2 :", **lfnt_fg_bg)
        self.add2_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.add2_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.add2_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        self.conv_dist_stx = RMS_LABEL(self.master, text="Dist. Less Than :", **lfnt_fg_bg)
        self.conv_dist_stx.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='e')
        self.conv_dist_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.conv_dist_tx.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w')
        self.conv_dist_tx.SetValue('0')
        wrow += 1
        self.phone_stx = RMS_LABEL(self.master, text="Phone :", **lfnt_fg_bg)
        self.phone_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.phone_tx = NUM_ENTRY(self.master, **efnt_fg_bg)
        self.phone_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        self.phone_stx_mess1 = RMS_LABEL(self.master, text="", **lfnt_fg_bg)
        self.phone_stx_mess1.grid(row=wrow, column=6, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        
        self.email_stx = RMS_LABEL(self.master, text="email :", **lfnt_fg_bg)
        self.email_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.email_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.email_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        wrow += 1
        self.office_stx = RMS_LABEL(self.master, text="Office Phone :", **lfnt_fg_bg)
        self.office_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.office_tx = NUM_ENTRY(self.master, **efnt_fg_bg)
        self.office_tx.grid(row=wrow, column=2, rowspan=1, columnspan=4, sticky='w')
        self.phone_stx_mess = RMS_LABEL(self.master, text="", **lfnt_fg_bg)
        self.phone_stx_mess.grid(row=wrow, column=6, rowspan=1, columnspan=1, sticky='w')
        
        self.conv_stx = RMS_LABEL(self.master, text="Convenience :", **lfnt_fg_bg)
        self.conv_stx.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='e')
        self.conv_cb = RMSCombobox(self.master, values=Conv_CB, state='readonly', width=10, **combx_fnt)
        self.conv_cb.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w')
        self.conv_cb.current(0)
        wrow += 1

        self.cmnt_stx = RMS_LABEL(self.master, text="Comment :", **lfnt_fg_bg)
        self.cmnt_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')
        self.cmnt_tx =RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.cmnt_tx.grid(row=wrow, column=2, rowspan=1, columnspan=3, sticky='w')
        
        wrow += 1
        self.save = RMS_BUTTON(self.master, text='Save', bd=3,
                    command=self.Onsave, **bfnt_fg_bg)
        self.save.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.delete = RMS_BUTTON(self.master, text='Delete', bd=3,
                                 command=self.OnDelBatch, **bfnt_fg_bg)
        self.delete.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        self.close = RMS_BUTTON(self.master, text='Close', bd=3,
                                command=self.OnClose, **bfnt_fg_bg)       
        self.close.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w')
        self.reset = RMS_BUTTON(self.master, text='Reset', bd=3,
                                command=self.OnReset, **bfnt_fg_bg)
        self.reset.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
        self.label_3 = RMS_LABEL(self.master, text='', **lfnt_fg_bg)
        self.editupd = BooleanVar()
        self.edit_update = RMSChkBut(self.master, text='- Edit',
                            variable=self.editupd, **chk_fg_bg)
        self.edit_update.grid(row=wrow, column=9, rowspan=1, columnspan=1, sticky='w')        
        wrow += 1

        btmwg_fg_bg = {'font': ['Courier New', self.ftsz, 'bold'], 'bg': 'SystemButtonFace', 'fg': 'blue'}
        self.kuddp = RMS_LABEL(self.master, text='0', width=12, **btmwg_fg_bg)
        self.kuddp.grid(row=wrow, column=1,)
        self.kuddisplay = RMS_LABEL(self.master, text='0', width=12, **btmwg_fg_bg)
        self.kuddisplay.grid(row=wrow, column=2,)
        wrow += 1
        
        self.status = RMS_LABEL(self.master, text='', **lfnt_fg_bg)
        self.status.grid(row=wrow, column=1, rowspan=1, columnspan=15)
        wrow += 1
       
        self.name_tx.bind('<Key>', self.name_tx_key)
        self.dob.bind('<Key>', self.dobkey)
        self.father_tx.bind('<Key>', self.father_tx_key)
        self.add1_tx.bind('<Key>', self.add1_tx_key)
        self.add2_tx.bind('<Key>', self.add2_tx_key)
        self.phone_tx.bind('<Key>', self.phone_tx_key)
        self.email_tx.bind('<Key>', self.email_tx_key)
        self.office_tx.bind('<Key>', self.office_tx_key)
        self.cmnt_tx.bind('<Key>', self.cmnt_tx_key)
        self.save.bind('<Key>', self.save_key)
        for r in range(wrow):
            self.master.rowconfigure(r, weight=1)
        for r in range(11):
            self.master.columnconfigure(r, weight=1)
        self.RefreshEntryBG(self.name_tx, self.name_tx)
        self.check = False

    def dobkey(self, event=None):
        self.NextFocus(event, self.dob, self.father_tx)

    def father_tx_key(self, event=None):
        self.NextFocus(event, self.father_tx, self.add1_tx)

    def add1_tx_key(self, event=None):
        self.NextFocus(event, self.add1_tx, self.add2_tx)

    def add2_tx_key(self, event=None):
        self.NextFocus(event, self.add2_tx, self.phone_tx)

    def phone_tx_key(self, event=None):
        self.NextFocus(event, self.phone_tx, self.email_tx)

    def email_tx_key(self, event=None):
        self.NextFocus(event, self.email_tx, self.office_tx)
        
    def office_tx_key(self, event=None):
        self.NextFocus(event, self.office_tx, self.cmnt_tx)

    def cmnt_tx_key(self, event=None):
        self.NextFocus(event, self.cmnt_tx, self.save)
        
    def NextFocus(self, event, currwdg, nxtwdg):
        text = currwdg.GetValue()
        if event.keysym in ['Return', 'Tab']:
            if text.strip() == '':
                return
            self.RefreshEntryBG(currwdg, nxtwdg)

    def name_tx_text(self, var):
        text = var.get()
        var.set(text)
        if self.ss:
            self.snlc.Clear()
            self.SNLC_SEARCH(text)
        
    def SNLCShow(self):
        if not self.snlcdata:
            self.snlc.Hide()
            return 
        self.snlc.grid(self.snlcpos)
        self.snlc.lift(aboveThis=None)
  
    def SNLC_SEARCH(self, name):
        
        if name == '':
            self.snlc.Hide()
            return
        self.snlc.DeleteAllItems()
        if self.ac_type_tx == 'student':
            Act = '0' ## 0 for Active Students in School
            Out = '1' ## 1 for OUT Students in School
            val = self.class_entry_cb.GetValue()
            try:
                key_val = Combox_Val(self, val)
            except KeyError:
                mess = RMSMBX(self, text="\n Select Student Class \n Than Search start searching...!!\n", info=True,
                  textclr='blue', bg='yellow')
                self.name_tx.SetValue('')
                return
            section = self.section_tx.GetValue().strip()
            if section == '':
                mess = RMSMBX(self, text="\n Select Student Section \n Than Search start searching...!!\n", info=True,
                  textclr='blue', bg='yellow')
                self.section_tx.SetFocus()
                return
            textlist = '00', '00', name, self.fyear, section, key_val, Act, Out
            self.snlcdata = self.snlc.SETDATA(self.sqry.Stu, textlist, 'name')
            self.SNLCShow()
        if self.ac_type_tx == 'teacher':
            textlist = '00', '00', name, self.fyear, 'T'
            self.snlcdata = self.snlc.SETDATA(self.tqry.Emp, textlist, 'name')
            self.SNLCShow()
            
        if self.ac_type_tx == 'other':
            textlist = '00', '00', name, self.fyear, 'O'
            self.snlcdata = self.snlc.SETDATA(self.tqry.Emp, textlist, 'name')
            self.SNLCShow()
            
    def DataFill(self, data=None):
        if data:
            d = data
        else:
            d = self.snlcdata
        self.ss = False
        self.txtID = d['lid']
        self.name_tx.SetValue(d['name'])
        if d['doa']:
            doa = datetime.strptime(str(d['doa']), "%Y-%m-%d").strftime("%d/%m/%Y")
            self.doa.SetValue(doa)
        if d['dob']:
            dob = datetime.strptime(str(d['dob']), "%Y-%m-%d").strftime("%d/%m/%Y")
            self.dob.SetValue(dob)
        if d['dot']:
            try:
                dot = datetime.strptime(str(d['dot']), "%Y-%m-%d").strftime("%d/%m/%Y")
                self.dot.SetValue(dot)
            except:
                pass
       
        if self.ac_type_tx == 'student':
            self.section_tx.SetValue(d['section']) 
        self.father_tx.SetValue(d['gname'])
        self.add1_tx.SetValue(d['add1'])
        self.add2_tx.SetValue(d['add2'])
        self.conv_dist_tx.SetValue(d['distance'])
        self.phone_tx.SetValue(d['phone'])
        self.office_tx.SetValue(d['office'])
        self.email_tx.SetValue(d['email'])
        self.cmnt_tx.SetValue(d['cmnt'])
        self.conv_cb.current(int(d['convb']))
        try:
            self.conv_bool_cb.current(int(d['convm']))
        except:
            self.conv_bool_cb.current(0)
        self.edit_update.SetValue(True)
        self.edit_update.bg('yellow')
        self.edit_update.fg('blue')
        #doa = datetime.strptime(str(doaa), "%d/%m/%Y").strftime("%Y-%m-%d")
        #dob = datetime.strptime(str(dobb), "%d/%m/%Y").strftime("%Y-%m-%d")

    def KUDDP(self, kidx, wdg):
        snkidx = sum([kidx, wdg.datavarlimit])
        self.kuddp.SetLabel(snkidx)
        srn_len = len(wdg.itemlc_dict)
        
    def name_tx_key(self, event=None):
        key = event.keysym
        self.save.Enable()
        self.ss = True ### search start
        try:
            self.snlcdata, kidx = self.snlc.KeyMove(key, 'name')
            
            self.KUDDP(kidx, self.snlc)          
        except Exception as err :
            kidx = 0
        
        if key in ['Return', 'Tab']:
            self.ss = False ### search stop
            if not self.snlcdata:
                self.dob.SetFocus()
                self.RefreshEntryBG(self.name_tx, self.dob)
                return
            self.DataFill(data=self.snlcdata)
            self.snlc.Hide()

    def GetLCSelectData(self, ridx, data, evtname):
        row, col, wdg = ridx
        if evtname == 'Return':
            getrowdata = data[row]
            if getrowdata:
                self.DataFill(data=getrowdata)
                self.snlc.Hide()
                
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

    def OnReset(self, event=None):
        self.clear_txt()

    def clear_txt(self):
        self.txtID=None
        self.name_tx.SetValue('')
        self.doa.SetValue(self.today)
        self.dob.SetValue(self.today)
        self.dot.SetValue(self.today)
        self.father_tx.SetValue('')
        self.add1_tx.SetValue('')
        self.edit_update.SetValue(False)
        self.edit_update.bg('#b0e0e6')
        self.edit_update.fg('black')
        self.add2_tx.SetValue('')
        self.phone_tx.SetValue('')
        self.office_tx.SetValue('')
        self.email_tx.SetValue('')
        self.cmnt_tx.SetValue('')
        self.conv_cb.current(0)
        self.conv_bool_cb.current(0)
        if self.ac_type_tx == 'student':
            self.section_tx.SetValue('')

    def OnCB_Trans(self):
        if self.transfer.GetValue() :
            RMSMBX(self, text="\nEnter Date of Transfer \n     Check Again !! \n", info=True, textclr='red', bg='white')
          
    def Save_School_t_ac(self, choice, key_val, section, name, ftn, add1, add2, phone, off, email, doa, dob, cmnt, conv, conv_dist, conv_b,):
    
        if choice == 'student':
                ## ACTYPE 1 = TEACHER : ACTYPE 2 = STUDENT :ACTYPE 3 = OTHER
                #actype = 2
                fval = key_val, name, ftn, add1, add2, phone, section, off, email, doa, dob, cmnt, conv, conv_dist, conv_b
                self.qryiu.Stu_Insert(2, fval)
                self.clear_txt()
        if choice == 'teacher':
                ## ACTYPE 1 = TEACHER : ACTYPE 2 = STUDENT: ACTYPE 3 = OTHER
                actype = 1
                fval = section, name, ftn, add1, add2, phone, off, email, doa, dob, cmnt, conv, conv_dist, conv_b
                self.qryiu.Emp_Insert(1, fval)
                self.clear_txt()
        if choice == 'other':
                actype = 3
                fval = 'O', name, ftn, add1, add2, phone, off, email, doa, dob, cmnt, conv, conv_dist, conv_b
                self.qryiu.Emp_Insert(3, fval)
                self.clear_txt()
                
    def Update_School_t_ac(self, choice, key_val, section, name, ftn, add1, add2, phone, off, email, doa, dob, udot,dot_status, cmnt,conv, conv_dist, conv_b,  acid):
        if choice == 'student':
            ### dot_status ; status ;  Student Transfer Status  0 = Active ; 1 = Out
            args = key_val, name, ftn, add1, add2, phone, section, off, dot_status, email, doa, dob, udot, cmnt, conv, conv_dist, conv_b, acid
            self.qryiu.Stu_Update(args)
        if choice == 'teacher':
            ### dot_status ; status ; teacher Transfer Status  0 = Active ; 1 = Out
            args = section, name, ftn, add1, add2, phone, off, dot_status, email, doa, dob, udot,cmnt, acid
            self.qryiu.Emp_Update(args)
        if choice == 'other':
            ### dot_status ; status ; teacher Transfer Status  0 = Active ; 1 = Out
            args = section, name, ftn, add1, add2, phone, off, dot_status, email, doa, dob, udot,cmnt, acid
            self.qryiu.Emp_Update(args)
        self.snlc.Hide()

    def transfer_date(self):
        dot = self.dot.GetValue()
        dott= self.transfer.GetValue()
        if dott == True:
            udot = datetime.strptime(str(dot), "%d/%m/%Y").strftime("%Y-%m-%d")
            dot_status = 1  ### Student Transfer Status  0 = Active ; 1 = Out
        else:
            udot = '0000-00-00'
            dot_status = 0  ### Student Transfer Status  0 = Active ; 1 = Out
        return udot, dot_status

    def save_key(self, event=None):
        if event.keysym in ['Return', 'Tab']:
            self.Onsave(event)
            
    def Onsave(self, event=None):
        key_val = ''
        val = self.class_entry_cb.GetValue()
        if self.ac_type_tx == 'student':
            key_val = Combox_Val(self, val)
        section = self.section_tx.GetValue().strip()
        udot, dot_status = self.transfer_date()
        choice = self.ac_type_tx
        acid = self.txtID
        name = self.name_tx.GetValue().upper()
        ftn = self.father_tx.GetValue().upper()
        add1 = self.add1_tx.GetValue().upper()
        add2 = self.add2_tx.GetValue().upper()
        phone = self.phone_tx.GetValue().upper()
        email = self.email_tx.GetValue()
        off = self.office_tx.GetValue().upper()
        cmnt = self.cmnt_tx.GetValue().upper()
        doaa = self.doa.GetValue()
        dobb = self.dob.GetValue()
        
        doa = datetime.strptime(str(doaa), "%d/%m/%Y").strftime("%Y-%m-%d")
        dob = datetime.strptime(str(dobb), "%d/%m/%Y").strftime("%Y-%m-%d")
         
        edit_update = self.edit_update.GetValue()
        ####################################################
        conv_dist = self.conv_dist_tx.GetValue().strip()        
        conv_b = self.cc_dic[self.conv_cb.GetValue().strip()]
        conv = self.cbc_dic[self.conv_bool_cb.GetValue().strip()]
       
        self.check_val()
        check = self.check
        
        if check == True:
            if edit_update == True:
                result = RMSMBX(self, text="SAVE Record ?? ??\n", info=False, pos=(400,350),
                          size=(220, 130),textclr='white', bg='black')
                if result.result:
                    if not self.txtID:
                        RMSMBX(self, text="No Account Selected ??\n", info=False, pos=(400,350),
                          size=(220, 130),textclr='red', bg='white')
                        return 
                    ##up_val = key_val, name, ftn, add1, add2, phone, off, email, doa, dob, udot, cmnt, acid
                    self.Update_School_t_ac(choice,key_val, section, name, ftn, add1, add2, phone, off, email,
                                            doa, dob, udot, dot_status, cmnt,conv, conv_dist, conv_b, acid)
                else:
                    return
            else:
                result = RMSMBX(self, text="SAVE Record ?? ??\n", info=False, pos=(500,350),
                          size=(220, 130),textclr='white', bg='black')
                if result.result:
                    self.Save_School_t_ac(choice, key_val, section, name, ftn, add1, add2, phone, off, email,
                                          doa, dob, cmnt,conv, conv_dist, conv_b)
                else:
                    return
            self.save.Disable()
            self.edit_update.SetValue(False)
            self.clear_txt()
            self.name_tx.SetFocus()

    def check_val(self):
        name = self.name_tx.GetValue().upper().strip()
        ftn = self.father_tx.GetValue().upper().strip()
        doa = self.doa.GetValue().strip()
        dob = self.dob.GetValue()
        add1 = self.add1_tx.GetValue().strip()
        phone = self.phone_tx.GetValue().strip()
        off = self.office_tx.GetValue().upper().strip()
        self.check = True
        if name == '' :
            RMSMBX(self, text="\nName is Empty \n     Check Again !! \n", info=True, textclr='red', bg='white')
            self.name_tx.SetFocus()
            self.delete.Disable()
            self.save.Disable()
            self.check = False
        if doa == '' :
            RMSMBX(self, text="\Date of Addmission is Empty\n     Check Again !! \n", info=True, textclr='red', bg='white')
            self.doa.SetFocus()
            self.delete.Disable()
            self.save.Disable()
            self.check = False
        if dob == '' :
            RMSMBX(self, text="\nDate of Birth is Empty \n     Check Again !! \n", info=True, textclr='red', bg='white')
            self.dob.SetFocus()
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
        if off == '' :
            RMSMBX(self, text="\nOff.Contact is Empty \n     Check Again !! \n", info=True, textclr='red', bg='white')
            self.office_tx.SetFocus()
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
        
    def OnDelBatch(self, event=None):pass
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
    sptag = {1:'teacher',2:'student',3:'other'}
    spnum = 1
    whxy = (1000, 600, 100, 50)
    app = student_teacher_ac(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()
"""
