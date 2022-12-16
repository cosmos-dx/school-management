#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

from rmsvalidators import *
from class_query import CLASS_SELECT
import string
import config


class FeeMaster(Frame):
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
        self.proid = RMS_LABEL(self.master, text='', **lfntfg_bgg)
        self.proid.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w')
        self.txtID = RMS_LABEL(self.master, text='', **lfntfg_bgg)
        self.txtID.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w')                
        self.upd = RMS_LABEL(self.master, text='', **lfntfg_bgg)
        wrow += 1

        self.class_entry_stx = RMS_LABEL(self.master, text='Class Name :', **lfntfg_bgg)
        self.class_entry_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e') 
        self.class_entry_cb = RMSCombobox(self.master, values=Clist, state='readonly', width=6, **combx_fnt)       
        self.class_entry_cb.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        
        self.total_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.total_fee_tx.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w')
        self.total_fee_stx = RMS_LABEL(self.master, text=":Maximum Fee", **lfntfg_bgg)
        #self.total_fee_stx.grid(row=wrow, column=6, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        FEEH =  config.Configuration().FEE_HEADINGS()

        self.one_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[0])+ ":"), **lfntfg_bgg)
        self.one_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.one_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.one_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.two_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[1])+ ":"), **lfntfg_bgg)
        self.two_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.two_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.two_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.three_fee_stx= RMS_LABEL(self.master, text=(str(FEEH[2])+ ":"), **lfntfg_bgg)
        self.three_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.three_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.three_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.four_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[3])+ ":"), **lfntfg_bgg)
        self.four_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.four_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.four_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.five_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[4])+ ":"), **lfntfg_bgg)
        self.five_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.five_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.five_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        self.six_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[5])+ ":"), **lfntfg_bgg)
        self.six_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.six_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.six_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        
        self.prymid = RMS_LABEL(self.master, **lfntfg_bgg)
        self.prymid.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='w')
        wrow += 1

        self.seven_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[6])+ ":"), **lfntfg_bgg)
        self.seven_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.seven_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.seven_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        wrow += 1
        
        self.eight_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[7])+ ":"), **lfntfg_bgg)
        self.eight_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.eight_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.eight_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        wrow += 1
        
        self.nine_fee_stx = RMS_LABEL(self.master, text=(str(FEEH[8])+ ":"), **lfntfg_bgg)
        self.nine_fee_stx.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='e')
        self.nine_fee_tx = NUM_ENTRY(self.master, width=10, **efnt_fg_bg)
        self.nine_fee_tx.grid(row=wrow, column=3, rowspan=1, columnspan=4, sticky='w')
        wrow += 1

        ####################################
        self.feelst = [self.one_fee_tx, self.two_fee_tx,self.three_fee_tx,self.four_fee_tx,
                self.five_fee_tx,self.six_fee_tx,self.seven_fee_tx, self.eight_fee_tx,
                        self.nine_fee_tx,]
        self.getfeewdgdict = {}
        self.getfeerecdict = {}
        fcount = 1
        for i in range(len(self.feelst)):
            svar = self.feelst[i].GetStrVar()
            svar.trace('w', lambda nm, idx, mode, var=svar:
                self.totalcal(var))
            self.getfeewdgdict[str(svar)]=fcount
            fcount += 1

        ###################################
            
            
        self.close = RMS_BUTTON(self.master, text='Close', bd=3,
                                command=self.OnClose, **bfnt_fg_bg) 
        self.close.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.save = RMS_BUTTON(self.master, text='Save', bd=3,
                                command=self.OnUpdate, **bfnt_fg_bg)
        self.save.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        self.reset = RMS_BUTTON(self.master, text='Reset', bd=3,
                                command=self.OnReset, **bfnt_fg_bg) 
        self.reset.grid(row=wrow, column=4, rowspan=1, columnspan=1, sticky='w')
               
        self.edit_stx = RMS_LABEL(self.master, text="", **lfntfg_bgg)
        self.edit_stx.grid(row=wrow, column=7, rowspan=1, columnspan=1, sticky='w')
        self.supid = RMS_LABEL(self.master, **lfntfg_bgg)
        self.supid.grid(row=wrow, column=8, rowspan=1, columnspan=1, sticky='w')
        wrow += 1
        
        self.status = RMS_LABEL(self.master, text='', **lfnt_fg_bg)
        self.status.grid(row=wrow, column=1, rowspan=1, columnspan=15)
        wrow += 2

        self.clqry = CLASS_SELECT()
        self.class_entry_cb.bind('<<ComboboxSelected>>', self.OnClass_entry_cb)
       
        self.save.bind('<Key>', self.Onsave_key)
        for r in range(wrow):
            self.master.rowconfigure(r, weight=1)
        for r in range(8):
            self.master.columnconfigure(r, weight=1)
        self.RefreshEntryBG(self.class_entry_cb, self.class_entry_cb)

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
            
    def OnClass_entry_cb(self, event):
        val = self.class_entry_cb.GetValue()
        key_val = Combox_Val(self, val)
        row = self.clqry.Select(key_val)
        i = 1
        for f in (self.feelst):
            f.SetValue(str(row[i]))
            i += 1
        self.save.Enable()
        self.one_fee_tx.SetFocus()
        

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
            totval = float(one)+float(two)+float(three)+float(four)+float(five)+float(six)+float(seven)+float(eight)+float(nine)
        except KeyboardInterrupt:
            pass
        self.total_fee_tx.SetValue(str(int(totval)))
        
    def Onsave_key(self, event):
        if event.keysym in ['Return',]:
            self.OnUpdate()
        if event.keysym in ['Left',]:
            self.close.SetFocus()
        if event.keysym in ['Right',]:
            self.reset.SetFocus()
            
    def OnUpdate(self):
        try:
            val = self.class_entry_cb.GetValue()
            key_val = Combox_Val(self, val)
            prym = self.prymid.GetValue().strip()    
            one = self.getfeerecdict[1] ###self.one_fee_tx.GetValue().strip()
            two = self.getfeerecdict[2] ###self.two_fee_tx.GetValue().strip()
            three = self.getfeerecdict[3] ###self.three_fee_tx.GetValue().strip()
            four = self.getfeerecdict[4] ###self.four_fee_tx.GetValue().strip()
            five = self.getfeerecdict[5] ###self.five_fee_tx.GetValue().strip()
            six = self.getfeerecdict[6] ###self.six_fee_tx.GetValue().strip()
            seven = self.getfeerecdict[7] ###self.seven_fee_tx.GetValue().strip()
            eight = self.getfeerecdict[8] ###self.eight_fee_tx.GetValue().strip()
            nine = self.getfeerecdict[9] ###self.nine_fee_tx.GetValue().strip()
        
            args = one, two, three, four, five, six, seven, eight, nine, key_val
            self.clqry.Update(args)
            self.clqry = CLASS_SELECT() ### refreshing class
        except Exception as err:
            RMSMBX(self, text="\n Error Found While Update Records \n [%s]\n"%str(err), info=True,
                  textclr='red', bg='yellow')
            self.save.Enable()
            return  
        self.save.Disable()
        self.class_entry_cb.SetFocus()
    
    def OnReset(self):
        self.Clear_Text()
        self.save.Disable()
        self.class_entry_cb.SetFocus()
        self.five_fee_tx.SetValue('0')

    def Clear_Text(self):
        self.txtID.SetValue('')
        for f in self.feelst:
            f.SetValue('0')
        self.supid.SetValue('')
        self.upd.SetValue('')
        self.prymid.SetValue('')
        self.total_fee_tx.SetValue('0')
        
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
    sptag = 'MASTER FEES ENTERY'
    spnum = 1
    whxy = (800, 600, 100, 50)
    app = FeeMaster(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()
"""
