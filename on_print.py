#!/usr/bin/python
# -*- coding: UTF-8 -*-

import num2word
import os, sys
from rmss_dates import *
import subprocess
def On_print (self, row, col, table):
        #table = self.__Grid.GetTable()
        #row = (table.GetNumberRows())
        #col = (table.GetNumberCols())
        self.data = []
        self.etdata = []
        e_bill = self.estimate_bill.GetValue().upper()
        dat = self.bill_date.GetValue()
        pname = self.sup_tx.GetValue()
        #pname3 = str(pnam3).replace(",", "")
        #cnn = MySQLdb.connect("localhost", "root", "pass",  "rmss" )
        cnn = mysql.connector.connect(host=rmss_config.HOST,database=rmss_config.MYDB,user=rmss_config.USER,password=rmss_config.PASS)
        cursor=cnn.cursor()
        own_det = ("SELECT pname, add1, add2, phone, licence, tin, "
                  " statutory1,statutory2,statutory3,statutory4 FROM owner_det WHERE owner_det_id = '1'")
        cursor.execute(own_det)
        owner_det = cursor.fetchall()
        for o in owner_det:
            owner,o_add1,o_add2,phone,o_dl_no,o_tin=o[0],o[1],o[2],o[3],o[4],o[5]
            statu1,statu2,statu3,statu4 = o[6], o[7],o[8],o[9]
        blank_space = '                         '
        date = (self.bill_date.GetValue())
        c_cr = (self.cb1.GetValue())
        party = (self.sup_tx.GetValue())
        p_add1 =(self.sup_tx1.GetValue())
        p_add2 =(self.sup_tx2.GetValue())
        p_add3= (self.sup_tx3.GetValue())
        p_add4= (self.sup_tx4.GetValue())
        bill_no = (self.inv_tx.GetValue())
        third_label2 = ' '
        third_label3 = ' '
        third_label4 = ' '
        if p_add4 == '':
                p_inv = 'SALE INVOICE'
        else:
                p_inv = 'TAX INVOICE'
        inv_details = '%s - %s' %(p_inv, c_cr)
        ###--- FOR ESTIMATE ---####################
        esti_ = 'ESTIMATE ONLY'
        esti_details = '%s - %s' %(esti_, c_cr)
        e_bill_no = self.inv_tx.GetValue()
        top_esti = '%s    %s \n '   % (blank_space,esti_details)
        label1_esti ='\x1BM    ','  |\x1BE%s \x1BF'%party,'    |SERIAL.N:%s'%e_bill_no
        label2_esti ='                 ','|%s'%p_add1,'\x1BE|DATE:%s \x1BF'%date
        label3_esti ='     ','|%s'%p_add2,'%s'%third_label2
        ###----FOR ESTIMATE ---####################
        banner = 'STOCKIST FOR:'
        cursor.execute("SELECT stockist FROM stockist_for ORDER BY stockist DESC")
        stockist = cursor.fetchall()
        for sto in stockist:
            sto_de = (sto[0])
            stockist_det = sto_de.strip()
        cnn.commit()
        vat = (self.vat_amtx.GetValue())
        sat = (self.sat_amtx.GetValue())
        subt =(self.amtx.GetValue())
        tax = (self.add_tax1.GetValue())
        dis = (self.dis.GetValue())
        othe_val = (self.other1_value.GetValue())
        itm_cnt = self.item_count.GetValue()
        if othe_val == '':
            othe_val = '0.00'
        else:
            pass
        tot = (self.total_amtx.GetValue())
        try:
            num_word = num2word.to_card(float(tot))
        except ValueError:
            wx.MessageBox("Nothing to Print !")
            self.add.SetFocus()
        printer_print = wx.MessageBox(
               "  WANT TO PRINT ??  ",
               "Print Confirmation !", wx.YES_NO |wx.ICON_EXCLAMATION)
        #--------------------------------------------------------------
        printer_init = ' \x1B\x40 '
        top = '%s   \x1B\x34 \x1BE%s\x1BF \x1B\x35  '   % (blank_space,inv_details)
        head = '\x1BE\x1BW\01%s \x1BF \x1B\x40  ' % owner
        static_line = 96 * "-"
        _space = 26 * " "
        h_space = 42 * " "
        eh_space = 50 * " "
        v_gap = '%s\n'%(self.cmnt.GetValue().upper())
        paper_cut = 9*'\n'
        label1 ='\x1BM%s'%o_add1,'  |\x1BE%s'%party,'    |BILL No:%s\x1BF'%bill_no
        label2 ='%s'%o_add2,'|%s'%p_add1,'\x1BE|DATE:%s\x1BF'%date
        label3 ='%s'%phone,'|%s'%p_add2,'%s'%third_label2
        label4 ='%s'%o_dl_no,'|%s'%p_add3,'%s'%third_label3
        label5 ='%s'%o_tin,'|%s'%p_add4,'%s'%third_label4
        st_for = '%s:%s'%(banner,stockist_det)
        d_label = 'PRODUCT','| PKG','| QTY','|FREE','| RATE','|VAT','|DIS','| AMOUNT','| MRP','EXP.D','|NET',' BATCH'
        bot1 ='VAT = %s and SAT = %s'%(vat,sat),'SUB TOTAL = %s'%subt
        bot2 ='%s'%statu1,'ADD TAX = %s'%tax
        bot3 ='%s'%statu2,'DISCOUNT = %s'%dis
        bot4 ='%s'%statu3,'OTHER = %s'%othe_val
        bot5 ='%s'%statu4,'\x1BETOTAL\x1BF = \x1BW\01%s '%tot
        ebot2 ='%s'%eh_space,'ADD TAX = %s'%tax
        ebot3 ='%s'%eh_space,'DISCOUNT = %s'%dis
        ebot4 ='%s'%eh_space,'OTHER = %s'%othe_val
        ebot5 ='%s'%eh_space,'\x1BETOTAL\x1BF = \x1BW\01%s '%tot
        blnk = '\x1B\x40 \x1BM'
        rs_words = '\x1BM\x1BERs. %s \x1BF only' %num_word
        Auth_Sign1 = 'Total Items = %s%s For : %s' %(itm_cnt,h_space, owner)
        greet = "Have a Nice Day !"
        Auth = 'AUTHORISED SIGNATURE '
        Auth_esti = 'SIGNATURE'
        Auth_Sign_esti = '%s%s    %s'%(greet,h_space, Auth_esti)
        Auth_Sign2 = '%s%s     %s'%(greet,h_space, Auth)
        sunil = '%s  \x1Bg +++DEVELOP BY SUNIL GUPTA 9935188831+++' %_space
        bottom_gap = ''' \x1B\x40 %s'''%paper_cut
        p0=(printer_init)
        p1=(top)
        p2=(head)
        p3=(FormatHeadItem(label1))
        p4=(FormatHeadItem(label2))
        p5=(FormatHeadItem(label3))
        p6=(FormatHeadItem(label4))
        p7=(FormatHeadItem(label5))
        p8=(static_line)
        p9=(st_for)
        p10=(static_line)
        p11=(FormatProdItem(d_label))
        p12=(static_line)
        p13=(static_line)
        p14=(FormatBottomItem(bot1))
        p15=(FormatBottomItem(bot2))
        p16=(FormatBottomItem(bot3))
        p17=(FormatBottomItem(bot4))
        p18=(FormatBottomItem(bot5))
        p19=(blnk)
        p20=(rs_words)
        p21=(Auth_Sign1)
        p22=(v_gap)
        p23=(Auth_Sign2)
        p24=(static_line)
        p25=(sunil)
        p26=(bottom_gap)
        ###-------### ESTIMATE ###----------###
        pe0 =(top_esti)
        pe1=(FormatHeadItem(label1_esti))
        pe2=(FormatHeadItem(label2_esti))
        pe3=(FormatHeadItem(label3_esti))
        pe4=(static_line)
        #self.etdata.append(d_label)
        pe5=(FormatProdItem(d_label))
        pe6=(static_line)
        pe7=(static_line)
        pe8=(FormatBottomItem(bot1))
        pe9=(FormatBottomItem(ebot2))
        pe10=(FormatBottomItem(ebot3))
        pe11=(FormatBottomItem(ebot4))
        pe12=(FormatBottomItem(ebot5))
        pe13=(blnk)
        pe14=(rs_words)
        pe15=(Auth_Sign_esti)
        pe16=(static_line)
        pe17=(sunil)
        pe18=(bottom_gap)
        if printer_print == wx.YES:
            if e_bill != 'E':
                p_head = ('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s'%(
                        p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12))
                file = open("print_receipt.txt","w")
                file.write('%s\n' % p_head)
                product_table = []
                dataa = []
                for r in range(0, row):
                    prod = table.GetValue(r, 1)
                    quant = table.GetValue(r, 4)
                    if prod and quant != '': 
                            item = []
                            item.append(''+table.GetValue(r, 1))
                            item.append(''+table.GetValue(r, 2))
                            item.append('|'+table.GetValue(r, 4))
                            item.append('|'+table.GetValue(r, 5))
                            item.append('|'+table.GetValue(r, 6))
                            item.append('|'+table.GetValue(r, 8))
                            item.append('|'+table.GetValue(r, 9))
                            item.append('|'+table.GetValue(r, 10))
                            item.append('|'+table.GetValue(r, 11))
                            exp_date = table.GetValue(r, 15)
                            ed = exp_date.replace("/", "")
                            #item.append('|'+table.GetValue(r, 15))
                            item.append(''+ed)                 
                            item.append('|'+table.GetValue(r, 12))
                            item.append('|'+table.GetValue(r, 3))
                            product_table.append(item)
                for ite in product_table:
                    #self.data.append(self.FormatProdItem(item))
                        p_body = (FormatProdItem(ite))
                        file.write('%s\n' % p_body)
                p_bott = ('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n'%(
                        p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26))
                file.write('%s' % p_bott)
                file.close()
                #os.system("lpr -o raw print_receipt.txt ") # FOR LINUX
                os.system("copy print_receipt.txt LPT1 "  ) # FOR WINDOW 7
                #os.system("echo '%s' | lpr -o raw " % (ed))
                #for md in self.data:
                        #print md
                        ##os.system("echo '%s' | lpr -o raw " % (md))
                        ##lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
                        ##lpr.stdin.write(md)
                        #print_file = open("print_receipt.txt", "w")
                        #print_file.write('%s' % md)
                        #print_file.close()
                        #os.system("copy print_receipt.txt LPT1 "  )
                        
            else:
                pe_head = ('%s\n%s\n%s\n%s\n%s\n%s\n%s'%(
                        pe0,pe1,pe2,pe3,pe4,pe5,pe6))
                file = open("print_receipt.txt","w")
                file.write('%s\n' % pe_head)
                product_table = []
                dataa = []
                for r in range(0, row):
                    prod = table.GetValue(r, 1)
                    quant = table.GetValue(r, 4)
                    if prod and quant != '': 
                            item = []
                            item.append(''+table.GetValue(r, 1))
                            item.append(''+table.GetValue(r, 2))
                            item.append('|'+table.GetValue(r, 4))
                            item.append('|'+table.GetValue(r, 5))
                            item.append('|'+table.GetValue(r, 6))
                            item.append('|'+table.GetValue(r, 8))
                            item.append('|'+table.GetValue(r, 9))
                            item.append('|'+table.GetValue(r, 10))
                            item.append('|'+table.GetValue(r, 11))
                            exp_date = table.GetValue(r, 15)
                            ed = exp_date.replace("/", "")
                            #item.append('|'+table.GetValue(r, 15))
                            item.append(''+ed)                 
                            item.append('|'+table.GetValue(r, 12))
                            item.append('|'+table.GetValue(r, 3))
                            product_table.append(item)
                for ite in product_table:
                    pe_body = FormatProdItem(ite)
                    file.write('%s\n' % pe_body)
                pe_bott = ('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n'%(
                        pe7,pe8,pe9,pe10,pe11,pe12,pe13,pe14,pe15,pe16,pe17,pe18))
                file.write('%s' % pe_bott)
                file.close()
                #os.system("lpr -o raw print_receipt.txt ") # FOR LINUX
                os.system("copy print_receipt.txt LPT1 "  ) # FOR WINDOW 7
                        
                cnn.close()
        return

def FormatHeadItem( head_item):
        "Takes a tuple from the product list control and formats for printing."
        col_widths = 36, 36, 23
        head_data = ''
        for i in range(3):
            if len(head_item[i]) < col_widths[i]:
                head_data += head_item[i] + (col_widths[i]-len(head_item[i]))*' '
            else:
                head_data += head_item[i][:col_widths[i]] 
        return head_data

def FormatProdItem( prod_item):
        "Takes a tuple from the product list control and formats for printing."
        col_widths = 24,5,7, 5, 8, 4, 4, 10, 8, 5, 8,8
        prod_data = ''
        for i in range(12):
            if len(prod_item[i]) < col_widths[i]:
                prod_data += prod_item[i] + (col_widths[i]-len(prod_item[i]))*' '
            else:
                prod_data += prod_item[i][:col_widths[i]] 
        return prod_data
def FormatBottomItem( bottom_item):
        "Takes a tuple from the bottom list control and formats for printing."
        col_widths = 65, 30
        bottom_data = ''
        for i in range(2):
            if len(bottom_item[i]) < col_widths[i]:
                bottom_data += bottom_item[i] + (col_widths[i]-len(bottom_item[i]))*' '
            else:
                bottom_data += bottom_item[i][:col_widths[i]] 
        return bottom_data
  

