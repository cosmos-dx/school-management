#!/usr/bin/python
# -*- coding: UTF-8 -*-
#

import config
from config import Calender_Start, MyCursor

###############################################################################
from class_query import Tables
class CREATE_DB(object):
    def __init__ (self, cnn, cursor):
        self.MYDB = "mschool"
        self.cal,self.cas,self.cla,self.empe,self.empg,self.ledg, self.own, self.sec, self.sht, self.stu, self.stug, self.tran = Tables()
        self.cnn, self.cursor = cnn, cursor
        self.DBCreate()
        self.DBPopulate()
    def DBPopulate(self):
        ownid = '1'
        own = 'MY SCHOOL'
        add1 = 'TEST ADD 1'
        add2 = 'TEST ADD 2'
        add3 = 'TEST ADD 3'
        phone = '9935188831'
        lic = 'abcd'
        tin = '12345678900'
        stat1 = 'Subject to DEORIA jurisdiction only on the'
        stat2 = 'assurance of the party that they have their'
        stat3 = 'LICENCE we are executing the indent '
        stat4 = '.'
        uid = '123'
        upass = '123'
        pport = 'LPT1'
        in_val = ownid,own, add1,add2,phone,lic,tin,stat1,stat2,stat3,stat4,uid,upass,pport
        prt = ('''INSERT INTO '''+self.own+''' (owner_det_id, pname, add1, add2, phone, licence, tin, 
        statutory1, statutory2, statutory3, statutory4, user_id, user_pass, pport) 
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''')
        self.cursor.execute(prt, in_val)
        self.cnn.commit()
        
        for r in range(12):
            val = r+1
            self.cursor.execute('''INSERT INTO '''+self.cla+''' (classID, fee0, fee1, fee2, fee3, fee4, fee5,fee6, fee7, fee8,fee9, fee10, fee11)
            VALUES('''+str(val)+''', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )''')
            self.cnn.commit()
        for r in range(4):
            val = r+50
            self.cursor.execute('''INSERT INTO '''+self.cla+''' (classID, fee0, fee1, fee2, fee3, fee4, fee5,fee6, fee7, fee8,fee9, fee10, fee11)
            VALUES('''+str(val)+''', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )''')
            self.cnn.commit()
        #todaytime = Calender_Start()
        self.cursor.execute('''INSERT INTO '''+self.cal+''' (fyear, year)
        VALUES(1, "'''+Calender_Start()+'''" )''')
        self.cnn.commit()
              
    def DBCreate(self):
            defd = '2000-01-01'
            defdtm = ''+defd+' 00:00:00'
        #try:
            #self.cursor.execute('''CREATE DATABASE  '''+self.MYDB+''' ''')
            #self.cnn.commit()
            self.cursor.execute('''
            CREATE TABLE `'''+self.stug+'''` (
            `sturegID` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `studentID` INT(11) NOT NULL DEFAULT '0',
            `ledgerID` INTEGER NOT NULL DEFAULT '0',
            `daytime` TIMESTAMP NOT NULL DEFAULT '',
            `fyear` SMALLINT(2) NOT NULL DEFAULT '0',
            `iddate` VARCHAR(20) NOT NULL DEFAULT '0')
            ;''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE UNIQUE INDEX `stugdateidx` ON '''+self.stug+''' (`iddate`);''')
            self.cnn.commit()
            self.cursor.execute('''
            CREATE INDEX `sturegindex` ON '''+self.stug+''' (`ledgerID`, `daytime`, `fyear`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            
            self.cursor.execute('''
            CREATE TABLE `'''+self.empg+'''` (
            `empregID` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `employeeID` INTEGER NOT NULL DEFAULT '0',
            `ledgerID` INTEGER NOT NULL DEFAULT '0',
            `ap` VARCHAR(1) NOT NULL DEFAULT 'A',
            `daytime` TIMESTAMP NOT NULL DEFAULT '',
            `fyear` SMALLINT(2) NOT NULL DEFAULT '0',
            `iddate` VARCHAR(20) NOT NULL DEFAULT '0' )
            ;''')
            self.cnn.commit()
            
            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE UNIQUE INDEX `empgdateidx` ON '''+self.empg+''' (`iddate`);''')
            self.cnn.commit()
            self.cursor.execute('''
            CREATE INDEX `empregindex` ON '''+self.empg+''' (`ledgerID`, `daytime`, `fyear`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            
            self.cursor.execute('''
            CREATE TABLE  `'''+self.cal+'''` (
            `fyear` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `year` DATE NOT NULL DEFAULT '' )
            ; ''')
            self.cnn.commit()

            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE INDEX `calenderindex` ON '''+self.cal+''' (`fyear`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            
            self.cursor.execute('''
                           CREATE TABLE `'''+self.cas+'''` (
            `cashID` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `transactionID` INT(11) NOT NULL DEFAULT '0',
            `ac_type` SMALLINT(2) NOT NULL DEFAULT '0',
            `debit` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `credit` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fyear` SMALLINT(2) NOT NULL DEFAULT '0' )
            ; ''')
            self.cnn.commit()

            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE INDEX `cashindex` ON '''+self.cas+''' (`transactionID`, `ac_type`, `fyear`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
           
            self.cursor.execute( '''
                            CREATE TABLE `'''+self.cla+'''` (
            `classID` SMALLINT(2) NOT NULL,
            `sectionID` SMALLINT(2) NOT NULL DEFAULT '0',
            `fee0` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee1` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee2` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee3` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee4` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee5` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee6` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee7` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee8` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee9` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee10` NUMERIC(8,2) NOT NULL DEFAULT '0.00',
            `fee11` NUMERIC(8,2) NOT NULL DEFAULT '0.00' 
             ) ; ''')
            self.cnn.commit()

            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE INDEX `classindex` ON '''+self.cla+''' (`classID`, `sectionID`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            
            self.cursor.execute( '''
                            CREATE TABLE `'''+self.empe+'''` (
            `employeeID` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `ledgerID` INT(11) NOT NULL DEFAULT '0',
            `designation` VARCHAR(25) NOT NULL DEFAULT 'T',
            `employee_name` VARCHAR(25) NOT NULL DEFAULT '',
            `guardian_name` VARCHAR(25) NOT NULL DEFAULT '',
            `add1` VARCHAR(25) NOT NULL DEFAULT '',
            `add2` VARCHAR(25) NOT NULL DEFAULT '',
            `email` VARCHAR(50) NOT NULL DEFAULT '',
            `phone` VARCHAR(11) NOT NULL DEFAULT '',
            `off_phone` VARCHAR(11) NOT NULL DEFAULT '',
            `status` TINYINT(1) NOT NULL DEFAULT '0' ,
            `conv_mode` TINYINT(2) NOT NULL DEFAULT '0' ,
            `conv_bool` TINYINT(1) NOT NULL DEFAULT '0' ,
            `distance` SMALLINT(3) NOT NULL DEFAULT '0',
            `dob` DATE NOT NULL DEFAULT '', 
            `doa` DATE NOT NULL DEFAULT '', 
            `dot` DATE NOT NULL DEFAULT '', 
            `comment` VARCHAR(30) NOT NULL DEFAULT '' )
            ;''')
            self.cnn.commit()

            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE INDEX `employeeindex` ON '''+self.empe+'''
            (`employeeID`, `ledgerID`, `employee_name`, `phone`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            
            self.cursor.execute( '''
                            CREATE TABLE `'''+self.ledg+'''` (
            `ledgerID` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `type` SMALLINT(2) NOT NULL DEFAULT '0' )
            ;''')
            self.cnn.commit()

            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE INDEX `ledgerindex` ON '''+self.ledg+''' (`ledgerID`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            
            self.cursor.execute( '''
                            CREATE TABLE `'''+self.own+'''` (
            `owner_det_id` SMALLINT(2) NOT NULL,
            `pname` VARCHAR(50) NOT NULL,
            `add1` VARCHAR(25) NOT NULL DEFAULT '',
            `add2` VARCHAR(25) NOT NULL DEFAULT '',
            `phone` VARCHAR(11) NOT NULL DEFAULT '',
            `licence` VARCHAR(25) NOT NULL DEFAULT '',
            `tin` VARCHAR(25) NOT NULL DEFAULT '',
            `user_id` VARCHAR(25) NOT NULL DEFAULT '',
            `user_pass` VARCHAR(25) NOT NULL DEFAULT '',
            `statutory1` VARCHAR(50) NOT NULL DEFAULT '',
            `statutory2` VARCHAR(50) NOT NULL DEFAULT '',
            `statutory3` VARCHAR(50) NOT NULL DEFAULT '',
            `statutory4` VARCHAR(50) NOT NULL DEFAULT '',
            `pport` VARCHAR(11) NOT NULL DEFAULT '' )
            ;''')
            self.cnn.commit()

            self.cursor.execute( '''
                            CREATE TABLE `'''+self.sec+'''` (
            `sectionID` INTEGER PRIMARY KEY AUTOINCREMENT,
            `section` VARCHAR(1) NOT NULL DEFAULT '' )
            ;''')
            self.cnn.commit()
            ### SHEET Table
            self.cursor.execute( '''
                              CREATE TABLE `'''+self.sht+'''` (
            `sheetID` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `ledgerIDstu` INT(11) NOT NULL DEFAULT '0',
            `ledgerIDemp` INT(11) NOT NULL DEFAULT '0',
            `classID` SMALLINT(2) NOT NULL DEFAULT '0',
            `category` SMALLINT(2) NOT NULL DEFAULT '0',
            `sheet_date` DATE NOT NULL DEFAULT '',
            `hindi` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `english` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `science` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `math` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `sstd` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `comp` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `bio` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `chem` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `phys` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `sans` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `civic` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `hist` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `geog` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `comm` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `sact` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `sport` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `other` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `attend` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fyear` SMALLINT(2) NOT NULL DEFAULT '0' )
            ; ''')

            self.cnn.commit()

            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE INDEX `sheetindex` ON '''+self.sht+''' (`sheetID`, `ledgerIDstu`, `ledgerIDemp`, `classID`,`fyear`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            
            self.cursor.execute( '''
                            CREATE TABLE `'''+self.stu+'''` (
            `studentID` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `ledgerID` INT(11) NOT NULL DEFAULT '0',
            `classID` SMALLINT(2) NOT NULL DEFAULT '0',
            `student_name` VARCHAR(25) NOT NULL DEFAULT '',
            `guardian_name` VARCHAR(25) NOT NULL DEFAULT '',
            `add1` VARCHAR(25) NOT NULL DEFAULT '',
            `add2` VARCHAR(25) NOT NULL DEFAULT '',
            `email` VARCHAR(50) NOT NULL DEFAULT '',
            `phone` VARCHAR(11) NOT NULL DEFAULT '',
            `section` VARCHAR(1) NOT NULL DEFAULT 'A',
            `off_phone` VARCHAR(11) NOT NULL DEFAULT '',
            `status` TINYINT(1) NOT NULL DEFAULT '0' ,
            `conv_mode` TINYINT(2) NOT NULL DEFAULT '0' ,
            `conv_bool` TINYINT(1) NOT NULL DEFAULT '0' ,
            `distance` SMALLINT(3) NOT NULL DEFAULT '0',
            `dob` DATE NOT NULL DEFAULT '', 
            `doa` DATE NOT NULL DEFAULT '', 
            `dot` DATE NOT NULL DEFAULT '', 
            `comment` VARCHAR(30) NOT NULL DEFAULT ' ' )
            ;''')
            self.cnn.commit()

            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE INDEX `studentindex` ON '''+self.stu+'''
            (`studentID`, `ledgerID`, `classID`, `student_name`, `phone`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            
            self.cursor.execute( '''
                                CREATE TABLE `'''+self.tran+'''` (
            `transactionID` INTEGER PRIMARY KEY AUTOINCREMENT ,
            `ledgerID` INT(11) NOT NULL DEFAULT '0',
            `classID` SMALLINT(2) NOT NULL DEFAULT '0',
            `fee0` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fee1` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fee2` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fee3` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fee4` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fee5` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fee6` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fee7` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `fee8` DECIMAL(8,2) NOT NULL DEFAULT '0.00',
            `date` DATE NOT NULL DEFAULT '', 
            `fyear` SMALLINT(2) NOT NULL DEFAULT '0' )
            ; ''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
            self.cursor.execute('''
            CREATE INDEX `transindx` ON `'''+self.tran+'''`
            (`ledgerID`, `fyear`);''')
            self.cnn.commit()
            ### CREATE INDEXING ###########
        #except :
       #     print 'Password Error From rmss_db_create.py line 417'
#if __name__ == '__main__':
#    DBCreate()
