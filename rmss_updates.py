#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

from rmsvalidators import *
import requests
import zipfile
import urllib
import shutil

def MrmsDownload_Thread(self, url, rundir_, filename, downdir, safepath, zipurl):
    self.threaddp = 'Wait.. !'
    try:
        workfile = Predifined_Dir_Thread(self, url, rundir_, filename, downdir, safepath, zipurl)
    except KeyboardInterrupt: #### Thread hasbeen Inturrupted by Deleteing Frame or otherwise...
        self.sdmess = None
        return
    con_status = False
    if workfile :
        con_status = True
        self.workfile = workfile
        self.rundir_ = rundir_
        self.sdmess = True
    else: ### some error return none
        self.workfile = None
        self.rundir_ = ''
        self.sdmess = None
        return
    
    if zipurl:
        self.threaddp = 'Done ==> %s'%zipurl
        workfile = Predifined_Dir_Thread(self, self.link2, rundir_, self.mrmspro, downdir, safepath, zipurl)
        con_status = False
        if workfile :
            con_status = True
            self.workfile = workfile
            self.rundir_ = rundir_
            self.sdmess = True
            self.threaddp = ' Copy Zip Files... Wait'
            ####  Graph Module Download block #####
            zippath = os.path.join(rundir_, downdir, self.zipdownloadfilename)
            try:
                Copy_ZipFile(self, zippath, rundir_, downdir, self.zipdownloadfilename)
                self.threaddp = ' Copied !'
            except Exception as err:
                self.threaddp = 'Error Found [%s]'%str(err)
            ####  Graph Module Download block #####
            
def upd_thread(self, count, total, status='', done=False):
    bar_len = 50
    filled_len = int(round(bar_len * count / float(total)))
    percent = round(100.0 * count/float(total), 1)
    bar = '#' * filled_len +'# '+ ' ' * (bar_len - filled_len)
    if done:
        self.threadtick = "[%s] %s%s ..%s\r"%(bar, 'Done ', str(count)," Bytes Done")
    else:
        self.threadtick = "[%s] %s%s ..%s\r"%(bar, percent, '%', status)
    sys.stdout.flush()
    
def download_file_thread(self, url, filename):
    r = requests.get(url, stream=True)
    site = urllib.urlopen(url)
    meta = site.info()
    try:
        dw_filesize = int(meta.getheaders("Content-Length")[0])
    except IndexError:
        dw_filesize = 10
    dbyte = 1024
    #total = dw_filesize/dbyte
    count=0
    with open(filename, "wb") as code:
        for chunk in r.iter_content(chunk_size=dbyte):
            count += len(chunk)
            if chunk:
                self.threaddp = "%s Bytes"%count
                upd_thread(self, count, dw_filesize, status="%s Bytes"%count)
                code.write(chunk)
                 
    #upd_thread(self, 100, 100, status="%s Bytes Done"%count, done=True)
    self.threaddp = "%s Bytes"%count
    
def Predifined_Dir_Thread(self, url, rundir_, filename, downdir, safepath, zipurl):
    ##newddir = '/'.join([rundir_, downdir])
    newddir = os.path.join(rundir_, downdir) ### '\\'.join([rundir_, downdir])
    if not os.path.exists(newddir):
        os.mkdir(newddir)
        return None
    workfile = os.path.join(rundir_, downdir, filename)###'\\'.join([rundir_, downdir, filename])
    scrfile = os.path.join(rundir_, filename)### '\\'.join([rundir_, filename])

    self.threaddp = 'Downloading File at %s'%workfile
    #self.printinfo1.SetLabel('Downloading File at %s'%workfile)
    self.threaddp2 = "Start %s Downloading ..... "%filename
    ## 2. Download file in Predifined Dir
    
    try:
        download_file_thread(self, url, workfile)
        self.copymess = True
      
    #except Exception as e:
    except KeyboardInterrupt as e:
        self.copymess = False
        el = str(e).split()
        try:
            self.threadtick = (' '.join([" ", el[0], el[len(el)-4], el[len(el)-3], el[len(el)-2], el[len(el)-1] ]))
        except:
            self.threadtick = (" You Are Offline or Other Error Occured !!, Try Again Later !!")
            
        return
    
    ## 3. Move old file in win_rms dir if dir not exist rename old file
    safe_folder = 'win_rms'
    self.threaddp2 = ("Moving File In [%s] "%safepath)
    
    try:
        ##safepath = '\\'.join([rundir_, safe_folder, filename])
        #safepath = '/'.join([rundir_, safe_folder, filename])
        #print scrfile, 'scrfile'
        #print safepath, 'safepath'
        try:
            shutil.copy(scrfile, safepath)
        except:
            Create_File(rundir_)
            shutil.copy(scrfile, safepath)
            
        self.threaddp3 = ("Old File Moved Sucessfully into %s"%safepath)
        ###self.dwn1.SetLabel(str(oldfinfo))
    except KeyboardInterrupt:
        tmext = str(int(float(time.time())))
        filesp = filename.split('.')
        renamefile = ''.join([filesp[0],'_',str(int(float(time.time()))), '.', filesp[1]])
        ##renamepath = '/'.join([rundir_, renamefile])
        renamepath = '\\'.join([rundir_, renamefile])
        try:
            os.rename(scrfile, renamepath)
            self.threaddp5 = ' File Renamed %s'%str(renamepath)
        except:
            pass
    
    return workfile

def Create_File(rmspath, filename='mrms_pro.exe'):
    rmspath_filename = os.path.join(rmspath, filename)
    file = open(rmspath_filename, 'w')
    file.close()
    
    pass
def Copy_ZipFile(self, workfile, rundir_, downdir, zfilename):
    src = os.path.join(rundir_, downdir)
    with zipfile.ZipFile(workfile, 'r') as zp:
        zp.extractall(rundir_)
        self.threaddp = 'Extracting File Path [%s]'%str(rundir_)
    ###mrmsexe = os.path.join(rundir_, downdir)

def RFT(rundir, winrmsfile):
    #os.remove(os.path.join(rundir, 'mrms_pro.exe'))
    shutil.copy2(winrmsfile, rundir)
    
class RmssUpdates(Frame):
    def __init__(self, parent, sptag, spnum, buttonidx, gpar,
        url="http://rmssoft.co.in/mrms_pro.exe",
        weblink1="http://rmssoft.co.in/mrms_pro.exe",
        weblink2="http://www.rmssoft.co.in/static/mgpkg/mrms_pro.exe",
        webziplink="http://www.rmssoft.co.in/static/mgpkg/mgpkg.zip", **kw):
        Frame.__init__(self, parent)
        self.rscr = kw['rscr']
        self.ftsz = int(self.rscr['sysfontnum'])
        self.webziplink = webziplink
        self.weblink2 = weblink2
        self.weblink1 = weblink1
        self.url = url
        self.sptag = sptag.lower()
       
        self.fyear = self.rscr['fyear']
        self.daterange = self.rscr['daterange']
        parent.iconbitmap(self.rscr['rmsicon'])
        
        sw= self.rscr['sw']
        sh= self.rscr['sh']
        wsw = sum([(int(sw/1.6)),200])  ### window Width
        wsh = sh-270   ### window Height
      
        xpos = (sw/2)-(wsw/2) ### Center On Screen
        ypos = 0 ####(sh/2)-(wsh/2)  ### Center On Screen
        self.master.geometry('%dx%d+%d+%d' % (wsw, wsh, xpos, ypos))
        #self.master.geometry("{0}x{1}+0+0".format(
        #self.master.winfo_screenwidth()-550, self.master.winfo_screenheight()-70))
        
        ### spdict = {1:'purchase', 2:'sales', 8:'purchasereturn', 9:'salesreturn',
        ###      11:'purchaseorder',12:'salesorder'}
        self.spnum = spnum
       
        self.leftpadd = 5 ### padding for left side of Frame
        self.ht = self.rscr['sh']   ### screen height from top to bottom
        ### Frame height will divided into 3 parts
        self.fupr = (15.0/100.0)*self.ht
        ### upper = 20 % for dates region
        self.fmpr = (55.0/100.0)*self.ht
        ### middle = 50 % for grid only
        self.fbpr = (30.0/100.0)*self.ht
        self.gpar = gpar
        self.buttonidx = buttonidx
        self.master.title(self.sptag.upper())
        labelfontsize = ['Courier New', self.ftsz, 'normal'] ###self.rscr['font']['label']['font']
        self.lfont = labelfontsize
        self.lfnt_fg_bg = {'font': ['Courier New', self.ftsz, 'normal'], 'bg': 'SystemButtonFace', 'fg':'black'} ###self.rscr['font']['label']
        lb_fg_bg = {'font': ['Courier New', self.ftsz, 'bold'], 'bg': '#b0e0e6', 'fg': 'black',} ###self.rscr['font']['listbox']
        lbfgbg = {'font': ['Courier New', self.ftsz-2, 'bold'],'bg':'SystemButtonFace', 'fg':'blue',} ###self.rscr['font']['listbox']
        self.ebg = '#b0e0e6'
        self.htcolor = 'light yellow'
        efnt_fg_bg = {'font': ['Courier New', self.ftsz, 'bold'], 'bd':3, 'bg':self.ebg, 'fg':'black', 'relief':'sunken'}
        self.efnt_fg_bg = efnt_fg_bg
        bfnt_fg_bg = {'font': ['Courier New', self.ftsz, 'bold'], 'bg':self.htcolor, 'fg':'black', 'relief':'raised'}
        chkbtn_fg_bg = {'font': ['Courier New', self.ftsz, 'normal'], 'fg':'black', 'relief':'raised'}

        self.txtpad = ''
        self.otherwidglist = []
        
        wminwidth = 15
        wmaxcolumn = 25
        wmaxrows = 20
        wrow = 1

        self.url2bv = BooleanVar()
        self.url2 = RMSChkBut(self.master, text='-Module', variable=self.url2bv,
                              command=self.Onurl2, **self.lfnt_fg_bg)
        self.url2.grid(row=wrow, column=0,columnspan=3,sticky = 'w')
        
        self.top = RMS_LABEL(self.master, text="-- %s' --"%self.sptag.title(),
                    justify='right', **self.lfnt_fg_bg)
        self.top.grid(row=wrow, column=2,columnspan=11,sticky = 'wens')
        wrow += 1

        ##############################################################################
        url = self.url
        self.dfolder1 = os.path.join(self.rscr['rmspath'], 'MyfileDownload')
        self.link1 = self.weblink1 
        self.dfolder2 = os.path.join(self.rscr['rmspath'],'MRMSGRAPH_files_Download')
        self.link2 = self.weblink2 
        url = self.link2
        self.link2zip = self.webziplink
        self.zipfname = 'mgpkg.zip'
        self.mrmspro = 'mrms_pro.exe'
        self.mgmd = False
        self.zipdownloadfilename = None 
        self.dsuccess = False
        ###url = "https://drive.google.com/uc?id=15gH75dCZ7G5ojX8OGf-ujWTMrF51-sYf"
        self.topstx = RMS_LABEL(self.master, text=url, **self.lfnt_fg_bg ) ##RMS_ENTRY(self.master, **self.efnt_fg_bg)
        self.topstx.bg('yellow')
        self.topstx.SetValue(self.link2)
        self.url = url
        self.topstx.grid(row=wrow, column=1,columnspan=20, sticky = 'wens')
        wrow += 1

        self.printinfo = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.printinfo.grid(row=wrow, column=0,columnspan=20, sticky = 'wens')
        wrow += 1

        self.go = RMS_BUTTON(self.master, text='Start Download', width=wminwidth,
                        command=self.Connect, **bfnt_fg_bg)
        self.go.grid(row=wrow, column=10,columnspan=10, sticky = 'e')
        wrow += 1

        self.printr = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.printr.grid(row=wrow, column=0,columnspan=20, sticky = 'wens')
        ###self.printr.bg('yellow')
        self.printr.fg('blue')
        wrow += 1

        self.printinfo1 = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.printinfo1.grid(row=wrow, column=0,columnspan=20, sticky = 'wens')
        wrow += 1

        self.printinfo2 = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.printinfo2.grid(row=wrow, column=0,columnspan=20, sticky = 'wens')
        wrow += 1

        self.ggo = RMS_BUTTON(self.master, text='GRAPH MODULE DOWNLOAD', 
                        command=self.GBconnect, **bfnt_fg_bg)
        self.ggo.grid(row=wrow, column=10,columnspan=10, sticky = 'e')
        wrow += 1

        self.printrr = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.printrr.grid(row=wrow, column=0,columnspan=20, sticky = 'w')
        wrow += 1

        self.print3 = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.print3.grid(row=wrow, column=0,columnspan=20, sticky = 'w')
        wrow += 1

        self.print4 = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.print4.grid(row=wrow, column=0,columnspan=20, sticky = 'w')
        wrow += 1
        
        self.dwn1 = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.dwn1.grid(row=wrow, column=0,columnspan=20, sticky = 'w')
        wrow += 1

        self.butt = RMS_BUTTON(self.master, text='EXIT', width=wminwidth,
                        command=self.Submit, **bfnt_fg_bg)
        self.butt.grid(row=wrow, column=10,columnspan=10, sticky = 'e')
        wrow += 1

        self.dwn2 = RMS_LABEL(self.master, text="", **self.lfnt_fg_bg )
        self.dwn2.grid(row=wrow, column=10,columnspan=20, sticky = 'wens')
        wrow += 1

        self.deloldfile = RMS_BUTTON(self.master, text='CLEAN OLD DOWNLOADED FILES', width=wminwidth,
                        command=self.OnDelOldFiles, **bfnt_fg_bg)
        self.deloldfile.grid(row=wrow, column=10,columnspan=10, sticky = 'e')
        wrow += 1

        ##############################################################################
        
        self.status = RMS_LABEL(self.master, text='', **self.lfnt_fg_bg)
        self.status.grid(row=wrow, column=0,columnspan=10, sticky = 'wens')
        wrow += 1
        
        imgframe = Frame(self, )
        self.imggif = RMS_GIF(self, self.master, dirname='bitmaps', **self.lfnt_fg_bg)

        self.otherwidglist = [self.go, self.ggo, self.deloldfile, self.butt,]
        self.master.protocol("WM_DELETE_WINDOW", self.OnClose_X)
        for r in range(wmaxrows):
            self.master.rowconfigure(r, weight=1)
        for c in range(wmaxcolumn):
            self.master.columnconfigure(c,weight=1)
            
    def Onurl2(self, event=None):
        if self.url2.GetValue():
            self.topstx.SetValue(self.url)
            self.url2.SetLabel('OLD Module')
        else:
            self.topstx.SetValue(self.link2)
            self.url2.SetLabel('NEW')
            self.url = self.link2
            
    def FilePrp(self, url, downdir, filename, zipurl=None):
        self.printinfo.SetLabel('Connecting.....')
        rundir_ = self.rscr['rmspath']###os.path.dirname(sys.argv[0])
        if not zipurl:
            ### zipurl=None When reular download button press
            ### zipurl=None will then check, if graph module already downloaded or not
            ### zipurl= GIVEN then forcefully download all files of graph modeule + self.mrmspro
            url, downdir = self.CheckDownloadFiles(url, downdir, rundir_) 
        self.topstx.ChangeValue(url)
        self.sdmess = None
        self.workfile = None
        self.threaddp = ''
        self.threaddp2 = ''
        self.threaddp3 = ''
        self.threaddp4 = ''
        self.threaddp5 = ''
        self.threadtick = ''
        self.printr.bg('yellow')
        self.DisableWidgets(self.go)
        safepath = os.path.join(rundir_, 'win_rms', filename) ###Old File Will Move to This Path '\\'.join([rundir_, safe_folder, filename])
        StatusDP(self.print3, 'New File is Downloading at [%s]'%downdir, fg='brown')
        StatusDP(self.print4, 'Old  File Will Move to  [%s]'%safepath, fg='brown')
        thr = threading.Thread(name='MRMS_Downloader', target=MrmsDownload_Thread,
                 args=(self, url, rundir_, filename, downdir, safepath, zipurl))
        thr.start()
        self.MonitorGo(thr)

    def MonitorGo(self, thr):
        if thr.is_alive():
            ###self.tcount += 1
            StatusDP(self.status, self.threaddp, fg='blue')
            StatusDP(self.printinfo, self.threaddp2, fg='blue')
            StatusDP(self.printinfo1, self.threaddp3, fg='blue')
            StatusDP(self.printinfo2, self.threaddp4, fg='blue')
            
            self.printr.SetLabel(self.threadtick)
            self.after(100, lambda:self.MonitorGo(thr))
        else:
            self.EnableWidgets()
            self.tcount = 0
            if self.sdmess:
                self.butt.SetLabel('Re-Start RMS')
                self.butt.fg('red')
                dinf = ("Download Task completed SuccessFully : Exit !")
                self.dsuccess = True
                self.dwn1.SetLabel(str(dinf))
                self.printr.SetLabel('100% Done !')
                StatusDP(self.status, dinf, fg='blue')
                StatusDP(self.printinfo, '', fg='blue')
                return
            else:
                errdsp = "Fail To Download, Check Your InternetConnection Once Again !!"
                self.printinfo.SetLabel(errdsp)
                StatusDP(self.status, errdsp, fg='red')
                self.go.SetLabel('Try Again')
                self.go.Enable()
                self.ggo.Enable()
                self.dsuccess = False
                self.butt.Enable()
                self.printr.bg('red')
                return
            
    def CheckDownloadFiles(self, url, downdir, rundir):
        chkpath = os.path.join(rundir, self.dfolder2, self.zipfname)
        if os.path.exists(chkpath):
            url = self.link2
            downdir = self.dfolder2   
        else:
            url = self.link1
            downdir = self.dfolder1
        return url, downdir
    
    def Connect(self, event=None):
        self.url = self.topstx.GetValue().strip()
        self.FilePrp(self.url, self.dfolder1, self.mrmspro)
        
    def GBconnect(self, event=None):
        self.mgmd = False
        self.url = self.topstx.GetValue().strip()
        self.zipdownloadfilename = self.zipfname
        self.FilePrp(self.link2zip, self.dfolder2, self.zipfname, zipurl=self.link2zip)
    
    def Copy_File(self, workfile, rundir_ ):
        ## 4. Copy New Downloaded File in Running Dir
        shutil.copy2(workfile, rundir_)
    
    def Submit(self, event=None):
        self.master.destroy()
        if self.dsuccess:
            try:
                ### if user close parent frame first then Error occured
                self.master.destroy()
                self.master.master.destroy()
                self.master.master.master.destroy()
            except:
                pass
            
            workfile = self.workfile
            rundir_ = self.rundir_
            if self.workfile:
                self.Copy_File(workfile, rundir_ )
            sys.exit(True)
        
    def OnDelOldFiles(self, event=None):
        filen = "mrms_pro_"
        for f in os.listdir('./'):
            if f.startswith(filen):
                os.remove('./%s'%f)
        self.deloldfile.fg('blue')
        if 'done' in self.deloldfile.GetLabel().lower():
            self.OnClose()
        self.deloldfile.SetLabel('Done !!')
        
    def OnRemovefileFiles(self, event=None):
        try:
            self.OnClose()
            rundir_ = os.path.dirname(sys.argv[0])
            rundir = self.parent.parent.resource_dic['myrmspath']
            winrmsfile = os.path.join(rundir, 'win_rms', 'mrms_pro.exe')
            t = threading.Thread(name='RFT', target=RFT, args=(rundir, winrmsfile))
            t.start()
        
            self.removefile.SetLabel('done')
            
            sys.exit(True)
        except Exception as err:
            StatusDP(self.printinfo, 'Cannot Remove Old Files [%s]'%str(err))
            
    def RefreshEntryBG(self, curentry, nextentry, resetcolor='white', mycolor='yellow', f=True):
        if f:
            self.RefreshWidgetFocus(curentry, nextentry)
        else:
            self.ResetAllEntry(resetcolor=resetcolor)
            
    def RefreshWidgetFocus(self, widg, nxtwidg):
        widg['bg'] = self['bg']
        nxtwidg['bg']='yellow'
        nxtwidg.focus_set()

    def Refresh3DButtEffect(self, downbutton=None):
        ### downbutton pass in strig so eval before reset
        for k,wdg in self.btndict.items():
            wdg.config(relief='raised')
            wdg.config(bg=self.bg)
        if downbutton:
            downbutton['relief']='sunken'
            downbutton['bg']=self.htcolor

    def OnClose_X(self, event=None):
        pass
    
    def OnClose(self, event=None):
        try:
            self.master.master.destroy()
        except Exception as err:
            pass
        
    def DisableWidgets(self, relwid, addjx=0, addjy=0):
        self.status.fg('red')
        self.status.SetLabel('Fetching Data.... Please Wait...!!')
        #x, y = self.WdgPOS(relwid)
        geo = {'r':2, 'c':0, 'cp':4, 'rp':4}
        ###self.imggif.GridShow(geo=geo)
        for w in self.otherwidglist:
            ##w['relief']='sunken'
            w.Disable()

    def EnableWidgets(self):
        ###self.imggif.GridHide()
        for w in self.otherwidglist:
            ##w['relief']='raised'
            w.Enable()
        self.status.fg('blue')
        self.status.SetLabel('Done')
        
"""        
def main():
    root = Tk()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    (mysofval, sdc, default_trade_rate, fontdct, fontid, df_discount,
    df_trade_marg, extend_marg, prt_name, prt_port, prt_share, taxname, 
    taxname2, xxdbinfo, hostn, prounit, expalert, bankinfo, owner, printmeth,
    taxdict, billseries, oemail, wcolor, sdc, stkmess, estifilter, txoe, onmoeb,
    decimalval, pdfpglines, iteminfo, qrcodeinfo, lockupdates, netpur_onsale_dp) = READ_RESOURCES_FILES()
    entryfsz = 12
    efnt_fg_bg = "Calibri Bold"
    subentryfont = "Calibri"
    fontd = {"calb":"Calibri Bold", "cal":"Calibri", "arl":"Arial", "arlb":"Arial Bold",
             "tnr":"Times New Roman", "tnrb":"Times New Roman Bold", "efnt_fg_bg":{'font': (efnt_fg_bg, entryfsz)},
             "subentryfont":{'font': (subentryfont, entryfsz)}}

    rmspath = os.path.dirname(sys.argv[0])
    #myprinter = GetPrinterDetails().GetDetails()
   
    reportlabfontdic = {'24': 'Times-Oblique', '03': 'Courier-BoldOblique', '01': 'Courier', '21': 'Times-Roman',
        '04': 'Courier-Oblique', '23': 'Times-BoldOblique', '1': 'Helvetica', '0': 'Courier',
        '3': 'Courier', '2': 'Times-Roman', '5': 'Courier-BoldOblique', '4': 'Courier-Bold',
        '7': 'Helvetica', '6': 'Courier-Oblique', '9': 'Helvetica-BoldOblique', '8': 'Helvetica-Bold',
        '02': 'Courier-Bold', '11': 'Helvetica-Bold',
        '10': 'Helvetica-Oblique', '13': 'Helvetica-Oblique', '12': 'Helvetica-BoldOblique', '22': 'Times-Bold'}
    reportlabfontid = '0'
    #ownerinfo, sdc, prpath, printerinfo, dbinfo, MyCalendarVal = InvokeF()
    ownerinfo, sdc, prpath, printerinfo, dbinfo, resetcursor, MyCalendarVal, oth_sett_rows, readconfigcsv, estibillseries = InvokeF()
    ostd = {'bill_series':oth_sett_rows[0],'pageline':oth_sett_rows[1], 'net_colm':oth_sett_rows[2],'party_bal':oth_sett_rows[3],
            'stockist_list':oth_sett_rows[4],
            'page_size':oth_sett_rows[5],'default_trade':oth_sett_rows[6],
            'billstartno':oth_sett_rows[7],'pdfpglines':oth_sett_rows[8],
            'sysfontnum':oth_sett_rows[9],'qrcodeinfo':oth_sett_rows[10],'lockupdates':oth_sett_rows[11],
            'netpur_onsale_dp':oth_sett_rows[12],}
    
    tax1 = {'0':'0', '2.5':'2.5', '6':'6', '9':'9', '14':'14',}
    tax2 = {'0':'0', '2.5':'2.5', '6':'6', '9':'9', '14':'14',}
    fpsum = {'oth': {'pay': [], 'recpt': [], 'bankrecpt': [], 'bankdep': [], 'bankpay': []},
             'sale': {'CREDIT': [], 'saledel': [], 'pcount': [], 'saleupdtcash': [],
                      'salereturn': [], 'returncount': [],
                      'CASH': [], 'saleupdtcredit': []},
             'pur': {'CREDIT': [], 'pcount': [], 'purreturn': [],
                     'purupdtcredit': [], 'returncount': [], 'purupdtcash': [],
                     'CASH': [], 'purdel': []}}
    prt_name, prt_port, prt_share = 'myprinter', 'LPT1', 'tvs'
    today = time.strftime('%d/%m/%Y', time.localtime(time.time()))
    today_db_f = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    fnlist = [u'', u'', u'', u'', u'', u'']
    rmsicon = os.path.join(rmspath, 'rmsicon.ico')
    billseries = oth_sett_rows[0]
    billstartno = oth_sett_rows[7]
    rscr = {'sw':sw, 'sh':sh, 'font':fontd, 'ownerdict':ownerinfo, 'fyear':'6','sdc':sdc,
            'daterange':{'fy':'fy6','dbfrm':'2021-04-01','frm':'01/04/2021','tod':'31/03/2022','partnum':'','dbtod':'2022-03-31'},
            'ledgerid':'0', 'itemid':'0', 'transid':'0', 'spid':'0', 'csid':'0', 'csname':'','dbinfo':dbinfo,'resetcursor':resetcursor,
            'itemidlist':[], 'spidlist':[],'renderlist':[],'rmsicon':rmsicon, 'rmspath':rmspath, 'prpath':prpath, 'printerinfo': printerinfo,
            'TABLENUM':'','the_time':'xx', 'mycalendar':MyCalendarVal, 'fpsum':fpsum, 'tax1':tax1, 'tax2':tax2,
            'itemname':'','sale':CSPD(), 'pur':SSPD(), 'saleupdt':CSPD(), 'purupdt':SSPD(), 'sitd':SITD(),
            'billseries':billseries,'sale_bill_series':billseries, 'sale_bill_start_no':billstartno,
            'esti_bill_series':estibillseries,'iteminfo':False,'printmeth':printmeth,'pdfpglines':oth_sett_rows[8],'page_size':oth_sett_rows[5],
            'qrcodeinfo':oth_sett_rows[10],'bankinfo':bankinfo, 
            'taxinvoice':True,'stkmess':'YES','decimalval':'2','last_esti_no':None, 'last_sale_bill_no':None,
            'fontdct':reportlabfontdic, 'fontid':reportlabfontid,'sysfontnum':14,'today':today, 'today_db_format':today_db_f,
            'prt_name':prt_name,'prt_port':prt_port,'prt_share':prt_share,'fnlist':fnlist}
    try:
        rscr['taxinfo']={'tax1name':readconfigcsv[6],'tax2name':readconfigcsv[7],'tax1lst':readconfigcsv[8].keys(),
                     'tax2lst':readconfigcsv[8].keys(), 'taxpayer':True}
    except :
        rscr['taxinfo']={'tax1name':'CGST', 'tax2name':'SGST','tax1lst':[], 'tax2lst':[], 'taxpayer':True}
    rscr['taxdict']=readconfigcsv[8]
    #sptag, spnum, buttonidx = 'RMS PLOT', 2, 0
    buttonidx = 9
    app = RmssUpdates(root, 'Upgrade RMSSoft', 1, buttonidx, None, rscr=rscr)
    root.mainloop()

if __name__ == '__main__':
    main()
"""
