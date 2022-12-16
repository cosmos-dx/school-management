# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Rambarun Komaljeet
# License: Freeware
# ---------------------------------------------------------------------------
import calendar
import time
#import re

from rmsvalidators import *

class RmsDatePicker(Toplevel):
    
    def __init__(self, widget=None, par=None, pclass=None, format_str=None):
        """
        :param widget: widget of parent instance.
        :param format_str: print format in which to display date.
        :type format_str: string
        Example::
            a = RmsDatePicker(self, widget=self.parent widget,
                             format_str='%02d-%s-%s')
        """

        #super().__init__()
        Toplevel.__init__(self)
        self.count = par.day #1
        self.display_month_days = []
        self.max_month_day = 0
        self.hltbg = 'yellow'
        self.bg = 'light blue'
        self.widget = widget
        self.str_format = format_str
        self.par = par 
        self.rscr = pclass.rscr ### pclass is actual parent class and another rscr is attribute
        self.title("RMS DatePicker")
        self.fontstr="['Courier New',"+str(self.rscr['sysfontnum'])+", 'bold']"
        self.font=['Courier New', self.rscr['sysfontnum'], 'bold']
        self.resizable(0, 0)
        #self.geometry("+630+390")
        #pwpos = widget.geometry().split('+')
        #self.entrytxt = par.txt
        #adj = sum([int(pwpos[2]), 70])
        #self.geometry("+%s+%s"%(pwpos[1], adj))
        self.entrytxt = par
        self.init_frames()
        self.init_needed_vars()
        self.init_month_year_labels()
        self.init_buttons()
        self.space_between_widgets()
        self.fill_days()
        self.make_calendar()
        
    def init_frames(self):
        self.frame1 = Frame(self)
        self.frame1.pack()

        self.frame_days = Frame(self)
        self.frame_days.pack()

    def init_needed_vars(self):
        self.month_names = tuple(calendar.month_name)
        self.month_num_name_dict = { v:'%02d'%i for i, v in enumerate(self.month_names)}
        self.day_names = tuple(calendar.day_abbr)
        self.year = time.strftime("%Y")
        self.month = time.strftime("%B")

    def init_month_year_labels(self):
        self.year_str_var = StringVar()
        self.month_str_var = StringVar()
        font = ['Courier New', str(self.rscr['sysfontnum']), 'bold']
        self.year_str_var.set(self.year)
        self.year_lbl = Label(self.frame1, textvariable=self.year_str_var,
                                 font=font)
        self.year_lbl.grid(row=0, column=5, padx=10)

        self.month_str_var.set(self.month)
        self.month_lbl = Label(self.frame1, textvariable=self.month_str_var,
                                  font=font)
        self.month_lbl.grid(row=0, column=1, padx=10)

    def init_buttons(self):
        self.left_yr = Button(self.frame1, text="←", width=5,font=self.font,
                        bg=self.bg, command=self.prev_year)
        self.left_yr.grid(row=0, column=4)

        self.right_yr = Button(self.frame1, text="→", width=5,font=self.font,
                        bg=self.bg, command=self.next_year)
        self.right_yr.grid(row=0, column=6)

        self.left_mon = Button(self.frame1, text="←", width=5,font=self.font,
                        bg=self.bg, command=self.prev_month)
        self.left_mon.grid(row=0, column=0)

        self.right_mon = Button(self.frame1, text="→", width=5,font=self.font,
                        bg=self.bg, command=self.next_month)
        self.right_mon.grid(row=0, column=2)

    def space_between_widgets(self):
        self.frame1.grid_columnconfigure(3, minsize=40)

    def prev_year(self):
        self.prev_yr = int(self.year_str_var.get()) - 1
        self.year_str_var.set(self.prev_yr)

        self.make_calendar()

    def next_year(self):
        self.next_yr = int(self.year_str_var.get()) + 1
        self.year_str_var.set(self.next_yr)

        self.make_calendar()

    def prev_month(self):
        index_current_month = self.month_names.index(self.month_str_var.get())
        index_prev_month = index_current_month - 1

        #  index 0 is empty string, use index 12 instead,
        # which is index of December.
        if index_prev_month == 0:
            self.month_str_var.set(self.month_names[12])
        else:
            self.month_str_var.set(self.month_names[index_current_month - 1])

        self.make_calendar()
        try:
            eval("self.btn_"+str(self.count))['bg']= self.bg
            eval("self.btn_"+str(self.max_month_day))['bg']= self.hltbg
            eval("self.btn_"+str(self.count))['relief']= 'raised'
            #seval("self.btn_"+str(self.max_month_day))['relief']= 'sunken'
            eval("self.btn_"+str(self.max_month_day)).focus()
        except:
            self.count = 1
            eval("self.btn_"+str(self.count))['bg']= self.hltbg
            eval("self.btn_"+str(self.count))['relief']= 'sunken'
            eval("self.btn_"+str(self.count)).focus()
            pass
    def next_month(self):
        index_current_month = self.month_names.index(self.month_str_var.get())

        try:
            self.month_str_var.set(self.month_names[index_current_month + 1])
        except IndexError:
            #  index 13 does not exist, use index 1 instead, which is January.
            self.month_str_var.set(self.month_names[1])
        
        self.make_calendar()
        try:
            eval("self.btn_"+str(self.count))['bg']= self.bg
            eval("self.btn_"+str(1))['bg']= self.hltbg
            eval("self.btn_"+str(self.count))['relief']= 'raised'
            #eval("self.btn_"+str(1))['relief']= 'sunken'
            eval("self.btn_"+str(1)).focus()
        except:
            pass
        
    def fill_days(self):
        col = 0
        ###Creates days label
        for day in self.day_names:
            if day == 'Sun':
                self.lbl_day = Label(self.frame_days, text=day, font=self.font, bg='orange')
            else:
                self.lbl_day = Label(self.frame_days, text=day, font=self.font, bg='white')
            self.lbl_day.grid(row=0, column=col, sticky='ewns')
            col += 1

    def make_calendar(self):
        #  Delete date buttons if already present.
        #  Each button must have its own instance attribute for this to work.
        #
        try:
            for dates in self.m_cal:
                for date in dates:
                    if date == 0:
                        continue                  
                    self.delete_buttons(date)
        except AttributeError:
            pass

        year = int(self.year_str_var.get())
        month = self.month_names.index(self.month_str_var.get())
        self.m_cal = calendar.monthcalendar(year, month)

        #  build dates buttons.
        self.display_month_days = [] ## Empty Previous month days
        for dates in self.m_cal:
            row = self.m_cal.index(dates) + 1
            for date in dates:
                col = dates.index(date)
                if date == 0:
                    continue
                self.make_button(str(date), str(row), str(col))
                self.display_month_days.append(date)
        self.max_month_day = max(self.display_month_days)
       
    def make_button(self, date, row, column):
        exec(
            "self.btn_" + date + " = Button(self.frame_days, text=" + date
            + ", width=5, bd=3, bg='"+self.bg+"', font="+self.fontstr+", command=self.mytest)\n"
            "self.btn_" + date + ".grid(row=" + row + " , column=" + column
            + ")\n")       
        self.bind('<Key>', self.mytest)
        self.bind('<Button-1>', self.button_date)
        self.bind('<Double-Button-1>', self.button_date_close)
        try:
            if self.max_month_day == 0:
                eval("self.btn_"+str(self.count)).focus()
                eval("self.btn_"+str(self.count))['bg']= self.hltbg
                eval("self.btn_"+str(self.count))['relief']= 'sunken'
        except:
            pass
       
    def RemoveDatePicker(self):
        self.frame1.pack_forget()
        self.frame_days.pack_forget()
        self.destroy()
        
    def mytest(self, clicked=None):
        try:
            if clicked.keysym == 'Escape':
                self.RemoveDatePicker()
                return
            
            if clicked.keysym == 'Right':
                if self.count < self.max_month_day:
                    eval("self.btn_"+str(self.count))['bg'] = self.bg
                    eval("self.btn_"+str(self.count))['relief']= 'raised'
                    self.count += 1
                else:
                    eval("self.btn_"+str(self.count))['bg'] = self.bg
                    eval("self.btn_"+str(self.count))['relief']= 'raised'
                    ### Sholud be empty before calling self.next_month()
                    self.next_month()
                    self.count = 1
                
            elif clicked.keysym == 'Left':
                if self.count > 1 :
                    eval("self.btn_"+str(self.count))['bg'] = self.bg
                    eval("self.btn_"+str(self.count))['relief']= 'raised'
                    self.count -= 1
                else:
                    self.prev_month()
                    eval("self.btn_"+str(1))['bg'] = self.bg
                    eval("self.btn_"+str(self.count))['relief']= 'raised'
                    self.count = self.max_month_day
            elif clicked.keysym == 'Down':
                if self.count < 1:
                    self.count = 1
                if self.count + 7 <= self.max_month_day:
                    eval("self.btn_"+str(self.count))['bg'] = self.bg
                    eval("self.btn_"+str(self.count))['relief']= 'raised'
                    self.count += 7
                    
                else:
                    self.next_month()
                    self.count = 7-(self.max_month_day-self.count)
                    eval("self.btn_"+str(1))['bg'] = self.bg
                    eval("self.btn_"+str(self.count))['relief']= 'raised'
            
                if self.count < 1:
                    self.count = 1
            elif clicked.keysym == 'Up':
                if self.count - 7 >= 0:
                #if self.count - 7 <= self.max_month_day:
                    eval("self.btn_"+str(self.count))['bg'] = self.bg
                    eval("self.btn_"+str(self.count))['relief']= 'raised'
                    self.count -= 7
                else:
                    self.prev_month()
                    self.count = (self.max_month_day-self.count)+1
                    eval("self.btn_"+str(self.max_month_day))['bg'] = self.bg
                    eval("self.btn_"+str(self.count))['relief']= 'raised'
                if self.count < 1:
                    self.count = self.max_month_day
            elif clicked.keysym == 'Return':
                clicked_button = clicked.widget
                year = self.year_str_var.get()
                month = self.month_str_var.get()
                date = clicked_button['text']
                try:
                    self.full_date = self.str_format % (date, self.month_num_name_dict[month], year)
                except:
                    date = 1
                    self.full_date = self.str_format % (date, self.month_num_name_dict[month], year)
                    
                #  Replace with parent 'widget' of your choice.
                try:
                    self.SetValue(self.widget, self.full_date)
                except AttributeError:
                    pass
                self.SetValue(self.entrytxt, self.full_date)
                self.RemoveDatePicker()
                return
            eval("self.btn_"+str(self.count)).focus()
            eval("self.btn_"+str(self.count))['bg'] = self.hltbg
            eval("self.btn_"+str(self.count))['relief']= 'sunken'
        except AttributeError:
            pass
            
    def delete_buttons(self, date):
        exec("self.btn_" + str(date) + ".destroy()")

    def SetValue(self, wdg, text, idx=0):
        wdg.delete(idx, 'end')
        wdg.insert(idx, text)
        
    def button_date(self, clicked=None): 
        clicked_button = clicked.widget
        year = self.year_str_var.get()
        month = self.month_str_var.get()
        date = clicked_button['text']
        try:
            self.full_date = self.str_format % (date, self.month_num_name_dict[month], year)
        except:
            date = 1
            self.full_date = self.str_format % (date, self.month_num_name_dict[month], year)
        self.SetValue(self.entrytxt, self.full_date)
        eval("self.btn_"+str(date)).focus()
        eval("self.btn_"+str(self.count))['bg'] = self.bg
        eval("self.btn_"+str(self.count))['relief']= 'raised'
            
        self.count = int(date)
        eval("self.btn_"+str(self.count))['bg'] = self.hltbg
        eval("self.btn_"+str(self.count))['relief']= 'sunken'
        #  Replace with parent 'widget' of your choice.
        
        try:
            self.SetValue(self.entrytxt, self.full_date)
        except Exception as err:
            self.RemoveDatePicker()
            
    def button_date_close(self, click=None):
        self.RemoveDatePicker()
        
class RmsDate(Entry):
    def __init__(self, parent, master, par, **kw):
        self.kw = kw
        try:
            entryparam = kw['kw'][1]['entryparam']
        except:
            entryparam = {'bd':3,'fg':'black', 'relief':'sunken'}
            entryparam.update(kw)
        self.parent = parent
        self.master = master
        self.par = par  ### <<< actual parent class
        
        self.dtformat = '%d/%m/%Y'
        self.eidx = 0
        lt = time.localtime(time.time())
        
        self.tdyear = lt.tm_year
        self.tdmonth = lt.tm_mon
        self.day = lt.tm_mday
        
        self.today = time.strftime(self.dtformat, lt)
        
        self.parent = parent
        self.var = StringVar(parent)
       
        self.year_str_var = StringVar()
        self.month_str_var = StringVar()
        self.month_names = tuple(calendar.month_name)
       
        self.maxday = self.GetMaxDay(self.tdyear, self.tdmonth)
        Entry.__init__(self, parent, textvariable=self.var, **entryparam)
        self.var.trace('w',  self.Varvalidate)
        self.bind('<Key>', self.KeyValidtion)
        self.bind('<FocusOut>', self.OnFOutKey)
        self.delete(0, "end")
        self.insert(0, self.today)
        #self.insert("end",'/07/2019')
        self.icursor(0)
        self.focus()
        
        
    def application(self):
        RmsDatePicker(self.master, par=self, pclass=self.par, format_str='%02d/%s/%s')

    def GetMaxDay(self, y, m):
        return max(max(calendar.monthcalendar(y, m)))

    def FirstDaySet(self):
        ltxt = len(self.get())
        if ltxt == 1:
            d = '%02d'%int(self.get())
            dt = ''.join([d, self.today[2:]])
            self.delete(0, "end")
            self.insert("end",dt)
            
    def OnFOutKey(self, event=None):
        try:
            d, m, y = self.get().split('/')
            mxd = self.GetMaxDay(int(y), int(m))
            if int(d) > mxd:
                cdate = '{0:02}/{1:02}/{2:04}'.format(int(mxd), int(m), int(y))
                self.ResetInsert(idx=0, nxtidx='end', inval=cdate)
        except Exception as err:
            self.ResetInsert(idx=0, nxtidx='end', inval=self.today)
            
    def KeyValidtion(self, event=None):
        if event.keysym in ['Return', 'Tab']:
            self.FirstDaySet()
        if event.keysym == 'BackSpace':
            v = self.get()
            cpos = self.index('insert')
            if cpos == 2:
                self.delete(0, 2)
                self.insert(0, str(''))
        if event.keysym == 'space':
            RmsDatePicker(self.parent, par=self, pclass=self.par, format_str='%02d/%s/%s')
        if event.keysym == 'Escape':
            self.par.OnClose()
            
    def YearSet(self):
        t = self.get()
        yt = t[8:10]
        try:
            v = int(yt)
            self.delete(8, 'end')
            self.insert(8, str(v))
        except:
            self.delete(8, 'end')
            self.insert(8, '')
            
    def MonthSet(self):
        t = self.get()
        ltxt = len(t)
        if ltxt > 2:
            try:
                v = int(t[3:5])
                st = t[3:5]
                if len(st)==1:
                    self.delete(3, 'end')
                    self.insert(3, str(st))
                    return True
    
                if v <= 12:
                    self.delete(3, 'end')
                    self.insert(3, ''.join(['%02d'%int(v), '/', str(self.tdyear)]))
                    return True
                else:
                    self.delete(3, 'end')
                    self.insert(3, '')
            except:
                self.delete(3, 'end')
                self.insert(3, '')
                return False
        return True

    def InValidatioin(self, val, idx=0, nxtidx=0, insertidx=0):
        try:
            int(val[idx:nxtidx])
            self.ResetInsert(idx=nxtidx, nxtidx=insertidx, inval='')
        except ValueError:
            self.ResetInsert(idx=idx, nxtidx=nxtidx, inval='')
           
    def MonthValidation(self, imv, idx=0, monthval=12):
        if imv > 12:
            self.ResetMonth(idx=idx, monthval=monthval)
            
    def ResetMonth(self, idx=0, monthval=12):
        self.delete(idx, 'end')
        #self.insert(idx, '{0:02}/{1:04}'.format(self.tdmonth, self.tdyear))
        self.insert(idx, '{0:02}/{1:04}'.format(monthval, self.tdyear))

    def ResetInsert(self, idx=0, nxtidx=0, inval=''):
        self.delete(idx, nxtidx)
        self.insert(idx, inval)
        
    def Varvalidate(self, *args):
        v = self.var.get()
        cpos = self.index('insert')
        if v[1:].startswith('/'):
            try:
                int(v[:1])
            except ValueError:
                self.ResetInsert(idx=0, nxtidx=1, inval='')
                return
        if v[0:1] == '/':
            pass
        else:
            try:
                dayval1 = int(v[0:1])
                dayval = int(v[0:2])
                if dayval == 0: #### Check and Remove Zero day entry
                    newdateval = ''.join(['01', v[3:]])
                    self.delete(0, 'end')
                    self.insert(0, newdateval)
                    self.icursor(1)
                    return
            except ValueError:
                self.ResetInsert(idx=0, nxtidx=1, inval='')
                return
        try:
            int(v[1:2])
        except ValueError:
            self.ResetInsert(idx=1, nxtidx=2, inval='')
            return
        
        if v.find('/') > 2:
            dv = v[:2]
            try:
                cdate = '{0:02}/{1:02}/{2:04}'.format(int(dv), self.tdmonth, self.tdyear)
                self.ResetInsert(idx=0, nxtidx='end', inval=cdate)
                self.icursor(1)
                if cpos == 2:
                   
                    if int(dv) > 30:
                        self.ResetInsert(idx=0, nxtidx=2, inval='31')
                        
                    self.icursor(3)
            except ValueError:
                self.ResetInsert(idx=0, nxtidx=2, inval='0')
        mv = v[3:5]

        try:
            fmv = v[3:4]
            if cpos == 4:
                self.InValidatioin(v, idx=3, nxtidx=4, insertidx=5)
                return
            if cpos == 5:
                self.InValidatioin(v, idx=4, nxtidx=5, insertidx=6)
                self.MonthValidation(int(mv), idx=3, monthval=self.tdmonth)
                self.icursor(11)
                return
                
            try:
                ifmv = int(fmv)
                if ifmv > 1:
                    self.ResetMonth(idx=3, monthval=ifmv)
                    mv = fmv
                else:
                    pass
            except ValueError:
                if fmv == '/':
                    pass
                else:
                    self.ResetInsert(idx=3, nxtidx=6, inval='')
                    
            self.MonthValidation(int(mv), idx=3)
                            
        except ValueError:
            pass
        if len(v) > 7:
            self.YearSet()
            return
        if len(v) <= 2:
            try:
                int(v)
                if len(v) == 2:
                    self.insert(2, '/')
            except ValueError:
                self.var.set('')
        mv = v[3:5]
        
        if len(mv) <= 2:
            self.MonthSet()

    def GetValue(self):
        return self.get()
    
    def SetValue(self, val):
        self.delete(0, 'end')
        self.insert('insert', val)
        
    def SetFocus(self):
        self.focus()
