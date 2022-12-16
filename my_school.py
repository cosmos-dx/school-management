#!/usr/bin/python
# -*- coding: UTF-8 -*-

from my_imports import * # Importing all modules
import time
import base64
from win32com.client import Dispatch
from rmsvalidators import *

def DesktopIcon():
    try:
        path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop','my_school Shortcut.lnk')
        wdir = os.path.dirname(sys.argv[0])
        target = os.path.join(wdir, 'my_school.exe')
        #icon = os.path.join(wdir, 'my_icon.ico')
        imgdata = base64.b64decode(images.rms)
        iconname = 'my_icon.ico'
        filename = iconname  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as icon:
            icon.write(imgdata)
        icon = os.path.join(wdir, iconname)
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wdir
        if icon == '':
            pass
        else:
            shortcut.IconLocation = icon
        shortcut.save()
    except :
        pass  


import shutil
import platform
    
class mmbar(Frame):
    def __init__(self, master, gpar, **kw):
        #super(LoginFrame, self).__init__()
        Frame.__init__(self, master)
        self.master = master
        self.gpar = gpar
        self.rscr = kw
        self.ftsz = int(self.rscr['sysfontnum'])
        self.font = ['Courier New', self.ftsz, 'normal']
        mb = Menu(master)
        fm = Menu(mb, tearoff=0, relief='groove', font=self.font, )
        mb.add_cascade(label="Master",  menu=fm)
        ################################
        fm.add_radiobutton(label="Open Teachher's Account", command=self.OpenTAccount,)             
        fm.add_separator()
        fm.add_radiobutton(label="Open Stodent's Account", command=self.OpenSAccount,)             
        fm.add_separator()
        fm.add_radiobutton(label="Open Other Account", command=self.OpenOAccount,)             
        fm.add_separator()
        fm.add_radiobutton(label="Master Fee Entry", command=self.MasterFee,)  
        fm.add_separator()
        fm.add_radiobutton(label="Settings", command=self.Pro_Settings,)  
        fm.add_separator()
        fm.add_radiobutton(label="Add New Finencial Year", command=self.AddNFYear,)          
        fm.add_separator()
        
        fm.add_radiobutton(label="exit", command=self.OnClose,)
        
        searchsp = Menu(mb, tearoff=0, font=self.font, )
        mb.add_cascade(label="New Entries",  menu=searchsp)
        master.config(menu=mb)
        searchsp.add_radiobutton(label="Student Performance Entry", command=self.StudentPerformanceEntry,)                      
        searchsp.add_separator()
        searchsp.add_radiobutton(label="FEES RECEIPTS", command=self.FeeEntry,)                
        searchsp.add_separator()  
        searchsp.add_radiobutton(label="Register Entry", command=self.Register,)                
        searchsp.add_separator()             
        
        item_ledger_sp = Menu(mb, tearoff=0, font=self.font,)
        mb.add_cascade(label="Search Details",  menu=item_ledger_sp)
        master.config(menu=mb)
        item_ledger_sp.add_separator()
        item_ledger_sp.add_radiobutton(label="Student MarkSheet Search", command=self.FindSheet,)
        item_ledger_sp.add_separator()
        item_ledger_sp.add_radiobutton(label="Fee Records MonthWise Search", command=self.FindFee,)                           
        item_ledger_sp.add_separator()
        
        user = Menu(mb, tearoff=0, font=self.font, activebackground='yellow',activeforeground='black',
                    
                    relief='sunken')
        user.add_checkbutton(label="Edit Login", command=self.LogSettings,)
        user.add_separator()
        user.add_checkbutton(label="My Calculator", command=self.RMS_Calculator,)
        user.add_separator()
        user.add_checkbutton(label="UpGrade MySchoolPro", command=self.Upgrade_MSP,)
        user.add_separator()
        
        mb.add_cascade(label="USER",  menu=user)
        master.config(menu=mb)
        
        self.wd = 5000
        self.ht = 30
        self.bbg = "gray99" #### Button Background Color
        self.htcolor = "yellow"
        self.fincolor = 'black'
        self.foutcolor = 'blue'
        self.btnlst = []
        self.btndictidx, self.btndictidx_rsvr = {}, {}
        self.btndict = {}
        self.buttonidx = 0
        self.btncount = 0
        self.maxbuttdisp = 5
        wrow = 12
        try:
            self.imgboyrun = RMS_GIF(self, master, gif='boy_run.gif',
                        dirname='bitmaps', framecount=6,)
            #self.imgboyrun.grid(row=wrow, column=1, rowspan=6, columnspan=6, padx=1, pady=1)
            self.imgboyrun.Show(pos=(self.rscr['sw']-660, self.rscr['sh']-760))
            
        except :
            ### When Image Path Not Available or AnyOne of Image is Missing
            self.imgboyrun = RMS_GIF(self, master, gif=None, framecount=0, )
        
        try:
            self.imgdogrun = RMS_GIF(self, master, gif='dog_run.gif',
                        dirname='bitmaps', framecount=7,)
            #self.imgdogrun.grid(row=wrow, column=1, rowspan=6, columnspan=6, padx=1, pady=1)
            self.imgdogrun.Show(pos=(self.rscr['sw']-500, self.rscr['sh']-600))
            
        except :
            ### When Image Path Not Available or AnyOne of Image is Missing
            self.imgdogrun = RMS_GIF(self, master, gif=None, framecount=0, )

        
        imgpath = os.path.join(self.rscr['rmspath'], 'bitmaps')
        '''
        img0 = PhotoImage(file=os.path.join(imgpath, "eg.gif"))
        img1 = PhotoImage(file=os.path.join(imgpath, "eg.gif"))
        img2 = PhotoImage(file=os.path.join(imgpath, "mf.gif"))
        img3 = PhotoImage(file=os.path.join(imgpath, "recpt.gif"))
        img4 = PhotoImage(file=os.path.join(imgpath, "ms.gif"))
        img5 = PhotoImage(file=os.path.join(imgpath, "cnt.gif"))
        img6 = PhotoImage(file=os.path.join(imgpath, "ls.gif"))
        img7 = PhotoImage(file=os.path.join(imgpath, "ext.gif"))
        img8 = PhotoImage(file=os.path.join(imgpath, "backup.gif"))
        img9 = PhotoImage(file=os.path.join(imgpath, "restore.gif"))
        img10 = PhotoImage(file=os.path.join(imgpath, "frecpt.gif"))
        img11 = PhotoImage(file=os.path.join(imgpath, "fs.gif"))
        img12 = PhotoImage(file=os.path.join(imgpath, "settings.gif"))s
        img13 = PhotoImage(file=os.path.join(imgpath, "cnt.gif"))
        img14 = PhotoImage(file=os.path.join(imgpath, "cnt.gif"))
        imglist = [img0,img1,img2,img3,img4,img5,img6,img7,
                img8,img9,img10,img11,img12,img13,img14,]
        '''
        
        imglist = [["img0.gif",10] ,["img1.gif",10],["img2.gif",9],["img3.gif",10],
                ["img4.gif",10],["img5.gif",10],["img6.gif",6],["img7.gif",8],
                ["img8.gif",5],["img9.gif",5],["img10.gif",7],["img11.gif",7],
                ["img12.gif",7],["img13.gif",7],["img13.gif",7],]
        
        self.listbutton = [['open student accounts', 'open teacher accounts', 'MASTER FEE', 'FEE RECEIPT',],
          ['MARK SHEET', 'Register', 'Log Sett',  ],
          [ 'EXIT', 'BACKUP',  'Restore',  'Find Fee',  ],
          ['Find Sheet', 'Settings', 'class upgrade',],] ### 23
        i = 0
        c = 0
        self.buttonbg = '#b0e0e6'
        
        bfnt_fg_bg = {'font': ['Courier', self.ftsz, 'bold'], 'bg':self.buttonbg, 'fg': 'black', 'bd':3, 'relief':'raised'}
        for r, btntxt in enumerate(self.listbutton):
            for c, txt in enumerate(btntxt):
                #btn = RMS_BUTTON(self.master, relief='raised', bg=self.bbg, fg="black", bd=3,
                #font="Dosis", text=txt.title(), command=lambda i=i,x=txt: self.openlink(i, btn))
                #btn = RMS_BUTTON(self.master, text=txt.title(),
                #    command=lambda i=i,x=txt: self.openlink(i, btn), **bfnt_fg_bg)
                #btn.grid(row=r+wrow, column=c, )
                img = imglist[i]
                btn = RMS_BTNGIF(self, self.master, text=txt.title(), gif=img[0],
                    dirname='bitmaps', framecount=img[1], bd=3, command=lambda i=i,x=txt: self.openlink(i, btn))
                btn.GridShow(geo={'r':sum([wrow,r, 1]), 'c':c, 'cp':1, 'rp':1})
                
                btn.bind('<Key>', self.OnKey)
                btn.bind('<Button-1>', self.OnKey)
                self.btnlst.append(btn)
                self.btndictidx[btn]=i
                self.btndictidx_rsvr[i]=btn
                self.btndict[txt]=btn
                
                i += 1
        
        self.master.protocol("WM_DELETE_WINDOW", self.OnClose)
        
    def openlink(self, i, btn):
        self.OpenFrame(text=self.btnlst[i]['text'], buttonidx=i)
        ###self.btnlst[i]['state']='disabled'
        
    def OnKey(self, event=None):
        key = event.keysym
        widget = event.widget
        currentidx = self.btndictidx[widget]
        text = widget['text']
        self.buttonidx = self.btnlst.index(widget)
        if event.type == '4': ### Mouse Left Click
            widget['state']='normal'
            
    def OpenFrame(self, text='', buttonidx=0):
        
        if text.lower().strip()=='open student accounts':
            self.OpenSAccount()
            
        if text.lower().strip()=='open teacher accounts':
            self.OpenTAccount() 
        
        if text.lower().strip()=='register':
            self.Register()
            
        if text.lower().strip()=='master fee':
            self.MasterFee()
            
        if text.lower().strip()=='fee receipt':
            self.FeeEntry()
            
        if text.lower().strip()=='exit':
            self.OnClose()
            
        if text.lower().strip()=='find sheet':
            self.FindSheet()
            
        if text.lower().strip()=='settings':
            self.Pro_Settings()
            
        if text.lower().strip()=='backup':
            self.BackUpRestore('Backup')
            
        if text.lower().strip()=='restore':
            self.BackUpRestore('Restore')
            
        if text.lower().strip()=='find fee':
            self.FindFee()
            
        if text.lower().strip()=='mark sheet':
            self.StudentPerformanceEntry()
            
        if text.lower().strip()=='log sett':
            self.LogSettings()
            
        if text.lower().strip()=='class upgrade':
            self.UpGradeClass()

    def BackUpRestore(self, mess):
        fdp = FileDialog.askdirectory()
        if fdp:
            self.gpar.status.SetValue('\nYou Have Selected [%s] For %s Data'%(fdp,mess))
        else:
            self.gpar.status.SetValue('\nYou Did Not Selected Any Directory Path')
                
    def OpenTAccount(self):
        filewin = Toplevel(self)
        sptag = {1:'teacher',2:'student',3:'other'}
        whxy = (1000, 600, 100, 50)
        student_teacher_ac(filewin, sptag, 1, 1, self.gpar, whxy, rscr=self.rscr)
        
    def OpenSAccount(self):
        filewin = Toplevel(self)
        sptag = {1:'teacher',2:'student',3:'other'}
        whxy = (1000, 600, 100, 50)
        student_teacher_ac(filewin, sptag, 2, 1, self.gpar, whxy, rscr=self.rscr)
        
    def OpenOAccount(self):
        filewin = Toplevel(self)
        sptag = {1:'teacher',2:'student',3:'other'}
        whxy = (1000, 600, 100, 50)
        student_teacher_ac(filewin, sptag, 3, 1, self.gpar, whxy, rscr=self.rscr)
        
    def AddNFYear(self):
        filewin = Toplevel(self)
        whxy = (800, 400, 300, 100)
        FYCalendar(filewin, 'Finencial Calendar Range', 1, 1, self.gpar, whxy, rscr=self.rscr)
        
    def Pro_Settings(self):
        filewin = Toplevel(self)
        whxy = (600, 300, 200, 100)
        Settings(filewin, 'Settings', 1, 1, self.gpar, whxy, rscr=self.rscr)
        
    def StudentPerformanceEntry(self): ### Search_Pur
        filewin = Toplevel(self)
        sptag = 'Student Performance Entry'
        whxy = (self.rscr['sw'], self.rscr['sh']-70, 0, 0)
        StudentPerformance(filewin, sptag, 1, 1, self.gpar, whxy, rscr=self.rscr)
       
    def FeeEntry(self):
        filewin = Toplevel(self)
        whxy = (800, 600, 100, 50)
        FeeReceipt(filewin, 'FEES RECEIPTS', 1, 1, self.gpar, whxy, rscr=self.rscr)

    def MasterFee(self):
        filewin = Toplevel(self)
        whxy = (800, 600, 100, 50)
        FeeMaster(filewin, 'MASTER FEES ENTERY', 1, 1, self.gpar, whxy, rscr=self.rscr)

    def Register(self):
        filewin = Toplevel(self)
        sptag = 'Register Entry'
        whxy = (self.rscr['sw'], self.rscr['sh']-70, 0, 0)
        rmss_register(filewin, sptag, 1, 1, self.gpar, whxy, rscr=self.rscr)

    def FindSheet(self):
        filewin = Toplevel(self)
        sptag = 'Student MarkSheet Search'
        whxy = (self.rscr['sw'], self.rscr['sh']-70, 0, 0)
        SheetRecords(filewin, sptag, 1, 1, self.gpar, whxy, rscr=self.rscr)

    def FindFee(self):
        filewin = Toplevel(self)
        sptag = 'Fee Records MonthWise Search'
        whxy = (self.rscr['sw'], self.rscr['sh']-70, 0, 0)
        FeeRecordsMonth(filewin, sptag, 1, 1, self.gpar, whxy, rscr=self.rscr)

    def RMS_Calculator(self):
        filewin = Toplevel(self)
        whxy = (350, 350, 400, 200)
        RMSCalculator(filewin, 'My Calculator', 1, 1, self.gpar, whxy, rscr=self.rscr)

    def Upgrade_MSP(self):
        filewin = Toplevel(self)
        RmssUpdates(filewin, 'Upgrade MySchoolPro', 1, 1, self.gpar, rscr=self.rscr)

    def UpGradeClass(self):
        filewin = Toplevel(self)
        whxy = (800, 600, 100, 50)
        Upgrade_Class(filewin, 'UPGRADE STUDENT CLASS', 1, 1, self.gpar, whxy, rscr=self.rscr)
            
    def LogSettings(self): 
        filewin = Toplevel(self)
        whxy = (600, 300, 300, 100)
        User_Login(filewin, 'RESET USER LOGIN', 1, 1, self.gpar, whxy, rscr=self.rscr)
        
    def OnClose(self, event=None):
        self.sw = self.master.winfo_screenwidth()
        self.sh = self.master.winfo_screenheight()
        self.exitw = 220
        self.exith = 130
        self.xpos =(self.sw/2) - (self.exitw/2) 
        self.ypos =(self.sh/2) - (self.exith/2)       
        mess = RMSMBX(self.master, text="\nWANT to EXIT ??\n", info=False,
                       pos=(self.xpos,self.ypos),
                          size=(self.exitw, self.exith),textclr='white', bg='black')
        if mess.result:
            try:
                self.master.destroy()
            except :
                pass
        
def StartPageDestroy(self):
    self.lab0.destroy()
    self.lab1.destroy()
    self.lab2.destroy()
    self.unamel.destroy()
    self.unamee.destroy()
    self.upassl.destroy()
    self.upasse.destroy()

def StartPageCreate(self, sw, sh, rscr):
    try:
        imgpath = os.path.join(self.rscr['rmspath'], 'bitmaps')
        img0 = PhotoImage(file=os.path.join(imgpath, "side0.gif"))
        img1 = PhotoImage(file=os.path.join(imgpath, "center.gif"))
        img2 = PhotoImage(file=os.path.join(imgpath, "side1.gif"))
        ribimg = PhotoImage(file=os.path.join(imgpath, "ribbon.gif"))        
    except KeyboardInterrupt:
        img0, img1, img2, ribimg = None, None, None, None
    return img0, img1, img2, ribimg

def PlaceImages(self, master, wrow, sw, sh, rscr):
    img0, img1, img2, ribimg = StartPageCreate(self, sw, sh, rscr)
    wrow += 1
    if img0:
        self.lab0 = RMS_LABEL(master, image=img0)
        self.lab0.image = img0
        self.lab0.grid(row=wrow, column=0, rowspan=10, columnspan=5, padx=1, pady=1)
        #self.lab0.place(x=10, y=10, )
    else:
        self.lab0 = RMS_LABEL(master, text='MISSING 1st IMAGE', font=('Courier New', sum([self.ftsz,5])), bg="lightyellow", fg="black")
        self.lab0.grid(row=wrow, column=0, rowspan=10, columnspan=5)
    
    if img1:
        self.lab1 = RMS_LABEL(master, image=img1)
        self.lab1.image = img1
        self.lab1.grid(row=wrow, column=6, rowspan=10, columnspan=5, padx=1, pady=1)
        #self.lab1.place(x=250, y=10, )
    else:
        self.lab1 = RMS_LABEL(master, text='MISSING 2nd IMAGE', font=('Courier New', sum([self.ftsz,5])), bg="lightyellow", fg="black")
        self.lab1.grid(row=wrow, column=6, rowspan=10, columnspan=5)
        ###self.lab1.place(x=500, y=10, )
        
    if img2:
        self.lab2 = RMS_LABEL(master, image=img2)
        self.lab2.image = img2
        self.lab2.grid(row=wrow, column=11, rowspan=10, columnspan=5, padx=1, pady=1)
        #self.lab2.place(x=sw-280, y=sum([sh,10])-sh,  )
    else:
        self.lab2 = RMS_LABEL(master, text=' MISSING 3rd IMAGE ', font=('Courier New', sum([self.ftsz,5])), bg="lightyellow", fg="black")
        self.lab2.grid(row=wrow, column=11, rowspan=10, columnspan=5, padx=1, pady=1)
        ##self.lab2.place(x=sw-280, y=sum([sh,10])-sh,  )
    wrow += 11
    if img2:
        self.rib2 = RMS_LABEL(master, image=ribimg)
        self.rib2.image = ribimg
        self.rib2.grid(row=sum([wrow,2]), column=0, rowspan=7, columnspan=25, padx=1, pady=1)
        #self.rib2.place(x=sum([sw,10])-sw, y=sh-270,  )
    else:
        self.rib2 = RMS_LABEL(master, text='MISSING 4th IMAGE', font=('Courier New', self.ftsz, 'bold'), bg="OliveDrab1", fg="black")
        self.rib2.grid(row=sum([wrow,2]), column=0, rowspan=7, columnspan=25, padx=1, pady=1)
        #self.rib2.place(x=sum([sw,10])-sw, y=sh-270,  )
    wrow += 2
    self.varn = StringVar()
    self.var = StringVar()
    wrow += 1

    lfnt_fg_bg0 = {'font': ['Courier New Bold', self.ftsz-2, 'bold'],'bg':'OliveDrab1', 'fg':'blue'}
    lfnt_fg_bg1 = {'font': ['Times New Roman Bold', self.ftsz, 'normal'], 'bg': 'OliveDrab1', 'fg': 'red'}
    lfnt_fg_bg2 = {'font': ['Times New Roman Bold', sum([self.ftsz,110]), 'normal'], 'bg': 'OliveDrab1', 'fg': 'blue'}
    self.lfnt_fg_bg = {'font': ['Courier New', self.ftsz, 'normal'], 'bg': 'SystemButtonFace', 'fg':'black'}
    
    self.status = RMS_LABEL(master, **lfnt_fg_bg1)
    self.unamel = RMS_LABEL(master, width=10, text="Username:", font=('Courier New', self.ftsz), bg="OliveDrab1", fg="black")
    self.unamee = RMS_ENTRY(master, **{'font':('Courier New', self.ftsz, 'bold'), 'bd':3, 'bg':"yellow", 'fg':"black",'textvariable':self.varn,})
    self.upassl = RMS_LABEL(master, text="Password:", font=('Courier New', self.ftsz), bg="OliveDrab1", fg="black")
    self.upasse = RMS_ENTRY(master, show="*", **{'font':('Courier New', self.ftsz, 'bold'), 'bd':3, 'bg':"yellow", 'fg':"black",'textvariable':self.var,})

    self.status.grid(row=sum([wrow,3]), column=0, rowspan=1, columnspan=25, padx=1, pady=1)
    wrow += 1
    self.unamel.grid(row=wrow, column=0, rowspan=1, columnspan=2, padx=1, pady=1)
    self.unamee.grid(row=wrow, column=4, rowspan=1, columnspan=2, padx=1, pady=1)
    self.upassl.grid(row=wrow, column=7, rowspan=1, columnspan=2, padx=1, pady=1)
    self.upasse.grid(row=wrow, column=9, rowspan=1, columnspan=2, padx=1, pady=1)
    wrow += 1
    self.uppos_y = sh-250

    self.threaddp = RMS_LABEL(master, text='xxx', **lfnt_fg_bg2) ### tnrb
    
    self.sunillink = RMS_LABEL(master, cursor='hand2', **lfnt_fg_bg0)
    self.sunillink.grid(row=wrow, column=0, rowspan=1, columnspan=1, padx=1, pady=1)
    #self.sunillink.bind("<Button-1>", lambda e: rmslinkopen("http://www.rmssoft.co.in"))
    
    self.ownerl = RMS_LABEL(master, text=self.rscr['ownerdict']['ownerinfo']['owner']['name'],font=('Courier New', sum([self.ftsz, 6]),'bold'),
                bg="OliveDrab1", fg="black")
    self.ownerl.grid(row=wrow, column=2, rowspan=1, columnspan=10, padx=1, pady=1)
    wrow += 1
    self.add1 = RMS_LABEL(master, text=self.rscr['ownerdict']['ownerinfo']['owner']['add1'],font=('Courier New', sum([self.ftsz, 2])),
                        bg="OliveDrab1", fg="black")
    self.add1.grid(row=wrow, column=2, rowspan=1, columnspan=10, padx=1, pady=1)
    self.sunilinfo1 = RMS_LABEL(master, **lfnt_fg_bg0)
    self.sunilinfo1.grid(row=wrow, column=1, rowspan=1, columnspan=1, padx=1, pady=1)

    wrow += 1
    self.add2 = RMS_LABEL(master, text=self.rscr['ownerdict']['ownerinfo']['owner']['add2'],font=('Courier New', sum([self.ftsz, 2])),
                        bg="OliveDrab1", fg="black")
    self.add2.grid(row=wrow, column=1, rowspan=1, columnspan=10, padx=1, pady=1)
    
    self.rmsclock = RMS_LABEL(master, font=('Courier New', sum([self.ftsz, -2])), bg="OliveDrab1", fg="black")
    self.rmsclock.grid(row=wrow, column=2, rowspan=1, columnspan=15, padx=1, pady=1)

    wrow += 1
    self.rmscal = RMS_LABEL(master, font=('Courier New', self.ftsz), bg="OliveDrab1", fg="black")
    self.rmscal.grid(row=wrow, column=5, rowspan=1, columnspan=10, padx=1, pady=1)
    
    return wrow

class LoginFrame(Frame):
    def __init__(self, master, **kw):
        #super(LoginFrame, self).__init__()
        Frame.__init__(self, master)
        
        self.kw = kw
        
        self.mmaster = master
        master.title('School Management Software')
        self.rscr = kw['rscr']
        
        self.font = kw['rscr']['font']
        sw, sh = self.rscr['sw'], self.rscr['sh']
        pad=2
        master.geometry("{0}x{1}+0+0".format(
        master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        self.fontsize = self.rscr['sysfontnum']
        self.ftsz = self.rscr['sysfontnum']
        wrow = 0
        self.reload = False
        # self.status.grid(row=wrow, column=0, rowspan=10, columnspan=5, padx=1, pady=1)
        
        wrow = PlaceImages(self, master, wrow, sw, sh, self.rscr)
        lb_fg_bg = {'font': ['Courier', self.ftsz, 'bold'], 'bg': '#b0e0e6', 'fg': 'black'}
        gbd, gbg, gfg = 2, '#b0e0e6', 'black'
        lbfont = ['Courier New', self.ftsz-1, 'bold']
        lcolconf = {0:{'idname':'fyn','text':'.','width':1,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},
                    1:{'idname':'frm','text':'From Date','width':25,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},
                    2:{'idname':'tod','text':'To Date','width':25,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},
                    3:{'idname':'fnum','text':'','width':1,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},}
        self.lc = RMSLBN(self.master, self, True, 15, lcolconf, **lb_fg_bg)
        ###self.lc.grid(row=wrow, column=1, columnspan=1, rowspan=15, sticky='w')
        
        for r in range(25):
            self.master.rowconfigure(r, weight=1)
        for r in range(25):
            self.master.columnconfigure(r, weight=1)
        self.mmbar = None ### Empty class from mainframe; Assign Later ... 
        self.count = 0
        self.keycount = 0
        self.kmdfm = 0
        self.vblnsbool = True  ## Take Value of Visible line per frame ONLY Once
        self.vblns = 1   ## Visble Lines Of ListBox
        self.tcount = 0
        self.unamee.focus()
        self.Lctmess = [None, '']

        self.unamee.bind('<Key>', self.OnunameeKey)
        self.upasse.bind('<Key>', self.OnupasseKey)
        try:
            master.iconbitmap(self.rscr['rmsicon'])
        except Exception as err:
            StatusDP(self.status, 'Error Found [%s]'%str(err), 'red')
        
        wrow = 2
        gbd, gbg, gfg = 2, '#b0e0e6', 'black'
        lbfont = ['Courier New', self.ftsz, 'bold']
        self.setwdg = self.rmscal
        lb_fg_bg = {'font': ['Courier New', self.ftsz, 'bold'], 'bg':'SystemButtonFace','fg':'blue'} ###self.rscr['font']['listbox']
        
        lcolconf = {0:{'idname':'fyn','text':'.','width':1,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},
                    1:{'idname':'frm','text':'From Date','width':25,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},
                    2:{'idname':'tod','text':'To Date','width':25,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},
                    3:{'idname':'fnum','text':'','width':1,'bd':gbd,'bg':gbg,'fg':gfg,'font':lbfont,'relief':'raised','wrow':wrow},}
        
        self.lc = RMSLBN(master, self, True, 15, lcolconf, **lb_fg_bg)
        self.lcpos = {'row':0, 'column':0, 'columnspan':15, 'rowspan':10, 'sticky':'nw'}
        ###self.lc.grid(row=0, column=0, columnspan=15, rowspan=15, sticky='w')
                
    def rmsclockfun(self):
        try:
            def change_value_the_time():
                the_time = self.rscr['the_time']
                newtime = time.time()
                if newtime != the_time:
                    the_time = self.Notify()
                    self.rscr['the_time'] = the_time
                    self.rmsclock.config(text=the_time)
                #self.rmsclock.after(20, change_value_the_time)
                self.after(20, change_value_the_time)
            change_value_the_time()
        except:
            pass
        
    def SecondTry(self):
        try:
            self.rscr = LoadCustomized(self.rscr)
        except Exception as err:
            StatusDP(self.status, 'STOP ! FATAL Error Found, SomeOne Corrupt RMS System Maunally. Contact RMS Service Provider [%s]'%str(err), 'red')
        try:
            cset = MySett(self.rscr)
            cset.ReadAll()
            self.rmsclockfun()
        except Exception as err:
            StatusDP(self.status, 'FATAL ERROR DATABASE NOT FOUND, RESTART May RESOLVE with NEW DATABASE [%s]'%str(err), fg='red')
         
    def FyNum_Set(fys):
        fy = fys.split('fy')[1]
        return fy
                  
    def ShiftBottomLabels_UP(self, wrow=18):
        self.ownerl.grid(row=wrow, column=1, columnspan=15, rowspan=2)
        wrow += 2
        self.add1.grid(row=wrow, column=1, columnspan=15, rowspan=1)
        wrow += 1
        self.add2.grid(row=wrow, column=1, columnspan=15, rowspan=1)
        wrow += 1
        self.rmsclock.grid(row=wrow, column=0, columnspan=12, rowspan=1)
        
        self.rmscal.grid(row=wrow, column=5, columnspan=10, rowspan=1)
            
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime("  %A  |   %d-%B-%Y  |  %W-Weeks  |  %j-Days  |  %I:%M:%S %p ", t)
        mst = ' '.join(['|',str(365 - int(st.split('|')[3].strip().split('-')[0])), 'Days Left'])
        return ' '.join([st,mst])
         
    def OnunameeKey(self, event=None):
        if event.keycode == 13 : ##Return Button
            self.upasse.SetFocus()
        self.count += 1

    def GetFinencialList(self):
        ### This will show table name in list if table incremneted  
        self.cursor.execute("SHOW TABLES LIKE '%cash%' ")
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            rlst = [r[0].split(tbname)[1] for r in rows]
        return rlst

    def ReLoadOwner(self):
        from class_query import USERLOGIN, DBTABLES
        try:
            self.userlog = USERLOGIN().LOG()
        except Exception as err:
            print (err, 'Create New Data Base sqlit3')
            DBTABLES()
            return
        self.rscr['ownerdict']['ownerinfo']['owner']['userpass'] = self.userlog[0]
        self.rscr['ownerdict']['ownerinfo']['owner']['userid'] = self.userlog[1]
        
        try:
            self.ownerl['text']=self.rscr['ownerdict']['ownerinfo']['owner']['name']
            self.add1['text']=self.rscr['ownerdict']['ownerinfo']['owner']['add1']
            self.add2['text']=self.rscr['ownerdict']['ownerinfo']['owner']['add2']
        except :
            pass
        
    def OnupasseKey(self, event=None):
        self.ReLoadOwner()
        
        try:
            upas = self.rscr['ownerdict']['ownerinfo']['owner']['userpass']
            uids = self.rscr['ownerdict']['ownerinfo']['owner']['userid']
        except KeyError:
            upas = 'pass'
            uids = 'pass'
        if event.keycode == 13 : ##Return Button
            ###self.lc.grid(self.lcpos)
            if self.unamee.GetValue() == uids:
                self.unamel['text'] ="Username"
                if self.upasse.GetValue() == upas.upper():
                    self.upassl['text'] ="Username"
                    
                    StartPageDestroy(self)
                    self.tcount = 0
                    self.mlist = None
                    try:
                        self.ReloadMyCalendar()
                    except Exception as err:
                        StatusDP(self.status, "FATAL ERROR FOUND 'Cannot Load Finencial Year Records' CLOSE RMS [%s]"%str(err), 'red')
                        return
                else:
                    self.upassl['text'] ="WRONG"
                    self.upasse.SetFocus()
            else:
                self.unamel['text'] ="WRONG"
                self.unamee.SetFocus()
                
    def ReloadMyCalendar(self):
        from my_calendar import LcRefresh
        buttonidx = 1
        parent = None
        sptag = 'Finencial Calendar Range'
        spnum = 1
        whxy = (1000, 800, 100, 50)
        self.lc.grid(row=2, column=1, columnspan=1, rowspan=15, sticky='w')
        nxv = LcRefresh(self, self.lc, self.unamee, self.unamee)
        self.lc.SetFocusRow(0)
        self.mmbar = mmbar

    def ReArrangeBottom(self):
        wrow = 20
        self.rib2.grid(row=wrow, column=0, rowspan=7, columnspan=30, padx=1, pady=1)
        wrow += 1
        self.sunillink.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='e')
        wrow += 1
        self.ownerl.grid(row=wrow, column=1, rowspan=1, columnspan=10, padx=1, pady=1)
        wrow += 1
        self.add1.grid(row=wrow, column=2, rowspan=1, columnspan=10, padx=1, pady=1)
        self.sunilinfo1.grid(row=wrow, column=0, rowspan=1, columnspan=1, sticky='e')
        wrow += 1
        self.add2.grid(row=wrow, column=1, rowspan=1, columnspan=10, padx=1, pady=1)
        self.rmsclock.grid(row=wrow, column=2, rowspan=1, columnspan=15, padx=1, pady=1)
        wrow += 1
        self.rmscal.grid(row=wrow, column=5, rowspan=1, columnspan=10, padx=1, pady=1)
    
    def GetLCSelectData(self, rd, itemlc_dict, evtname):
        row, col, wdgidf = rd
        self.lcdata = itemlc_dict[row]
        fy = itemlc_dict[row]['fyn']
        dbfrm = itemlc_dict[row]['frm']
        dbtod = itemlc_dict[row]['tod']
        partnum = itemlc_dict[row]['fnum']
        self.rscr['daterange']=[dbfrm, dbtod]
        self.rscr['calendar']['fy']=fy
        frm = datetime.strptime(str(dbfrm),"%Y-%m-%d").strftime("%d/%m/%Y")
        tod = datetime.strptime(str(dbtod),"%Y-%m-%d").strftime("%d/%m/%Y")
        self.rscr['calendar']['frm']=frm
        self.rscr['calendar']['tod']=tod
        self.rscr['calendar']['dbfrm']=dbfrm
        self.rscr['calendar']['dbtod']=dbtod
        self.rscr['calendar']['partnum']=partnum
        self.rscr['fyear']=partnum
        self.rscr['partname']=fy
        if evtname == 'Return':
            self.lc.destroy()
            self.rmscal.SetValue(''.join([str(frm),'-',str(tod)]))
            self.ReArrangeBottom()
            mmbarframe = self.mmbar(self.master, self, **self.rscr)
            self.master.state("zoomed")
 
def LoadDefault(root):
    import config
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
    own = {'name':'School Managing Soft','add1':'','add2':'','phone':'','reg':'', 'gstin':'','statu1':'','statu2':'','statu3':'','statu4':''}
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
            'fyear':'0', 'daterange':['2021-04-01','2022-03-31'],
            'calendar':{'fy':'','dbfrm':'2021-04-01','frm':'01/04/2021','tod':'31/03/2022','partnum':'','dbtod':'2022-03-31'},
            'ledgerid':'0','itemid':'0','transid':'0','spid':'0','csid':'0','csname':'',
            'rmspath':rmspath,'rmsicon':rmsicon, 'pardir': rmspath, 'prpath':prpath,'taxinfo':taxinfo,'printerinfo': printerinfo,
            'TABLENUM':'','today':today, 'today_db_format':today_db_f,'tax1':'0', 'tax2':'0',
            'the_time':'', 'itemidlist':[], 'spidlist':[],'renderlist':[],
            'taxinvoice':True,'stkmess':'YES','decimalval':'2','last_esti_no':None, 'last_sale_bill_no':None,
            'exp_alert':90,'estifilter':False,'sdc':'1','mysoft':'1','mysoftval':'1','compbool':True, 'config':cofdic}
    return rscr

def main():
    root = Tk()
    #root.geometry("350x300+300+300")
    rscr = LoadDefault(root)
    LoginFrame(root, rscr=rscr)
    root.mainloop()
    
if __name__ == "__main__":
    main()

