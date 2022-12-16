#!/usr/bin/python
# -*- coding: UTF-8 -*-
#

import os, sys
import sqlite3
from  datetime import datetime
###########################################################################
def Calender_Start():
        import time
    
        try:
            if int(time.localtime()[1]) < 4 :
                ttyy = str(int(time.localtime()[0])-1)
            else:
                ttyy = str(time.localtime()[0])
            todaytime =  str(ttyy)+'-'+str(Configuration().SESSION())+'-'+str('01')
        except:
            todaytime = str(time.localtime()[0])+'-04-01'
        return todaytime

def Tables():
    cal,cas,cla,empe,empg = "calndr","cash","class","employee","empreg"
    ledg, own, sec, sht, stu, stug, tran = "ledg","owndt","sec","sheet","student","stureg","trans"
    return cal,cas,cla,empe,empg,ledg, own, sec, sht, stu, stug, tran

class DBTABLES(object):
    def __init__ (self):
        self.MYDB = "mschool"
        #cal,cas,cla,empe,empg = "`calender`","cash","`class`","employee","empreg"
        #led, own, sec, sht, stu, stug, tran = "`ledger`","owner_det","`section`","sheet","student","stureg","`transaction`"
        self.cal,self.cas,self.cla,self.empe,self.empg,self.ledg, self.own, self.sec, self.sht, self.stu, self.stug, self.tran = Tables()
        #cal,cas,cla,empe,empg,led, own, sec, sht, stu, stug, tran
        ####################################################################
        rmss_db_path = './resources/mdb/'
        filepath =  os.path.join(rmss_db_path, '%s.db'%self.MYDB)
        
        if os.path.exists(filepath):
            self.cnn = sqlite3.connect(filepath)
            self.cursor = self.cnn.cursor()
        else:
            if not os.path.exists(rmss_db_path):
                os.makedirs(rmss_db_path)
            filepath =  os.path.join(rmss_db_path, '%s.db'%self.MYDB)
           
            self.cnn = sqlite3.connect(filepath)
            self.cursor = self.cnn.cursor()
            from rmss_db_create import CREATE_DB
            CREATE_DB(self.cnn, self.cursor)
##############################################################################
class DB_CAL_QUERIES(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
    def Open_Cnn(self):
        self.cursor = self.cursor
        self.cnn = self.cnn
        
    def Close_Cnn(self):
        self.cnn.close()
        return
##############################################################################
class STU_INFO(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)

    def Stu(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, text, fyear, section, key, Act, Out  = textlist
        qry = (" SELECT ledgerID, student_name, guardian_name, add1, add2, phone, section,"
           " off_phone, email, doa, dob, dot, comment, conv_mode, distance, conv_bool, studentID "
           " FROM "+self.stu+" WHERE classID = '"+str(key)+"' AND status = '"+Act+"' "
           " AND student_name LIKE '"+text+"%' AND section = '"+section+"' "
           " ORDER BY student_name ASC LIMIT "+str(varlimt)+","+str(staticlimit)+" " )
        self.cursor.execute(qry)
        drow={i:{'idx':i, 'lid':r[0],'name':r[1],'gname':r[2],'add1':r[3],'add2':r[4],
            'phone':r[5],'section':r[6],'office':r[7],'email':r[8],'doa':r[9],
            'dob':r[10],'dot':r[11],'cmnt':r[12],'convm':r[13],'distance':r[14],
            'convb':r[15],'esid':r[16],} for i,r in enumerate(self.cursor.fetchall())}
        return drow

    def Student_Data_Fill(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, text, fyear, getid, sval, key_val, section, Act  = textlist
        ##Act = '0' ## 0 for Active Students in School
        ##Out = '1' ## 1 for OUT Students in School
        if sval != '':
            self.cursor.execute(" SELECT "+getid+", student_name, guardian_name, add1, add2, phone, "
               " section, off_phone, email, doa, dob, dot, comment, 0, 0, 0, studentID, 0 "
               " FROM "+self.stu+" WHERE student_name LIKE '"+sval+"%' "
               " AND classID = '"+key_val+"'  AND section = '"+section+"' AND "
               " status = '"+Act+"' ORDER BY student_name ASC LIMIT "+str(varlimt)+","+str(staticlimit)+" " )
        else:
            self.cursor.execute(" SELECT "+getid+", student_name, guardian_name, add1, add2, phone, "
               " section, off_phone, email, doa, dob, dot, comment, 0, 0, 0, studentID, 0 "
               " FROM "+self.stu+" WHERE  classID = '"+key_val+"' AND section = '"+section+"' AND status = '"+Act+"' "
               " ORDER BY student_name ASC LIMIT "+str(varlimt)+","+str(staticlimit)+" " )
        
        drow={i:{'idx':i, 'lid':r[0],'name':r[1],'gname':r[2],'add1':r[3],'add2':r[4],
            'phone':r[5],'section':r[6],'office':r[7],'email':r[8],'doa':r[9],
            'dob':r[10],'dot':r[11],'cmnt':r[12],'convm':r[13],'distance':r[14],
            'convb':r[15],'esid':r[16],} for i,r in enumerate(self.cursor.fetchall())}
        return drow

    def Student_Data_Fill_UG(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, text, fyear, getid, sval, key_val, section, Act  = textlist
        ##Act = '0' ## 0 for Active Students in School
        ##Out = '1' ## 1 for OUT Students in School
        
        self.cursor.execute(" SELECT studentID, student_name, guardian_name, add1, add2, phone, "
               " section, off_phone, email, doa, dob, dot, comment, 0, 0, 0, studentID, 0 "
               " FROM "+self.stu+" WHERE  classID = '"+key_val+"' "
               " ORDER BY student_name ASC LIMIT "+str(varlimt)+","+str(staticlimit)+" " )
        
        drow={i:{'idx':i, 'lid':r[0],'name':r[1],'gname':r[2],'add1':r[3],'add2':r[4],
            'phone':r[5],'section':r[6],'office':r[7],'email':r[8],'doa':r[9],
            'dob':r[10],'dot':r[11],'cmnt':r[12],'convm':r[13],'distance':r[14],
            'convb':r[15],'esid':r[0],} for i,r in enumerate(self.cursor.fetchall())}
        return drow

    def Student_Data_Fill_old(self, lc, getid, sval, key_val, section, Act, ):
        lc.DeleteAllItems()
        ##Act = '0' ## 0 for Active Students in School
        ##Out = '1' ## 1 for OUT Students in School
        if sval != '':
            self.cursor.execute(" SELECT "+getid+", student_name, guardian_name, add1, add2, phone, "
               " off_phone, email, doa, dob, dot, comment "
               " FROM "+self.stu+" WHERE student_name LIKE '"+sval+"%' "
               " AND classID = '"+key_val+"'  AND section = '"+section+"' AND "
               " status = '"+Act+"' ORDER BY student_name ASC LIMIT 100 " )
        else:
            self.cursor.execute(" SELECT "+getid+", student_name, guardian_name, add1, add2, phone, "
               " off_phone, email, doa, dob, dot, comment "
               " FROM "+self.stu+" WHERE  classID = '"+key_val+"' AND section = '"+section+"' AND status = '"+Act+"' "
               " ORDER BY student_name ASC LIMIT 100 " )
        
        rows = self.cursor.fetchall()
        #rows = [(2, u'SUNIL GUPTA', u'DGFDGDFG FG', u'DFG DFGDFG', u'DFGGHGF ', u'44444444444', u'44444444444', u'rsfgdf', u'2017-11-29', u'2017-11-29', u'', u'SDFSF'),
        #     (1, u'TEST STUDENT1', u'TEST FATHER1', u'TEST ADD1', u'TEST ADD1', u'11111111111', u'22222222222', u'ssd', u'2017-11-29', u'2017-11-29', u'', u'DSFSDF'),
        #        (2, u'SUNIL GUPTA', u'DGFDGDFG FG', u'DFG DFGDFG', u'DFGGHGF ', u'44444444444', u'44444444444', u'rsfgdf', u'2017-11-29', u'2017-11-29', u'', u'SDFSF'),
        #     (1, u'TEST STUDENT1', u'TEST FATHER1', u'TEST ADD1', u'TEST ADD1', u'11111111111', u'22222222222', u'ssd', u'2017-11-29', u'2017-11-29', u'', u'DSFSDF')]
        for i in range(0, len(rows)):
            lc.InsertStringItem(i, str(rows[i][0]))
            lc.SetStringItem(i, 0, str(rows[i][0]))
            lc.SetStringItem(i, 1, str(rows[i][1]))
            lc.SetStringItem(i, 2, str(rows[i][2]))
            lc.SetStringItem(i, 3, str(rows[i][3]))
            lc.SetStringItem(i, 4, str(rows[i][5]))
            
    def IdSearch(self, stid):
        qry = (" SELECT ledgerID, student_name, guardian_name, add1, add2, phone, "
               " off_phone, email, doa, dob, dot, comment, conv_mode, distance, conv_bool, studentID "
               " FROM "+self.stu+" WHERE ledgerID = '"+stid+"'  " )
        self.cursor.execute(qry)
        row = self.cursor.fetchone()
        return row

    def StudentIDSearch(self, stid):
        qry = (" SELECT studentID, student_name, guardian_name, add1, add2, phone,section, "
               " off_phone, email, doa, dob, dot, comment, ledgerID "
               " FROM "+self.stu+" WHERE studentID = '"+stid+"'  ")
        
        self.cursor.execute(qry)
        row = self.cursor.fetchone()
        return row
    def StudentSec_Search(self, stid, section):
        self.cursor.execute(" SELECT studentID, student_name, guardian_name, add1, add2, phone "
               " off_phone, email, doa, dob, dot, comment, ledgerID "
               " FROM "+self.stu+" WHERE studentID = '"+stid+"' AND section = '"+section+"'  " )
        row = self.cursor.fetchone()
        return row
    def TOTAL_STUDENT_QUERY(self, value, section, Act):
        ##Act = '0' ## 0 for Active Students in School
        ##Out = '1' ## 1 for OUT Students in School
        self.cursor.execute(" SELECT ledgerID, student_name, guardian_name FROM "+self.stu+" "
         " WHERE classid = '"+(value)+"' AND student.section = '"+section+"' AND status = '"+Act+"' ")  ### Student Status  0 = Active Student ; 1 = Out students
        stidrows = self.cursor.fetchall()
        return stidrows, len(stidrows)

    def StudentUpgradeALL(self,classid,key_val):
        self.cursor.execute("UPDATE student SET classID = %s WHERE classID = %s "%(classid,key_val))
        self.cnn.commit()

    def StudentUpgradeOneByOne(self,classid,key_val,stid):
        self.cursor.execute("UPDATE student SET classID = %s WHERE classID = %s AND studentID = %s "%(classid,key_val,stid))
        self.cnn.commit()
        
#############################################################################
class EMP_INFO(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
        
    def Emp(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, text, self.fyear, des = textlist
        qry = (" SELECT ledgerID, employee_name, guardian_name, add1, add2, phone, designation, "
           " off_phone, email, doa, dob, dot, comment, conv_mode, distance, conv_bool, employeeID "
           " FROM "+self.empe+" WHERE employee_name LIKE '"+text+"%' AND designation = '"+des+"' "
           " ORDER BY employee_name ASC LIMIT "+str(varlimt)+","+str(staticlimit)+" " )
       
        self.cursor.execute(qry)
        drow={i:{'idx':i, 'lid':r[0],'name':r[1],'gname':r[2],'add1':r[3],'add2':r[4],
            'phone':r[5],'section':r[6],'office':r[7],'email':r[8],'doa':r[9],
            'dob':r[10],'dot':r[11],'cmnt':r[12],'convm':r[13],'distance':r[14],
            'convb':r[15],'esid':r[16],} for i,r in enumerate(self.cursor.fetchall())}
        return drow
    def TeacherSearch(self, tcid):
        self.cursor.execute(" SELECT employeeID, employee_name, guardian_name, add1, add2, phone, "
               " off_phone, email, doa, dob, dot, comment, ledgerID "
               " FROM employee WHERE employeeID = '"+tcid+"'  " )
        row = self.cursor.fetchone()
        return row
#############################################################################
class CLASS_SELECT(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
    def Select(self, key):
        self.cursor.execute(" SELECT sectionID, fee0, fee1, fee2, fee3, fee4, fee5, fee6, fee7, fee8, fee9,"
                               " fee10, fee11 FROM "+self.cla+" WHERE classID = '"+key+"' " )
        return self.cursor.fetchone()

    def Update(self, args):
        query = ("UPDATE "+self.cla+" SET fee0 = ?, fee1 = ?, fee2 = ?, fee3 = ?, fee4 = ?, "
                " fee5 = ?, fee6 = ?, fee7 = ?, fee8 = ? WHERE classID = ? ")
        self.cursor.execute(query, args)
        self.cnn.commit()
        
#############################################################################
class FEERECEIPT(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
    def Rnum(self, actype):
        self.cursor.execute(" SELECT cashID FROM "+self.cas+" WHERE ac_type = '"+actype+"' ORDER BY  cashID DESC LIMIT 1 " )
        row = self.cursor.fetchone()
        return row
    def CheckTransFee(self, fyear, ledid, fdd, tdd):
        self.cursor.execute(" SELECT transactionID FROM "+self.tran+" WHERE fyear = '"+str(fyear)+"' AND ledgerID = '"+ledid+"' "
                       " AND (date BETWEEN '"+fdd+"' AND '"+tdd+"' )  " )
        rows = self.cursor.fetchone()
        return rows
    def OnFeeEdit(self, stid, fdate, tdate):
        self.cursor.execute(" SELECT classID, fee0, fee1,fee2,fee3,fee4,fee5,fee6,fee7,fee8,date,transactionID "
                       " FROM "+self.tran+" WHERE ledgerID = '"+stid+"' AND date BETWEEN '"+fdate+"' AND '"+tdate+"' " )
        row = self.cursor.fetchone()
        return row
    def FeeInsert(self, args, deb, fyear):
        query = ('''INSERT INTO '''+self.tran+''' (ledgerID, classID, fee0, fee1, fee2, fee3, fee4,fee5, fee6, fee7, fee8, date, fyear)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?)''' )
        self.cursor.execute(query, args)
        trans_id =  self.cursor.lastrowid
        self.cnn.commit()
        cashq = ('''INSERT INTO '''+self.cas+''' (transactionID, debit, fyear) VALUES (?, ?, ?)''')
        cash_args = trans_id, deb, fyear
        
        self.cursor.execute(cashq, cash_args)
        self.cnn.commit()
    def FeeUpdate(self, deb, upargs, trans_upid, ):
        query = ("UPDATE "+self.tran+" SET classID = ?, fee0 = ?, fee1 = ?, fee2 = ?, fee3 = ?, fee4 = ?, "
                " fee5 = ?, fee6 = ?, fee7 = ?, fee8 = ?, date = ? WHERE transactionID = ? ")
        self.cursor.execute(query, upargs)
        self.cnn.commit()
        cashq = ('''UPDATE '''+self.cas+''' SET debit = ? WHERE transactionID = ? ''')
        cash_args = deb, trans_upid
        self.cursor.execute(cashq , cash_args)
        self.cnn.commit()
    def ALL_STUDENT_FEE_REC (self, key_val, section, fyear):
        format = '%d/%m/%Y'
        self.cursor.execute(" SELECT trn.ledgerID,trn.transactionID,"
       " trn.date,  stu.student_name, "
       " trn.fee0,  "
       " trn.fee1,   "
       " trn.fee2,   "
       " trn.fee3,   "
       " trn.fee4,   "
       " trn.fee5,   "
       " trn.fee6,   "
       " trn.fee7,   "
       " trn.fee8    "
       " FROM "+self.stu+" as stu LEFT JOIN "+self.tran+" as trn ON stu.ledgerID = trn.ledgerID "
       " WHERE stu.classID = '"+key_val+"' AND stu.section = '"+section+"' AND trn.fyear = '"+str(fyear)+"'  "
       " ORDER BY trn.date DESC " )
        rows = self.cursor.fetchall()
        return rows

    def INDIVIDUAL_STUDENT_FEE_REC (self, frm, tod, key_val, section, fyear, ledgerid):
        format = '%d/%m/%Y'
        self.cursor.execute(" SELECT trn.ledgerID, trn.transactionID,"
        " trn.date, stu.student_name, "
        " trn.fee0,  "
        " trn.fee1,   "
        " trn.fee2,   "
        " trn.fee3,   "
        " trn.fee4,   "
        " trn.fee5,   "
        " trn.fee6,   "
        " trn.fee7,   "
        " trn.fee8    "
        " FROM "+self.stu+" as stu LEFT JOIN "+self.tran+" as trn ON stu.ledgerID = trn.ledgerID "
        " LEFT JOIN "+self.cla+" as cla ON stu.classID = cla.classID "
        " WHERE stu.classID = '"+key_val+"' AND stu.section = '"+section+"' AND trn.fyear = '"+str(fyear)+"' "
        " AND (trn.date BETWEEN '"+frm+"' AND '"+tod+"' ) AND trn.ledgerID = '"+ledgerid+"' "
        " ORDER BY trn.date DESC " )
        rows = self.cursor.fetchall()
        return rows

    ###def NEW_STUDENT_RECORDS_FETCH(self, key_val, section, frm, tod, fyear):
    def NEW_STUDENT_RECORDS_FETCH(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, key_val, section, studname, fyear, studentID = textlist
        if studentID:
            stid = ''.join(["AND studentID = ", str(studentID)]) 
            stuid = ''.join(["AND stu.studentID = ", str(studentID)])
        else:
            stid = ""
            stuid = ""
        format = '%d/%m/%Y'
        self.cursor.execute(" SELECT ledgerID, '0', 'N.A', student_name, "
            " '0','0','0','0','0','0','0','0','0' "
            " FROM "+self.stu+" WHERE classID = '"+str(key_val)+"' "+stid+" " )
        srows = self.cursor.fetchall()
        studic = {}
        stu_list = []
        for r in srows:
            studic[r[0]]= (r[0],r[1],r[2],r[3],'0','0','0','0','0','0','0','0','0','0')
            stu_list.append(r[0])

        qry=(" SELECT trn.ledgerID, trn.transactionID,"
        " strftime('%d/%m/%Y', trn.date) as rdate,  stu.student_name, "
        " trn.fee0,  "
        " trn.fee1,  "
        " trn.fee2,  "
        " trn.fee3,  "
        " trn.fee4,  "
        " trn.fee5,  "
        " trn.fee6,  "
        " trn.fee7,  "
        " trn.fee8,  "
        " SUM(trn.fee0+trn.fee1+trn.fee2+trn.fee3+trn.fee4+trn.fee5+trn.fee6+trn.fee7+trn.fee8) as tsum "  
        " FROM "+self.stu+" as stu LEFT JOIN "+self.tran+" as trn ON stu.ledgerID = trn.ledgerID "
        " LEFT JOIN "+self.cla+" as cla ON stu.classID = cla.classID "
        " WHERE stu.classID = '"+str(key_val)+"' AND stu.section = '"+section+"' "+stuid+" AND (trn.date BETWEEN '"+frm+"' AND '"+tod+"' ) "
        " AND trn.fyear = '"+str(fyear)+"'  " )
        
        self.cursor.execute(qry)
        trows = self.cursor.fetchall()
            
        tr_list = []
        for t in trows:
            tr_list.append(t[0])
        pdval = [x for x in stu_list if x not in tr_list]
        for p in pdval:
            trows.append(studic[p])

        drow={i:{'idx':i, 'lid':r[0],'transid':r[1],'rdate':r[2],'name':r[3],'afee':r[4],
            'tfee':r[5],'mfee':r[6],'lfee':r[7],'ofee':r[8],'cfee':r[9],'efee':r[10],'add1':r[11],
            'add2':r[12],'total':r[13],} for i,r in enumerate(trows)}
        return drow

    def FRChk(self, transid, fdate, tdate):
        self.cursor.execute(" SELECT tr.classID, tr.fee0, tr.fee1,tr.fee2, "
           " tr.fee3,tr.fee4,tr.fee5,tr.fee6,tr.fee7,tr.fee8,tr.date, "
           " st.student_name, st.guardian_name ,st.add1, st.add2, st.phone "
           " FROM "+self.tran+" as tr LEFT JOIN student as st ON tr.ledgerID = st.ledgerID "
           " WHERE tr.transactionID = '"+transid+"' AND tr.date BETWEEN '"+fdate+"' AND '"+tdate+"' " )
        rows = self.cursor.fetchall()
        return rows
    def FEE_RECEIVED_COUNT(self, value, section, frm, tod, fyear):
        self.cursor.execute(" SELECT trn.ledgerID "
         " FROM "+self.tran+" as trn LEFT JOIN "+self.stu+" as stu ON stu.ledgerID = trn.ledgerID "
         " WHERE trn.classID = '"+str(value)+"' AND "
         "(trn.date BETWEEN '"+frm+"' AND '"+tod+"' ) AND trn.fyear = '"+str(fyear)+"' AND stu.section = '"+section+"' " )
        paidrows = self.cursor.fetchall()
        return paidrows, len(paidrows)
#############################################################################
class AC_INS_UPD(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
    def Stu_Insert(self, actype, fval):
        self.cursor.execute('''INSERT INTO '''+self.ledg+''' (type) VALUES ('''+str(actype)+''')''')
        self.cnn.commit()
        led_id = self.cursor.lastrowid
       
        key_val, name, ftn, add1, add2, phone, section, off, email, doa, dob, cmnt, conv, conv_dist, conv_b = fval
        in_val = led_id, key_val, name, ftn, add1, add2, phone, section, off, email, doa, dob, cmnt, conv, conv_dist, conv_b
        query = ('''INSERT INTO '''+self.stu+''' (ledgerID, classID, student_name, guardian_name, add1, add2, phone, section,
                 off_phone, email, doa, dob, comment, conv_mode, distance, conv_bool)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''' )
        args = in_val
        self.cursor.execute(query, args)
        self.cnn.commit()     
    def Emp_Insert(self, actype, fval):
        self.cursor.execute('''INSERT INTO '''+self.ledg+''' (type) VALUES ('''+str(actype)+''')''')
        self.cnn.commit()
        led_id = self.cursor.lastrowid
        section, name, ftn, add1, add2, phone, off, email, doa, dob, cmnt, conv, conv_dist, conv_b = fval
        tin_val = led_id, section, name, ftn, add1, add2, phone, off, email, doa, dob, cmnt, conv, conv_dist, conv_b
        tquery = ('''INSERT INTO '''+self.empe+''' (ledgerID, designation, employee_name, guardian_name, add1, add2, phone, 
                 off_phone, email, doa, dob, comment, conv_mode, distance, conv_bool )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''' )
        targs = tin_val
        self.cursor.execute(tquery, targs)
        self.cnn.commit()
    def Stu_Update(self, args):
        query = ("UPDATE "+self.stu+" SET classID = ?, student_name = ?, guardian_name = ?, add1 = ?, add2 = ?, phone = ?, section = ?, "
                     " off_phone = ?, status = ?, email = ?, doa = ?, dob = ?, dot = ?, comment = ?, "
                     " conv_mode = ?, distance = ?, conv_bool = ? WHERE ledgerID = ? ")
        self.cursor.execute(query, args)
        self.cnn.commit()
    def Emp_Update(self, args):
        query = ("UPDATE "+self.empe+" SET designation = ?, employee_name = ?, guardian_name = ?, add1 = ?, add2 = ?, phone = ?, "
              " off_phone = ?, status = ?, email = ?, doa = ?, dob = ?, dot = ?,  comment = ? WHERE ledgerID = ? ")
        self.cursor.execute(query, args)
        self.cnn.commit()
#############################################################################
class SHEET_REC(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
    
    def DateCheck(self, stid, fdate, tdate):
        self.cursor.execute(" SELECT sheet_date "
          " FROM "+self.sht+" WHERE ledgerIDstu = '"+stid+"' AND sheet_date BETWEEN '"+fdate+"' AND '"+tdate+"' " )
        row = self.cursor.fetchone()
        return row
    def Get_TrnasID(self, stid, fdate, tdate):
        self.cursor.execute(" SELECT sheetID FROM "+self.sht+" WHERE "
            " ledgerIDstu = '"+stid+"' AND (sheet_date BETWEEN '"+fdate+"' AND '"+tdate+"' )  " )
        row = self.cursor.fetchone()
        return row    
    def SheetStuID(self, stid, fdate, tdate):
        self.cursor.execute(" SELECT ledgerIDstu,ledgerIDemp,classID,category,sheet_date,hindi,english,science,math,sstd,comp,bio, "
               " chem,phys,sans,civic,hist,geog,comm,sact,sport,other,attend,sheetID "
               " FROM "+self.sht+" WHERE ledgerIDstu = '"+stid+"' AND sheet_date BETWEEN '"+fdate+"' AND '"+tdate+"' " )
        row = self.cursor.fetchone()
        return row
    def Sheetrec(self, stid, fdate, tdate):
        self.cursor.execute(" SELECT hindi,english,science,math,sstd,comp,bio, "
               " chem,phys,sans,civic,hist,geog,comm,sact,sport,other,attend,sheet_date "
               " FROM "+self.sht+" WHERE ledgerIDstu = '"+stid+"' AND sheet_date BETWEEN '"+fdate+"' AND '"+tdate+"' "
               " ORDER BY sheet_date ASC " )
        rows = self.cursor.fetchall()
        return rows

    def SheetDictRec(self, stid, fdate, tdate):
        qry=(" SELECT hindi,english,science,math,sstd,comp,bio, "
               " chem,phys,sans,civic,hist,geog,comm,sact,sport,other,attend,sheet_date "
               " FROM "+self.sht+" WHERE ledgerIDstu = '"+stid+"' AND sheet_date BETWEEN '"+fdate+"' AND '"+tdate+"' "
               " ORDER BY sheet_date ASC " )
        
        self.cursor.execute(qry)
        drow={i:{'idx':i, 'hindi':r[0],'english':r[1],'science':r[2],'math':r[3],'sstd':r[4],
            'comp':r[5],'bio':r[6],'chem':r[7],'phys':r[8],'sans':r[9],'civic':r[10],'hist':r[11],
            'geog':r[12],'comm':r[13],'sact':r[14],'sport':r[15],'other':r[16],
            'attend':r[17],'sheetdate':datetime.strptime(r[18], "%Y-%m-%d").strftime("%d/%m/%Y"),
                 } for i,r in enumerate(self.cursor.fetchall())}
        return drow

    def TeacherSearch(self, techrid):
        self.cursor.execute(" SELECT employee_name,ledgerID FROM "+self.empe+" WHERE employeeID = '"+str(techrid)+"'  " )
        row = self.cursor.fetchone()
        return row
    def SheetInsert(self, args):
        query = ('''INSERT INTO '''+self.sht+''' (ledgerIDstu,ledgerIDemp,classID,category,sheet_date,hindi,english,
            science,math,sstd,comp,bio,chem,phys,sans,civic,hist,geog,comm,sact,sport,other,attend,fyear)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''' )
        self.cursor.execute(query, args)
        self.cnn.commit()
    def SheetUpdate(self, args):
        query = ("UPDATE "+self.sht+" SET ledgerIDemp = ?, classID = ?, category = ?, sheet_date = ?, "
          " hindi = ?, english = ?, science = ?, math = ?, sstd = ?, comp = ?, "
          " bio = ?, chem = ?, phys = ?, sans = ?, civic = ?, "
          " hist = ?, geog = ?, comm = ?, sact = ?, sport = ?, "
          " other = ?, attend = ? WHERE sheetID = ? ")
        self.cursor.execute(query, args)
        self.cnn.commit()
    def SheetDelete(self, stid, ddate):
        self.cursor.execute("DELETE FROM "+self.sht+" WHERE ledgerIDstu = '"+stid+"' AND sheet_date = '"+ddate+"' " )
        self.cnn.commit()
    def FetchSheet(self, frm, tod, key_val, fyear):
        self.cursor.execute(" SELECT sht.sheetID, stu.classID, "
        " stu.student_name, "
        " SUM(sht.hindi),  "
        " SUM(sht.english),  "
        " SUM(sht.science),  "
        " SUM(sht.math),  "
        " SUM(sht.sstd),  "
        " SUM(sht.comp),  "
        " SUM(sht.bio),  "
        " SUM(sht.chem),  "
        " SUM(sht.phys),   "
        " SUM(sht.sans),  "
        " SUM(sht.civic),  "
        " SUM(sht.hist),  "
        " SUM(sht.geog),  "
        " SUM(sht.comm),  "
        " SUM(sht.sact),  "
        " SUM(sht.sport),  "
        " SUM(sht.other), '', "
        " SUM(sht.attend)   "
        " FROM "+self.stu+" as stu LEFT JOIN "+self.sht+" as sht ON stu.classID = sht.classID AND stu.ledgerID = sht.ledgerIDstu "
        " WHERE stu.classID = '"+key_val+"' AND sht.fyear = '"+fyear+"' "
        " GROUP BY stu.ledgerID ")
        rows = self.cursor.fetchall()
        
        return rows

    def FetchSheet2(self, frm, tod, ledid, fyear):
        self.cursor.execute(" SELECT sht.sheetID, sht.sheet_date, stu.student_name, "
        " sht.hindi,  "
        " sht.english,  "
        " sht.science,  "
        " sht.math,  "
        " sht.sstd,  "
        " sht.comp,  "
        " sht.bio,  "
        " sht.chem,  "
        " sht.phys,   "
        " sht.sans,  "
        " sht.civic,  "
        " sht.hist,  "
        " sht.geog,  "
        " sht.comm,  "
        " sht.sact,  "
        " sht.sport,  "
        " sht.other, '', "
        " sht.attend   "    
        " FROM "+self.stu+" as stu LEFT JOIN "+self.sht+" as sht ON stu.classID = sht.classID AND stu.ledgerID = sht.ledgerIDstu "
        " WHERE sht.ledgerIDstu = '"+ledid+"' AND (sht.sheet_date BETWEEN '"+frm+"' AND '"+tod+"' ) AND sht.fyear = '"+str(fyear)+"' " )
        rows = self.cursor.fetchall()
        return rows

#############################################################################
class REG_REC(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
    
    def Stud_Reg_Search_By_Date(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, text, fyear, section  = textlist
        if text:
            lid = ''.join([" str.studentID = ", str(text), " AND " ])
        else:##
            lid = " "
        qry = ("SELECT str.studentID, (str.daytime), "
        " stu.classID, stu.student_name, stu.guardian_name, stu.phone, stu.section"
        " FROM "+self.stug+" as str LEFT JOIN "+self.stu+" as stu ON str.studentID = stu.studentID "
        " WHERE "+lid+" DATE(daytime) BETWEEN '"+frm+"' AND '"+tod+"' LIMIT "+str(varlimt)+","+str(staticlimit)+" ")
        self.cursor.execute(qry)
        drow={i:{'idx':i, 'lid':r[0],'daytime':r[1],'desg':r[2],'name':r[3],'gname':r[4],
            'phone':r[5],'section':r[6],} for i,r in enumerate(self.cursor.fetchall())}
        return drow   
        
    def Emp_Reg_Search_By_Date(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, text, fyear, desg  = textlist
        if text:
            lid = ''.join([" emr.employeeID = ", str(text), " AND emp.designation = ","'",desg,"' AND " ])
        else:
            lid = ''.join([" emp.designation = ","'",desg,"' AND " ])
        qry = ("SELECT emr.employeeID, (emr.daytime), "
        " emp.designation, emp.employee_name, emp.guardian_name, emp.phone, emr.ap "
        " FROM "+self.empg+" as emr LEFT JOIN "+self.empe+" as emp ON emr.employeeID = emp.employeeID "
        " WHERE "+lid+" DATE(daytime) BETWEEN '"+frm+"' AND '"+tod+"' ORDER BY emr.employeeID ASC LIMIT "+str(varlimt)+","+str(staticlimit)+" ")
       
        self.cursor.execute(qry)
        drow={i:{'idx':i, 'lid':r[0],'daytime':r[1],'desg':r[2],'name':r[3],'gname':r[4],
            'phone':r[5],'section':r[6],} for i,r in enumerate(self.cursor.fetchall())}
        return drow

    def Check_Save_Data_Students(self, date_):
        format = '%d/%m/%Y'
        self.cursor.execute("SELECT str.studentID, (str.daytime), "
        " stu.classID, stu.student_name, stu.guardian_name, stu.phone, stu.section "
        " FROM "+self.stug+" as str LEFT JOIN "+self.stu+" as stu "
        " ON str.studentID = stu.studentID WHERE DATE(daytime) = '"+date_+"' LIMIT "+str(varlimt)+","+str(staticlimit)+" " )
        rows = self.cursor.fetchall()
        return rows

    def CheckStudentRegister(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, date_, fyear, x  = textlist
        qry = ("SELECT str.studentID, COALESCE(str.daytime,'"+date_+"')as dt, "
        " stu.classID, stu.student_name, stu.guardian_name, stu.phone, stu.studentID, stu.section "
        " FROM "+self.stug+" as str LEFT JOIN "+self.stu+" as stu "
        " ON str.studentID = stu.studentID WHERE DATE(str.daytime) = '"+date_+"' LIMIT "+str(varlimt)+","+str(staticlimit)+" " )
        self.cursor.execute(qry)
        #### classID column using here with desg as key  
        drow={i:{'idx':i, 'lid':r[0],'daytime':r[1],'desg':r[2],'name':r[3],'gname':r[4],
            'phone':r[5],'esid':r[6], 'section':r[7],} for i,r in enumerate(self.cursor.fetchall())}
        return drow

    def CheckTeacherRegister(self, rscr, textlist, varlimt=0, staticlimit=10):
        frm, tod, date_, fyear, esid, desg  = textlist
        if esid:
            where = ''.join([" WHERE emp.employeeID = ", str(esid)," AND emp.designation = ","'",desg,"'"])
        else:
            where = ''.join([" WHERE emp.designation = ", "'",desg,"'"])
        qry = (" SELECT emp.employeeID, COALESCE(emr.daytime,'"+date_+"')as dt, emp.designation, "
              " emp.employee_name, emp.guardian_name, emp.phone, emp.employeeID, "
              " COALESCE((SELECT ap FROM "+self.empg+" WHERE employeeID = emp.employeeID "
              " AND daytime = '"+date_+"'), 'A') as ap "
              " FROM "+self.empe+" as emp LEFT JOIN "+self.empg+" as emr "
              " ON emp.employeeID = emr.employeeID "+where+" "
              " LIMIT "+str(varlimt)+","+str(staticlimit)+" ")
        self.cursor.execute(qry)
        ### ap = apsent present, using section as ap key
        drow={i:{'idx':i, 'lid':r[0],'daytime':r[1],'desg':r[2],'name':r[3],'gname':r[4],
            'phone':r[5],'esid':r[6], 'section':r[7],} for i,r in enumerate(self.cursor.fetchall())}
        return drow

    def Check_Save_Data_Teacher(self, Atend, Static, date_, desg):
        format = '%d/%m/%Y'
        qry = (" SELECT emr.employeeID, (emr.daytime), "
        " emp.designation, emp.employee_name, emp.guardian_name, emp.phone, emr.ap "
        " FROM "+self.empg+" as emr LEFT JOIN "+self.empe+" as emp ON emr.ledgerID = emp.employeeID "
        " WHERE DATE(emr.daytime) = '"+date_+"' AND emp.designation = '"+desg+"' " )
        self.cursor.execute(qry)
        rows = self.cursor.fetchall()
       
        qry = ("SELECT emp.ledgerID, '"+date_+"', "
        " emp.designation, emp.employee_name, emp.guardian_name, emp.phone, '"+Atend+"' "
        " FROM "+self.empe+" as emp WHERE emp.designation = '"+desg+"' ")
        self.cursor.execute(qry)
        emp_rows = self.cursor.fetchall()
        return rows, emp_rows

    def GetEmpID(self, date_):
        self.cursor.execute("SELECT emr.ledgerID " 
                       " FROM "+self.empg+" as emr WHERE DATE(emr.daytime) = '"+date_+"'" )
        row = self.cursor.fetchone()
        return row
    def StuExport(self, status):
        self.cursor.execute(" SELECT studentID, classID, section, student_name, guardian_name,  "
        " add1, add2, phone, off_phone, email, doa, dob, comment "
        " FROM "+self.stu+" WHERE  status = '"+status+"' "
        " ORDER BY classID DESC " )
        rows = self.cursor.fetchall()
        return rows
    def EmpExport(self, status):
        self.cursor.execute("SELECT employeeID, designation, employee_name, guardian_name, "
        " add1, add2, phone, off_phone, email, doa, dob, comment "
        " FROM "+self.empe+" WHERE  status = '"+status+"' "
        " ORDER BY employee_name ASC " )
        rows = self.cursor.fetchall()
        return rows
    def StrInsert(self, args, ):
        query =  ('''INSERT INTO '''+self.stug+''' (studentID, daytime, iddate, fyear)
        VALUES (?, ?, ?, ?)''' )
        self.cursor.execute(query, args)
        self.cnn.commit()
    def EmrInsert(self, args, ):
        query = ('''INSERT INTO '''+self.empg+''' (employeeID, ap, daytime, iddate, fyear)
        VALUES (?, ?, ?, ?, ?)''' )
        self.cursor.execute(query, args)
        self.cnn.commit()
#############################################################################
class GETCAL(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
    def GetDates(self, order):
        self.cursor.execute(" SELECT * FROM "+self.cal+" ORDER BY fyear "+order+" ")
        row = self.cursor.fetchone()
        return row
    def GetDates_ALL(self, order):
        self.cursor.execute(" SELECT * FROM "+self.cal+" ORDER BY fyear "+order+" ")
        row = self.cursor.fetchall()
        return row
    def DateInsert(self, args):
        query = ('''INSERT INTO '''+self.cal+''' (fyear, year)
        VALUES (?, ?)''' )
        self.cursor.execute(query, args)
        self.cnn.commit()
    def DateDelete(self, fyear):
        self.cursor.execute("DELETE FROM "+self.cal+" WHERE fyear = '"+fyear+"' " )
        self.cnn.commit()
#############################################################################
class USERLOGIN(DBTABLES):
    def __init__ (self):
        DBTABLES.__init__(self)
    def LOG(self):
        self.cursor.execute("SELECT user_id, user_pass FROM "+self.own+" WHERE owner_det_id = '1'")
        rows = self.cursor.fetchone()
        return rows
    def LogUpdate(self, args):
        query = ("UPDATE "+self.own+" SET user_id = ?, user_pass = ? WHERE owner_det_id = '1' ")
        self.cursor.execute(query, args)
        self.cnn.commit()
#if __name__ == '__main__':
#    DBTABLES()

