#!/usr/bin/python
# -*- coding: UTF-8 -*-



import os
from rmsvalidators import *
from class_query import STU_INFO

class Upgrade_Class(Frame):
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
        lb_fg_bg = {'font': ['Courier', self.ftsz, 'bold'], 'bg':'#b0e0e6', 'fg': 'black'} 
        topbg = {'font': ['Calibri', sum([self.ftsz,2]), 'bold'], 'bg': 'SystemButtonFace', 'fg':'red'}
        lfnt_fg_bg = {'font': ['Calibri', self.ftsz, 'normal'], 'bg': 'SystemButtonFace', 'fg': 'black'}
        lfntfg_bgg = {'font': ['Calibri', sum([self.ftsz,2]), 'normal'],'bg': 'SystemButtonFace', 'fg':'blue'}
        bfnt_fg_bg = {'font':['Times New Roman Bold',self.ftsz,'bold'],'bg':'OliveDrab1','fg':'black'} ###self.rscr['font']['button']
        combx_fnt = {'font': ['Courier', self.ftsz, 'bold'],}
        efnt_fg_bg = {'font':['Courier',self.ftsz,'bold'],'bg':'#b0e0e6','fg':'black','bd':2}
        
        if self.whxy:
            self.master.geometry('%dx%d+%d+%d' % self.whxy)
        else:
            self.master.geometry('%dx%d+%d+%d' % (wsw, wsh, xpos, ypos))
        wrow +=1
        self.top = RMS_LABEL(self.master, text="ALERT >> UPGRADE FROM HEIGHER TO LOWER CLASS", **topbg)
        self.top.grid(row=wrow, column=0, rowspan=1, columnspan=15, sticky='nwes')
        wrow += 1
        self.top2 = RMS_LABEL(self.master, text="Example >> First UPGRADE  10th Class Then 9th Then 8th then 7th", **lfntfg_bgg)
        self.top2['fg']='red'
        self.top2.grid(row=wrow, column=0, rowspan=1, columnspan=15, sticky='nwes')
        wrow += 1

        self.class_entry_stx = RMS_LABEL(self.master, text='Class Name :', **lfntfg_bgg)
        self.class_entry_stx.grid(row=wrow, column=1, rowspan=1, columnspan=1, sticky='w') 
        self.class_entry_cb = RMSCombobox(self.master, values=Clist, state='readonly', width=6, **combx_fnt)       
        self.class_entry_cb.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.class_entry_cb.current(3)

        self.class_txt = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        self.class_txt.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        
        wrow += 1
        self.studid = 0
        self.name_tx = RMS_ENTRY(self.master, textvariable=StringVar(), **efnt_fg_bg)
        
        rows = 11
        colconf = {0:{'idname':'name','text':'Name','width':30,'bd':2,'bg':'white','fg':'black','font':lb_fg_bg,'relief':'raised',},}
            
        self.snlc = RMSLBN(self.master, self, True, rows, colconf, **efnt_fg_bg)
        self.snlcpos = {'row':wrow-1, 'column':3,'columnspan':8,'rowspan':rows, 'sticky':'w'}

        wrow += rows
        self.close = RMS_BUTTON(self.master, text='Close', bd=3,
                                command=self.OnClose, **bfnt_fg_bg)       
        self.close.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='w')
        self.upall = RMS_BUTTON(self.master, text='UPGRADE ALL', bd=3,
                    command=self.OnUPALL, **bfnt_fg_bg)
        self.upall.grid(row=wrow, column=2, rowspan=1, columnspan=1, sticky='w')
        self.upone = RMS_BUTTON(self.master, text='UPGRADE ONE', bd=3,
                                 command=self.OnUPONE, **bfnt_fg_bg)
        self.upone.grid(row=wrow, column=3, rowspan=1, columnspan=1, sticky='w')
        
        self.save = RMS_BUTTON(self.master, text='SAVE', bd=3,
                                command=self.OnSave, **bfnt_fg_bg)
        self.save.grid(row=wrow, column=5, rowspan=1, columnspan=1, sticky='w')
          
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
        for r in range(wrow):
            self.master.rowconfigure(r, weight=1)
        for r in range(6):
            self.master.columnconfigure(r, weight=1)
        self.sqry = STU_INFO()
        self.wdfiddict = {self.snlc:'snlc'}
        self.collectids = set()
        self.upgradeall = False
        
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
            
            return
        
        textlist = '00', '00', '', self.fyear, 'ledgerID', '', key_val, '0', '0'
        self.snlcdata = self.snlc.SETDATA(self.sqry.Student_Data_Fill_UG, textlist, 'name')
        if self.snlcdata:
            self.studid = str(self.snlcdata['esid'])
            self.SNLCShow()
        
    def GetLCSelectData(self, ridx, data, evtname):
        row, col, wdg = ridx
        if evtname == 'Return':
            wdgname = self.wdfiddict[wdg]
            if wdgname == 'snlc':
                getrowdata = data[row]
                if getrowdata:
                    self.studid = str(getrowdata['esid'])
                    self.collectids.add(self.studid)
                    self.SNLC_SEARCH('')
                    self.class_txt.SetValue(getrowdata['name'])
                    
    def OnUPALL(self):
        self.OnUPONE()
        self.collectids = [v['esid'] for k,v in self.snlc.itemlc_dict.items()]
        self.upgradeall = True
        
    def OnUPONE(self):
        self.SNLC_SEARCH('')
        self.upgradeall = False
        
    def OnSave(self):
        logid = self.class_txt.GetValue()
        oldpass = self.name_tx.GetValue()
        val = self.class_entry_cb.GetValue()
        key_val = Combox_Val(self, val)
        
        if key_val == '52':
            classid = '1'
        else:
            kval = int(float(key_val))
            clid = sum([kval,1]) 
            classid = str(clid)
        mess = RMSMBX(self.master, text="\n Are You Sure ??\n UpGrade Student to\n Next Class \n"
                      "Action Will Not Reverse !\n", info=False, pos=(500,350),
                          size=(220, 130),textclr='red', bg='yellow')
        if mess.result:
            try:
                if self.upgradeall:
                    self.sqry.StudentUpgradeALL(classid, key_val)  
                else:
                    if self.collectids:
                        for stid in self.collectids:
                            self.sqry.StudentUpgradeOneByOne(classid,key_val,str(stid))
                    else:
                        RMSMBX(self, text="\nNo Student Selected \nSelect Student First \n", info=True, textclr='white', bg='black')
            except Exception as e:
                RMSMBX(self, text="\nError Line 267 ??\n[%s]"%str(e), info=True, textclr='white', bg='black')
       
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
    sptag = 'UPGRADE STUDENT CLASS'
    spnum = 1
    whxy = (800, 600, 100, 50)
    app = Upgrade_Class(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()
"""
