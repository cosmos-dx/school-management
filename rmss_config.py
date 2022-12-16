#!/usr/bin/python
# -*- coding: UTF-8 -*-
#



import os
XLS_EXPORT_PATH = 'D:/win_rms/xlwt'
#from config import GetPrinterDetails
#pntdet = GetPrinterDetails().GetDetails()
pport, ppntname = 'USB001','Epson M200'##pntdet[0], pntdet[1]
PPORT = pport
#PPORT = 'test'

def linukchk_path():
    newPath = r'./rmsfiles'
    newPath_C_U_F = './rmsfiles/Rms_User_Files'
    newPath_C_BK = './rmsfiles/RMS_BACKUP'
    newPath_tools = './rmsfiles/tools'
    print_test_C = './rmsfiles/tools/print_test.txt'
    print_receipt_C = './rmsfiles/tools/print_receipt.txt'
    print_report_C = './rmsfiles/tools/print_report.txt'
    print_pdff_C = './rmsfiles/Rms_User_Files/Student_Fee_Receipt.pdf'
    if not os.path.exists(newPath):
        #os.makedirs(newPath)
        os.makedirs(newPath_C_U_F)
        os.makedirs(newPath_C_BK)
        os.makedirs(newPath_tools)
    open(print_test_C,'w')
    open(print_receipt_C,'w')
    open(print_report_C,'w')
    try:
        open(print_pdff_C,'w')
    except:
        pass
    print_tes = print_test_C
    print_rec = print_receipt_C
    print_rep = print_report_C
    print_pdf = print_pdff_C
    rmss_user_f = newPath_C_U_F
    rmss_backup = newPath_C_BK
    return print_tes,print_rec,print_rep,print_pdf,rmss_user_f,rmss_backup

def chk_path():
    drvPath_D = r'D:'
    newPath_C = r'C:\win_rms\tools'
    newPath_C_U_F = r'C:\win_rms\Rms_User_Files'
    newPath_D = r'D:\win_rms\tools'
    newPath_D_U_F = r'D:\win_rms\Rms_User_Files'
    newPath_C_BK = r'C:\win_rms\RMS_BACKUP'
    newPath_D_BK = r'D:\win_rms\RMS_BACKUP'
    #PPATH_BILL = 'D:/Rmss_Codes/print_receipt.txt'
    #PPATH_REPORT = 'D:/Rmss_Codes/print_report.txt'
    if  os.path.exists(drvPath_D):
        print_test_D = 'D:\\win_rms\\tools\\print_test.txt'
        print_receipt_D = 'D:\\win_rms\\tools\\print_receipt.txt'
        print_report_D = 'D:\\win_rms\\tools\\print_report.txt'
        print_pdff_D = 'D:\\win_rms\\Rms_User_Files\\Student_Fee_Receipt.pdf'
        if not os.path.exists(newPath_D):
            os.makedirs(newPath_D)
        if not os.path.exists(newPath_D_U_F):
            os.makedirs(newPath_D_U_F)
        if not os.path.exists(newPath_D_BK):
            os.makedirs(newPath_D_BK)
        open(print_test_D,'w')
        open(print_receipt_D,'w')
        open(print_report_D,'w')
        open(print_pdff_D,'w')
        print_tes = print_test_D
        print_rec = print_receipt_D
        print_rep = print_report_D
        print_pdf = print_pdff_D
        rmss_user_f = newPath_D_U_F
        rmss_backup = newPath_D_BK
    else:
        print_test_C = 'C:\\win_rms\\tools\\print_test.txt'
        print_receipt_C = 'C:\\win_rms\\tools\\print_receipt.txt'
        print_report_C = 'C:\\win_rms\\tools\\print_report.txt'
        print_pdff_C = 'C:\\win_rms\\Rms_User_Files\\Student_Fee_Receipt.pdf'
        if not os.path.exists(newPath_C):
            os.makedirs(newPath_C)
        if not os.path.exists(newPath_C_U_F):
            os.makedirs(newPath_C_U_F)
        if not os.path.exists(newPath_C_BK):
            os.makedirs(newPath_C_BK)
        open(print_test_C,'w')
        open(print_receipt_C,'w')
        open(print_report_C,'w')
        try:
            open(print_pdff_C,'w')
        except:
            pass
        print_tes = print_test_C
        print_rec = print_receipt_C
        print_rep = print_report_C
        print_pdf = print_pdff_C
        rmss_user_f = newPath_C_U_F
        rmss_backup = newPath_C_BK
    return print_tes,print_rec,print_rep,print_pdf,rmss_user_f,rmss_backup

import platform
if platform.system() == 'Linux':
    chk = linukchk_path()
else:
    chk = chk_path()
print_test,print_receipt,print_report,print_pdf,rmss_user_file,rmss_backup_path = chk[0],chk[1],chk[2],chk[3],chk[4],chk[5]
PPATH_BILL = print_receipt
PPATH_REPORT = print_report
PP_EXPORT = rmss_user_file
BACKUP_PATH = rmss_backup_path
PPATH_PDF = print_pdf

def OWNER_DETAILS():
    owner = "RMS DWMO SCHOOL"
    o_add1 = "RMS DEMO ADDRESS1, PART 1"
    o_add2 = "RMS DEMO ADDRESS2"
    pphone = "1234567890 , 9999999991"
    
    return owner, o_add1, o_add2, pphone

def kdwnf(self, LC, Kdwn, event): ###
    print ('rmss_config.py function = kdwnf line 122')
