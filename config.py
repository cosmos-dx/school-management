#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import csv
import os, sys

class Configuration(object):
    'Handles the CVS functions for the config.csv object'
    def __init__(self, filename = 'config.csv'):
        
        filename = self._fPath(filename)
       
        if not os.path.isfile(filename):
            if __name__ != '__main__':
                    filename = self._fPath(filename)
            fpath = './resources/config.csv'
            dirpath = './resources'
            try:
                config_mydb()
            except IOError as e:
                os.makedirs(dirpath)
            #config_mydb()
            file = open(fpath, 'wb')
            pntdet = GetPrinterDetails().GetDetails()
            pport, ppntname = pntdet[0], pntdet[1]
            
            writer = csv.writer(file, dialect='excel')
            writer.writerow(['ID'] + ['Value'])
            
            writer.writerow(['FARE_MODE1'] + ['RIKSHAW']+[50]+[100]+[150]+[200])
            writer.writerow(['FARE_MODE2'] + ['AUTO']+[60]+[110]+[160]+[210])
            writer.writerow(['FARE_MODE3'] + ['BUS']+[100]+[150]+[200]+[250])
            writer.writerow(['LATE_FEE_DATE'] + [15])
            writer.writerow(['HALF_YEARLY_MONTH'] + [10])
            writer.writerow(['ANNUAL_MONTH'] + [3])
            writer.writerow(['MONTHLY_TEST'] + [30])
            writer.writerow(['HALF_YEARLY'] + [100])
            writer.writerow(['ANNUAL'] + [100])
            writer.writerow(['SESSION_START'] + [4])
            writer.writerow(['FEE_HEADINGS'] + ['Admission Fee']+ ['Tution Fee']+ ['Maintenance Fee']
                            +['Late Fee']+ ['Others']+ ['Basic Convenience']+ ['Examination Fee']
                            +['Additional Fee1']+['Additional Fee2'])
            writer.writerow(['MONTHS_HEAD'] + ['JAN']+ ['FEB']+ ['MAR']
                            +['APR']+ ['MAY']+ ['JUNE']+['JULY']+ ['AUG']
                            +['SEP']+['OCT']+ ['NOV']+ ['DEC']+['H-Yrly']+['Annual'])
            writer.writerow(['SUBJECTS_H'] + ['Hindi']+['English']+['Science']+['Maths']+['G.K']+
                            ['Hindi Oral']+['English Oral']+['Chemistry']+['Physics']+['Biology']+
                            ['Civics']+['History']+['Geography']+['Commerce']+['Sc.ACT.']+
                            ['Sports']+['Others']+['Atnds.'])
            writer.writerow(['SUBJECTS_L'] + ['Hindi']+['English']+['Science']+['Maths']+['G.K']+
                            ['Atnds.']+['Hindi Oral']+['English Oral']+['Chemistry']+['Physics']+['Biology']+
                            ['Civics']+['History']+['Geography']+['Commerce']+['Sc.ACT.']+
                            ['Sports']+['Others'])
            writer.writerow(['SUBJECTS_ROW_H'] + [18])
            writer.writerow(['SUBJECTS_ROW_L'] + [6])

            writer.writerow(['H_CLASS_FONT_SIZE'] + [7])
            writer.writerow(['L_CLASS_FONT_SIZE'] + [9])
            
            writer.writerow(['HEADER_MARGIN'] + [150])
            writer.writerow(['FOOTER_MARGIN'] + [10])
            writer.writerow(['LEFT_MARGIN'] + [4])
            writer.writerow(['RIGHT_MARGIN'] + [0])
            writer.writerow(['EXTEND_MARGIN'] + ['1'])
            writer.writerow(['SLOGAN'] + ['KEEP PRACTICING'])
            writer.writerow(['PRINT_PDF_C_O'] + ['2'])

            writer.writerow(['PRINTER_PORT'] + [pport])
            writer.writerow(['PRINTER_NAME'] + [ppntname])
            writer.writerow(['RGB TEXT'] + [255]+ [255]+ [200])
            writer.writerow(['RGB PANEL'] + [245]+ [255]+ [250])
            writer.writerow(['GRID_BACKGROUND_ALL'] + [173]+ [216]+ [230])
            writer.writerow(['GRID_BACKGROUND_MID'] + [200]+ [210]+ [190])
            writer.writerow(['GRID_CELL_TEXTCOLOUR'] + [150]+ [40]+ [50])
            writer.writerow(['LINUX_EXPORT_FILE'] + ['/home/'])
            file.close()
        
    #----------------------------------------------------------------------
    def _wOpen(self, filename = 'config.csv'):
        'Opens the file to be written to'
        if __name__ != '__main__':
            filename = self._fPath(filename)
        self.cFile = open(filename, 'wb')
    
    #----------------------------------------------------------------------
    def RGB_Colour(self, filename = 'config.csv'):
        'Opens the file to be read'
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        rgb_text,rgb_panel = '',''
        for row in reader:
            if row[0] == 'RGB TEXT':
                rgb_text = row[1],row[2],row[3]
            if row[0] == 'RGB PANEL':
                rgb_panel = row[1],row[2],row[3]
        return rgb_text,rgb_panel
    #----------------------------------------------------------------------
    def RGB_GRID_Colour(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        rgb_back_all,rgb_back_mid,rgb_grid_text = '','',''
        for row in reader:
            if row[0] == 'GRID_BACKGROUND_ALL':
                rgb_back_all = row[1],row[2],row[3]
            if row[0] == 'GRID_BACKGROUND_MID':
                rgb_back_mid = row[1],row[2],row[3]
            if row[0] == 'GRID_CELL_TEXTCOLOUR':
                rgb_grid_text = row[1],row[2],row[3]
        return rgb_back_all,rgb_back_mid,rgb_grid_text
    
    #----------------------------------------------------------------------
    def SLOGAN(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        slogan = ''
        for row in reader:
            if row[0] == 'SLOGAN':
                slogan = row[1]
        return slogan
    #----------------------------------------------------------------------
    def FARE_MODE1(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'FARE_MODE1':
                value = row[1],row[2],row[3],row[4],row[5]
        return value
    #----------------------------------------------------------------------
    def FARE_MODE2(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'FARE_MODE2':
                value = row[1],row[2],row[3],row[4],row[5]
        return value
    #----------------------------------------------------------------------
    def FARE_MODE3(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'FARE_MODE3':
                value = row[1],row[2],row[3],row[4],row[5]
        return value
    #----------------------------------------------------------------------
    def LATE_FEE_DATE(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'LATE_FEE_DATE':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def ANNUAL_HY_MONTH(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        hy_mnth = ''
        anl_mnth = ''
        for row in reader:
            if row[0] == 'HALF_YEARLY_MONTH':
                hy_mnth = row[1]
            if row[0] == 'ANNUAL_MONTH':
                anl_mnth = row[1]
        return hy_mnth, anl_mnth
    #----------------------------------------------------------------------
    def HEAD_MARGIN(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'HEADER_MARGIN':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def FOOT_MARGIN(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'FOOTER_MARGIN':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def LEFT_MARGIN(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'LEFT_MARGIN':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def RIGHT_MARGIN(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'RIGHT_MARGIN':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def EXTEND_MARGIN(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'EXTEND_MARGIN':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def SUBJECTS_HIGHER(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'SUBJECTS_H':
                value = row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18]
        return value
    #----------------------------------------------------------------------
    def SUBJECTS_LOWER(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'SUBJECTS_L':
                value = row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18]
        return value
    #----------------------------------------------------------------------
    def SUBJECTS_ROW_HIGHER(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'SUBJECTS_ROW_H':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def SUBJECTS_ROW_LOWER(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'SUBJECTS_ROW_L':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def HEIGHER_CLASS_FONT_SIZE(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'H_CLASS_FONT_SIZE':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def LOWER_CLASS_FONT_SIZE(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        value = ''
        for row in reader:
            if row[0] == 'L_CLASS_FONT_SIZE':
                value = row[1]
        return value
    #----------------------------------------------------------------------
    def OUTOFF_LIST(self, filename = 'config.csv'):
        'Opens the file to be read'
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        food,cst,vat,sat = '','','',''
        for row in reader:
            if row[0] == 'MONTHLY_TEST':
                month = row[1]
            if row[0] == 'HALF_YEARLY':
                halfy = row[1]
            if row[0] == 'ANNUAL':
                annual = row[1]
            
        return month,halfy,annual
    #----------------------------------------------------------------------
    def SESSION(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        session = ''
        for row in reader:
            if row[0] == 'SESSION_START':
                session = row[1]
        return session
    
    
    #----------------------------------------------------------------------
    def FEE_HEADINGS(self, filename= 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        feehead = ''
        for row in reader:
            if row[0] == 'FEE_HEADINGS':
                feehead = row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]
        return feehead
    #----------------------------------------------------------------------
    def MONTHS_HEAD(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        session = ''
        for row in reader:
            if row[0] == 'MONTHS_HEAD':
                session = row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]
        return session
    #----------------------------------------------------------------------
    def PRINT_PDF_STYLE(self, filename = 'config.csv'):
        'Opens the file to be read'
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        pdf_style = ''
        for row in reader:
            if row[0] == 'PRINT_PDF_C_O':
                pdf_style = row[1]
        return pdf_style
    #----------------------------------------------------------------------
    def EXPORT_PATH(self, filename = 'config.csv'):
        filename = self._fPath(filename)
        myf = open(filename, 'rt')
        reader = csv.reader(myf)
        PP_EXPORT = ''
        for row in reader:
            if row[0] == 'LINUX_EXPORT_FILE':
                PP_EXPORT = row[1]
        return PP_EXPORT 
    #----------------------------------------------------------------------
    def _fPath(self, filename = 'config.csv'):
        'This writes the correct filepath to the config.csv file'
        if hasattr(sys, 'frozen'):
            fullpath = os.path.abspath('./resources/config.csv')
            
        else:
            fullpath = os.path.split(__file__)[0]
            fullpath = os.path.join(fullpath, 'resources', filename)
            
        return fullpath
    
    #----------------------------------------------------------------------
    def _ReadConfig(self):
        'Reads the configuration values and returns them as a list'
        self._rOpen()
        reader = csv.reader(self.cFile, dialect='excel')
        config_table = []
        for row in reader:
            config_table.append(row[-1])
        return config_table
        cFile.close()
        
    # Return the language config
    #----------------------------------------------------------------------
    def cLanguage(self):
        'Returns the current language setting as a string'
        clist = self._ReadConfig()
        return clist[1]
            
    # Return the Currency symbol and decimal places
    #----------------------------------------------------------------------
    def cCurrency(self):
        'Returns the symbol and number of decimal places as a list.'
        clist = self._ReadConfig()
        rtn = clist[2:4]
        rtn[0] = unicode(rtn[0].decode('utf8'))
        return clist[2:4]
        
    # Return a Boolean value for the thousands separator
    #----------------------------------------------------------------------
    def ThousandsSep(self):
        'Returns a boolean value indicating if the user wants a thousands sep'
        clist=self._ReadConfig()
        if clist[4] == '1':
            return True
        else:
            return False
        
    # Return the information for the sales tax
    #----------------------------------------------------------------------
    def SalesTaxInfo(self):
        'Returns the toggle and rate for Sales Tax'
        clist=self._ReadConfig()
        # rslt = [toggle value, sales tax percent]
        rslt = [clist[5], clist[6]]
        return rslt
    
    # Return the language
    #----------------------------------------------------------------------
    def LangInfo(self):
        'Returns the selected language'
        clist = self._ReadConfig()
        return clist[1]
        
    # Return all configuration information
    #----------------------------------------------------------------------
    def ConfigSettings(self):
        'Returns all the current configuration information'
        clist = self._ReadConfig()
        return clist
    
    # Write new config settings to config.csv
    #----------------------------------------------------------------------
    def SetConfig(self, settings):
        '''Takes user choices from the prefs.py dlg and puts 
        them into the csv file'''
        if hasattr(sys, 'frozen'):
            path = os.path.abspath('./resources/config.csv')
        else:
            path = os.path.split(__file__)[0]
            path = os.path.join(path, 'resources', 'config.csv')
        file = open(path, 'wb')
        
        writer = csv.writer(file, dialect='excel')
        writer.writerow(['ID'] + ['Value'])
        writer.writerow(['Language'] + [settings[0]])
        writer.writerow(['Currency Sign'] + [settings[1]])
        writer.writerow(['Currency Decimal Points'] + [settings[2]])
        writer.writerow(['Toggle Thousands Sep'] + [settings[3]])
        writer.writerow(['Toggle Sales Tax'] + [settings[4]])
        writer.writerow(['Sales Tax'] + [settings[5]])
        file.close()
###########################################################################
import configparser as ConfigParser
class config_mydb(object):
    def __init__(self):
        
        filename = './resources/dbgatepass.cfg'
        filename2 = './resources/licence.ini'
        self.filename = filename
        self.filename2 = filename2
        config = ConfigParser.RawConfigParser()
        config2 = ConfigParser.RawConfigParser()
        self.config = config
        if not os.path.isfile(filename):
            self._FILE_WRITE_(config, filename)
            self._LICENCE_WRITE_(config2, filename2)
            if __name__ != '__main__':
                try:
                    self._FILE_WRITE_(config, filename)
                    self._LICENCE_WRITE_(config2, filename2)
                except:
                    pass
            else:
                try:
                    self._FILE_WRITE_(config, filename)
                    self._LICENCE_WRITE_(config2, filename2)
                except:
                    pass
    def _FILE_WRITE_(self, config, filename):
        config.add_section('DBD')
        config.set('DBD', 'HOST', 'localhost')
        config.set('DBD', 'DATABASE','school')
        config.set('DBD', 'USER','root')
        config.set('DBD', 'PASSWORD', 'pass')
        dirpath = './resources'
        try:
            with open(filename, 'wb') as configfile_me:
                config.write(configfile_me)
        except IOError as e:
            os.makedirs(dirpath)
    def _LICENCE_WRITE_(self, config2, filename2):
        import platform
        config2.add_section('licence')
        ur = platform.uname()[1]
        fw = (ur.encode('hex'))
        fw2 = ("_DemO_".encode('hex'))
        config2.set('licence', 'id', fw)
        config2.set('licence', 'key', fw2)
        dirpath = './resources'
        
        try:
            with open(filename2, 'wb') as configfile_me:
                config2.write(configfile_me)
        except IOError as e:
            os.makedirs(dirpath)    
    def READ_FILE_VALUE(self):
        #filen = (filename)
        config = self.config
        try:
            config.read(self.filename)
            host = config.get('DBD','HOST')
            mydb = config.get('DBD','DATABASE')
            user = config.get('DBD', 'USER')
            password = config.get('DBD','PASSWORD')
            er = None
        except ConfigParser.ParsingError as e:
            host, mydb, user, password = '','','',''
            er = e
        return host, mydb, user, password, er
    def READ_LICENCE(self):
        #filen = (filename)
        config = self.config
        try:
            config.read(self.filename2)
            value = config.get('licence','id')
            value2 = config.get('licence','key')
            
        except ConfigParser.ParsingError as e:
            value, value2 = '', ''
        return value, value2

###########################################################################
class GetPrinterDetails(object):
    def __init__(self):
        import platform
        if platform.system() == 'Windows':
            import win32printing as win32print
            printer_name = win32print.GetDefaultPrinter()
            val = win32print.EnumPrinters(win32print.PRINTER_ENUM_NAME, None, 2)
            #print printer_name
            pnt_list = []
            for v in range(len(val)):
                #print val
                if printer_name in str(val[v]):
                    #print val[v]['pPortName'],'  ==> Port Names'
                    #print val[v]['pDriverName'],'  ==> Driver Names'
                    #print val[v]['pPrinterName'],'  ==> Printer Names'
                    try:
                        port = val[v]['pPortName'].split(':')[0]
                    except IndexError:
                        port = 'LPT1'
                    pnt_list.append(val[v]['pPortName'])
                    pnt_list.append(val[v]['pPrinterName'])
                    
            if pnt_list != []:
                gpntlist = pnt_list
            else:
                gpntlist = ['USB001', 'myprinter']
        if platform.system() == 'Linux':
            gpntlist = ['USB001', 'myprinter']
        self.gpntlist = gpntlist
    def GetDetails(self):
        return self.gpntlist
#gpntlist = GetPrinterDetails().GetDetails()
#print gpntlist
#print GetPrinterDetails().GetDetails()[0]
###########################################################################

#USER = 'root'
#PASS = 'passs'
#HOST = 'localhost'
#MYDB = 'school'
#conf = config.Configuration()
#database = conf.DATABASE_()
#MYDB = database
#MYDB = Configuration().DATABASE_()
#USER = Configuration().USER()
#HOST = Configuration().HOST()
SQLVAL = config_mydb().READ_FILE_VALUE()
HOST = SQLVAL[0]
MYDB = SQLVAL[1]
USER = SQLVAL[2]
PASS = SQLVAL[3]
SQERROR = SQLVAL[4]
#print HOST, MYDB, USER,  PASS

def MyCursor():
    try:
        cnn = mysql.connector.connect(host=HOST,database=MYDB,user=USER,password=PASS)
        cursor=cnn.cursor()
        return cnn, cursor
    except mysql.connector.ProgrammingError as e:
        SQERROR = e
        return SQERROR
        #exit
###########################################################################
def Calender_Start():
    import time

    try:
        if int(time.localtime()[1]) < 4 :
            ttyy = str(int(time.localtime()[0])-1)
        else:
            ttyy = str(time.localtime()[0])
            month = "%02d" % int(Configuration().SESSION())
        todaytime =  str(ttyy)+'-'+str(month)+'-'+str('01')
    except:
        todaytime = str(time.localtime()[0])+'-04-01'
    return todaytime

###########################################################################
def MONTHS_HEADINGS():
    monthsval = Configuration().MONTHS_HEAD()
    mkey = {}
    for f in range(len(monthsval)):
        mkey[f+1]=str(monthsval[f])
    return mkey
def REVERSE_MONTHS_HEADINGS():
    monthsval = Configuration().MONTHS_HEAD()
    rvmkey = {}
    for f in range(len(monthsval)):
        rvmkey[str(monthsval[f])] = f+1
    return rvmkey
# Create object for testing            
#if __name__ == '__main__':
#    j = Configuration()
