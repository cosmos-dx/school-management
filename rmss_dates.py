#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.8 on Mon Mar  9 08:27:54 2015
#

import wx
import sys
import string
import MySQLdb
import mysql.connector
import _mysql_exceptions
import rmss_config
import wx.grid as gridlib
import wx.grid
from MyDateCtrl import *
from  datetime import datetime
import config
from config import MyCursor


def FYEAR_RETURN(self):
        try:
            fyear = self.date_partition.GetValue().strip()
            #fyear = int(fyear) - 1
            fyear = int(fyear) 
        except:
            fyear = '0'
        return fyear

bil_date = 0

def Combox_Val(self, val):
        str_type = {'Prep':'51','L.K.G':'52','U.K.G':'53','I':'1','II':'2','III':'3','IV':'4','V':'5',
                    'VI':'6','VII':'7','VIII':'8','IX':'9','X':'10','XI':'11','XII':'12'}
        key_val = str_type[val]
        return key_val
def Combox_Val_Reverse(re_val):
        str_type = {'51':'Prep','52':'L.K.G','53':'U.K.G','1':'I','2':'II','3':'III','4':'IV','5':'V',
                    '6':'VI','7':'VII','8':'VIII','9':'IX','10':'X','11':'XI','12':'XII'}
        key_val_reverse = str_type[re_val]
        return key_val_reverse

def date_frm(self):
    dfv = self.from_.GetValue()
    sdfv = self.from_.GetValue().split('/')
    dt_rng = str(self.date_range.GetValue()).split('-')
    dtr_fr = dt_rng[0] # From Date Range
    dtr_t = dt_rng[1]  # To Date Range UPTO PARTITIONS
    ############### # To Date Range split ######################
    dtr_t_ = str(dtr_t).split("/")                          # To Date Range split
    dtf_dd, dtf_m, dtf_y = dtr_t_[0],dtr_t_[1],dtr_t_[2]
    dtf_dd = 1
    dtf_dd = "%02d" % dtf_dd
    dtf_mm = int(dtf_m)+ 1
    dtf_mm = "%02d" % dtf_mm
    dtf_yy = dtf_y
    to_dt_rng = str(dtf_dd)+"/"+str(dtf_mm)+"/"+str(dtf_yy)
    dtr_to = datetime.strptime(str(to_dt_rng), "%d/%m/%Y")
    dfv_fv = datetime.strptime(str(dfv), "%d/%m/%Y")
    dtr_frm = datetime.strptime(str(dtr_fr), "%d/%m/%Y") # This is FROM DATE ALWAYS SMALLER VALUE
    dtcount = self.dhit_count
    #####################################
    try:
            fr_d, fr_m ,fr_y  = sdfv [0], sdfv[1], sdfv[2]
            if int(fr_d) > 31 :
                wx.MessageBox("from INVALID Day >> %s" % fr_d )
            elif int(fr_m) > 12 :
                wx.MessageBox("INVALID Month >> %s" % fr_m )
    except IndexError, e:
            wx.MessageBox("DATE ERROR line 27 >> %s" % e )
            self.from_.SetFocus()
    try:
        if dtr_to > dfv_fv :
            pass
        else:
            self.from_.SetFocus()
            wx.MessageBox("CHECK DATES of FINENCIAL YEAR")
            dtcount = dtcount + 1
            self.dhit_count = dtcount
            if int(dtcount) > 5:
                self.Freeze()
        if dfv_fv < dtr_frm :
            self.from_.SetFocus()
            wx.MessageBox("WORKING IN PREVIOUS FINENCIAL YEAR", " CHECK AGAIN !!", wx.ICON_HAND)
            dtcount = dtcount + 1
            self.dhit_count = dtcount
            if int(dtcount) > 5:
                self.Freeze()
        else:
            pass
    except ValueError, e:
        wx.MessageBox("DATE ERROR line 63 >> %s" % e )
        self.from_.SetFocus()
    return

def dates_frm(self):
    dfv = self.from_.GetValue()
    dtv = self.to_.GetValue()
    sdfv = self.from_.GetValue().split('/')
    sdtv = self.to_.GetValue().split('/') 
    try :
            fd = datetime.strptime(str(dfv), "%d/%m/%Y").strftime("%Y-%m-%d")
            fd1 = datetime.strptime(str(dtv), "%d/%m/%Y").strftime("%Y-%m-%d")
            if fd > fd1:
                wx.MessageBox("FROM DATE CAN NOT EXCEED\t\n\tfrom TO (today) DATE\t")
                self.from_.SetFocus()
    except ValueError, e:
            wx.MessageBox("DATE ERROR from line 88 >> %s" % e )
            self.from_.SetFocus()
            
    try:
            fr_d, fr_m ,fr_y  = sdfv [0], sdfv[1], sdfv[2]
            if int(fr_d) > 31 :
                wx.MessageBox("from INVALID Day >> %s" % fr_d )
            elif int(fr_m) > 12 :
                wx.MessageBox("INVALID Month >> %s" % fr_m )
    except IndexError, e:
            wx.MessageBox("DATE ERROR from line 98 >> %s" % e )
            self.from_.SetFocus()
    return
def dates_to(self):
    dfv = self.from_.GetValue()
    dtv = self.to_.GetValue()
    sdtv = self.to_.GetValue().split('/')
    try:
        to_d, to_m ,to_y  = sdtv[0], sdtv[1], sdtv[2]
        if to_d < 31 :
            wx.MessageBox("INVALID day >> %s" % to_d )
        elif to_m < 12 :
            wx.MessageBox("INVALID Month >> %s" % to_m )    
    except IndexError, e:
        wx.MessageBox("DATE ERROR to line 112 >> %s" % e )
        self.to_.SetFocus()
    try:
        fd = datetime.strptime(str(dfv), "%d/%m/%Y").strftime("%Y-%m-%d")
        fd1 = datetime.strptime(str(dtv), "%d/%m/%Y").strftime("%Y-%m-%d")
        if fd > fd1:
            wx.MessageBox("FROM DATE CAN NOT EXCEED\t\n\tfrom TO (today) DATE\t")
            self.to_.SetFocus()
    except ValueError, e:
        wx.MessageBox("DATE ERROR to line 121 >> %s" % e )
        self.to_.SetFocus()
    return

class StudentLC(wx.ListCtrl):
    '''
    For StudentLC
    '''
    def __init__(self, parent, *args, **kwargs):
        super(StudentLC, self).__init__(parent, *args, **kwargs)

        default = '','', '', '',''
        self.c0, self.c1, self.c2,self.c3, self.c4 = default
        self.InsertColumn(0, self.c0)
        self.SetColumnWidth(0, 0)
        self.InsertColumn(1, self.c1)
        self.SetColumnWidth(1, 150)
        self.InsertColumn(2, self.c2)
        self.SetColumnWidth(2, 80)
        self.InsertColumn(3, self.c3)
        self.SetColumnWidth(3, 90)
        self.InsertColumn(4, self.c4)
        self.SetColumnWidth(4, 0)
        sfont = wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.SetFont(sfont)
        self.SetBackgroundColour((200,180,300))
def Student_Data_Fill(self, getid, sval, key_val, section):
    self.snlc.DeleteAllItems()
    cnn, cursor = MyCursor()
    Act = '0' ## 0 for Active Students in School
    Out = '1' ## 1 for OUT Students in School
    if sval != '':
        cursor.execute(" SELECT "+getid+", student_name, guardian_name, add1, add2, phone, "
                       " off_phone, email, doa, dob, dot, comment "
                       " FROM student WHERE student_name LIKE '"+sval+"%' "
                       " AND classID = '"+key_val+"'  AND section = '"+section+"' AND status = '"+Act+"' ORDER BY student_name ASC LIMIT 100 " )
    else:
        cursor.execute(" SELECT "+getid+", student_name, guardian_name, add1, add2, phone, "
                       " off_phone, email, doa, dob, dot, comment "
                       " FROM student WHERE  classID = '"+key_val+"' AND section = '"+section+"' AND status = '"+Act+"' "
                       " ORDER BY student_name ASC LIMIT 100 " )
    std_r = cursor.fetchall()
    index = 0
    for r in  std_r:
        self.snlc.InsertStringItem(index, str(r[0]))
        self.snlc.SetStringItem(index, 0, str(r[0]))
        self.snlc.SetStringItem(index, 1, str(r[1]))
        self.snlc.SetStringItem(index, 2, str(r[2]))
        self.snlc.SetStringItem(index, 3, str(r[3]))
        self.snlc.SetStringItem(index, 4, str(r[5]))
    cnn.close()
    
def esc_key(self, event):
        key = event.GetKeyCode()
        if key in [wx.WXK_ESCAPE,wx.WXK_END]:
            result = wx.MessageBox(" Do YOu Want to / EXIT ?? ", "Confirm !! ", wx.YES_NO| wx.ICON_QUESTION)
            if result == wx.YES:
                self.GetParent().Close()
        event.Skip()
###########################################################################
"""
#def single_date(self):
ALPHA_ONLY = 1
DIGIT_ONLY = 2
FLOAT_ONLY = 0
ACC_ONLY = 3
class MyValidator(wx.PyValidator):
    def __init__(self, flag=None, pyVar=None):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)
    def Clone(self):
        return MyValidator(self.flag)

    def Validate(self, win):
        tc = self.GetWindow()
        val = tc.GetValue()
        input_val = 0
        acc_input = 3
        if self.flag == ALPHA_ONLY:
            for x in val:
                if x not in string.letters:
                    return False

        elif self.flag == DIGIT_ONLY:
            for x in val:
                if x not in string.digits:
                    return False
        
        elif self.flag == FLOAT_ONLY:
            for x in val:
                if x not in input_val:
                    return False
        elif self.flag == ACC_ONLY:
            for x in val:
                if x not in acc_input:
                    return False

        return True


    def OnChar(self, event):
        key = event.GetKeyCode()
        input_val = ".0123456789"
        acc_input = "-.0123456789"
        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if self.flag == ALPHA_ONLY and chr(key) in string.letters:
            event.Skip()
            return

        if self.flag == DIGIT_ONLY and chr(key) in string.digits:
            event.Skip()
            return
        if self.flag == FLOAT_ONLY and chr(key) in input_val:
            event.Skip()
            return
        if self.flag == ACC_ONLY and chr(key) in acc_input:
            event.Skip()
            return
        if not wx.Validator_IsSilent():
            wx.Bell()

        # Returning without calling even.Skip eats the event before it
        # gets to the text control
        return

"""