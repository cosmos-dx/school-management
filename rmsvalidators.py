#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
try:
    # for Python2
    from Tkinter import *
    import ttk
    from ttk import Notebook, Combobox
    import tkFont
    import tkFileDialog as FileDialog
    import tkColorChooser as FiCor
    import Queue as queue
    #import Tkinter as tk
    #tk = Tk()
except ImportError:
    #print ('Python3 ')
    # for Python3
    from tkinter import filedialog as FileDialog
    from tkinter import colorchooser as FiCor
    from tkinter import *
    import tkinter as ttk
    import tkinter.font as tkFont
    from tkinter.ttk import Notebook, Combobox, Treeview, Style
    import queue as queue
from my_calculator import RMSCalculator
from datetime import datetime
import time

import operator
from functools import partial
import num2word as num2word
from collections import OrderedDict
from multiprocessing.pool import ThreadPool
import threading

def dates_frm(self):
    dfv = self.from_.GetValue()
    dtv = self.to_.GetValue()
    sdfv = self.from_.GetValue().split('/')
    sdtv = self.to_.GetValue().split('/')
    datebool = True
    try :
        fd = datetime.strptime(str(dfv), "%d/%m/%Y").strftime("%Y-%m-%d")
        fd1 = datetime.strptime(str(dtv), "%d/%m/%Y").strftime("%Y-%m-%d")
        if fd > fd1:
            RMSMBX(self, text="FROM DATE NEVER EXCEED THAN\n TO (today) DATE", textclr='red')
            self.from_.SetValue(self.rscr['today'])    
            self.from_.SetFocus()
            datebool = False
    except ValueError as err:
        pass
            
    try:
        fr_d, fr_m ,fr_y  = sdfv [0], sdfv[1], sdfv[2]
        if int(fr_d) > 31 :
            RMSMBX(self, text="INVALID Month From [%s]" % fr_d, textclr='red')
            
        elif int(fr_m) > 12 :
            RMSMBX(self, text="INVALID Month From [%s]" % fr_m, textclr='red')
            
    except IndexError as err:
        RMSMBX(self, text="DATE ERROR line 553 \n[%s]"%str(err), textclr='red')
        self.from_.SetFocus()
    return datebool

def dates_to(self):
    dfv = self.from_.GetValue()
    dtv = self.to_.GetValue()
    sdtv = self.to_.GetValue().split('/')
    try:
        to_d, to_m ,to_y  = sdtv[0], sdtv[1], sdtv[2]
        if to_d < 31 :
            RMSMBX(self, text="INVALID Month [%s]" % to_d, textclr='red')
        elif to_m < 12 :
            RMSMBX(self, text="INVALID Month [%s]" % to_m, textclr='red')
              
    except IndexError as err:
        RMSMBX(self, text="DATE ERROR line 568 \n[%s]"%str(err), textclr='red')
        self.to_.SetFocus()
    try:
        fd = datetime.strptime(str(dfv), "%d/%m/%Y").strftime("%Y-%m-%d")
        fd1 = datetime.strptime(str(dtv), "%d/%m/%Y").strftime("%Y-%m-%d")
        if fd > fd1:
            RMSMBX(self, text="FROM DATE CAN NOT EXCEED\nTHAN TO DATE", textclr='red') 
            self.to_.SetFocus()
    except ValueError as err:
        pass
    return True

Clist = ['Prep', 'L.K.G', 'U.K.G', 'I', 'II', 'III', 'IV','V','VI','VII','VIII','IX','X','XI','XII']
def Combox_Val(self, val):
    str_type = {'Prep':'50','L.K.G':'51','U.K.G':'52','I':'1','II':'2','III':'3','IV':'4',
                'V':'5','VI':'6','VII':'7','VIII':'8','IX':'9','X':'10','XI':'11','XII':'12'}
    key_val = str_type[val]
    return key_val
def Combox_Val_Reverse(re_val):
        str_type = {'51':'Prep','52':'L.K.G','53':'U.K.G','1':'I','2':'II','3':'III','4':'IV','5':'V',
                    '6':'VI','7':'VII','8':'VIII','9':'IX','10':'X','11':'XI','12':'XII'}
        key_val_reverse = str_type[re_val]
        return key_val_reverse
    
def RECDIC():
    return {'pan':{'id':'', 'billdate':'','invdate':'','billno':'','billas':'','crdr':'','dbcscr':'1','itype':'1',
    'cscr':'',
    'dbbilldate':'2000-01-01','dbinvdate':'2000-01-01','spid':'','ledid':'','csid':'','transid':'',
    'partyid':'','partyname':'','partyadd1':'','partyadd2':'','partyadd3':'','partyadd4':'',
    'gstn':'','regn':'','phn':'','mobile':'','email':'','pincode':'','modetx':'','cmnt':'',
    'partybal':'','prvcmnt':'','prvbal':'','partition':'','daterange':'','cmntdisp':'','cmntdisp1':'',
    'roundoff':'', 'gtot':'','tamt':'', 'ttaxable':'','ttaxamt':'','tax1amt':'','tax2amt':'','tdisamt':'',  
    'gtwords':'','itmcount':'','tax':'0','tax1':'0','tax2':'0','ttaxamt':'0','ddis':'0','pr_lo':[],'partydict':{},
    'updtval':'','pexpense':'','acentries':None,
    'static':{'pr_lo':0,'roundoff':'', 'gtot':'','tamt':'', 'ttaxable':'','tax1amt':'','tax2amt':'',
              'ttaxamt':'', 'tdisamt':'','gtwords':''}},  
    'ac':({'acname1':'','acval1':'','acledid1':'','actype1':'','actrasid1':'',
      'acname2':'','acval2':'','acledid2':'','actype2':'','actrasid2':'',
      'acname3':'','acval3':'','acledid3':'','actype3':'','actrasid3':'',}),
    'grid':({}),
    'edit':False, }
    
def CSPD():
    return {'partyinfo':None, 'transid':'0', 'bill_no':None, 
        'i_type':'1','saleid':'0','disamt':0,'taxamt':0, 'tax1amt':0, 'tax2amt':0,
        'netamt':0, 'payable':None, 'cgst':0,'sgst':0, 'spid':0, 'ledgerid':0, 'roundoff':0,
        'disc':'0', 'cmnt':'', 'expense':0, 'inv_date':'0', 'bil_date':None,'pryitmid':[], 
        'edit':False, 'amt':0, 'subtot':0, 'qty':None,'bill_as':'M','cscr':'1', 'itembatdict':{},'searchstkdict':{},
        'sit':{}, 'other':{},'taxadd':True}
        ### itemid+batck as key and value as {'itemid':id, 'bat':'batch', 'balstk':stk, 'exp':exp} will insert/update into Database directly
        ### will keep tracking Duplicate item entry and edit stock accordingly
        ### itembatdict = {'itemid':id, 'bat':'batch', 'balstk':stk, 'exp':exp}
def SSPD():
    return {'partyinfo':None, 'transid':'0', 'bill_no':None, 
        'i_type':'1','purchaseid':'0','disamt':0,'taxamt':0, 'tax1amt':0, 'tax2amt':0,
        'netamt':0, 'payable':None, 'cgst':0,'sgst':0, 'spid':0, 'ledgerid':0, 'roundoff':0,
        'disc':'0', 'cmnt':'','expense':0, 'inv_date':'0', 'bil_date':None,'pryitmid':[], 
        'edit':False, 'amt':0, 'subtot':0, 'qty':None,'bill_as':'M','cscr':'1','itembatdict':{},'searchstkdict':{},
        'sit':{}, 'other':{},'taxadd':True}
        ### itemid+batck as key and value as {'itemid':id, 'bat':'batch', 'balstk':stk, 'exp':exp} will insert/update into Database directly
        ### will keep tracking Duplicate item entry and edit stock accordingly
        ### itembatdict = {'itemid':id, 'bat':'batch', 'balstk':stk, 'exp':exp}
def SITD():
    return {'itemid':None, 'pname':None, 'pack':None, 'unit':None, 'bonus':'0', 'pr':0,
        'sr':0, 'rate1':0, 'rate2':0, 'mrp':0, 'tax1':0, 'tax2':0, 'itax':0, 'dis':0, 
        'psupid':0, 'hsnc':'','supid':0, 'dis':'0','netamt':0, 'qty':0, 'amt':0, 'taxamt':0, 
        'tax1amt':0,'tax2amt':0, 'disamt':0, 'net':0,'bat':'', 'stqty':0,'stqtyvar':0,
        'updtstaticstk':0, 'batstk':None,'exp':None,'pryitmid':None, 'rate_tax':'0',
        'group':'', 'rack':'', 'pitmnet':0}

def POSDICT():
    posdict = {'01':'Jammu And Kashmir','02':'Himachal Pradesh','03':'Punjab','04':'Chandigarh','05':'Uttarakhand','06':'Haryana',
    '07':'Delhi','08':'Rajasthan','':'', '09':'Uttar Pradesh','10':'Bihar','11':'Sikkim','12':'Arunachal Pradesh',
    '13':'Nagaland','14':'Manipur','15':'Mizoram','16':'Tripura','17':'Meghalaya','18':'Assam','19':'West Bengal','20':'Jharkhand',
    '21':'Odisa','22':'Chattisgarh','23':'Madhya Pradesh','24':'Gujarat','25':'Daman and Diu','26':'Dadar and Nagar Haveli',
    '27':'Maharashtra','28':'Andra Pradesh','29':'Karanataka','30':'Goa','31':'Lakshwadeep','32':'Kerala','33':'Tamil Nadu',
    '34':'Punducherry','35':'Andaman and Nicobar Island','36':'Telangana','37':'Andra Pradesh(New)', 15:True,
    'C':'COMPANY', 'P':'PERSON', 'H':'HUF', 'F':'FIRM', 'A':'(AOP)', 'T':'AOP(TRUST)','B':'(BOI)','L':'LOCAL AUTHORITY',
    'J': 'JURIDICAL PERSON', 'G':'GOVERNMENT', True:('Writing..','blue'), False:('Wrong Input','red'), }
    return posdict

def Reconnect(self):
    ### To Catch Newly Inserted/Updated/Deleted Data in real time
    cnn, cursor = self.rscr['resetcursor'](self.rscr['dbinfo']['host'],
                    self.rscr['dbinfo']['user'], self.rscr['dbinfo']['pass'],
                    self.rscr['dbinfo']['mydb'],)
    self.rscr['dbinfo']['cnn'] = cnn
    self.rscr['dbinfo']['cursor'] = cursor

def Flash(self, wdg, gt=250):
    bg = wdg.cget("background")
    fg = wdg.cget("foreground")
    wdg.configure(background=fg, foreground=bg)
    self.after(gt, lambda:Flash(self, wdg, gt))
    
def StatusDP(wdg, msg, fg='blue'):
    try:
        wdg.configure(fg=fg)
        wdg.configure(text=msg)
    except:   ### unexpected TclError Throw while running under threading
        pass
    
def FindRatio(tot, lst):
    "(total, list)"
    part = tot/(sum(lst))
    return [part*x for x in lst]
    
def txtvalid(setwidg, txt, posd, boolarg):
    #setwidg['text'] = posd[boolarg()][0]
    setwidg.config(text=posd[boolarg()][0])

def ON_ESCAPE_KEY(self, key, text=False, textclr='red', size=(300,100), pos=(300,200)):
    ''' mess=True, On Escape/End key will not display,
        MessageBox Close Directly, Default is False
    '''
    
    if key in ['Escape', 'End']:
        try:
            mbx = RMSMBX(self, text=text, textclr=textclr, info=False, size=size, pos=pos)
            if mbx.result:
                self.destroy()
                self.parent.destroy()
        except KeyboardInterrupt:
            pass
    if key in ['F12','F10']:
        from rmsof.my_calculator import Calculator
        Calculator().Show()
    return

def GSTTEXT_ENTRY(gstn, posd, setwidg, ln = 15, fgwc='red', fgrc='blue'):
    """Get GSTNumbers and Allow its Validation"""
    try:
        posd[gstn[:2]]
        for i in range(len(gstn[:2])):
            txtvalid(setwidg, gstn[:2], posd, gstn[:2][i].isdigit)
        setwidg['fg']=fgrc
        setwidg['text'] = posd[gstn[:2]]
        inctxt1 = posd[gstn[:2]]
    except KeyError:
        setwidg['fg'] = fgwc
        setwidg['text']='First Two Characters Must Be Interger Less Than 37'
        return False
    try:
        if gstn[2:7] == "":
            return False
        for i in range(len(gstn[2:7])):
            txtvalid(setwidg, gstn[2:7], posd, gstn[2:7][i].isalpha)
        try:
            inctxt1 = ' '.join([inctxt1, posd[gstn[2:6][3:4]]])
            setwidg['fg']=fgrc
            setwidg['text']= inctxt1
        except KeyError:
            pass
    except KeyError:
        return False
    try:
        if gstn[7:11] == "":
            return False
        for i in range(len(gstn[7:11])):
            txtvalid(setwidg, gstn[7:11], posd, gstn[7:11][i].isdigit)
    except KeyError:
        return False
    try:
        if gstn[11:12] == "":
            return False
        txtvalid(setwidg, gstn[11:12], posd, gstn[11:12].isalpha)
    except KeyError:
        return False
    try:
        if gstn[13:14] == "":
            return False
        txtvalid(setwidg, gstn[13:14], posd, gstn[13:14].isalpha)
        if gstn[13:14].upper() == "Z":
            setwidg['fg']=fgrc
            setwidg['text'] = inctxt1
        else:
            setwidg['bg']='red'
            setwidg['text']= 'Wrong Input'
    except KeyError:
        return False
    
def GstinChker(gstin):
    chrval = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chlen = len(chrval)
    chrdic = {chrval[i]:i for i in range(len(chrval))}
    numdic = {i:chrval[i] for i in range(len(chrval))}
    gstsp = [c for c in gstin]
    slgst = gstsp[:14] ### slice gst to fix up 14 chr, to validate last 15th chr
    get_weg = [chrdic[gstsp[i].upper()] if i%2 ==0 else chrdic[gstsp[i].upper()]*2
               for i in range(len(slgst))]
    get_qut = [get_weg[i]//chlen for i in range(len(slgst))]
    get_rmd = [get_weg[i]-(get_qut[i]*chlen) for i in range(len(get_weg))]
    get_tot = [sum([get_rmd[i],(get_qut[i])]) for i in range(len(get_weg))]
    lsttot = sum(get_tot)
    lstfnl = sum([lsttot, -((lsttot//chlen)*chlen)])
    vldnum = chlen-lstfnl
    partychr = gstin[14:15]
    try:
        rmsvald = numdic[vldnum]
    except:
        return False
    if partychr == rmsvald:
        return True#'GSTIN is VALID' 
    else:
        return False#'STOP =>> This GSTIN IS INVALID, WRONG'

def SetFocus(cw, cbg, nw, nbg):
    cw['bg']=cbg
    nw.focus()
    nw['bg']=nbg

def RMSThreadPlay(widg, text, msg, tevent):
    #ml = ['','','','=>','=','==','==','===>','===>','====','====','=====>','=====>',
    #      '======','======','=======>','=======>','=======>',]
    ##ml = ['',' W ',' Wa ',' Wai ',' Wait ',' Wait. ',' Wait.. ',' Wait... ',' Wait...! ',]
    count = 0
    widg.SetForegroundColour('black')
    tevent.wait()
    #### Display Thread will wait until main thread task is clear
    ### [ must clear in main thread after fininshing task, other wise display thread is active and continue displaying text]
    while tevent.isSet(): #### event is waiting and perform display Task here
        try:
            widg.SetLabel(''.join([str(msg), str(count), '',]))
            count += 1
            if count > 1000:
                widg.SetForegroundColour('blue')
            if count > 10000:
                widg.SetForegroundColour('red')
        except :
            break
    widg.SetLabel(text)
   
def RMSPLAY(widg, text, msg, tevent,):
    
    #self.rmsplaystx = wx.StaticText(self, wx.ID_ANY, (""),)
    #self.rmsplaystx.SetFont(wx.Font(40, wx.TELETYPE, wx.NORMAL, wx.BOLD))
    #self.rmsplaystx.Show()
    #self.rmsplaystx.SetPosition((350, 280))
    #self.status.SetBackgroundColour('white')
    #self.status.SetForegroundColour('green')
    
    tp = threading.Thread(name='RMSThreadPlay', target=RMSThreadPlay,
                         args=(widg, text, msg, tevent))
    #tp.setDaemon = True
    tp.start()

def LastYearDatesWidget(self, master, fyear, daterange, txt="Last Year Records:", **kw):
    frmdate = daterange['frm']
    todate = daterange['tod']
    self.lastfyear = int(fyear)-1
    self.fyeardtrange = [frmdate, todate]
    self.staticdates = [fyear, self.fyeardtrange]
    
    self.lastyearbv = BooleanVar()
    
    #self.lastyearcb = Checkbutton(master, text=txt, variable=self.lastyearbv)
    self.lastyearcb = RMSChkBut(master, text=txt, variable=self.lastyearbv, **kw) 
    self.lastfyeardtrange = [''.join([frmdate[:6], str(int(frmdate[6:])-1)]),
                        ''.join([todate[:6], str(int(todate[6:])-1)])]
    
    self.lastyearcb.bind('<Button-1>', self.Onlastyearcb)
    self.lastyearcb.bind('<Return>', self.Onlastyearcb)
    return self.lastyearbv, self.lastyearcb
    
def LastYearDates(self):
    'To View Last Year Records'
    if not self.lastyearbv.get():
        self.fyear = self.lastfyear
        self.fyeardtrange = self.lastfyeardtrange
        self.from_.SetValue(self.lastfyeardtrange[0])
        self.to_.SetValue(self.lastfyeardtrange[1])
        
    else:
        self.fyear = self.staticdates[0]
        self.fyeardtrange = self.staticdates[1]
        self.from_.SetValue(self.fyeardtrange[0])
        self.to_.SetValue(self.fyeardtrange[1])

class FlashLabel(Label):
    def flash(self, count=None):
        bg = self.cget('background')
        fg = self.cget('foreground')
        self.configure(background=fg,foreground=bg)
        ##count +=1
        ##if (count < 31):
        self.after(1000,self.flash, count)
             
class RMSChkBut(Checkbutton):
    def __init__(self, master=None, **kw):
        self.boolvar = kw['variable']
        Checkbutton.__init__(self, master, **kw)
        
    def GetLabel(self):return self['text']
    def SetLabel(self, txt):
        try:self.config(text=txt)#self['text']=txt
        except:pass
    def GetValue(self):return self.boolvar.get()
    def SetValue(self, b):self.boolvar.set(b)
    def ChangeValue(self, b):self.boolvar.set(b)
    def Enable(self):
        try:self.config(state='normal') #self['state']='normal'
        except:pass
    def Disable(self):
        try:self.config(state='disabled') #self['state']='disabled'
        except:pass
    def SetFocus(self):self.focus()
    def Show(self): pass
    def Hide(self): pass
    def fg(self, clr):
        try:self.config(fg=clr)#self['fg']=clr
        except:pass
    def bg(self, clr):
        try:self.config(bg=clr)#self['bg']=clr
        except:pass
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr

class RMSCombobox(Combobox):
    def __init__(self, master=None, **kw):
        if kw.get('textvariable'):
            self.var = kw['textvariable']
        else:
            self.var = StringVar(master)
        kw['textvariable'] = self.var
        Combobox.__init__(self, master, **kw)
        lft = kw.get('font')
        if not lft:
            lft = ('Calibri', '12', 'bold')
        master.option_add("*TCombobox*Listbox*Font", tuple(lft))
        
    def GetLabel(self):return self.var.get()
    def SetLabel(self, idx):
        try:self.current(idx)
        except:pass
    def GetValue(self):return self.var.get()
    def SetValue(self, val, idx=None):
        self.var.set(val)
        values = list(self['values'])
        values.append(val)
        self['values']=tuple(values)
            
    def ChangeValue(self, idx):self.current(idx)
    def Select(self, idx):self.current(idx)
    def Enable(self):
        try:self.config(state='normal') #self['state']='normal'
        except:pass
    def Disable(self):
        try:self.config(state='disabled') #self['state']='disabled'
        except:pass
    def SetFocus(self):self.focus()
    def Show(self): pass
    def Hide(self): pass
    def fg(self, clr):
        try:self.config(fg=clr)#self['fg']=clr
        except:pass
    def bg(self, clr):
        try:self.config(bg=clr)#self['bg']=clr
        except:pass
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr
    
class RMSRadioBut(Radiobutton):
    def __init__(self, master=None, **kw):
        self.boolvar = kw['variable']
        Radiobutton.__init__(self, master, **kw)
        
    def GetLabel(self):return self['text']
    def SetLabel(self, txt):
        try:self.config(text=txt)#self['text']=txt
        except:pass
    def GetValue(self):
        return self['value']
        ##return self.boolvar.get()
    def SetValue(self, b):
        self['value']=b
        self.boolvar.set(b)
    def ChangeValue(self, b):self.boolvar.set(b)
    def Enable(self):
        try:self.config(state='normal') #self['state']='normal'
        except:pass
    def Disable(self):
        try:self.config(state='disabled') #self['state']='disabled'
        except:pass
    def SetFocus(self):self.focus()
    def Show(self): pass
    def Hide(self): pass
    def fg(self, clr):
        try:self.config(fg=clr)#self['fg']=clr
        except:pass
    def bg(self, clr):
        try:self.config(bg=clr)#self['bg']=clr
        except:pass
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr
    
class RMS_LABEL(Label):
    def __init__(self, master=None, **kw):
        try:
            kw['bg']
        except :
            kw['bg'] = 'light yellow'
            kw['relief']=RIDGE
        Label.__init__(self, master, **kw)
        
    def GetLabel(self):return self['text']        
    def GetValue(self):
        try:
            return self['text']
        except:
            return ''
        
    def SetLabel(self, txt):
        try:
            self.config(text=txt)#self['text']=txt
        except Exception as err:
            pass
    def SetValue(self, txt):self.config(text=txt)#self['text']=txt
    def ChangeValue(self, txt):self.config(text=txt)#self['text']=txt
    def Show(self): pass
    def Hide(self): pass
    def Enable(self):self.config(state='normal') #self['state']='normal'
    def Disable(self):self.config(state='disabled') #self['state']='disabled'
    
    def fg(self, clr):self.config(fg=clr)#self['fg']=clr
    def bg(self, clr):self.config(bg=clr)#self['bg']=clr
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr

class RMS_IMGBUTTON(Button):
    def __init__(self, fpath, master=None, **kw):
        self.master = master
        self.fpath = fpath
        img = PhotoImage(file=fpath)
        Button.__init__(self, master, **kw)
        Button.config(image=img)
        self.bind('<Key>', self.OnKey)
        
    def OnKey(self, event=None):
        if event.keysym == 'Escape':
            self.master.master.OnClose(event) ### Calling Parent Class OnClose
        #if event.keysym == 'F12':
        #    filewin = Toplevel(self)
        #    RMSCalculator(filewin, 'RMS Calculator', 1, 1, self.master.master, rscr=self.rscr)
        #    return
        
    def GetLabel(self):return self['text']
    def SetLabel(self, txt):
        try:self.config(text=txt)#self['text']=txt
        except:pass
    def GetValue(self):return self['text']
    def SetValue(self, txt):self.config(text=txt)#self['text']=txt
    def ChangeValue(self, txt):self.config(text=txt)#self['text']=txt
    def Enable(self):
        try:self.config(state='normal') #self['state']='normal'
        except:pass
    def Disable(self):
        try:self.config(state='disabled') #self['state']='disabled'
        except:pass
    def IsEnable(self):
        st = False
        if self['state']!='disabled':
            st = True
        return st
    def IsDisable(self):
        st = False
        if self['state']=='disabled':
            st = True
        return st
    def SetFocus(self):self.focus()
    def Show(self, geo=[None, None]):
        ### geo zero index gives geometry type
        ### first index gives geometry information
        if geo[0] == 'grid':
            ginfo = geo[1] ### will be dictionary
            self.grid(row=ginfo['r'], column=ginfo['c'],
                      columnspan=ginfo['cp'],rowspan=ginfo['rp'],)
        if geo[0] == 'place':
            ginfo = geo[1] ### will be dictionary
            self.place(x=ginfo['x'],y=ginfo['y'])
            
    def Hide(self):
        self.pack_forget()
        self.grid_forget()
        self.place_forget()
        
    def fg(self, clr):
        try:self.config(fg=clr)#self['fg']=clr
        except:pass
    def bg(self, clr):
        try:self.config(bg=clr)#self['bg']=clr
        except:pass
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr
    
class RMS_BUTTON(Button):
    def __init__(self, master=None, **kw):
        self.master = master
        Button.__init__(self, master, **kw)
        self.bind('<Key>', self.OnKey)
    def OnKey(self, event=None):
        if event.keysym == 'Escape':
            self.master.master.OnClose(event) ### Calling Parent Class OnClose
        #if event.keysym == 'F12':
        #    filewin = Toplevel(self)
        #    RMSCalculator(filewin, 'RMS Calculator', 1, 1, self.master.master, rscr=self.rscr)
        #    return
        
    def GetLabel(self):return self['text']
    def SetLabel(self, txt):
        try:self.config(text=txt)#self['text']=txt
        except:pass
    def GetValue(self):return self['text']
    def SetValue(self, txt):self.config(text=txt)#self['text']=txt
    def ChangeValue(self, txt):self.config(text=txt)#self['text']=txt
    def Enable(self):
        try:self.config(state='normal') #self['state']='normal'
        except:pass
    def Disable(self):
        try:self.config(state='disabled') #self['state']='disabled'
        except:pass
    def IsEnable(self):
        st = False
        if self['state']!='disabled':
            st = True
        return st
    def IsDisable(self):
        st = False
        if self['state']=='disabled':
            st = True
        return st
    def SetFocus(self):self.focus()
    def Show(self, geo=[None, None]):
        ### geo zero index gives geometry type
        ### first index gives geometry information
        if geo[0] == 'grid':
            ginfo = geo[1] ### will be dictionary
            self.grid(row=ginfo['r'], column=ginfo['c'],
                      columnspan=ginfo['cp'],rowspan=ginfo['rp'],)
        if geo[0] == 'place':
            ginfo = geo[1] ### will be dictionary
            self.place(x=ginfo['x'],y=ginfo['y'])
            
    def Hide(self):
        self.pack_forget()
        self.grid_forget()
        self.place_forget()
        
    def fg(self, clr):
        try:self.config(fg=clr)#self['fg']=clr
        except:pass
    def bg(self, clr):
        try:self.config(bg=clr)#self['bg']=clr
        except:pass
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr
    
class CAP_ENTRY(Entry):
    def __init__(self, master=None, **kwargs):
        
        self.var = StringVar(master)
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        text = kwargs.get('text')
        if text:
            self.SetValue(text)
        self.var.trace('w', self.validate)

    def GetStrVar(self):return self.var
    def validate(self, *args):
        self.var.set(self.var.get().upper())

    def GetValue(self):return self.var.get()

    def SetValue(self, txt):self.var.set(txt)
    def ChangeValue(self, txt):self.var.set(txt)
    def SetFocus(self, select=True):
        self.focus()
        if select:
            self.select_range(0, 'end')
            self['state'] = 'normal'

    def Show(self): pass
    def Hide(self): pass
    def Enable(self):self.config(state='normal') #self['state']='normal'
    def Disable(self):self.config(state='disabled') #self['state']='disabled'
    def ReadOnly(self):self.config(state='readonly')
    def fg(self, clr):self.config(fg=clr)#self['fg']=clr
    def bg(self, clr):self.config(bg=clr)#self['bg']=clr
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr

class FLOAT_ENTRY(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar(master)
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        
        self.var.trace('w', self.validate)
        
    def GetStrVar(self):return self.var
    def validate(self, *args):
        try:
            float(self.var.get())
        except:
            self.var.set("")
            
    def GetValue(self):return self.var.get()
    def GetLabel(self):return self.GetValue()
    def SetValue(self, txt):
        self.delete('0', 'end')
        self.insert('end', txt)
    def ChangeValue(self, txt):self.var.set(txt)
    def SetFocus(self, select=True):
        self.focus()
        if select:
            self.select_range(0, 'end')
            self['state'] = 'normal'
    def SetLabel(self, txt):self.SetValue(txt)
    def Show(self): pass
    def Hide(self): pass
    def Enable(self):self.config(state='normal') #self['state']='normal'
    def Disable(self):self.config(state='disabled') #self['state']='disabled'
    def ReadOnly(self):self.config(state='readonly')
    def fg(self, clr):self.config(fg=clr)#self['fg']=clr
    def bg(self, clr):self.config(bg=clr)#self['bg']=clr
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr
    
class NUM_ENTRY(Entry):
    def __init__(self, master=None, varinsert=None, **kwargs):
        
        self.var = StringVar(master)
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.var.trace('w', self.validate)

    def GetStrVar(self):return self.var
    def validate(self, *args):
        if self.var.get().isdigit():
            self.var.set(self.var.get())
        else:
            self.var.set("")

    def GetValue(self):return self.var.get()
    def GetLabel(self):return self.GetValue()
    def SetValue(self, txt):
        self.delete('0', 'end')
        self.insert('end', txt)
    def SetLabel(self, txt):self.SetValue(txt)
    
    def ChangeValue(self, txt):self.var.set(txt)
    
    def SetFocus(self, select=True):
        self.focus()
        if select:
            self.select_range(0, 'end')
            self['state'] = 'normal'

    def SelectAll(self):
        self.select_range(0, 'end')
        
    def Show(self): pass
    def Hide(self): pass
    def Enable(self):self.config(state='normal') #self['state']='normal'
    def Disable(self):self.config(state='disabled') #self['state']='disabled'
    def ReadOnly(self):self.config(state='readonly')
    def fg(self, clr):self.config(fg=clr)#self['fg']=clr
    def bg(self, clr):self.config(bg=clr)#self['bg']=clr
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr
    
class RMS_ENTRY(Entry):
    def __init__(self, master=None, **kw):
        self.kw = kw
        
        try:
            ### self.vld >> True for uppercase AND False for lowercase
            self.vld = kw['kw'][1]['vld']
        except:
            ### for lowercase
            self.vld = False
        try:
            self.limit = kw['kw'][1]['limit']
        except:
            self.limit = 4
        try:
            if kw.get('kw'):
                self.var = StringVar(master)
                entryparam = kw['kw'][1]['entryparam']
            else:
                self.var = kw['textvariable']
                entryparam = kw
        except Exception as err:
            self.var = StringVar(master)
            entryparam = {'bd':3,'fg':'black', 'relief':'sunken'}
            entryparam.update(kw)
        
        Entry.__init__(self, master, **entryparam)
        text = kw.get('text')
        #if text:
        #    self.SetValue(text)
        self.var.trace('w', self.validate)
        self.bind('<Key>', self.OnKey)
        
    def GetStrVar(self):return self.var
    def OnKey(self, event=None):
        
        if event.keysym == 'Escape':
            try:
                self.master.master.OnClose(event) ### Calling Parent Class OnClose
            except AttributeError:
                pass
        #if event.keysym == 'F12':
        #    filewin = Toplevel(self)
        #    RMSCalculator(filewin, 'RMS Calculator', 1, 1, self.master.master, rscr=self.rscr)
        #    return
        
    def validate(self, *args):
        self.var.set(self.var.get().upper())
        if self.vld:
            try:
                self.var.set(self.var.get().upper()[:self.limit])
            except:
                return True
        else:
            return True

    def GetValue(self):return self.var.get()
    def GetLabel(self):return self.GetValue()
    def SetValue(self, txt):
        try:
            self.delete('0', 'end')
            self.insert('end', txt)
        except :
            pass
    def SetLabel(self, txt):self.SetValue(txt)
    def ChangeValue(self, txt):self.var.set(txt)
    
    def SetFocus(self, select=True):
        self.focus()
        if select:
            self.select_range(0, 'end')
            self['state'] = 'normal'

    def Show(self): pass
    def Hide(self):
        self.pack_forget()
        self.grid_forget()
        self.place_forget()

    def SelectAll(self):
        self.select_range(0, 'end')
        
    def Enable(self):
        try:
            self.config(state='normal') #self['state']='normal'
        except:pass
    def Disable(self):
        try:
            self.config(state='disabled') #self['state']='normal'
        except:pass
        
    def ReadOnly(self):
        try:
            self.config(state='readonly') #self['state']='normal'
        except:pass
        
    def fg(self, clr):self.config(fg=clr)#self['fg']=clr
    def bg(self, clr):self.config(bg=clr)#self['bg']=clr
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr
    
class RMSLBX(Listbox):
    def __init__(self, master, parent, **kw):
        Listbox.__init__(self, master, **kw)
        self.itemlc_dict = {}
        try:
            self.staticlimit = int(kw['height'])-1
        except:
            self.staticlimit = 10
        self.datavarlimit = 0
        self.r,self.c = -1,-1
        self._number_of_rows=0 
        self.kmcount = -1
        self.datalen = None
        self.rscr = parent.rscr
        self.parent = parent
        self.qfunc = None
        self.text = ''
        self.bind('<Key>', self.OnKey)
        
    def OnKey(self, event=None):
        if event.keysym == 'Escape':
            self.master.master.OnClose(event) ### Calling Parent Class OnClose
                
    def ReturnErrorOnKeyMove(self):
        self.kmcount = 0
        if self.itemlc_dict:
            return [self.itemlc_dict[self.kmcount], self.kmcount]
        else:
            return [self.itemlc_dict, self.kmcount]
        
    def KeyMove(self, key, dpkey):
        knum, msg = 0, None
        if key in ['Down']:
            knum, kidx = self.MoveDown(dpkey)
            try:
                return [self.itemlc_dict[knum], kidx]
            except:
                return self.ReturnErrorOnKeyMove()
        if key in ['Up']:
            knum, kidx = self.MoveUp(dpkey)
            try:
                return [self.itemlc_dict[knum], kidx]
            except KeyError:
                return self.ReturnErrorOnKeyMove()
                
        if key in ['Return','Tab','End']:
            self.datavarlimit = 0
            return [self.itemlc_dict[self.kmcount], self.kmcount]
        if key in ['equal','plus','Insert']:
            return [self.itemlc_dict[knum], self.kmcount]
        if self.itemlc_dict:
            return [self.itemlc_dict[0], self.kmcount]
        
        else:
            self.selection_set(0)
            return [None, self.kmcount]
        
    def MoveDown(self, dpkey):
        if self.kmcount == self.staticlimit-1:
            self.datavarlimit += self.staticlimit
            if self.qfunc:
                self.setdata_(self.qfunc, self.text, dpkey)
               
            return [self.kmcount, self.kmcount]
        self.selection_clear(self.kmcount) ### clear is less than set when move down
        self.kmcount += 1
        self.selection_set(self.kmcount) ### set is greater than clear when move down
        return [self.kmcount, self.kmcount]
        
    def MoveUp(self, dpkey):
        if self.kmcount<1:
            self.datavarlimit -= self.staticlimit
            if self.datavarlimit < 0:
                self.datavarlimit = 0
                return [self.kmcount, self.kmcount]
            if self.qfunc:
                self.setdata_(self.qfunc, self.text, dpkey)
                self.kmcount = self.staticlimit-1
                self.selection_set(self.staticlimit-1)
                self.selection_clear(0)
            return [self.kmcount, self.kmcount]
        self.selection_clear(self.kmcount) ### clear is grater than set when move up
        self.kmcount -= 1
        self.selection_set(self.kmcount) ### set is less than clear when move up
        return [self.kmcount, self.kmcount]
        
    def InsertStringItem(self, i, txt=''):
        self.r += 1
        self._number_of_rows=self.r
        self.kmcount = -1
        
    def SetStringItem(self, r, c, txt):
        self.itemlc_dict[self.r]=txt.encode('utf-8')
        ###self.boxes[c].insert(self.r, str(txt))
        self.insert(self.r, txt.encode('utf-8')) ### to prevent 'ascii' code error
        ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
        self.kmcount = 0
        self.selection_set(self.kmcount)

    def VertualSetString(self, r, c, txt):
        ### self.itemlc_dict NEVER take assigments here
        self.insert(r, txt.encode('utf-8'))
        self.r = r
        self.kmcount = 0
        self.selection_set(self.kmcount)
        
    def SetDictItem(self, dict, idxkey, dpkey):
        self.r += 1
        self.itemlc_dict[self.r]=dict
        r = len(self.itemlc_dict)
        self.delete(0, 'end')
        for i, (k,v) in enumerate(self.itemlc_dict.items()):
            self.insert(i, v['prodname'])
        #self.insert(r, self.itemlc_dict[idxkey][dpkey]) ### to prevent 'ascii' code error
        ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
        self.kmcount = 0
        self.selection_set(self.kmcount)
        
    def DeleteAllItems(self):
        self.delete(0, 'end') ### Clear Box First
        self.Reset_arg()
    def DeleteItem(self, r):self.delete(r, 'end')
    def GetNumberRows(self):return len(self.itemlc_dict)
    def GetNumberCols(self):return self.columns
    def GetColLabelValue(self, idx):return self.colconf[idx]['text']
    def SetColLabelValue(self, idx, text):self.colconf[idx]['text']=text
    def GetFocusedItem(self):return self.curselection()
    def GetFirstSelected(self):return self.curselection()
    def GetIndex(self):return self.curselection()
    def GetItemCount(self):return self.size()
    def ItemCount(self):return self.size()
    def GetColumnCount(self):return 1
    def GetValue(self, idx):return self.get(idx)
    def GetText(self):return self.get(0)
    def GetItemText(self, idx):return self.get(idx)
    def GetItemData(self, r):return self.GetRowItem(r)
    def GetRowItem(self, r):return self.get(r)
    def GetRowDict(self, r):return self.itemlc_dict[r]
    def SetItemBackgroundColour(self,idx, clr):pass
    def SetFocus(self):self.focus_set()
    def GETDATA(self, idx=0):
        try:
            return self.itemlc_dict[idx]
        except KeyError:
            return {}
        
    def SETDATA(self, qfunc, text, dpkey, staticlimit=None):
        self.qfunc = qfunc
        self.text = text
        if staticlimit:
            self.staticlimit = staticlimit
        else:
            staticlimit = self.staticlimit
        
        self.setdata_(qfunc, text, dpkey, staticlimit=staticlimit)
        return self.GETDATA()
    
    def setdata_(self, qfunc, text, dpkey, staticlimit=None):
        if not staticlimit:
            staticlimit = self.staticlimit
        self.delete(0, 'end') ### Clear Box First
        self.itemlc_dict = qfunc(self.rscr, text, varlimt=self.datavarlimit, staticlimit=staticlimit)
        for i, (k,v) in enumerate(self.itemlc_dict.items()):
            self.InsertStringItem(i, str(''))
            self.insert(i, str(v[dpkey].encode('utf-8')))
        self.kmcount = 0
        self.selection_set(self.kmcount)
        
    def Show(self):
        self.datavarlimit = 0
    def Hide(self):
        self.datavarlimit = 0
    def Refresh(self):pass
    def RefreshItems(self):pass
    def RefreshItem(self):pass
    def Reset_arg(self):
        self.itemlc_dict = {} ### containing name as key(r,c) and values 
        self._number_of_rows = 0
        self.r = 0
        self.kmcount = -1
        
    def Enable(self):self.config(state='normal') #self['state']='normal'
    def Disable(self):self.config(state='disabled') #self['state']='disabled'
    def fg(self, clr):self.config(fg=clr)#self['fg']=clr
    def bg(self, clr):self.config(bg=clr)#self['bg']=clr
    def SetForegroundColour(self, clr):self.config(fg=clr)#self['fg']=clr
    def SetBackgroundColour(self, clr):self.config(bg=clr)#self['bg']=clr

class RMSLBN(Frame):
    def __init__(self, master, parent, header, height, colconf, **kw):
        Frame.__init__(self, master )
        #Frame.__init__(self, master, **kw)
        self.master = master
        self.header = header
        self.height = height
        self.colconf = colconf
        self.columns = len(colconf)
        self.collabel = {}
        self.rlst = [] ## return selected list to parent/master
        self.ColorTags = False
        self.rscr = parent.rscr
        self.parent = parent
        ##self.grid(row=8, column=4)
        self.SetupLB(colconf)
        self.loadnext = True
        self.itemlc_dict = {} ### containing name as key(r,c) and values
        self.uniqueid_dict = {} ### will assign with uniqueid as key; work on demand only 
        self.staticlimit = height ###10
        
        self.rows = height
        self.datavarlimit = 0
        self.r,self.c = -1,-1
        self._number_of_rows=0 
        self.kmcount = -1
        self.datalen = None
        self.qfunc = None
        self.text = ''
        self.sumcr_dr = [0,0]
        
    def GetSumCr_Dr(self):
        return self.sumcr_dr
    
    def ResetBox(self):
        self.headlab.grid_forget()
        self.headlab.destroy()
        for box in self.boxes:
            box.grid_forget()
            box.destroy()
      
    def SetupLB(self, colconf):
        self.boxes = []
        self.r, self.c = 0, 0
        self.index = 0
        self.lbkidx = 0
        #self.rowconfigure(1, weight=1)
        
        wrow = colconf[0].get('wrow')
        if wrow:
            wrow = wrow
        else:
            wrow = 0
        master = self.master
        srow = wrow
        self.headerdict, self.boxdict = {}, {}
        chkkeys = ['width','bd','bg','fg','relief','font','height',]
        
        if self.header:
            for k, v in colconf.items():
                kw = {}
                for x in chkkeys:
                    if v.get(x):
                        kw[x]=v[x]
                '''
                if v.get('width'):
                    kw = {'width':v['width'],'bd':v['bd'],'bg':v['bg'],
                      'fg':v['fg'],'font':v['font'],'relief':v['relief'],}
                else:
                    kw = {'bd':v['bd'],'bg':v['bg'],
                      'fg':v['fg'],'font':v['font'],'relief':v['relief'],}
                '''
                self.headlab = Label(self, text=v['text'], **kw)
                self.headlab.grid(row=srow, column=k, sticky='s',)
                self.headerdict[k]={'label':self.headlab, 'kw':kw}
            srow += 1
        for col, v in colconf.items():
            kw = {}
            for x in chkkeys:
                if v.get(x):
                    kw[x]=v[x]
            kw['height']=self.height
            '''
            if v.get('width'):
                kw = {'width':v['width'],'bd':v['bd'],'bg':v['bg'],'height':self.height,
                  'fg':v['fg'],'font':v['font'],'relief':v['relief'],}
            else:
                kw = {'bd':v['bd'],'bg':v['bg'],'height':self.height,
                  'fg':v['fg'],'font':v['font'],'relief':v['relief'],}
            '''
            box = Listbox(self, exportselection=False, **kw)
            ##box.bind('<<ListboxSelect>>', self.OnSelectedL, )
            box.bind('<Double-1>', self.OnDoubleClick)
            box.bind('<Return>', self.OnSelectedR)
            box.bind('<Key>', self.OnKey)
            
            self.bind("<Enter>", self.OnScroll)
            self.bind("<Leave>", self.OffScroll)
            ##box.grid(**v['wrc'])
            box.grid(row=srow, column=col, sticky='n', )
            #self.columnconfigure(col, weight=1)
            self.boxes.append(box)
            self.boxdict[col]={'box':box, 'kw':kw}
            self.collabel[col]=v['idname'] 
        self.colconf = colconf
        for r in range(self.height):
            self.rowconfigure(r, weight=1)
        for r in range(self.columns):
            self.columnconfigure(r, weight=1)

    def OnDoubleClick(self, event=None):
        ### Double Click will act as Return Key [Both behaviour are taken as same]
        self.OnSelected(event, evtname='Return')        
    def OnSelectedR(self, event=None): 
        self.OnSelected(event, evtname='Return')
    def OnSelectedL(self, event=None): 
        self.OnSelected(event, evtname='LB')
    def OnSelected(self, event, evtname):
        try:
            r, c = event.widget.curselection()##[0]
        except (IndexError,ValueError) :
            try:
                r = event.widget.curselection()[0]
            except IndexError:
                r = 0
            c = 0
        self.r = r, c, self
        if self.r:
            self.parent.GetLCSelectData(self.r, self.itemlc_dict, evtname)
            #for i, box in enumerate(self.boxes):
            #    box.selection_clear(i)
            self.Lselection_clear(self.kmcount)
            if isinstance(self.r, int):
                self.kmcount = self.r
            else:
                self.kmcount = self.r[0]
            self.Lselection_set(self.kmcount)
        return [self.r, self.itemlc_dict]

    def OnScroll(self, event):
        for box in self.boxes:
            box.bind_all("<MouseWheel>", self.ScrollStart)
        
    def OffScroll(self, event):
        for box in self.boxes:
            box.unbind_all("<MouseWheel>")
    
    def ScrollStart(self, event):
        
        if event.delta < 0:
            self.lcdata, kidx = self.KeyMove('Down', 'name') 
        else:
            self.lcdata, kidx = self.KeyMove('Up', 'name')
        try:
            self.r = (kidx,)
            self.parent.GetLCSelectData(self.r, self.itemlc_dict, 'Scroll')
        except Exception as err:
            pass
        
    def OnKey(self, event):
        key = event.keysym
        if key in ['Next','End']:
            self.lcdata, kidx = self.KeyMove('Down', 'name')
            self.r = [kidx, 0, self]
            self.parent.GetLCSelectData(self.r, self.itemlc_dict, 'Scroll')
            return
        if key in ['Prior','Home']:
            self.lcdata, kidx = self.KeyMove('Up', 'name')
            self.r = [kidx, 0, self]
            self.parent.GetLCSelectData(self.r, self.itemlc_dict, 'Scroll')
            return

        self.lcdata, kidx = self.KeyMove(key, 'name')
        if key == 'Escape':
            try:
                self.master.OnClose(event) ### Calling Parent Class OnClose
            except :
                pass
            
        if key == 'F12':
            filewin = Toplevel(self)
            RMSCalculator(filewin, 'RMS Calculator', 1, 1, self.parent, rscr=self.rscr)
            return
        try:
            r = event.widget.curselection()[0]
        except Exception :
            r = 0
        c = 0
        self.r = [r,c,self]
        self.parent.GetLCSelectData(self.r, self.itemlc_dict, key)
        
    def ReturnErrorOnKeyMove(self):
        self.kmcount = 0
        if self.itemlc_dict:
            return [self.itemlc_dict[self.kmcount], self.kmcount]
        else:
            return [self.itemlc_dict, self.kmcount]
        
    def KeyMove(self, key, dpkey):
        knum, msg = 0, None
        if key in ['Down']:
            knum, kidx = self.MoveDown(dpkey)
            try:
                return [self.itemlc_dict[knum], kidx]
            except KeyError:
                return self.ReturnErrorOnKeyMove()
        if key in ['Up']:
            knum, kidx = self.MoveUp(dpkey)
            try:
                return [self.itemlc_dict[knum], kidx]
            except KeyError as err:
                return self.ReturnErrorOnKeyMove()
                
        if key in ['Return','Tab','End']:
            if self.qfunc:
                ### if qfunc(database query) is given for data flow in chunks
                ### self.datavarlimit reset to ZERO to allow new data
                ### else self.datavarlimit remain constant, to catch accurate index of data
                self.datavarlimit = 0
            
            if self.itemlc_dict:
                return [self.itemlc_dict[self.kmcount], self.kmcount]
            else:
                return ['', self.kmcount]
        if self.itemlc_dict:
            return [self.itemlc_dict[0], self.kmcount]
        
        else:
            self.Lselection_set(0)
            return [None, self.kmcount]
    
    def MoveDown(self, dpkey):
        if self.kmcount == self.staticlimit-1:
            self.datavarlimit += self.staticlimit
            if self.qfunc:
                if self.text[0]:
                    self.setdata_(self.qfunc, self.text, dpkey)
                else:
                    pass
            else:
                if self.loadnext:
                    self.VirtualDeleteAllItems()
                    self.DisplayLBData(chunk=False, idx=self.datavarlimit)
                self.Lselection_clear(self.kmcount) ### clear is less than set when move down
                self.kmcount = 0
                self.Lselection_set(self.kmcount) ### set is greater than clear when move down
            
            return [self.kmcount, self.kmcount]
        if self.GetSize()-1 == self.kmcount: ### reached at last visible Item
            self.Lselection_clear(self.kmcount)
            self.kmcount = 0
            self.Lselection_set(self.kmcount)
            return [self.kmcount, self.kmcount]
        if self.GetSize() == 0: ##ListBox is Empty and need to refill From Start
            self.Lselection_clear(self.kmcount)
            self.DisplayLBData()
            self.kmcount = 0
            self.Lselection_set(self.kmcount)
            return [self.kmcount, self.kmcount]
        self.Lselection_clear(self.kmcount) ### clear is less than set when move down
        self.kmcount += 1
        self.Lselection_set(self.kmcount) ### set is greater than clear when move down
        return [self.kmcount, self.kmcount]
        
    def MoveUp(self, dpkey):
        if self.kmcount<1:
            self.datavarlimit -= self.staticlimit
            if self.datavarlimit < 0:
                self.datavarlimit = 0
                return [self.kmcount, self.kmcount]
            if self.qfunc:
                self.setdata_(self.qfunc, self.text, dpkey)
                self.kmcount = self.staticlimit-1
                self.Lselection_set(self.staticlimit-1)
                self.Lselection_clear(0)
            else:
                if self.loadnext:
                    self.VirtualDeleteAllItems()
                    self.DisplayLBData(chunk=False, idx=self.datavarlimit)
                self.kmcount = self.staticlimit-1
                self.Lselection_set(self.kmcount) 
                self.Lselection_clear(0) 
            return [self.kmcount, self.kmcount]
        self.Lselection_clear(self.kmcount)   ### clear is grater than set when move up
        self.kmcount -= 1
        self.Lselection_set(self.kmcount)  ### set is less than clear when move up
        return [self.kmcount, self.kmcount]

    def GETDATA(self, idx=0):
        try:
            return self.itemlc_dict[idx]
        except KeyError:
            return {}
        
    def SETDATA(self, qfunc, text, dpkey, staticlimit=None):
        self.qfunc = qfunc
        self.text = text
        if staticlimit:
            self.staticlimit = staticlimit
        else:
            staticlimit = self.staticlimit
        
        self.setdata_(qfunc, text, dpkey, staticlimit=staticlimit)
        return self.GETDATA()
    
    def setdata_(self, qfunc, text, dpkey, staticlimit=None):
        if not staticlimit:
            staticlimit = self.staticlimit
        for box in self.boxes:
            try:
                box.delete(0, 'end') ### Clear Box First   
            except:
                pass
        self.itemlc_dict = qfunc(self.rscr, text, varlimt=self.datavarlimit, staticlimit=staticlimit)
        if self.itemlc_dict:
            self._number_of_rows = len(self.itemlc_dict)
        else:
            self._number_of_rows = 0
        self.DisplayLBData()
       
        self.kmcount = 0
        self.Lselection_set(self.kmcount)

    def DisplayLBData(self, chunk=True, idx=0):
        keyerr = [False, '']
        
        if not self.itemlc_dict:
            return [True, 'No Data Found']
        if chunk:
            for k in range(self.staticlimit):
                try:
                    self.itemlc_dict[k]['sno']=sum([self.datavarlimit, k])
                except KeyError:
                    pass
                for c in range(self.columns):
                    ckey = self.colconf[c]['idname']
                    try:
                        self.boxes[c].insert('end', self.itemlc_dict[k][ckey])
                    except (KeyError, TypeError) as err:
                        keyerr = [True, str(err)]
        else:
            
            for r in range(self.staticlimit):
                try:
                    self.itemlc_dict[idx]['sno']=sum([self.datavarlimit, idx])
                except KeyError:
                    pass
                for c in range(self.columns):
                    ckey = self.colconf[c]['idname']
                    try:
                        self.boxes[c].insert('end', self.itemlc_dict[idx][ckey])
                    except (KeyError, TypeError) as err:
                        keyerr = [True, str(err)]
                idx += 1
        self._number_of_rows = len(self.itemlc_dict)
        
        if self.ColorTags:
            if not self.itemlc_dict:
                return keyerr
            if self.itemlc_dict[0].has_key('name'):
                self.ResetPartyColorTags()
            else:
                self.ResetLedgerColorTags()
        
        return keyerr

    def ResetPartyColorTags(self):
        ### spid = 1 (suppliers)(powderblue); spid = 2 (customer)(lightgreen); 
        ### spid = 3 (expence)(lightyellow); spid = 4 (not defined yet); 
        ### spid = 5 (cash)(lightgrey); spid = 6 (company)(purpel); spid = 7 (bank)(lightorange);
        ### #ffff80 = light yellow; #c6ffb3 = light green; #e6ffff = light aqua blue
        ### #f2f2f2 = light grey; #c6ffb3 = light green; #ffd699 = light orange
        ### #ffb3b3 = light red; #ccb3ff= light purpel; yellow = #ffff4d
        clrdic = {0:{'bg':'white'},1:{'bg':'#e6ffff'},2:{'bg':'#c6ffb3'},3:{'bg':'#ffff4d'},
            4:{'bg':'#ffffb3'},5:{'bg':'#f2f2f2'},6:{'bg':'#ccb3ff'},7:{'bg':'#ffd699'},
            8:{'bg':'#ffb3b3'},9:{'bg':'#ffb3b3'},}
        reloadata = False
        for i in range(self.rows):
            for lb in self.boxes:
                try:
                    lb.itemconfig(i, clrdic[self.itemlc_dict[i]['spid']])
                except Exception :
                    reloadata = True
                    break
        
    def ResetLedgerColorTags(self):
        ### spid = 1 (suppliers)(powderblue); spid = 2 (customer)(lightgreen); 
        ### spid = 3 (expence)(lightyellow); spid = 4 (not defined yet); 
        ### spid = 5 (cash)(lightgrey); spid = 6 (company)(purpel); spid = 7 (bank)(lightorange);
        ### #ffff80 = light yellow; #c6ffb3 = light green; #e6ffff = light aqua blue
        ### #f2f2f2 = light grey; #c6ffb3 = light green; #ffd699 = light orange
        ### #ffb3b3 = light red; #ccb3ff= light purpel; #ffff4d = yellow
        clrdic = {0:{'bg':'white'},1:{'bg':'#e6ffff'},2:{'bg':'#c6ffb3'},3:{'bg':'#ffff4d'},
            4:{'bg':'#ffffb3'},5:{'bg':'#f2f2f2'},6:{'bg':'#ccb3ff'},7:{'bg':'#ffd699'},
            8:{'bg':'#ffb3b3'},9:{'bg':'#ffb3b3'},}
        idx = self.datavarlimit
        for i in range(self.rows):
            #print clrdic[self.itemlc_dict[idx]['spid']]
            for lb in self.boxes:
                try:
                    lb.itemconfig(i, clrdic[self.itemlc_dict[idx]['spid']])
                except Exception as err:
                    pass
                
            idx += 1
    
    def SetFocus(self):
        self.boxes[0].focus_set()

    def SetFocusRow(self, row):
        for box in self.boxes:
            box.focus_set()
            box.selection_set(0, None)
        self.kmcount = 0
        
    def Hide(self, data=True):
        self.kmcount = 0
        try:
            self.grid_forget()
            self.place_forget()
        except :
            pass
        if data:
            self.Reset_arg()
        
    def Show(self, x=400, y=200, ):
        self.kmcount = 0
        self.lift(aboveThis=None)
        self.place(x=x, y=y)

    def ShowGrid(self, r=0, c=0, rsp=1, csp=1, sticky='e'):
        self.kmcount = 0
        self.grid(row=r, column=c,
                rowspan=rsp, columnspan=csp, sticky=sticky)
        self.lift(aboveThis=None)
        
    def GetNumberRows(self):return len(self.itemlc_dict)
    def GetNumberCols(self):return self.columns
    def GetColLabelValue(self, idx):return self.colconf[idx]['text']
    def SetColLabelValue(self, idx, text):self.colconf[idx]['text']=text
    
    def GetIndex(self):
        self.index = [box.curselection() for box in self.boxes][0][0]
        return self.index
    
    def GetItem(self, r, c):
        self.r, self.c = r, c
        return self
    
    def GetItemData(self, r):return self.GetRowItem(r)
    
    def GetRowItem(self, r):return [box.get(r) for box in self.boxes]
        
    def GetText(self):return [box.get(self.r) for box in self.boxes][self.c]
    
    def GetItemText(self, idx):return [box.get(idx) for box in self.boxes][0]
        ### Text first column

    def GetRowDict(self, r):return self.itemlc_dict[r]
        
    def GetFocusedItem(self):return self.GetIndex()

    def GetFirstSelected(self):return self.GetIndex()
    
    def GetItemCount(self):return self.boxes[0].size()
    def ItemCount(self):return self.boxes[0].size()

    def GetColumnCount(self):return len(self.boxes)

    def SetItemBackgroundColour(self,idx, clr):
        pass

    def Enable(self):
        try:self.config(state='normal') #self['state']='normal'
        except:pass
    def Disable(self):
        try:self.config(state='disabled') #self['state']='disabled'
        except:pass
        
    def Reset_arg(self):
        self.itemlc_dict = {} #### containing name as key(r,c) and values 
        self._number_of_rows = 0
        self.r = 0
        self.kmcount = -1
        self.datavarlimit = 0
        
    def VirtualDeleteAllItems(self):
        for i in range(self.GetSize()):
            for box in self.boxes:
                box.delete(i, 'end')
                
    def DeleteAllItems(self):
        for i in range(self.GetSize()):
            for box in self.boxes:
                box.delete(i, 'end')
        self.Reset_arg()

    def ClearAll(self):
        self.DeleteAllItems()

    def Clear(self):
        self.DeleteAllItems()
        
    def DeleteItem(self, r):
        delitems = []
        for box in self.boxes:
            delitems.append(box.get(r))
            box.delete(r, 'end')
        return delitems
    
    def RefreshItems(self):pass

    def RefreshItem(self):
        ### Remove Dublicates in list box and itemlc_dict
        pass
    
    def InsertItem(self, r, txt=''):
        self.r += 1
        self._number_of_rows=self.r
        self.kmcount = -1
       
    def SetItem(self, r, c, txt): ##self.boxes[c].insert(r, str(txt))
        self.itemlc_dict[(self.r, c)]=txt
        self.boxes[c].insert(self.r, str(txt))
        ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
        self.getrowvalue = self.itemlc_dict[0]
        
    def InsertStringItem(self, r, txt=''):
        self._number_of_rows += 1
        self.kmcount = -1

    def ReSetData(self, data):
        self.DeleteAllItems() ### Clean All Previous Records; Ready For Fresh Entries
        tdict = {}
        i = 0
        for i, (k, v) in enumerate(data.items()):
            tdict[i]=v
            self.SetStringItem(0, 'name', v)
        self.r = i, 0, self
        self._number_of_rows = i
        self.itemlc_dict = tdict ### Reset/Force Correct Index Key for itemlc_dict
        
    def SetStringItem(self, r, c, lcdict):
        ###self.itemlc_dict[rowkey][colkey]
        ###self._number_of_rows should automatically configure indexes
        self.itemlc_dict[self._number_of_rows] = lcdict
        r = 0
        for r in range(self.staticlimit):
            try:
                self.itemlc_dict[self._number_of_rows]['sno']=sum([self.datavarlimit, self._number_of_rows])
            except Exception:
                pass
            for c in range(self.columns):
                ckey = self.colconf[c]['idname']
                try:
                    self.boxes[c].insert('end', self.itemlc_dict[self._number_of_rows][ckey])
                except (KeyError, TypeError) as err:
                    keyerr = [True, str(err)]
            self._number_of_rows += 1
        self.kmcount += 1
        self.r = r, 0, self
        
    def SetUniqueStringItem(self, r, uniquekey, lcdict):        
        self.DeleteAllItems()
        self.uniqueid_dict[lcdict[uniquekey]]=lcdict
        i = 0
        for i, (k,v) in enumerate(self.uniqueid_dict.items()):
            self.itemlc_dict[i]=v
            for c in range(self.columns):
                ckey = self.colconf[c]['idname']
                try:
                    self.boxes[c].insert('end', v[ckey])
                except (KeyError, TypeError) as err:
                    keyerr = [True, str(err)]
        self._number_of_rows = i
        self.r = i, 0, self
        
    def Lyview(self): ### ItemLB
        return [box.yview() for box in self.boxes][0]
    
    def Lselection_clear(self, idx):  ### ItemLB
        try:
            return [box.selection_clear(idx) for box in self.boxes][0]
        except Exception as err:
            pass
    def Lselection_set(self, idx, last=None): ### ItemLB
        try:
            return [box.selection_set(idx, last) for box in self.boxes][0]
        except :
            return None
    def GetSize(self): ### ItemLB
        try:
            return [box.size() for box in self.boxes][0]
        except :
            return self.height
    def Ldelete(self, idx=0, pos='end'): ### ItemLB
        return [box.delete(0, 'end') for box in self.boxes][0]

    def SetValue(self, text, pos='end'): ### ItemLB
        return [box.insert(pos, text) for box in self.boxes][0]
      
    def GetValue(self, idx): ### ItemLB
        return [box.get(idx) for box in self.boxes][0]
    
    def GetTupleValue(self, idx): ### ItemLB
        return [box.get(idx) for box in self.boxes]
    def GetColValue(self, idx, col=0): ### ItemLB
        return [b.get(idx) for i, b in enumerate(self.boxes) if col==i][0].split('||')
    def Lyview_moveto(self, mvy): ### ItemLB
        return [box.yview_moveto(mvy) for box in self.boxes][0]
    def Lcurselection(self): ### ItemLB
        return [box.curselection() for box in self.boxes][0]

    def ListData_Fill(self, data):
        for i, v in enumerate(data):
            self.itemlc_dict[i]=v
            for c, key in enumerate(self.collabel):
                self.boxes[c].insert('end', v[c])
        if self.itemlc_dict:
            ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
            self.getrowvalue = self.itemlc_dict[0]

    def ExFill(self, dictdata, full=False, searcstartswith=None):
        ### Fresh Display;
        ### full; will fill all data by increasing listbox height
        ### searcstartswith is dict {'key':'search into','text':'want to search'} 
        ### Function used whenever data display required from outside this class
        ### Only Used WHEN SINGLE BOX is available
        if full:
            lendictdata = len(dictdata)
            self.staticlimit = lendictdata
            self.boxes[0]['height']=lendictdata
        self.itemlc_dict = dictdata
        if searcstartswith:
            for k,v in dictdata.items():
                self.boxes[0].delete(k, 'end')
                if v[searcstartswith['key']].startswith(searcstartswith['text']): 
                    self.boxes[0].insert('end', v['name'])
        else:    
            for k,v in dictdata.items():
                self.boxes[0].delete(k, 'end')
                self.boxes[0].insert('end', v['name'])
        self.kmcount = 0
        self.Lselection_set(0)
            
    def Fill(self, data={}, keylist=['prodname','compname',], itemsd=True): ### ItemLB
        self.Reset_arg()
        if isinstance(data, (tuple, list)):
            self.ListData_Fill(data)
        else:
            
            for i, (k, val) in enumerate(data.items()):
                #self.itemlc_dict[i]=val
                self._number_of_rows = i
                #for c, (ktg, text) in val.items():
                for c in range(self.columns):
                    self.boxes[c].insert('end', val[keylist[c]])
            self.itemlc_dict = data
        ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
        if self.itemlc_dict:
            self.getrowvalue = self.itemlc_dict[0]
    
    def curselection(self): ### ItemLB
        '''get the currently selected row'''
        selection = self.boxes[0].curselection()
        return selection[0] if selection else None

class RMSTRV(Treeview):
    def __init__(self, master, parent, columninfo, colkw, vsbkw, **kw):
        Treeview.__init__(self, master, **kw)
        self.vsb = Scrollbar(master,orient="vertical",
                    command = self.yview)
        
        self.configure(yscrollcommand = self.vsb.set)
        self.itemlc_dict = {}
        self.col = len(columninfo)
        self["columns"] = [i for i in range(self.col)] 
        self['show'] = 'headings'
        self.columninfo = columninfo
        style = Style()
        style.configure("Treeview.Heading", **colkw)
        style.configure("Treeview", **colkw)
        self.vsbkw = vsbkw
        for k, v in columninfo.items():
            self.column(k, width=v['width'], anchor=v['anchor'])
            self.heading(k, text=v['text'], anchor=v['anchor'])
        self.Show()
       
    def Fill(self, list):
        for i, l in enumerate(list):
            self.itemlc_dict[i]=l
            self.insert('', 'end', values=l)

    def Hide(self):
        if self.vsbkw['vsbset']=='pack':
            self.pack_forget()
            self.vsb.pack_forget()
        if self.vsbkw['vsbset']=='grid':
            self.grid_forget()
            self.vsb.grid_forget()
        if self.vsbkw['vsbset']=='place':
            self.place_forget()
            self.vsb.place_forget()
            
    def Show(self):
        if self.vsbkw['vsbset']=='pack':
            self.vsb.pack(side=self.vsbkw['side'],fill=self.vsbkw['fill'])
        if self.vsbkw['vsbset']=='grid':
            self.vsb.grid(row=self.vsbkw['row'],column=self.vsbkw['col'],rowspan=self.vsbkw['rowspan'],
                columnspan=self.vsbkw['columnspan'], sticky=self.vsbkw['sticky'])
            self.grid(row=self.vsbkw['row'],column=self.vsbkw['col']-self.vsbkw['columnspan'],
                rowspan=self.vsbkw['rowspan'],columnspan=self.vsbkw['columnspan'],)
        if self.vsbkw['vsbset']=='place':
            self.vsb.place(x=self.vsbkw['x'], y=self.vsbkw['y'], width=self.vsbkw['width'])
    def DeleteItem(self, r):
        self.delete(self.get_children()[r])
    def DeleteAllItems(self):
        for item in self.get_children():
            self.delete(item)
        self.itemlc_dict = {}
    def SetFocus(self):
        try:
            self.selection_set('I001')
        except:
            pass
    def GetItemText(self, r, c=0):return self.itemlc_dict[r][c] 
    def GetItemData(self, r):return self.itemlc_dict[r]
    def GetRowItem(self, r):return self.itemlc_dict[r]
    def GetRowDict(self, r):return self.itemlc_dict[r]
    def GetCellValue(self, r, c):
        m = self.get_children()[r]
        return self.item(m)['values'][c]
    def GetItemCount(self):return len(self.itemlc_dict)
    def GetColumnCount(self):return self.col
        
def PrintFileRead(iteminfo=False, rmspath='./pgsett.ini'):
    from rmsprt.rmss_objects import mbillinfo, On_print_pdf
    from rmsmaster.billpps import PRINT_DISCRIPTION
    rmspath = os.path.join(rmspath, 'resources', 'pgsett.ini')
    printdic = {True:mbillinfo, False:On_print_pdf}
    if os.path.exists(rmspath):
        pfr = True
        prinfodict = PRINT_DISCRIPTION().READFILE(getfile=rmspath)
    else:
        pfr = False
        prinfodict = None
    """
    ###printmeth = [printdic[pfr], prinfodict]
    if prinfodict:
        if prinfodict[2]['_END0'][1] in range(380, 450): 
            #### DEFAULT pagebottm_margin >>> pagebottm_margin = 420 range(380, 450) for half A4_size_page;
            #### Full A4_size_page has pagebottm_margin = 10
            if iteminfo:
                maxline = 12 ###12 line will default with item discription below itemname
            else:
                maxline = 17 ###17 line will default
        else:
            if iteminfo:
                maxline = 24 ###24 line will default with item discription below itemname
            else:
                maxline = 35 ###17 line will default
    """
    printmeth = [printdic[pfr], prinfodict, On_print_pdf, PRINT_DISCRIPTION]
    ##[0]=page setting ini function,[1]=page setting ini values, [2]=default/old pdf print method
    return printmeth

def MAPDATE(frmdt, todt, getformat, setformat):
    try:
        fd = datetime.strptime(str(frmdt.strip()), getformat).strftime(setformat)
        td = datetime.strptime(str(todt.strip()), getformat).strftime(setformat)
    except Exception as err:
        return '', ''          
    return fd, td

def GetBankInfo(bankinfo):
    bankinfodict = {'name':'Direct', 'ifsc':'', 'ac':''}
    try:
        bki = bankinfo.split(',')
        bankinfo = {'name':bki[0][:30], 'ifsc':bki[1], 'ac':bki[2]}
    except:
        bankinfo = {'name':'', 'ifsc':bankinfo, 'ac':''}
    return bankinfo

def READ_RESOURCES_FILES():
    from cofg import dbdict, MyCursor
    
    filename = './resources/mysoft.txt'
    file = open(filename,"rb")
    file.readline(1)
    mysofval,sdc,default_trade_rate,df_discount, df_trade_marg, extend_marg, prt_name,prt_port,prt_share = '','','','', '', '', '','',''
    
    sdc = dbdict['sdc']
    softintlist = ['1', '2']
    if not sdc.isdigit():
        sdc = '1'
    else:
        if sdc not in softintlist:
            sdc = '1'
    fontdct = {'0':'Courier', '1':'Helvetica', '2':'Times-Roman', '3':'Courier','4':'Courier-Bold','5':'Courier-BoldOblique','6':'Courier-Oblique',
               '7':'Helvetica','8':'Helvetica-Bold','9':'Helvetica-BoldOblique','10':'Helvetica-Oblique',
               '11':'Helvetica-Bold','12':'Helvetica-BoldOblique','13':'Helvetica-Oblique',
               '01':'Courier','02':'Courier-Bold','03':'Courier-BoldOblique','04':'Courier-Oblique',
               '21':'Times-Roman','22':'Times-Bold','23':'Times-BoldOblique','24':'Times-Oblique'}
    caldecimalval = '2'
    
    (fontdct,fontid,default_trade_rate,df_discount,df_trade_marg,extend_marg,
         taxname,taxname2,taxdict,exp_alert,bankinfo,stkmess, estifilter, txoe, onmoeb,
         hostn, dbn, prounit, pcolordict, caldecimalval, iteminfo) = dbdict['readfn']
    iteminfodic = {'YES':True, 'NO':False}
   
    iteminfo = iteminfodic[iteminfo]
    bankinfo = GetBankInfo(bankinfo)
    ownerlst = []
    bills_dic = {}
    pdfpglines = 17
    qrcodeinfo = 1
    lockupdates = 0
    netpur_onsale_dp = ''
    ##pdir = os.path.dirname(sys.argv[0])
    ##MyCursor(pdir, 'root', 'pass', 'localhost', 'mrms', 'mrms')
    ##cnn, cursor = MyCursor(pdir, dbdict['user'], dbdict['pass'],
    ##            dbdict['host'], dbdict['db'],dbdict['db'], ) 
    prt_name,prt_port,prt_share = dbdict['printerinfo']
    ###eadd, password, er = dbdict['uemailinfo']
    dbinfo = {'user':dbdict['user'], 'pass':dbdict['pass'], 'host':dbdict['host'],
              'db':dbdict['db'], 'sdc':sdc, 'MyCursor':MyCursor}
    
    printmeth = PrintFileRead(iteminfo)
     
    return (mysofval,sdc,default_trade_rate,fontdct,fontid,df_discount, df_trade_marg,
           extend_marg, prt_name,prt_port,prt_share, taxname, taxname2, dbinfo, hostn, prounit,
           exp_alert, bankinfo, ownerlst, printmeth, taxdict, bills_dic, dbdict['oemail'],dbdict['wcolor'],sdc,
           stkmess, estifilter, txoe, onmoeb, caldecimalval, pdfpglines, iteminfo, qrcodeinfo, lockupdates, netpur_onsale_dp)
    
######################################################################################################

class RMS_BTNGIF(Button):
    def __init__(self, parent, master=None, gif='round.gif', dirname='img',
                 framecount=8, size=(50,50), **kw):
        rmspath = parent.rscr['rmspath']
        self.parent = parent
        self.master = master
        if gif:
            self.gif = os.path.join(rmspath, dirname, gif)
        else:
            ### When Image Path is Not Available
            self.gif = None
        self.gifid = None
        self.framecount = framecount
        self.width, self.height = size
        self.frameCnt = self.framecount
        self.frames=[PhotoImage(file=self.gif,format='gif -index %i'%(i))
              for i in range(self.frameCnt)]
        Button.__init__(self, master, **kw)

    def Load(self, ind):
        
        try:
            frame = self.frames[ind]
            ind += 1
            if ind == self.frameCnt:
                ind = 0
            self.configure(image=frame)
            self.gifid = self.after(100, self.Load, ind)
        except :
            print ('error')
            return False
        
    def ReSize(self, pos):
        x, y = pos
        try:
            self.master.place(x=x, y=y)
            self.master.configure(relief='raised')
            self.master.configure(borderwidth='2')
            #self.configure(width=50)
            #self.configure(height=50)
            self.configure(width=self.width)
            self.configure(height=self.height)
            ###self.parent.lift(aboveThis=None)
        except:
            self.place(x=x, y=y)
            
    def GridHide(self):
        self.grid_forget()
        
    def GridShow(self, geo=None):
        if not geo: ### geo = geometry not given
            return
        self.grid(row=geo['r'], column=geo['c'],columnspan=geo['cp'],rowspan=geo['rp'],)
        self.frameCnt = self.framecount
        self.frames=[PhotoImage(file=self.gif,format='gif -index %i'%(i))
              for i in range(self.frameCnt)]
        self.Load(0, )

    def PlaceShow(self, pos=None):
        if not pos: ### pos = geometry not given
            return
        self.place(x=pos[0], y=pos[1],)
        self.frameCnt = self.framecount
        self.frames=[PhotoImage(file=self.gif,format='gif -index %i'%(i))
              for i in range(self.frameCnt)]
        self.Load(0, )
        
    def Show(self, pos=(500, 500)):
        if not pos: ### pos = geometry not given
            self.place(x=450, y=450)
        else:    
            self.ReSize(pos)
        self.frameCnt = self.framecount
        self.frames=[PhotoImage(file=self.gif,format='gif -index %i'%(i))
              for i in range(self.frameCnt)]
        self.Load(0, )
        
    def Hide(self, msg='Done !'):
        if self.gifid:
            self.after_cancel(self.gifid)
            self.gifid = None
        try:
            self.master.place(x=-100, y=-100)
        except AttributeError:
            pass
        ###self.master.place_forget()
        self.configure(width=0)
        self.configure(height=0)
        ###self.frameCnt = 0
        ###self.frames = []
        self.configure(image='')
        self.configure(text='')
        return True
    
    def Stop(self, msg='Done !'):
        self.Hide(msg=msg)
        

class RMS_GIF(Label):
    def __init__(self, parent, master=None, gif='round.gif', dirname='img',
                 framecount=8, size=(50,50), **kw):
        rmspath = parent.rscr['rmspath']
        self.parent = parent
        self.master = master
        if gif:
            self.gif = os.path.join(rmspath, dirname, gif)
        else:
            ### When Image Path is Not Available
            self.gif = None
        self.gifid = None
        self.framecount = framecount
        self.width, self.height = size
        self.frameCnt = self.framecount
        self.frames=[PhotoImage(file=self.gif,format='gif -index %i'%(i))
              for i in range(self.frameCnt)]
        Label.__init__(self, master, **kw)

    def Load(self, ind):
        
        try:
            frame = self.frames[ind]
            ind += 1
            if ind == self.frameCnt:
                ind = 0
            self.configure(image=frame)
            self.gifid = self.after(100, self.Load, ind)
        except :
            print ('error')
            return False
        
    def ReSize(self, pos):
        x, y = pos
        try:
            self.master.place(x=x, y=y)
            self.master.configure(relief='raised')
            self.master.configure(borderwidth='2')
            #self.configure(width=50)
            #self.configure(height=50)
            self.configure(width=self.width)
            self.configure(height=self.height)
            ###self.parent.lift(aboveThis=None)
        except:
            self.place(x=x, y=y)
            
    def GridHide(self):
        self.grid_forget()
        
    def GridShow(self, geo=None):
        if not geo: ### geo = geometry not given
            return
        self.grid(row=geo['r'], column=geo['c'],columnspan=geo['cp'],rowspan=geo['rp'],)
        self.frameCnt = self.framecount
        self.frames=[PhotoImage(file=self.gif,format='gif -index %i'%(i))
              for i in range(self.frameCnt)]
        self.Load(0, )

    def PlaceShow(self, pos=None):
        if not pos: ### pos = geometry not given
            return
        self.place(x=pos[0], y=pos[1],)
        self.frameCnt = self.framecount
        self.frames=[PhotoImage(file=self.gif,format='gif -index %i'%(i))
              for i in range(self.frameCnt)]
        self.Load(0, )
        
    def Show(self, pos=(500, 500)):
        if not pos: ### pos = geometry not given
            self.place(x=450, y=450)
        else:    
            self.ReSize(pos)
        self.frameCnt = self.framecount
        self.frames=[PhotoImage(file=self.gif,format='gif -index %i'%(i))
              for i in range(self.frameCnt)]
        self.Load(0, )
        
    def Hide(self, msg='Done !'):
        if self.gifid:
            self.after_cancel(self.gifid)
            self.gifid = None
        try:
            self.master.place(x=-100, y=-100)
        except AttributeError:
            pass
        ###self.master.place_forget()
        self.configure(width=0)
        self.configure(height=0)
        ###self.frameCnt = 0
        ###self.frames = []
        self.configure(image='')
        self.configure(text='')
        return True
    
    def Stop(self, msg='Done !'):
        self.Hide(msg=msg)
        
class PrintMB(Toplevel):
    def __init__(self, parent, title="RMS PRINT (Print Copies)",
                 titleclr='black', text='0, 1, 2, 3, 4 ', textclr='blue', bg='lightyellow',
                 fontsize=15, font2=15, size=(300, 150), pos=None):
        Toplevel.__init__(self, parent, )

        if pos:
            x, y = pos
        else:
            sw = parent.rscr['sw']
            sh = parent.rscr['sh']
            x = (sw/2) - (w/2)
            y = (sh/2) - (h/2)
        
        self.geometry('+%s+%s'%(x, y))
        
        self.parent = parent
        wrow = 0
        self['bg']=bg
        
        lbfgbg = {'font': ['Courier New', fontsize, 'bold'], 'bg':bg, 'fg':textclr} ###self.rscr['font']['listbox']
        btfgbg = {'font': ['Calibri', fontsize, 'bold'], 'bg':'white', 'fg':'black', 'relief':'raised'} ###self.rscr['font']['listbox']
        self.lhead = RMS_LABEL(self, text=title, **lbfgbg)#, size=(width, texthight))
        self.lhead.grid(row=wrow, column=0, columnspan=4, rowspan=3,)
        wrow += 3
        self.label = RMS_LABEL(self, text=text, **lbfgbg)#, size=(width, texthight))
        self.label.grid(row=wrow, column=0, columnspan=4, rowspan=2,)
        wrow += 2
        self.okbutton = RMS_BUTTON(self, text="OK", width=10, **btfgbg)
        self.okbutton.grid(row=wrow, column=1, columnspan=1, rowspan=1, padx=85)
        
        self.okbutton.bind("<Button-1>",  self.onOK)
        self.okbutton.bind("<Key>", self.onOKKD)
        
        self.result = None
        self.cp = None
        self.okbutton.focus()
        self.overrideredirect(1)
        self.transient()
        self.grab_set()
        self.wait_window()
        
    def onOK(self, event):
        self.result = 1
        self.destroy()
        
    def onOKKD(self, event):
        key = event.keysym
        self.cp = 1
        if key == '0':
            self.cp = None
        elif key == '1':
            self.cp = 1
        elif key == '2':
            self.cp = 2
        elif key == '3':
            self.cp = 3
        elif key == '4':
            self.cp = 4
        elif key in ['End', 'Escape', 'BackSpace', 'Delete', 'Home']:
            self.cp = None
        elif key == 'Return':
            self.cp = 1
        self.result = self.cp
        self.destroy()
        
class RMSMBX(Toplevel):
    def __init__(self, parent, title='',  text="RMS INFO MESSAGE", info=True,default='yes',
                 size=(300, 130), pos=None, fontsize=12, textclr='blue', bg='lightyellow'):
        Toplevel.__init__(self, parent, )
        try:
            fontsize = parent.rscr['sysfontnum']
        except:
            fontsize = 12
        w, h = size
        if pos:
            x, y = pos
        else:
            sw = parent.rscr['sw']
            sh = parent.rscr['sh']
            x = (sw/2) - (w/2)
            y = (sh/2) - (h/2)
        
        ###self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.geometry('+%d+%d'%(x, y))
        self.parent = parent
        
        self['bg']=bg
        lbfgbg = {'font': ['Courier New', fontsize, 'bold'], 'bg':bg, 'fg':textclr} ###self.rscr['font']['listbox']
        lbfgbg2 = {'font': ['Courier', 1, 'normal'], 'bg':bg, 'fg':textclr}
        btfgbg = {'font': ['Calibri', fontsize, 'bold'], 'bg':'white', 'fg':'black', 'relief':'raised'} ###self.rscr['font']['listbox']
        self.label = RMS_LABEL(self, text=text, **lbfgbg)#, size=(width, texthight))
        ###self.label.grid(row=1, column=0, columnspan=6, rowspan=3,)
        self.label.pack(fill='both',expand=True)
        self.info = info
        if info:
            self.okbutton = RMS_BUTTON(self, text="OK", width=10, **btfgbg)
            ###self.okbutton.grid(row=4, column=1, padx=10, columnspan=1, rowspan=1,)
            self.okbutton.pack(fill='both',expand=True)
            labelpadd = RMS_LABEL(self, **lbfgbg2)
            labelpadd.pack(fill='x',side='bottom')
            self.okbutton.focus()
        else:
            self.okbutton = RMS_BUTTON(self, text="YES", width=10, **btfgbg)
            ###self.okbutton.grid(row=4, column=1, padx=10, columnspan=1, rowspan=1,)
            self.cancelbut = RMS_BUTTON(self, text="NO", width=10, **btfgbg)
            ###self.cancelbut.grid(row=4, column=2, columnspan=1, rowspan=1,)
            labelpadd = RMS_LABEL(self, **lbfgbg2)
            labelpadd.pack(fill='x',side='bottom')
            self.okbutton.pack(fill='x',side='left')
            self.cancelbut.pack(fill='x',side='bottom')
            self.cancelbut.bind("<Button-1>", self.onCancel)
            self.cancelbut.bind("<Key>", self.onCKD)
            if default.lower() == 'yes':
                self.okbutton.focus()
            else:
                self.cancelbut.focus()
        self.okbutton.bind("<Button-1>", self.onOK)
        self.okbutton.bind("<Key>", self.onOKKD)
        self.result = None
        
        self.overrideredirect(1)
        self.transient()
        self.grab_set()
        self.wait_window()

    def onOK(self, event):
        self.result = True
        self.destroy()
        
    def onOKKD(self, event):
        key = event.keysym
        result = None
        
        if key in ['Right', 'Left', 'Up', 'Down',]:
            if not self.info:
                self.cancelbut.focus()
        elif key in ['End', 'Escape', 'BackSpace',]:
            result = None
            self.onCancel(event)
            return None
        elif key in ['Return']:
            self.onOK(event)
            return True
        self.result = result
        
    def onCKD(self, event):
        key = event.keysym
        result = None
        if key in ['Return', 'End', 'Escape', 'BackSpace',]:
            result = None
            self.onCancel(event)
            return
        elif key in ['Right', 'Left', 'Up', 'Down',]:
            if not self.info:
                self.okbutton.focus()
        self.result = result
        
    def onCancel(self, event):
        self.result = None
        self.destroy()
        
###############################################################################################
def RECDIC_INIT(self):
    self.rowcount = set()
    self.keyid = 0
    self.wgkeyid = 0
    ogd = OrderedDict() 
    return {'pan':{},'ac':{},'grid':ogd,'edit':False,'resume':{}}


class RMSGRID(Frame):
    def __init__(self, master, parent, wrow,rows,colrange,colconf, header, griditems=False,
                 setbg=True, srn_width=5, **kw):
        Frame.__init__(self, master)
        #self.master = master  ### Configure
        self.parent = parent
        self.rows = rows
        self.colrange = colrange
        self.wrow = wrow
        self.cols = len(colconf)
        self.columns = self.cols
        self.header = header ### bool
        self.rscr = parent.rscr
        self.kw = kw
        self.srn_width = srn_width
        ### self.xFocus = False use when focus required to move to another widget OTHER THAN grid
        ### self.xFocus = True will not take focus for grid widget and allow to move focus to parent widget
        self.xFocus = False 
        self.collabel = {}
        self.stbg, self.mbg = 'white', 'yellow'
        self.rlst = [] ## return selected list to parent/master
        self.ColorTags = False
        self.loadnext = True
        self.itemlc_dict = {} ### containing name as key(r,c) and values 
        self.staticlimit = rows ###10
        self.datavarlimit = 0
        self._number_of_rows=0 
        self.kmcount = -1
        self.datalen = None
        self.qfunc = None
        self.text = ''
        self.sumcr_dr = [0,0]
        self.colconf = colconf
        self.MoveCursorDown = True
        self.griditems = griditems
        self.setbg = setbg
        self.fpf = ''.join(["%0.", self.rscr['decimalval'], 'f'])
        self.sdc = self.rscr['sdc']
        self.mysoftval = self.rscr['mysoftval']
        self.compbool = self.rscr['compbool']
       
        self.spnum = parent.spnum
        self.keyid = 0
        #############################
        self.AllowTxtStart()
        
        if kw:
            if kw.get('sbar'):
                cnvkw = kw['sbar']['cnv']
                
                self.canvas = Canvas(master, background="#ffffff")
                self.frame = Frame(self.canvas)
                self.canvas.grid(cnvkw)
                ##self.frame.grid(cnvkw)
                
                hsbkw = kw['sbar'].get('hsb')
                
                if hsbkw:
                    self.hsb = Scrollbar(master, orient="horizontal", command=self.canvas.xview)
                    self.canvas.configure(xscrollcommand=self.hsb.set)
                    self.hsb.grid(hsbkw)
                vsbkw = kw['sbar'].get('vsb')
                if vsbkw:
                    
                    self.vsb = Scrollbar(master, orient="vertical", command=self.canvas.yview)
                    self.canvas.configure(yscrollcommand=self.vsb.set)
                    self.vsb.grid(vsbkw)
                
                self._window = self.canvas.create_window((0,0), window=self.frame, anchor="nw", )
                self.canvas.rowconfigure(0, weight=1)
                self.canvas.columnconfigure(0, weight=1)                
                self.canvas.bind("<Configure>", self.onFrameConfigure)
            else:
                self.frame = self.AddFrame(master)
        else:
            self.frame = self.AddFrame(master)
        self.SetupLB(colconf)

    def AddFrame(self, master):
        self.frame = Frame(master, relief='raised')
        self.frame.grid(row=self.wrow, column=self.colrange,
            columnspan=sum([self.columns,1]), rowspan=self.rows)  ####################
        return self.frame
    
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        ##self.canvas.configure(scrollregion=(0,0,1200,200))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    
    def GetSumCr_Dr(self):
        return self.sumcr_dr
    
    def ResetBox(self):
        self.headlab.grid_forget()
        self.headlab.destroy()
        for box in self.boxes:
            box.grid_forget()
            box.destroy()
      
    def SetupLB(self, colconf, wrow=None):
        self.boxes = []
        self.wgdict = {}
        self._widf = {}
        self.snwg = {}
        self.colldict = {}
        self.r = [0,0,self] ###[row, col, self]
        self.c = 0
        self.index = 0
        self.lbkidx = 0
        self.headerdict, self.boxdict = {}, {}
        if wrow :
            self.wrow = wrow
        self.wdgcontainer = []
        rowcontainer = []
        ##self.container = Frame(self.master, relief='raised')
        ###self.container.place(x=10, y=300)  ####################
        ##self.container.grid(row=self.rows, column=self.colrange, columnspan=sum([self.columns,1]), rowspan=self.rows)  ####################
        srn_width = self.srn_width  #### RMS_LABEL width
        self.wrow += 1
        self.colids = {}
        self.colnumids = {}
        if self.header:
            for r in range(1):
                ###mcl = sum([self.colrange,0])
                mcl = self.colrange
                sno = RMS_LABEL(self.frame, text='Sr.N.', width=srn_width, bg=colconf[0]['bg'], fg=colconf[0]['fg'], font=colconf[0]['font'])
                sno.grid(row=self.wrow, column=mcl, columnspan=1,sticky='ens')
                self.colldict['sno']=sno
                rowcontainer.append(sno)
                for k, v in colconf.items():
                    kw = {'width':v['width'],'bd':v['bd'],'bg':v['bg'],
                          'fg':v['fg'],'font':v['font'],}
                    cl = sum([self.colrange,k])
                    mcl += 1
                    headlab = RMS_LABEL(self.frame, text=v['text'], **kw)
                    headlab.grid(row=self.wrow, column=mcl,  sticky='wens')
                    self.headerdict[k]={'label':headlab, 'kw':kw}
                    self.colldict[k]=headlab
                    rowcontainer.append(headlab)
        self.wrow += 1
        self.wdgcontainer.append(rowcontainer)
        ### -N or -I will Accept Negative Integers
        vcmddict = {'AN':self.ValidateAN,'F':self.ValidateF,'I':self.ValidateI,'ITEM':self.ValidateITEM,
            'N':self.ValidateI,'NN':self.ValidateNI,'NI':self.ValidateNI, 'BAT':self.ValidateBAT,
            'QTY':self.ValidateQTY,'BONUS':self.ValidateBONUS, 'EXP':self.ValidateEXP, 'MRP':self.ValidateMRP,
            'RATE':self.ValidateRATE,'DIS':self.ValidateDIS,'NET':self.ValidateNET, }
        
        for r in range(self.rows):
            mcl = sum([self.colrange,0])
            rowcontainer = []
            sno = RMS_LABEL(self.frame, text=r, width=srn_width, bg=colconf[0]['bg'], fg=colconf[0]['fg'], font=colconf[0]['font'],)
            sno.grid(row=self.wrow, column=mcl, sticky='ens')
            self.snwg[r]=sno
            rowcontainer.append(sno)
            for col, v in colconf.items():
                kw = {'width':v['width'],'bd':v['bd'],'bg':v['bg'],'fg':v['fg'],
                      'font':v['font'], 'relief':v['relief'],}
                self.txvar = StringVar()
                vcmd = (self.master.register(vcmddict[v['vcmd']]), "%P")
                box = RMS_ENTRY(self.frame, textvariable=self.txvar,
                    validatecommand=vcmd, validate='key', **kw)
                ##box.bind('<me>', partial(self.parent.OnGridTxt, r, self.txvar,),)             
                ##box.bind("", partial(self.parent.OnGridTxt, param=self.txvar))
                self._widf[box]=(r, col)
                mcl += 1
                box.grid(row=self.wrow, column=mcl, sticky='wens')
                self.wgdict[(r, col)] = [box, sno, self.txvar]
                ####box.bind('<<ListboxSelect>>', self.OnSelectedL, )
                box.bind('<Double-1>', self.OnDoubleClick)
                #box.bind('<Return>', self.OnSelectedR)
                box.bind('<Key>', self.OnKey)
                box.bind("<Enter>", self.OnScroll)
                box.bind("<Leave>", self.OffScroll)
                self.boxes.append(box)
                self.boxdict[col]={'box':box, 'kw':kw}
                self.collabel[col]=v['idname']
                self.colids[v['idname']]=col
                self.colnumids[col]=v['idname']
                rowcontainer.append(box)
            self.wrow += 1
            self.wdgcontainer.append(rowcontainer)
            
            self.frame.rowconfigure(r, weight=1)
            self.frame.columnconfigure(r, weight=1)
            
        self.colconf = colconf

    def ValidateITEM(self, text):
        if self.gridtxtstart:
            if text.isupper():
                ### text is converting from small to upper case;
                ### so, to avoid two time search for same charecter(lower and upper); taking only upper case
                self.parent.OnGridTxt(self.r, text)
                return True
            else:
                if not text:
                    self.parent.ItemLcHide()
        return True

    def ValidateBAT(self, bat):
        if self.gridbatstart:
            ### text is converting from small to upper case;
            ### so, to avoid two time search for same charecter(lower and upper); taking only upper case
            self.parent.OnGridBat(self.r, bat) 
            return True
        return True

    def ValidateBONUS(self, bonus):
        bcount = bonus.count('+')
        if bcount > 1:
            return False
        if not self.gridbonusstart:
            return True
        
        self.bonuschkl = ['0','1','2','3','4','5','6','7','8','9','+']
        if bonus.strip() == "":
            ### Resetting Calculation
            self.parent.OnGridBonus(self.r, '0')
            return True
        
        mess = True
        for x in bonus:
            if x in self.bonuschkl:
                mess = True
            else:
                mess = False
                return False
        if not mess :
            return False
        try:
            self.parent.OnGridBonus(self.r, bonus)
            return True
        except IndexError:
            ### Resetting Calculation only '10+' <<< is given
            self.parent.OnGridBonus(self.r, '0')
            return True
        if bonus not in self.bonuschkl:
            self.bell()
            self.parent.OnGridBonus(self.r, '0')
            return True
        
        self.parent.OnGridBonus(self.r, bonus)
        return True
    
    def ValidateQTY(self, qty): ## ### will Accept Negative Integers Also
        
        if not self.gridqtystart:
            return True
        if qty.strip() == '':
            ### required for ClearGrid, empty string
            self.parent.OnGridQty(self.r, 0)
            return True
        #if qty.strip() == '-':
        if qty.startswith('-'):
            ### Accepting Negative Intergers also
            #if qty.isdigit():
            if len(qty)==1:
                return True
            try:
                iqty = int(qty)
                self.parent.OnGridQty(self.r, iqty)
                return True
            except (ValueError, KeyError):
                return False
            return True
        try:
            if qty.isdigit():
                iqty = int(float(qty))
                self.parent.OnGridQty(self.r, iqty)
                return True
            return False
        except (ValueError, KeyError):
            return False
        return True

    def ValidateRATE(self, rate):
        if not self.gridratestart:
            return True
        if rate.strip() == '':
            self.OnGridRate(self.r, 0)
            return True
        try:
            ratef = float(rate)
            self.OnGridRate(self.r, ratef)
            return True
        except ValueError:
            self.OnGridRate(self.r, 0)
            return False
        return True

    def ValidateDIS(self, dis):
        if not self.griddisstart:
            return True
        if dis.strip() == '':
            self.OnGridDis(self.r, 0)
            return True
        try:
            disc = float(dis)
            self.OnGridDis(self.r, disc)
        except ValueError:
            self.OnGridDis(self.r, 0)
            return False
        return True
    
    def ValidateEXP(self, dt):
        self.expedit = True
        dt = dt.title()
        if self.gridexpstart is False:
            return True
        if str(dt).find('/')==1:
            val = ''.join(['0', dt])
            self.OnGridExp(self.r, val)
            return True
        try:
            dt2 = dt.split('/')[1]
            if dt2.isdigit():
                if len(str(dt2))==2:
                    try:
                        dtfromat = '%m/%y'
                        val = time.strftime(dtfromat, time.strptime(str(dt), dtfromat))
                    except:
                        val = str(dt)[:6]
                    self.OnGridExp(self.r, val)
                else:
                    val = str(dt)[:5]
                    self.OnGridExp(self.r, val)
            else:
                val = str(dt)[:3]
                self.OnGridExp(self.r, val)
            return True
        except IndexError:
            try:
                sdt = dt
                dt = int(dt)
                if dt in range(1,13):
                    if len(str(dt))==2:
                        self.OnGridExp(self.r, '%s/'%str(dt))
                        return True
                    else:
                        if str(sdt).startswith('0'):
                            self.OnGridExp(self.r, '%s/'%str(sdt))
                            return True
                        self.OnGridExp(self.r, sdt)
                        return True
                else:
                    if dt == 0:
                        self.OnGridExp(self.r, dt)
                        return True
                    self.OnGridExp(self.r, "")
                    return True
            except ValueError:
                self.OnGridExp(self.r, "")
        return True

    def ValidateNET(self, net):
        if not self.gridnetstart:
            return True
        
        if net.strip() == '':
            self.OnGridNet(self.r, 0)
            return True
        try:
            ratenet = float(net)
            self.OnGridNet(self.r, ratenet)
            return True
        except ValueError:
            self.OnGridNet(self.r, 0)
            return False
        return True

    def ValidateMRP(self, text):
        if self.gridmrpstart:
            if P.strip() == '':
                self.OnGridMrp(self.r, 0)
                return True
            try:
                f = float(P)
                self.OnGridMrp(self.r, f)
            except ValueError:
                self.master.bell()
                self.OnGridMrp(self.r, 0)
                return False
            return True
        else:
            return True
        
    
    def ValidateAN(self, P):
        return True
    
    def ValidateF(self, P):
        if P.strip() == '':
            return True
        try:
            f = float(P)
        except ValueError:
            self.master.bell()
            return False
        return True
    
    def ValidateI(self, P):
        if P.strip() == '':
            ### required for ClearGrid, empty string
            return True
        try:
            f = int(float(P))
        except ValueError:
            self.master.bell()
            return False
        return True
    
    def ValidateNI(self, P): ### will Accept Negative Integers Also
        if P.strip() == '':
            ### required for ClearGrid, empty string
            return True
        if P.strip() == '-':
            ### Accepting Negative Intergers also
            return True
        try:
            f = int(float(P))
        except ValueError:
            self.master.bell()
            return False
        return True

    def RecdicKeyVal_Empty(self):
        ### key => 'staticqty' will use in Edited/Update Mode #
        ### spitemid => is sales_itemID/purchase_itemID, which will available during update items
        return {'idx':0,'sno':0,'itemid':None,'proid':'','compid':0,'spitemid':None,'supid':0,
          'rate':0,'rate1':0,'rate2':0,'salerate':0,'salerate_a':0.0,'prate':0,'netrate':0,'suptaxrate':'','pnet':0,'retailunit':1,
          'pack':'1*1','taxableamt':0,'ttaxamt':0,'netamt':0,'disamt':0,'totnetamt':0,'pnetamt':0,'amt':0,
          'qty':0,'batqty':0,'batstock':0,'batstk':0,'dbstock':0,'totqty':0,'totstock':0,
          'staticqty':0,'updatedqty':'','totstk':0,'stkvariable':0,'statictotstk':0,'stockid':0,'stkdic':{'':{'batstock':'',
                                                                    'bat':'','stockid':None,'proid':'',}},
          'tax':0,'tax1':0,'tax2':0,'tax1amt':0,'tax2amt':0,'satamt':0,'taxamt':0,
          'prodname':'','compname':'','bat':'','batinfo':'','pr_lo':'',
          'bonus':'0','mrp':0,'dis':0,'hsnc':'','pgroup':'','prack':'',
          'addstk':None,'dgreturn':None,'edited':None,
          'exp':'','expdate':'','expdbf':'2000-01-01',}
    
    def AllowTxtStart(self):
        self.gridtxtstart = True
        self.gridbatstart = True
        self.gridqtystart = True
        self.gridbonusstart = True
        self.gridratestart = True
        self.griddisstart = True
        self.gridnetstart = True
        self.gridmrpstart = True
        self.gridexpstart = True
        
    def MuteTxtStart(self):
        self.gridtxtstart = False
        self.gridbatstart = False
        self.gridqtystart = False
        self.gridbonusstart = False
        self.gridratestart = False
        self.griddisstart = False
        self.gridmrpstart = False
        self.gridnetstart = False
        self.gridexpstart = False
        
    def OnGridDis(self, rd, dis): ### Calling from child rmsgrid class from rmsvalidators.py
        row, col, wdgidf = rd
        
        if self.griddisstart:
            try:
                self.gridratestart = False
                self.gridnetstart = False
                keyid = int(self.wgdict[(row, col)][1].GetValue()) ### Get sno of grid
                self.keyid = keyid
                self.itemlc_dict[keyid]['dis']=dis
                self.parent.recdic['grid'][keyid]['dis']=dis
                self.keyid = keyid
                recdicfill = self.parent.recdic['grid'].get(keyid)
                self.Oncalculation(keyid, row, col, recdicfill=recdicfill)
                self.wgdict[(row, self.colids['netrate'])][0].ChangeValue(recdicfill['netrate'])
                
            except Exception as err:
                StatusDP(self.parent.status, 'Wrong Entry in Discount Column of Row No:%s'%str(err), 'red' )
            ###self.gridratestart = True
            ###self.gridnetstart = True

    def OnGridRate(self, rd, rate): ### Calling from child rmsgrid class from rmsvalidators.py
        row, col, wdgidf = rd
        if self.gridratestart:
            
            self.gridnetstart = False
            keyid = int(self.wgdict[(row, col)][1].GetValue()) ### Get sno of grid
            self.itemlc_dict[keyid]['rate']=rate
            getqty = self.wgdict[(row, self.colids['qty'])][0].GetValue()
            if getqty:
                self.itemlc_dict[keyid]['qty']=int(getqty)
            else:
                self.itemlc_dict[keyid]['qty']=0
            self.keyid = keyid
            self.parent.recdic['grid'][keyid]['rate']
            recdicfill = self.parent.recdic['grid'][keyid]
            
            try:
                self.Oncalculation(keyid, row, col, recdicfill=recdicfill)
                self.wgdict[(row, self.colids['netrate'])][0].ChangeValue(recdicfill['netrate'])
            except KeyError as err:
                pass
            self.gridnetstart = True
           
    def OnGridNet(self, rd, net): ### Calling from child rmsgrid class from rmsvalidators.py
        row, col, wdgidf = rd
        if self.gridnetstart:
            try:
                self.gridratestart = False
                keyid = int(self.wgdict[(row, col)][1].GetValue()) ### Get sno of grid
                self.keyid = keyid
                self.itemlc_dict[keyid]['netrate']=net
                self.parent.recdic['grid'][keyid]['netrate']=net
                self.keyid = keyid
                recdicfill = self.parent.recdic['grid'].get(keyid)
                self.Oncalculation(keyid, row, col, netedit=net, recdicfill=recdicfill)
                #self.gridratestart = True
            except Exception as err:
                StatusDP(self.parent.status, 'Wrong Entry in Net Rate Column of Row No:%s'%str(err), 'red' )

    def OnGridMrp(self, row, col, keyid, mrp, recdicfill): ### Calling from child rmsgrid class from rmsvalidators.py
        if self.sdc == '2': ### For Retails MedicalStores Only
            if self.spnum == 1: ### Edit For Purchase Only
                retailrate, retailqty, units = GET_RETAIL_RATE_UNIT(recdicfill['pack'], getrate=mrp, getqty=recdicfill['totqty'],
                                     spliton='*', fpf=self.fpf)
                self.parent.recdic['grid'][keyid]['salerate']=retailrate
                self.parent.recdic['grid'][keyid]['rate1']=retailrate
                self.wgdict[(row, self.colids['rate1'])][0].SetValue(retailrate)
        
    def OnGridExp(self, rd, exp): ### Calling from child rmsgrid class from rmsvalidators.py
        row, col, wdgidf = rd
        if self.gridexpstart:
            try:
                expf = datetime.strptime(str(exp), "%m/%y").strftime("%b/%y")
                expdbf = datetime.strptime(str(exp), "%m/%y").strftime("%Y-%m-%d")
            except Exception as err:
                expf = ""
                expdbf = '2000-01-01'
                try: ### To display expdate on scroll/up/down; expdate which is already formated
                    expf = datetime.strptime(str(exp), "%b/%y").strftime("%b/%y")
                    expdbf = datetime.strptime(str(exp), "%b/%y").strftime("%Y-%m-%d")
                except Exception as err:
                    expf = ""
                    expdbf = '2000-01-01'
            keyid = int(self.wgdict[(row, col)][1].GetValue()) ### Get sno of grid
            self.keyid = keyid
            self.itemlc_dict[keyid]['exp']=expf
            self.parent.recdic['grid'][keyid]['exp']=expf
            self.itemlc_dict[keyid]['expdate']=expf
            self.parent.recdic['grid'][keyid]['expdate']=expf
            self.itemlc_dict[keyid]['expdbf']=expdbf
            self.parent.recdic['grid'][keyid]['expdbf']=expdbf

    def BatchQtyStk(self, recdicfill, totqty, batstock, statictotstk):
        ### *** statictotstk is total of given available item stock
        ### *** statictotstk and batstock remains static never change throughout any edited or repeat entrie
        ### *** while dbstock is represent updated/edited total stock
        ### *** and  stkvariable represent updated/edited batch stock
        
        chkbat = recdicfill['bat']
        
        stkdic = {}
        #stkdic = self.parent.stkdic
        if recdicfill['spitemid']:
            ### In Edit/Update Mode stkdic update
            stkdic = OrderedDict()
            stkdic[chkbat]={'batstock':recdicfill['batstock'], 'bat':chkbat, 'expdbf':recdicfill['expdbf'],
                'fill':False,'qty':recdicfill['batstock'],'stockid':recdicfill['stockid'], 'proid':recdicfill['proid'],}
            #self.parent.stkdic = stkdic
            recdicfill['stkdic'] = stkdic
            ## flag edited 1 means NO changes has been made in Edit/Update Mode
            ## flag edited 2 means YES changes has been made in Edit/Update Mode
            if recdicfill['edited'] == 1:
                ### No need to send in Check_Loop_Insert; so return back 
                return
        
        ### check and fill stk for fresh entry
        self.Check_Loop_Insert(recdicfill, stkdic, totqty, batstock, statictotstk, chkbat)

    def Check_Loop_Insert(self, recdicfill, stkdic, totqty, batstock, statictotstk, chkbat):
        if totqty > statictotstk:
            ### 'cannot add stock ; execess stock given than available stock'
            raise Exception('execess stock given than available stock [Error Code 2529]') 
        if totqty <= batstock:
            ### 'NO NEED to send in loop; Given qty is available in given batch stock '
            recdicfill['stkdic'][chkbat]={'stockid':stkdic[chkbat]['stockid'],
                        'bat':stkdic[chkbat]['bat'],'qty':totqty,'fill':True,}
        else:
            ##recdicfill['stkdic'][chkbat]={'stockid':stkdic[chkbat]['stockid'], 'bat':stkdic[chkbat]['bat'], 'qtybonus':stkdic[chkbat]['batstock']}
            #for i, (k, v) in enumerate(stkdic.items()):
            updtqty = 0
            for i, (k, v) in enumerate(recdicfill['stkdic'].items()):
                updtqty += v['batstock']
                if updtqty >= totqty:
                    #### Check Once only; this is Partial fill;
                    #### totqty will be completed by taking stock qty from
                    #### very first index of this if clause and this will be partial fill, Always
                    #### After comparing first index stock STOP this loop;
                    #### because NO further requirement of this loop; condition fully Satisfied
                    balstk = v['batstock']-(updtqty-totqty)
                    recdicfill['stkdic'][k]['qty']=balstk
                    recdicfill['stkdic'][k]['fill']=True
                    break  #### because NO further requirement of this loop; condition fully Satisfied
                else:
                    recdicfill['stkdic'][k]['qty']=v['batstock']
                    recdicfill['stkdic'][k]['fill']=True
		
    def ChkBillEditItem_Qty(self, keyid, row, col, recdicfill, qty, bonus, totqty, batstock, statictotstk,):
        ### must have key = 'staticqty' that will use to comapre if any changes made
        ### must have key = 'updatedqty' that will update stock qty
        ### must have key = 'edited' >>> flag edited or not, 2=True or 1=False; Default is 1=False
        ### *** statictotstk and batstock remains static never change throughout any edited or repeat entrie ** statictotstk == total stk of an item
        ### *** while dbstock is represent updated/edited total stock
        ### *** and  stkvariable represent updated/edited batch stock
        ## flag edited None/0 Fresh New Entries.... 
        ## flag edited 1 means NO changes has been made in Edit/Update Mode
        ## flag edited 2 means YES changes has been made in Edit/Update Mode
        totstock = recdicfill['totstock'] ### totstock remain CONSTANT during update, Never Change its Value 
        dbstock = recdicfill['dbstock']
        staticqty = recdicfill['staticqty']  ### 'staticqty' never change during update stock//old qty//original bill qty
        updatedstock = totqty-staticqty ### 'staticqty' never change during update stock
        
        #print recdicfill['totstock']
        recdicfill['edited'] = 2   ### 2 = True; 1 = False
        
        updateval = sum([batstock,updatedstock])
        dbupdateval = sum([statictotstk,updatedstock])
        ###self.parent.InfoDPN(recdicfill)
        
        if updatedstock < 0:
            
            ### Sales Update Qty/Stock
            ### -ve, Excess Stock given compare to previous static stock
            ### db stock/batch stock will Decrease
            
            if self.spnum in [2, 8]: ### Sale and PurchaseReturn
                if (updatedstock) > batstock :
                    ### restoring recdic 'stkvariable' and 'dbstock' keys at its original/starting position, while update
                    ### because during update user give more stock qty than available database stock (staticstock)
                    recdicfill['stkvariable'] = batstock     ### rejecting update here
                    recdicfill['dbstock'] = statictotstk     ### rejecting update here
                    recdicfill['edited'] = 1   ### 2 = True; 1 = False; resetting to False
                    self.wgdict[(row, self.colids['qty'])][0].SetValue(str(staticqty))
                    ##StatusDP(self.parent.stockdp, 'Batch Stock:%s\nTotal Stock:%s'%(batstock, dbstock), 'red')
                    StatusDP(self.parent.errorinfod, '%s'%'Stock_Nahi_Hai()', fg='red')
                    return
                else:
                    updatedstock = updatedstock
                totstkchanged = sum([totstock, -updatedstock]) ### Stock Reduce
            elif self.spnum in [1, 9]: ### Purchase and SalesReturn:
                updatedstock = -self.PurchaseUpdateStk(qty, updatedstock, batstock, statictotstk)
                totstkchanged = sum([totstock, updatedstock])
                
        else:
            if self.spnum in [2, 8]: ### Sale and PurchaseReturn
                updatedstock = updatedstock
                totstkchanged = sum([totstock, -updatedstock]) ### Stock Reduce
            elif self.spnum in [1, 9]: ### Purchase and SalesReturn:
                updatedstock = abs(self.PurchaseUpdateStk(qty, updatedstock, batstock, statictotstk))
                totstkchanged = sum([totstock, updatedstock])
                
        StatusDP(self.parent.stockdp, 'Edited Stk:%s\nBatch Stock:%s\nTotal Stock:%s'%(
            updatedstock, qty, totstkchanged), 'red')
        
        ### Stock is Subtracting From Main Stock [Default] in Sales and Adding in Purchase; recdicfill['updatedqty'] remain SAME
        recdicfill['updatedqty']=updatedstock
        ####recdicfill['updatedqty'] = recdicfill['totqty']-recdicfill['staticqty'] 
        recdicfill['stkvariable'] = updateval
        recdicfill['dbstock'] = dbupdateval
        
        self.Oncalculation_OnUpdate(keyid, row, col, recdicfill)
        self.parent.isgridqtyedited = True
        
    def PurchaseUpdateStk(self, qty, updatedstock, batstock, statictotstk):
        if abs(updatedstock) > batstock :
            #### stock qty increased to its actual qty during update;
            #### so updatedstock must be +ve in numbers and increase stock
            updatedstock = abs(updatedstock)
        else:
            #### stock qty decrease to its actual qty during update;
            #### so updatedstock must be -ve in numbers and decrease stock
            updatedstock = -updatedstock
        return updatedstock

    def SalesUpdateStk(self, qty, updatedstock, batstock, statictotstk, recdicfill):
        if updatedstock > batstock :
            #### stock qty increased to its actual qty during update;
            #### so updatedstock must be -ve in numbers and decrease stock in Sales
            updatedstock = -(updatedstock)
        else:
            #### stock qty decrease to its actual qty during update;
            #### so updatedstock must be +ve in numbers and increase stock in Sales
            updatedstock = updatedstock
        recdicfill['edited'] = 2   ### 2 = True; 1 = False; resetting to False
        return updatedstock

    def OnDoubleClick(self, event=None):
        ### Double Click will act as Return Key [Both behaviour are taken as same]
        self.OnSelected(event, evtname='Return')        
    def OnSelectedR(self, event=None):
        self.OnSelected(event, evtname='Return')
    def OnSelectedL(self, event=None): 
        self.OnSelected(event, evtname='LB')
    def OnSelected(self, event, evtname):
        r,c=self._widf[event.widget]
        self.r = [r,c,self]
        if self.r:
            self.parent.GetLCSelectData(self.r, self.itemlc_dict, evtname)
            if self.MoveCursorDown:
                self.Lselection_clear(self.kmcount)
                ### to move cursor down self.kmcount must increment by One
                self.kmcount += 1
                self.Lselection_set(self.kmcount)
        return [self.r, self.itemlc_dict]
        
    def OnScroll(self, event):
        for box in self.boxes:
            box.bind_all("<MouseWheel>", self.ScrollStart)
        
    def OffScroll(self, event):
        for box in self.boxes:
            box.unbind_all("<MouseWheel>")
        
    def ScrollStart(self, event):
        if event.delta < 0:
            self.lcdata, kidx = self.KeyMove('Down', 'name') 
        else:
            self.lcdata, kidx = self.KeyMove('Up', 'name')
        
        try:
            r,c=self._widf[event.widget]
            self.r = [r,c,self]
            self.parent.GetLCSelectData(self.r, self.itemlc_dict, 'Scroll')
        except Exception as err:
            pass
        
    def OnKey(self, event):
        key = event.keysym
        self.lcdata, kidx = self.KeyMove(key, 'name')
        if key == 'Escape':
            try:
                self.parent.OnClose(event) ### Calling Parent Class OnClose
            except AttributeError:
                pass
        r,c=self._widf[event.widget]
        self.r = [r,c,self]
        if key == 'Right':
            try:
                w=self.wgdict[(r,sum([c,1]))][0] 
                w['bg']=self.mbg
                w.focus()
            except KeyError:
                pass
        if key == 'Left':
            try:
                w=self.wgdict[(r,sum([c,-1]))][0] 
                w['bg']=self.mbg
                w.focus()
            except KeyError:
                pass
        if key == 'F12':
            filewin = Toplevel(self)
            RMSCalculator(filewin, 'RMS Calculator', 1, 1, self.parent, rscr=self.rscr)
            return
            
        self.parent.GetLCSelectData(self.r, self.itemlc_dict, key)
        
    def ReturnErrorOnKeyMove(self):
        self.kmcount = 0
        try:
            if self.itemlc_dict:
                return [self.itemlc_dict[self.kmcount], self.kmcount]
            else:
                return [self.itemlc_dict, self.kmcount]
        except KeyError:
            return [self.itemlc_dict, 0]
        
    def KeyMove(self, key, dpkey):
        knum, msg = 0, None
        if key in ['Down','Return',]:
            knum, kidx = self.MoveDown(dpkey)
            try:
                return [self.itemlc_dict[knum], kidx]
            except KeyError:
                return self.ReturnErrorOnKeyMove()
        if key in ['Up']:
            knum, kidx = self.MoveUp(dpkey)
            try:
                return [self.itemlc_dict[knum], kidx]
            except KeyError as err:
                return self.ReturnErrorOnKeyMove()
                
        if key in ['Tab','End']:
            self.datavarlimit = 0
            if self.itemlc_dict:
                try:
                    return [self.itemlc_dict[self.kmcount], self.kmcount]
                except KeyError:
                    return [self.itemlc_dict[0], 0]
            else:
                return ['', self.kmcount]
        if self.itemlc_dict:
            try:
                return [self.itemlc_dict[0], self.kmcount]
            except KeyError:
                return [self.itemlc_dict, 0]
        else:
            if self.griditems:
                return [None, self.kmcount]
            self.Lselection_set(0)
            return [None, self.kmcount]
    
    def MoveDown(self, dpkey):
        
        if self.kmcount == self.staticlimit-1:
            self.datavarlimit += self.staticlimit
            if self.qfunc:
                if self.text[0]:
                    self.setdata_(self.qfunc, self.text, dpkey)
                else:
                    pass
                
            else:
                if self.loadnext:
                    self.VirtualDeleteAllItems()
                    self.DisplayLBData(chunk=False, idx=self.datavarlimit)
                
                self.Lselection_clear(self.kmcount) ### clear is less than set when move down
                self.kmcount = 0
                self.Lselection_set(self.kmcount) ### set is greater than clear when move down
               
            return [self.kmcount, self.kmcount]
        
        if self.GetSize()-1 == self.kmcount: ### reached at last visible Item
            self.Lselection_clear(self.kmcount)
            self.kmcount = 0
            
            if self.griditems:
                return [self.kmcount, self.kmcount]
            self.Lselection_set(self.kmcount)
            return [self.kmcount, self.kmcount]
        if self.GetSize() == 0: ##ListBox is Empty and need to refill From Start
            self.Lselection_clear(self.kmcount)
            self.DisplayLBData()
            self.kmcount = 0
            
            if self.griditems:
                return [self.kmcount, self.kmcount]
            
            self.Lselection_set(self.kmcount)
            return [self.kmcount, self.kmcount]
        
        self.Lselection_clear(self.kmcount) ### clear is less than set when move down
        if self.griditems:
            return [self.kmcount, self.kmcount]
        
        self.kmcount += 1
        self.Lselection_set(self.kmcount) ### set is greater than clear when move down
        return [self.kmcount, self.kmcount]
        
    def MoveUp(self, dpkey):
        if self.kmcount<1:
            self.datavarlimit -= self.staticlimit
            if self.datavarlimit < 0:
                self.datavarlimit = 0
                return [self.kmcount, self.kmcount]
            if self.qfunc:
                self.setdata_(self.qfunc, self.text, dpkey)
                self.kmcount = self.staticlimit-1
                self.Lselection_set(self.staticlimit-1)
                self.Lselection_clear(0)
            else:
                if self.loadnext:
                    self.VirtualDeleteAllItems()
                    self.DisplayLBData(chunk=False, idx=self.datavarlimit)
                self.kmcount = self.staticlimit-1
                self.Lselection_set(self.kmcount) 
                self.Lselection_clear(0) 
            return [self.kmcount, self.kmcount]
        
        self.Lselection_clear(self.kmcount)   ### clear is grater than set when move up
        if self.griditems:
            return [self.kmcount, self.kmcount]
        self.kmcount -= 1
        self.Lselection_set(self.kmcount)  ### set is less than clear when move up
        return [self.kmcount, self.kmcount]

    def GETDATA(self, idx=0):
        try:
            return self.itemlc_dict[idx]
        except KeyError:
            return {}
        
    def SETDATA(self, qfunc, text, dpkey, staticlimit=None):
        self.qfunc = qfunc
        self.text = text
        if staticlimit:
            self.staticlimit = staticlimit
        else:
            staticlimit = self.staticlimit
        
        self.setdata_(qfunc, text, dpkey, staticlimit=staticlimit)
        return self.GETDATA()
    
    def setdata_(self, qfunc, text, dpkey, staticlimit=None):
        if not staticlimit:
            staticlimit = self.staticlimit
         
        self.itemlc_dict = qfunc(self.rscr, text, varlimt=self.datavarlimit, staticlimit=staticlimit)
        self._number_of_rows = len(self.itemlc_dict)
        self.DisplayLBData()
       
        self.kmcount = 0
        self.Lselection_set(self.kmcount)

    def DisplayLBData(self, chunk=True, idx=0):
        keyerr = [False, '']
        if not self.itemlc_dict:
            return [True, 'No Data Found']
        if chunk:
            for k in range(self.staticlimit):
                sno = sum([self.datavarlimit, k])
                try:
                    self.itemlc_dict[k]['sno']=sno
                except KeyError:
                    pass
                for c in range(self.columns):
                    ckey = self.colconf[c]['idname']
                    try:
                        self.TxtSet(self.wgdict[(k, c)][0], self.itemlc_dict[k][ckey]) 
                        ###self.boxes[c].insert('end', self.itemlc_dict[k][ckey])
                    except (KeyError, TypeError) as err:
                        keyerr = [True, str(err)]
                self.wgdict[(k,0)][1]['text']=sno
        else:
            if idx > self._number_of_rows:
                idx = 0
                self.datavarlimit = 0
            for r in range(self.staticlimit):
                try:
                    self.itemlc_dict[idx]['sno']=idx ##sum([self.datavarlimit, idx])
                    self.wgdict[(r,0)][1]['text']=idx
                except KeyError:
                    self.wgdict[(r,0)][1]['text']=''
                    pass
                for c in range(self.columns):
                    ckey = self.colconf[c]['idname']
                    try:
                        self.SetCellValue(r, c, self.itemlc_dict[idx][ckey])
                    except (KeyError, TypeError) as err:
                        keyerr = [True, str(err)]
                idx += 1
            
        self._number_of_rows = len(self.itemlc_dict)
        
        if self.ColorTags:
            if not self.itemlc_dict:
                return keyerr
            if self.itemlc_dict[0].has_key('name'):
                self.ResetPartyColorTags()
            else:
                self.ResetLedgerColorTags()
        
        return keyerr
    
    def TxtSet(self, w, text, erase=False, fg='black', bg='white'):
        #w.var.set(text)
        try:
            w.delete(0, 'end')
        except:
            pass
        if erase:
            return
        try:
            w.insert(0, text)
            w['fg']=fg
            w['bg']=bg
        except :
            pass
        
        
    def SetGridCursorRow(self, r=0, c=0):
        self.getr, self.getc = r, c

    def SetGridCursor(self, r=0, c=0 ):
        self.SetGridCursorRow(r, c)
    def SetCellValue(self, row, col, text, fg='blue', bg='white'):
        try:
            wg = self.wgdict[(row,col)][0]
            self.TxtSet(wg, text, fg=fg, bg=bg)
        except :
            pass
    def GetCellValue(self, row=None, col=None, itemlc=False):
        if row is None:
            return self.itemlc_dict
        if col is None:
            return self.itemlc_dict[row]
        return self.wgdict[(row,col)][0].get()

    def GetNumberRows(self):
        return len(self.itemlc_dict)
    
    def GetGridCursorRow(self):
        return (self.getr, self.getc)

    def GetGridCursor(self):
        return self.GetGridCursorRow()
    
    def GetRow(self):
        return self.getr

    def GetCol(self):
        return self.getc
    
    def fg(self, row, col, clr):
        wg = self.wgdict[(row,col)][0]
        wg['fg']=clr

    def bg(self, row, col, clr):
        wg = self.wgdict[(row,col)][0]
        wg['bg']=clr

    def Enable(self):
        try:self.config(state='normal') #self['state']='normal'
        except:pass
    def Disable(self):
        try:self.config(state='disabled') #self['state']='disabled'
        except:pass

    def Refresh(self):
        self.update()
        
    def ResetPartyColorTags(self):
        ### spid = 1 (suppliers)(powderblue); spid = 2 (customer)(lightgreen); 
        ### spid = 3 (expence)(lightyellow); spid = 4 (not defined yet); 
        ### spid = 5 (cash)(lightgrey); spid = 6 (company)(purpel); spid = 7 (bank)(lightorange);
        ### #ffff80 = light yellow; #c6ffb3 = light green; #e6ffff = light aqua blue
        ### #f2f2f2 = light grey; #c6ffb3 = light green; #ffd699 = light orange
        ### #ffb3b3 = light red; #ccb3ff= light purpel; yellow = #ffff4d
        clrdic = {0:{'bg':'white'},1:{'bg':'#e6ffff'},2:{'bg':'#c6ffb3'},3:{'bg':'#ffff4d'},
            4:{'bg':'#ffffb3'},5:{'bg':'#f2f2f2'},6:{'bg':'#ccb3ff'},7:{'bg':'#ffd699'},
            8:{'bg':'#ffb3b3'},9:{'bg':'#ffb3b3'},}
        reloadata = False
        for i in range(self.rows):
            for lb in self.boxes:
                try:
                    lb.itemconfig(i, clrdic[self.itemlc_dict[i]['spid']])
                except Exception :
                    reloadata = True
                    break
        
    def ResetLedgerColorTags(self):
        ### spid = 1 (suppliers)(powderblue); spid = 2 (customer)(lightgreen); 
        ### spid = 3 (expence)(lightyellow); spid = 4 (not defined yet); 
        ### spid = 5 (cash)(lightgrey); spid = 6 (company)(purpel); spid = 7 (bank)(lightorange);
        ### #ffff80 = light yellow; #c6ffb3 = light green; #e6ffff = light aqua blue
        ### #f2f2f2 = light grey; #c6ffb3 = light green; #ffd699 = light orange
        ### #ffb3b3 = light red; #ccb3ff= light purpel; #ffff4d = yellow
        clrdic = {0:{'bg':'white'},1:{'bg':'#e6ffff'},2:{'bg':'#c6ffb3'},3:{'bg':'#ffff4d'},
            4:{'bg':'#ffffb3'},5:{'bg':'#f2f2f2'},6:{'bg':'#ccb3ff'},7:{'bg':'#ffd699'},
            8:{'bg':'#ffb3b3'},9:{'bg':'#ffb3b3'},}
        idx = self.datavarlimit
        for i in range(self.rows):
            #print clrdic[self.itemlc_dict[idx]['spid']]
            for lb in self.boxes:
                try:
                    lb.itemconfig(i, clrdic[self.itemlc_dict[idx]['spid']])
                except Exception as err:
                    pass
            idx += 1
    
    def SetFocus(self, row=1, col=0): 
        wg = self.wgdict[(row,col)][0]
        if self.setbg :
            wg.bg(self.mbg)
        wg.focus()

    def GridFocus(self, row=1, col=0): 
        wg = self.wgdict[(row,col)][0]
        wg.focus()

    def SelectAll(self, row=1, col=0):
        wg = self.wgdict[(row,col)][0]
        wg.select_range(0, 'end')
       
    def Hide(self, data=True):
        self.kmcount = 0
        self.frame.grid_forget()
        if data:
            self.Reset_arg()
        
    def Show(self, r=0, c=0, rsp=1, csp=1, sticky='w'):
        self.kmcount = 0
        self.frame.grid(row=r, column=c,
                rowspan=rsp, columnspan=csp, sticky=sticky)
        self.frame.lift(aboveThis=None)
             
    def GetNumberRows(self):return len(self.itemlc_dict)
    def GetNumberCols(self):return self.columns
    def GetColLabelValue(self, idx):return self.colconf[idx]['text']
    def SetColLabelValue(self, idx, text):
        self.colconf[idx]['text']=text
        self.colldict[idx].SetLabel(text)
    def GetRowLabelValue(self, r):
        return self.snwg[r]['text']
    def SetRowLabelValue(self, r, value):
        self.snwg[r]['text']=str(value)
    def GetIndex(self):
        self.index = [box.curselection() for box in self.boxes][0][0]
        return self.index
    
    def GetItem(self, r, c):
        return self.r
    
    def GetItemData(self, r):return self.GetRowItem(r)
    
    def GetRowItem(self, r):return [box.get(r) for box in self.boxes]
        
    def GetText(self):return [box.get(self.r) for box in self.boxes][self.c]

    def GetItemText(self, idx):return [box.get(idx) for box in self.boxes][0]
        ### Text first column

    def GetRowDict(self, r):return self.itemlc_dict[r]
        
    def GetFocusedItem(self):return self.GetIndex()

    def GetFirstSelected(self):return self.GetIndex()
    
    def GetItemCount(self):return self.boxes[0].size()
    def ItemCount(self):return self.boxes[0].size()

    def GetColumnCount(self):return len(self.boxes)

    def SetItemBackgroundColour(self,idx, clr):
        pass

    def Reset_arg(self):
        self.itemlc_dict = {} #### containing name as key(r,c) and values 
        self._number_of_rows = 0
        self.r = [0,0,self]   
        self.kmcount = -1
        self.datavarlimit = 0
        
    def VirtualDeleteAllItems(self):
        for i in range(self.GetSize()):
            for box in self.boxes:
                box.delete(i, 'end')
                
    def DeleteAllItems(self):
        for r in range(self.rows):
            for wdg in self.boxes:
                self.TxtSet(wdg, '', erase=True)
        self.Reset_arg()

    def ClearAll(self):
        self.DeleteAllItems()

    def Clear(self):
        self.DeleteAllItems()

    def ClearGrid(self):
        self.DeleteAllItems()
        
    def DeleteItem(self, r):
        delitems = []
        for box in self.boxes:
            delitems.append(box.get(r))
            box.delete(r, 'end')
        return delitems
    
    def RefreshItems(self):pass

    def RefreshItem(self):pass

    def InsertItem(self, r, txt=''):
        self.r += 1
        self._number_of_rows=self.r
        self.kmcount = -1
       
    def SetItem(self, r, c, txt): ##self.boxes[c].insert(r, str(txt))
        self.itemlc_dict[(self.r, c)]=txt
        self.boxes[c].insert(self.r, str(txt))
        ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
        self.getrowvalue = self.itemlc_dict[0]
        
    def InsertStringItem(self, r, txt=''):
        self.r += 1
        self._number_of_rows=self.r
        self.kmcount = -1
        
    def SetStringItem(self, r, c, txt):
        self.itemlc_dict[(self.r, c)]=txt
        ###self.boxes[c].insert(self.r, str(txt))
        self.boxes[c].insert(self.r, txt.encode('utf-8')) ### to prevent 'ascii' code error
        ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
        self.getrowvalue = self.itemlc_dict[0]

    def Lyview(self): 
        return [box.yview() for box in self.boxes][0]
    
    def Lselection_clear(self, idx): 
        self.Lselection(idx, self.stbg, f=False)
        
    def Lselection(self, r, tag, f=True):
        #for r in range(self.rows):
        for c in range(self.columns):
                wgid = (r, c)
                if wgid in self.wgdict:
                    w=self.wgdict[wgid][0]
                    w['bg']=tag
                    if f:
                        w.focus()
    def Lselection_set(self, idx, last=None):
        if self.xFocus :  ### if focus migrated to next widget OTHER THAN GRID
            return
        try:
            self.SetFocus(row=idx, col=self.r[1])
        except:
            pass
               
    def GetSize(self): ### ItemLB
        return len(self.itemlc_dict)
    def Ldelete(self, idx=0, pos='end'): ### ItemLB
        return [box.delete(0, 'end') for box in self.boxes][0]
     
    def GetValue(self, idx): ### ItemLB
        return [box.get(idx) for box in self.boxes][0]
    def GetTupleValue(self, idx): ### ItemLB
        return [box.get(idx) for box in self.boxes]
    def GetColValue(self, idx, col=0): ### ItemLB
        return [b.get(idx) for i, b in enumerate(self.boxes) if col==i][0].split('||')
    def Lyview_moveto(self, mvy): ### ItemLB
        return [box.yview_moveto(mvy) for box in self.boxes][0]
    def Lcurselection(self): ### ItemLB
        return [box.curselection() for box in self.boxes][0]

    def ListData_Fill(self, data):
        for i, v in enumerate(data):
            self.itemlc_dict[i]=v
            for c, key in enumerate(self.collabel):
                self.boxes[c].insert('end', v[c])
        if self.itemlc_dict:
            ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
            self.getrowvalue = self.itemlc_dict[0]

    def ExFill(self, dictdata, full=False, searcstartswith=None):
        ### Fresh Display;
        ### full; will fill all data by increasing listbox height
        ### searcstartswith is dict {'key':'search into','text':'want to search'} 
        ### Function used whenever data display required from outside this class
        ### Only Used WHEN SINGLE BOX is available
        if full:
            lendictdata = len(dictdata)
            self.staticlimit = lendictdata
            self.boxes[0]['height']=lendictdata
        self.itemlc_dict = dictdata
        if searcstartswith:
            for k,v in dictdata.items():
                self.boxes[0].delete(k, 'end')
                if v[searcstartswith['key']].startswith(searcstartswith['text']): 
                    self.boxes[0].insert('end', v['name'])
        else:    
            for k,v in dictdata.items():
                self.boxes[0].delete(k, 'end')
                self.boxes[0].insert('end', v['name'])
        self.kmcount = 0
        self.Lselection_set(0)
            
    def Fill(self, data={}, keylist=['prodname','compname',], itemsd=True): ### ItemLB
        self.Reset_arg()
        if isinstance(data, (tuple, list)):
            self.ListData_Fill(data)
        else:
            
            for i, (k, val) in enumerate(data.items()):
                #self.itemlc_dict[i]=val
                self._number_of_rows = i
                #for c, (ktg, text) in val.items():
                for c in range(self.columns):
                    self.boxes[c].insert('end', val[keylist[c]])
            self.itemlc_dict = data
        ### while setting new item self.getrowvalue will collect value of Zero Key/Index by default  
        if self.itemlc_dict:
            self.getrowvalue = self.itemlc_dict[0]

    def WChangeValue(self, wg, val=''):
        ### *** Most Important startitemsearch BOOL Disable self.var Invoking while shuffeling key up and down
        ### *** When recdic set data to widget durring shuffling key startitemsearch must set to False | STOP Invoking self.var
        ### *** if not implemented then value will overlap or duplicate in widget as well as in recdic        
        wg.var.set(str(val))
        #wg.delete(0,"end")
        #wg.insert(0, val)
        
    def Fill_Via_Recdict(self, recdic,):
        keyid = 0
        self.MuteTxtStart()
        for cr in range(self.rows):
            if recdic['grid'].get(keyid):
                for k, v in recdic['grid'][keyid].items():
                    txwg = self.wgdict.get((cr,self.colids.get(k))) ###
                    if txwg:
                        self.WChangeValue(txwg[0], unicode(v))
                keyid += 1
        #self.AllowTxtStart()
                
    def ClearGridCells(self, text=''):
        self.MuteTxtStart()
        for r in range(self.rows):
            for c in range(self.cols):
                txwg = self.wgdict[(r, c)]
                if txwg:
                    self.WChangeValue(txwg[0], text)
                
    def CommonItemBat_Entry_item_select(self):
        try:
            itemid = str(self.tempitembatlist[0])
        except:
            if self.cmoveupdown:
                StatusDP(self.parent.status, '')
            else:
                if self.nobatchgivenpur :
                    StatusDP(self.parent.status, "** Select Item First; ",
                           " Without Selecting Item Your Item will Not Save in Records !", 'red')
                    self.nobatchgivenpur = False
            itemid = None
        return itemid
    
    def CommonItemBat_Entry_qty_bonus_validity(self, qtty, bonus):
        if bonus.isdigit():
            qty = sum([int(qtty), int(bonus)])
        else:
            try:
                qty = int(qtty)
            except:
                qty = None
        return qty

    def GetItemBatkey(self, itemid, bat, totstk, qty):
        #totstk = self.tempitembatlist[2]
        balstk = sum([totstk, qty])
        itembatkey = ''.join([itemid, bat.strip()])
        return totstk, balstk, itembatkey
    
    def StockCalculation(self, qty, staticstk, staticbatstk, statictotstk):
        updtqty = sum([qty, -staticstk])
        
        if self.par.sp == 'purupdt':
            if self.parent.recdic['grid'][self.keyid].get('pryitmid'):
                if qty >= staticstk:
                    updtbatstk = sum([staticbatstk, updtqty])
                    updttotstk = sum([statictotstk, updtqty]) 
                else:
                    updtbatstk = sum([staticbatstk, - abs(updtqty)])
                    updttotstk = sum([statictotstk, - abs(updtqty)])
            else:
                ### Adding New Items Stock in Old Bill while updating bill
                updtbatstk = sum([staticbatstk, qty])
                updttotstk = sum([statictotstk, qty])
        else:
            if self.parent.recdic['grid'][self.keyid].get('pryitmid'):
                if qty >= staticstk:
                    updtbatstk = sum([staticbatstk, - updtqty])
                    updttotstk = sum([statictotstk, - updtqty])
                    
                else:
                    updtbatstk = sum([staticbatstk, abs(updtqty)])### Adding stk if qty is reduced from previous qty while updating
                    updttotstk = sum([statictotstk, abs(updtqty)])### Adding stk if qty is reduced from previous qty while updating
            else:
                ### Subtracting New Items Stock in Old Bill while updating bill
                updtbatstk = sum([staticbatstk, - qty])
                updttotstk = sum([statictotstk, - qty])

        return updtbatstk, updttotstk
    
    def ChkIntVal(self, val, defaultval=0):
        try:
            intval = int(val)
        except ValueError:
            intval = defaultval
        return intval

    def BonusSplit(self, bbv, qty, splitstr):
        try:
            sp_main, sp_last = bbv.split(splitstr) ### m
            spmain = self.ChkIntVal(sp_main, defaultval=10) ### user did not give first value and start with +, eg: +2; so set default 10
            splast = self.ChkIntVal(sp_last, defaultval=0)  ### user did not give second value eg: 10+; so set default 0, 10+0
            modbv = '+'.join([str(spmain), str(splast)])
            nfstval, nsndval = spmain, splast
        except IndexError :
            spmain, splast, modbv = 10, 0, '0'
        return modbv, nfstval, nsndval

    def SetBonus(self, qty, bbv):
        modbv = '0'
        try:
            if int(bbv):
                modbv = bbv
        except ValueError :
            modbv = modbv
        nfstval, nsndval = qty, bbv
        bonus, net = True, False
        if '=' in bbv:
            modbv, nfstval, nsndval = self.BonusSplit(bbv, qty, '=')
            bonus, net = False, True
        if '+' in bbv:
            modbv, nfstval, nsndval = self.BonusSplit(bbv, qty, '+')
            bonus, net = False, True
        return modbv, nfstval, nsndval, bonus, net
    
    def Oncalculation(self, keyid, r, c, qty=None, netedit=None, recdicfill=None):
        rate = float(recdicfill['rate'])    
        tax1 = recdicfill['tax1']
        tax2 = recdicfill['tax2']
        bonus = recdicfill['bonus']
        dis = float(recdicfill['dis'])
        qty = recdicfill['qty']
        bonus_str = str(bonus) ### bonus given in string format
        totqty = recdicfill['totqty']
        
        addbonus_into_qty, bonus_str, nfstval, nsndval, bns_, net = self.GetBonusDetails(qty, bonus)
        erreport, amount, dis_amt, tax1_amt, tax2_amt, net_rate = self.ActiveCalculation(recdicfill,
            r, c, qty, totqty, bonus_str, rate, dis, tax1, tax2, nfstval, nsndval, self.colids,
            netedit=netedit, spnum=self.parent.spnum, sdc=self.sdc, mysoftval=self.mysoftval, fpf=self.fpf )
        
        if erreport:
            return #### Error Found during calculation return back
        
        if recdicfill:
            try:
                recdicfill['amt']=amount
                recdicfill['satamt']=tax1_amt
                recdicfill['taxamt']=tax2_amt
                recdicfill['tax1amt']=tax1_amt
                recdicfill['tax2amt']=tax2_amt
                recdicfill['ttaxamt']=sum([tax1_amt, tax2_amt])
                recdicfill['disamt']=dis_amt
                recdicfill['netrate']=format(self.fpf % net_rate)
                
                if self.spnum == 2: ### for sale only
                    if self.sdc == '2':
                        txabel = amount-dis_amt
                        taxableamt = txabel-(tax1_amt+tax2_amt)
                        netamt = txabel
                    else:
                        taxableamt = amount-dis_amt
                        netamt = sum([taxableamt, tax1_amt, tax2_amt])
                elif self.mysoftval == 11:
                    txabel = amount-dis_amt
                    taxableamt = txabel-(tax1_amt+tax2_amt)
                    netamt = txabel
                else:
                    taxableamt = amount-dis_amt
                    netamt = sum([taxableamt, tax1_amt, tax2_amt])
                
                taxableamt = amount-dis_amt
                netamt = sum([taxableamt, tax1_amt, tax2_amt])
                recdicfill['taxableamt']=taxableamt
                recdicfill['totnetamt']=netamt #totnetamt
                recdicfill['netamt']=netamt
                
                totqty = float(recdicfill['totqty'])
                purnetrate = float(recdicfill['pnet'])
                #####>>>> 'pnetamt':will use to compare (purchase_net_rate * qty) with (sale_net_rate * qty) to evaluate proffit and loss during sales
                recdicfill['pnetamt'] = sum([totqty*purnetrate])
            except Exception as err:
                for k in ['amt','satamt','taxamt','tax1amt','tax2amt','ttaxamt','disamt','netrate',
                          'taxableamt','totnetamt','netamt','pnetamt',]:
                    recdicfill[k]=0
                StatusDP(self.parent.status, 'STOP ! Cannot Leave Blank [%s]'%str(err), fg='red')
            
        if self.spnum in [2, 8, 12]: ### DBStock Will Decrease in [Sale and PurchaseReturn] 
            ### (int) spnum will act as identifier of frame
            ### 1 = Purchase; 2 = Sale; 8 = PurchaseReturn; 9 = SalesReturn;
            ### 11 = PurchaseOrder; 12 = SalesOrder
            ### DBStock will Reduce in Sales
            try:
                dbstock = int(float(recdicfill['totstock'])) - sum([qty, addbonus_into_qty])    ### 'totstock' Must remain constant; never try to update/change
                stkvariable = int(float(recdicfill['batstock'])) - sum([qty, addbonus_into_qty])### 'batstock' Must remain constant; never try to update/change
            except:
                dbstock = recdicfill['totstock']
                stkvariable = 0
           
            recdicfill['dbstock']=dbstock          ### 'dbstock' should UPDATE/change; when user enter qty or int bonus, consider total stock updated item stock 
            recdicfill['stkvariable']=stkvariable  ### 'stkvariable' should UPDATE/change; when user enter qty or int bonus, consider batch wise stock updated item stock
            
            self.GTotal_Calculation_Sale(keyid, self.parent.spnum, 'pp', fpf=self.fpf)
            #GTotal_Calculation_Sale(self.parent, keyid, self.parent.spnum, 'pp', fpf=self.fpf)
        else:   ### DBStock Will Increase in [Purchase and SalesReturn]
            ### (int) spnum will act as identifier of frame
            ### 1 = Purchase; 2 = Sale; 8 = PurchaseReturn; 9 = SalesReturn;
            ### 11 = PurchaseOrder; 12 = SalesOrder
            ### DBStock will Reduce in Sales
            try:
                if self.sdc == '2':
                    ### For Retails MedicalStores stkvariable value  updated in Qty and Bonus Chk_For_Retail_Med function
                    dbstock = recdicfill['dbstock']
                    stkvariable = recdicfill['stkvariable']
                else:
                    dbstock = sum([int(float(recdicfill['totstock'])), sum([qty, addbonus_into_qty])])     ### 'totstock' Must remain constant; never try to update/change
                    stkvariable = sum([int(float(recdicfill['batstock'])), sum([qty, addbonus_into_qty])]) ### 'batstock' Must remain constant; never try to update/change
            except:
                dbstock = recdicfill['totstock']
                stkvariable = None ### Prepare for Insert New Stock Add Stock
            recdicfill['dbstock']=dbstock         ### 'dbstock' should UPDATE/change; when user enter qty or int bonus, consider total stock updated item stock 
            recdicfill['stkvariable']=stkvariable ### 'stkvariable' should UPDATE/change; when user enter qty or int bonus, consider batch wise stock updated item stock

            self.GTotal_Calculation_Pur(keyid, self.parent.spnum, 'pp', fpf=self.fpf)
            ##GTotal_Calculation_Pur(self.parent, keyid, self.parent.spnum, 'pp', fpf=self.fpf)
        
        ### DLabel args >>> (Taxable,DisAmt,TaxAmt,NetRate,NetAmount,tax=tax)
      
        self.parent.DLabel(
            "{0:.2f}".format(taxableamt),"{0:.2f}".format(dis_amt),
            "{0:.2f}".format(sum([float(tax1_amt), float(tax2_amt)])),
            "{0:.2f}".format(float(recdicfill['netrate'])),"{0:.2f}".format(netamt),
            tax=recdicfill['tax'])
        
    def GetBonusDetails(self, qty, bonus):
        bonus_str = str(bonus) ### bonus given in string format
        nfstval, nsndval, bns_, net = 0, 0, True, False
        if isinstance(bonus, int):
            ### No Net Given, pure bonus/free given; bns_ = True; net = False; default is ZERO 0 in int
            addbonus_into_qty = bonus
        else:
            if bonus.replace('.', '', 1).isdigit(): #### Checking wheather value is with + or = net bonus given or not
                ### No Net Given, pure bonus/free given; bns_ = True; net = False
                addbonus_into_qty = int(float(bonus))
            else:
                ### Net is Given in 10+2,1+1, ...,; bns_ = False; net = True
                addbonus_into_qty = 0
                bonus_str, nfstval, nsndval, bns_, net = self.SetBonus(qty, bonus)
        return addbonus_into_qty, bonus_str, nfstval, nsndval, bns_, net

    def ActiveCalculation(self, recdicfill, r, c, qty, totqty, bonus_str, rate, dis, 
            tax1, tax2, nfstval, nsndval, ucpi, netedit=None, spnum=1,
            sdc='1', mysoftval=1, fpf='%0.2f' ):
        erreport = False
        
        try:
            ## oncalculation ## AmountCal_WS function is already define in rscr when rmssoft start and
            ## oncalculation ## AmountCal_Retail is used as sdc = '2' for retail calculation stored in rscr
            ## oncalculation ## these function asre avialable in rmstxt\text_validator.py
            if netedit:
                if nfstval:
                    xnfstval, xnsndval = nfstval, nsndval
                else:
                    ### This will Stop float division by zero
                    ### xnsndval will remain ZERO; otherwise xnfstval, xnsndval will sum and become 2, gives wrong output
                    xnfstval, xnsndval = 1, 0
                ### During netedit Addjusting rate first than calculate
               
                rate = float(netedit)/((float(xnfstval)/sum([xnfstval, xnsndval]))*((100-dis)/100)*(sum([100,tax1,tax2])/100 ))
                recdicfill['rate']=rate
                if self.colids.get('rate'):
                    self.wgdict[(r, self.colids['rate'])][0].SetValue(format(self.fpf % rate))
                
            amount, dis_amt, tax1_amt, tax2_amt, net_rate = AmountCal_WS(r, c, qty, totqty, bonus_str, rate, dis, 
                tax1, tax2, nfstval, nsndval, self, ucpi, netedit=netedit, sp=spnum, sdc=sdc, mysoftval=mysoftval, fpf=fpf)
            
            if not netedit:
                ### *** Never use >>> SetValue to netrate column itself stop responding/infinity loop
                pass
                #self.wgdict[(r, self.colids['netrate'])][0].SetValue(format(self.fpf % net_rate))
                #self.SetCellValue(r, 'netrate', format(self.fpf % net_rate))
                #self.SetCellValue(r, 'amt', format(self.fpf % amount))
                #self.WChangeValue(self.wgdict[(r, ucpi['netrate'])][0], format(self.fpf % net_rate))
            else:
                recdicfill['rate']=rate
                if self.colids.get('rate'):
                    self.wgdict[(r, self.colids['rate'])][0].SetValue(format(self.fpf % rate))
                #self.SetCellValue(r, 'rate', format(self.fpf % rate)) ### netrate is given by user; never update netrate here 
                #self.SetCellValue(r, 'amt', format(self.fpf % amount))
                
                
        #except Exception as err:
        except Exception as err:
            
            prodname = self.wgdict[(r, 0)][0].var.get()
            StatusDP(self.parent.status, 'Error On [%s], At Col No: %s [%s]'%(prodname, c, str(err)), 'red')
            amount, dis_amt, tax1_amt, tax2_amt, net_rate = 0, 0, 0, 0, 0
            erreport = True
        return erreport, amount, dis_amt, tax1_amt, tax2_amt, net_rate
    
    def Oncalculation_OnUpdate(self, keyid, r, c, recdicfill, netedit=None, ):
        rate = float(recdicfill['rate'])    
        tax1 = recdicfill['tax1']
        tax2 = recdicfill['tax2']
        bonus = recdicfill['bonus']
        dis = float(recdicfill['dis'])
        qty = recdicfill['qty']
        totqty = recdicfill['totqty']
        
        addbonus_into_qty, bonus_str, nfstval, nsndval, bns_, net = self.GetBonusDetails(qty, bonus)
        erreport, amount, dis_amt, tax1_amt, tax2_amt, net_rate = self.ActiveCalculation(recdicfill,
            r, c, qty, totqty, bonus_str, rate, dis, tax1, tax2, nfstval, nsndval, self.colids,
            netedit=netedit, spnum=self.parent.spnum, sdc=self.sdc, mysoftval=self.mysoftval, fpf=self.fpf )
        if erreport:
            return #### Error Found during calculation return back
          
        recdicfill['amt']=amount
        recdicfill['satamt']=tax1_amt
        recdicfill['taxamt']=tax2_amt
        recdicfill['tax1amt']=tax1_amt
        recdicfill['tax2amt']=tax2_amt
        recdicfill['ttaxamt']=sum([tax1_amt, tax2_amt])
        recdicfill['disamt']=dis_amt
        recdicfill['netrate']=format(self.fpf % net_rate)
        taxableamt = amount-dis_amt
        netamt = sum([taxableamt, tax1_amt, tax2_amt])
        recdicfill['taxableamt']=taxableamt
        recdicfill['totnetamt']=netamt #totnetamt
        recdicfill['netamt']=netamt
        
        totqty = recdicfill['totqty']
        purnetrate = recdicfill['pnet']
        #####>>>> 'pnetamt':will use to compare (purchase_net_rate * qty) with (sale_net_rate * qty) to evaluate proffit and loss during sales
        recdicfill['pnetamt'] = sum([totqty*float(purnetrate)])
        
        if self.spnum in [2, 8, 12]: ### DBStock Will Decrease in [Sale and PurchaseReturn] 
            ### (int) spnum will act as identifier of frame
            ### 1 = Purchase; 2 = Sale; 8 = PurchaseReturn; 9 = SalesReturn;
            ### 11 = PurchaseOrder; 12 = SalesOrder
            
            self.GTotal_Calculation_Sale(keyid, self.parent.spnum, 'pp', fpf=self.fpf)
            #GTotal_Calculation_Sale(self.parent, keyid, self.parent.spnum, 'pp', fpf=self.fpf)
        else:   ### DBStock Will Increase in [Purchase and SalesReturn]
            ### (int) spnum will act as identifier of frame
            ### 1 = Purchase; 2 = Sale; 8 = PurchaseReturn; 9 = SalesReturn;
            ### 11 = PurchaseOrder; 12 = SalesOrder

            self.GTotal_Calculation_Pur(keyid, self.parent.spnum, 'pp', fpf=self.fpf)
        
        
    def GTotal_Calculation_Sale(self, keyid, sp, pp, fpf="%0.2f", proflossval=None):
        totnetamt, amt, tax1amt, tax2amt, disamt, taxableamt, prolo  = [],[],[],[],[],[],[]
        totnetamtv, amtv, tax1amtv, tax2amtv, disamtv, taxableamtv, prolov = 0, 0, 0, 0, 0, 0, 0
        recdicfill = self.parent.recdic['grid'][keyid]
        if recdicfill['dgreturn']:
            recdicfill['totqty']=-recdicfill['totqty']
            recdicfill['netamt']=-float(recdicfill['netamt'])
            recdicfill['amt']=-recdicfill['amt']
            recdicfill['satamt']=-recdicfill['satamt']
            recdicfill['taxamt']=-recdicfill['taxamt']
            recdicfill['tax1amt']=-recdicfill['tax1amt']
            recdicfill['tax2amt']=-recdicfill['tax2amt']
            recdicfill['disamt']=-recdicfill['disamt']
            recdicfill['taxableamt']=-recdicfill['taxableamt']

        for k, v in self.parent.recdic['grid'].items():
            ###if v['qty'].isdigit():
            prolo.append(float(v['netamt'])-float(v['prate'])*float(v['qty']))
            ###else:
            ###    prolo.append(0)
            totnetamt.append(v['netamt'])
            amt.append(v['amt'])
            tax1amt.append(v['taxamt'])
            disamt.append(v['disamt'])
            taxableamt.append(v['taxableamt'])
        prolov = sum(prolo)
        
        totnetamtv, amtv, tax1amtv, disamtv, taxableamtv = sum(totnetamt), sum(amt), sum(tax1amt), sum(disamt), sum(taxableamt)
        tax2amtv = tax1amtv
        tottaxv = sum([tax1amtv, tax2amtv])
        finaltotal = round(totnetamtv)
        roundval = finaltotal-(totnetamtv)
        str(roundval).replace('-','')
        
        self.Fill_Total_Values(tax1amtv, tax2amtv, disamtv, amtv, taxableamtv, totnetamtv,
                     roundval, finaltotal, prolov, fpf=fpf)
        #Fill_Total_Values(self, tax1amtv, tax2amtv, disamtv, amtv, taxableamtv, totnetamtv,
        #             roundval, finaltotal, prolov, fpf=fpf)
    
    def GTotal_Calculation_Pur(self, keyid, sp, pp, fpf="%0.2f", proflossval=None):
        totnetamt, amt, tax1amt, tax2amt, disamt, taxableamt, prolo  = [],[],[],[],[],[],[]
        totnetamtv, amtv, tax1amtv, tax2amtv, disamtv, taxableamtv, prolov = 0, 0, 0, 0, 0, 0, 0

        for k, v in self.parent.recdic['grid'].items():
            totnetamt.append(v['netamt'])
            amt.append(v['amt'])
            #tax1amt.append(v['taxamt'])
            tax1amt.append(v['tax1amt'])
            disamt.append(v['disamt'])
            taxableamt.append(v['taxableamt'])
        totnetamtv, amtv, tax1amtv, disamtv, taxableamtv = sum(totnetamt), sum(amt), sum(tax1amt), sum(disamt), sum(taxableamt)
        tax2amtv = tax1amtv
        tottaxv = sum([tax1amtv, tax2amtv])
        finaltotal = round(totnetamtv)
        roundval = finaltotal-(totnetamtv)
        str(roundval).replace('-','')

        self.Fill_Total_Values(tax1amtv, tax2amtv, disamtv, amtv, taxableamtv, totnetamtv,
                     roundval, finaltotal, prolov, fpf=fpf)

    def GETTING_OTHER_VALUES(self):
        try:
            oth_1val = float(self.parent.other1_value.get())
        except ValueError :
            oth_1val = 0
        try:
            oth_2val = float(self.parent.other2_value.get())
        except ValueError:
            oth_2val = 0
        try:
            oth_3val = float(self.parent.other3_value.get())
        except ValueError:
            oth_3val = 0
        try:
            round_off = float(self.parent.round_off['text'])
        except ValueError:
            round_off = 0
        return oth_1val,oth_2val,oth_3val,round_off
    
    def Fill_Total_Values(self, totaltax1sum, totaltax2sum, totaldiscsum, subamtsum,
                      amtwithdisc, rawtotal, roundval, finaltotal, proflosssum, fpf="%0.2f", fillrecdic=True):
    
        #self.amount.SetValue(str(subamtsum))  # <<< on Amount total text Field NON VATABLE
        subamtsum = format(fpf % subamtsum)
        totaltax = sum([float(totaltax1sum), float(totaltax2sum)])
        totaltax = format(fpf % totaltax)
        totaltax1sum = format(fpf % totaltax1sum)
        totaltax2sum = format(fpf % totaltax2sum)
        totaldiscsum = format(fpf % totaldiscsum)
        amtwithdisc = format(fpf % amtwithdisc)
        roundval = format(fpf % roundval)
        self.parent.amount['text']=subamtsum  # <<< on Amount total text Field NON VATABLE
        self.parent.add_tax1['text']=totaltax
        self.parent.vat_amtx['text']=totaltax1sum
        self.parent.sat_amtx['text']=totaltax2sum
        self.parent.dis['text']=totaldiscsum
        self.parent.amtx['text']=amtwithdisc   # <<< THIS IS  VATABLE Amount
        
        oth_1val, oth_2val, oth_3val, round_off = self.GETTING_OTHER_VALUES()
        OthSum = sum([float(oth_1val), float(oth_2val), float(oth_3val)])
        BillTotal = sum([finaltotal, OthSum])
        num_word = 'N.A'
        try:
            num_word = num2word.to_card(int(float(BillTotal)))
        except OverflowError: ### must be less than 1000000000000.
            pass
        StatusDP(self.parent.sale_v_words, ('Rs:%s'%num_word),fg='blue')
        StatusDP(self.parent.status, ('Rs:%s'%num_word),fg='blue')
        
        ##self.parent.sale_v_words['text']=('Rs:%s'%num_word)
        BillTotal = format("%.2f" % float(BillTotal))
        self.parent.round_off['text']=(''.join([roundval, '  of [', str(rawtotal), ']']))
        self.parent.total_amtx['text']=BillTotal
        #### BillTotal #######################
        
        
        if proflosssum:
            if proflosssum < 0 :
                self.parent.pr_lo['fg']='red'
            else:
                self.parent.pr_lo['fg']='blue'
            proflosssum = format(fpf % proflosssum)
            self.parent.pr_lo['text']=str(proflosssum)
        else:
            proflosssum = '0'
            self.parent.pr_lo['text']=str(proflosssum)
        if fillrecdic:
            self.parent.recdic['pan']['tax1amt']=totaltax1sum
            self.parent.recdic['pan']['tax2amt']=totaltax2sum
            self.parent.recdic['pan']['ttaxamt']=totaltax
            self.parent.recdic['pan']['ttaxable']=amtwithdisc
            self.parent.recdic['pan']['tamt']=subamtsum
            self.parent.recdic['pan']['gtot']=BillTotal
            self.parent.recdic['pan']['pr_lo']=proflosssum
            #self.parent.recdic['pan']['static']['pr_lo']=proflosssum
            self.parent.recdic['pan']['tdisamt']=totaldiscsum
            self.parent.recdic['pan']['roundoff']=roundval
            self.parent.recdic['pan']['gtwords']=num_word
            
        return num_word

def AmountCal_WS(r, c, qty, totqty, bbv, rate, dis, tax1, tax2, nfstval, nsndval,
        grid=None, calcol=None, netedit=None, sp=1, sdc='1', mysoftval=1, fpf='%0.2f' ): 
    tax1_tax2 = sum([float(tax1), float(tax2)])
    dis_rate = sum([sum([100.0, -float(dis)])/100.0])
    gross_tax_rate = sum([sum([100.0, float(tax1_tax2)])/100.0])
    
    if bbv.isdigit():
        nrate = float(rate)
        amount = nrate*float(qty)
        
        try:
            if sdc == '2':
                if sp == 2: ### for retail sales only
                    net_rate = sum([sum([sum([nrate*float(qty)])/totqty]) * dis_rate])
                else:
                    net_rate = sum([sum([sum([nrate*float(qty)])/totqty]) * sum([dis_rate*gross_tax_rate])])
                      
            elif mysoftval == 11:
                if sp == 2: ### for retail sales only
                    net_rate = sum([sum([sum([nrate*float(qty)])/totqty]) * dis_rate])
                else:
                    net_rate = sum([sum([sum([nrate*float(qty)])/totqty]) * sum([dis_rate*gross_tax_rate])])                     
            else:
                net_rate = sum([sum([sum([nrate*float(qty)])/totqty]) * sum([dis_rate*gross_tax_rate])])
               
        except Exception as err: ### ZeroDivisionError
            if sdc == '2':
                net_rate = rate * dis_rate
            elif mysoftval == 11:
                net_rate = rate * dis_rate
            else:
                net_rate = sum([rate * dis_rate * gross_tax_rate])
        
    else: ### bonus given in net form 10+2, 10+1, 18+2 ..... etc.
        
        nrate = sum([sum([rate * nfstval])/sum([nfstval, nsndval])])
        amount = nrate*float(qty)

        if sdc == '2':
            net_rate = sum([sum([sum([rate * float(nfstval)])/sum(
            [float(nfstval),float(nsndval)])])*dis_rate])
        elif mysoftval == 11:
            net_rate = sum([sum([sum([rate * float(nfstval)])/sum(
            [float(nfstval),float(nsndval)])])*dis_rate])
        else:  
            net_rate = sum([sum([sum([rate * float(nfstval)])/sum(
            [float(nfstval),float(nsndval)])])*sum([dis_rate* gross_tax_rate])])
    
    dis_amt = sum([amount, - sum([sum([amount * sum([100.0, -dis])])/100.0])])
    tax1_amt = sum([sum([sum([amount, -dis_amt])* sum(
        [100.0, tax1])/100.0]) - sum([amount, -dis_amt])])  ### TAX1 ON DISCOUNTED AMOUNT
    tax2_amt = sum([sum([sum([amount, -dis_amt])* sum(
        [100.0, tax2])/100.0]) - sum([amount, -dis_amt])])  ### TAX2 ON DISCOUNTED AMOUNT
    
    return amount, dis_amt, tax1_amt, tax2_amt, net_rate

def GET_RETAIL_RATE_UNIT(pack, getrate=0, getqty='1', spliton='*', fpf="%0.2f"):
### <<<This function is using in spframe and open_csac scripts >>> ###
    ### calling from child class
    ##pack = recdicfill['pack'] 
    ##totqty = recdicfill['totqty']
    ###rate = recdicfill['rate']
    
    spack = pack.split(spliton)
    if spliton not in str(pack):          ## When * symbol not in Packing or except Tab,Cap item
        units = '1'  ## Must be String
    else :                              ## This is for Tab,Cap Items
        try:
            units = spack[2]
        except IndexError:
            units = spack[1]
    if units.isdigit():
        units = int(float(units))
    else:
        units = 1
    try:
        ###retailrate = format(float(getrate)/float(units), '0.2f')
        rrate = float(getrate)/float(units)
        retailrate = format(fpf % rrate)
    except:
        retailrate = 0
    if isinstance(getqty, (int, float)):
        retailqty = getqty
    else:
        if getqty.isdigit():
            retailqty = int(float(getqty))
        else:
            retailqty = 0
    retailqty = retailqty*units
    return retailrate, retailqty, units
