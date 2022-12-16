#!/usr/bin/python
# -*- coding: UTF-8 -*-


#import ctypes.util
#import uuid
import os, sys, stat

import rmss_config

from  datetime import datetime

from student_t_ac import student_teacher_ac
from rmss_register import rmss_register
from Master_Fee import FeeMaster
from Fee_receipt import FeeReceipt
from student_perf import StudentPerformance
from my_calendar import FYCalendar
from student_sheet_records import SheetRecords
from student_class_upgrade import Upgrade_Class
from student_fee_records_month import FeeRecordsMonth
from setting import Settings
from my_calculator import RMSCalculator
from user_login_setting import User_Login
from rmss_updates import RmssUpdates

def date_range_val(self,trg):
    val = self.select_date.GetValue()
    fyval = self.select_date_partition.GetValue()
    trg.panel.date_range.SetValue(str(val))
    trg.panel.date_partition.SetValue(str(fyval))
    return
def date_range_panel_val(self,trg):
    va = self.panel
    val = va.select_date.GetValue()
    fyval = va.select_date_partition.GetValue()
    trg.panel.date_range.SetValue(str(val))
    trg.panel.date_partition.SetValue(str(fyval))
    return
