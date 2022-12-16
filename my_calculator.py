#======================#
#  Tkinter Calculator  #
#----------------------#
#  Konstantinos Thanos #
#   Mathematician, MSc #
#======================#

from __future__ import division
from rmsvalidators import *

class RMSCalculator(Frame):
    def __init__(self, parent, sp, spnum, buttonidx, impar, whxy, **kw):
   
        Frame.__init__(self, parent)
        self.rscr = kw['rscr']
        self.whxy = whxy
        self.fyear = self.rscr['fyear']

        self.master.configure(bg="#293C4A", bd=10)
        self.master.title("RMS Calculator")
        parent.iconbitmap(self.rscr['rmsicon'])
        self.master.geometry('%dx%d+%d+%d'% (340, 340, 0, 350))
        self.calc_operator = ""
        
        entryfgbg = {'font':('sans-serif', 20, 'bold'), 'bg':'#BBB', 'justify':'right', 'bd':5, 'insertwidth': 5,}

        self.text_input = StringVar()
        self.text_input.trace('w', lambda nm, idx, mode, var=self.text_input:
                          self.OnTextDP(var))
        
        self.text_display = Entry(self.master, textvariable=self.text_input, **entryfgbg)
                             
        self.text_display.grid(columnspan=5, padx = 10, pady = 15)
        self.text_display.bind('<Key>', self.OnTextDPKey)
        button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
        button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

        if self.whxy:
            self.master.geometry('%dx%d+%d+%d' % self.whxy)
        else:
            self.master.geometry('%dx%d+%d+%d' % (wsw, wsh, xpos, ypos))
            
        self.button_7 = Button(self.master, text='7',
                          command=lambda:self.button_click('7'), **button_params_main)
        self.button_7.grid(row=6, column=0, sticky="nsew")
        self.button_8 = Button(self.master, text='8',
                          command=lambda:self.button_click('8'), **button_params_main)
        self.button_8.grid(row=6, column=1, sticky="nsew")
        self.button_9 = Button(self.master, text='9',
                          command=lambda:self.button_click('9'), **button_params_main)
        self.button_9.grid(row=6, column=2, sticky="nsew")
        delbutt = {'bd':5, 'fg':'#000', 'font':('sans-serif', 20, 'bold'),'bg':'#db701f'}
        self.delete_one = Button(self.master, text='C',
                       command=self.button_delete, **delbutt)
        self.delete_one.grid(row=6, column=3, sticky="nsew")
        
        self.delete_all = Button(self.master, text='AC',
                       command=self.button_clear_all, **delbutt)
        self.delete_all.grid(row=6, column=4, sticky="nsew")

        self.button_4 = Button(self.master, text='4',
                          command=lambda:self.button_click('4'), **button_params_main)
        self.button_4.grid(row=7, column=0, sticky="nsew")
        self.button_5 = Button(self.master, text='5',
                          command=lambda:self.button_click('5'), **button_params_main)
        self.button_5.grid(row=7, column=1, sticky="nsew")
        self.button_6 = Button(self.master, text='6',
                          command=lambda:self.button_click('6'), **button_params_main)
        self.button_6.grid(row=7, column=2, sticky="nsew")
        self.mul = Button(self.master, text='*',
                     command=lambda:self.button_click('*'), **button_params_main)
        self.mul.grid(row=7, column=3, sticky="nsew")
        self.div = Button(self.master, text='/',
                     command=lambda:self.button_click('/'), **button_params_main)
        self.div.grid(row=7, column=4, sticky="nsew")

        #--8th row--
        self.button_1 = Button(self.master, text='1',
                          command=lambda:self.button_click('1'), **button_params_main)
        self.button_1.grid(row=8, column=0, sticky="nsew")
        self.button_2 = Button(self.master, text='2',
                          command=lambda:self.button_click('2'), **button_params_main)
        self.button_2.grid(row=8, column=1, sticky="nsew")
        self.button_3 = Button(self.master, text='3',
                          command=lambda:self.button_click('3'), **button_params_main)
        self.button_3.grid(row=8, column=2, sticky="nsew")
        self.add = Button(self.master, text='+',
                     command=lambda:self.button_click('+'), **button_params_main)
        self.add.grid(row=8, column=3, sticky="nsew")
        self.sub = Button(self.master, text='-',
                     command=lambda:self.button_click('-'), **button_params_main)
        self.sub.grid(row=8, column=4, sticky="nsew")

        #--9th row--
        self.button_0 = Button(self.master, text='0',
                          command=lambda:self.button_click('0'), **button_params_main)
        self.button_0.grid(row=9, column=0, sticky="nsew")
        self.point = Button(self.master,  text='.',
                       command=lambda:self.button_click('.'), **button_params_main)
        self.point.grid(row=9, column=1, sticky="nsew")
       
        self.equal = Button(self.master, text='=',
                       command=self.button_equal, **button_params_main)
        self.equal.grid(row=9, columnspan=3, column=2, sticky="nsew")
        self.text_display.focus_set()
        
    def OnTextDP(self, var):
        txt = var.get()
        try:
            self.text = str(eval(txt))
        except :
            if '+' in txt:
                return
            if '-' in txt:
                return
            if '*' in txt:
                return
            if '/' in txt:
                return
            self.text_input.set(txt[:-1])
            
    def OnTextDPKey(self, event):
        key = event.keysym
        kchar = event.char
        if key == 'Escape':
            self.OnClose(event) ### Calling Parent Class OnClose
            return
        if kchar:
            if ord(kchar) in range(43,58):
                pass
            if ord(kchar) > 58:
                text = self.text_input.get()
                self.text_input.set(text[:-1])
                return
            
        if key in ['Return', 'Tab']:
            try:
                text = self.text_input.get()
                self.text_input.set(str(eval(text)))
            except :
                self.text_input.set('0')

    def OnClose(self, event=None):
        self.master.destroy()
                   
    def button_click(self, char):
        self.calc_operator += str(char)
        self.text_input.set(self.calc_operator)

    # Function to clear the whole entry of text display
    def button_clear_all(self):
        self.calc_operator = ""
        self.text_input.set("")

    # Function to delete one by one from the last in the entry of text display
    def button_delete(self):
        text = self.calc_operator[:-1]
        self.calc_operator = text
        self.text_input.set(text)

    # Function to calculate the factorial of a number
    def factorial(self, n):
        if n==0 or n==1:
            return 1
        else:
            return n*factorial(n-1)

    # Funtion to find the result of an operation
    def button_equal(self):
        temp_op = str(eval(self.calc_operator))
        self.text_input.set(temp_op)
        self.calc_operator = temp_op
"""        
def main():
    import config
    root = Tk()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    #"Calibri Bold", "Calibri", "Arial", "Arial Bold", "Times New Roman", "Times New Roman Bold"
    sysfontnum = 12  ### Default is given Upate Later/User Given 
    entryfont = "Calibri Bold"
    subentryfont = "Calibri"
    fontd = {"calb":"Calibri Bold", "cal":"Calibri", "arl":"Arial", "arlb":"Arial Bold",
                 "tnr":"Times New Roman", "tnrb":"Times New Roman Bold", "entryfont":{'font': (entryfont, sysfontnum)},
                 "subentryfont":{'font': (subentryfont, sysfontnum)}}
    today = time.strftime('%d/%m/%Y', time.localtime(time.time()))
    today_db_f = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    
    mycalendar = (('fy0', today_db_f, today_db_f, u''),)
    rmspath = os.path.dirname(os.path.realpath(__file__))
    pdir = os.path.dirname(rmspath)
    
    rmsicon = os.path.join(rmspath, 'my_icon.ico')
    ostd = {'pageline':60, 'net_colm':'Y','party_bal':'N','stockist_list':'Y',
                'page_size':'4','default_trade':0,'bill_series':'S'}
    own = {'name':'RMS SOFT','add1':'http://www.rmssoft.co.in','add2':'','phone':'','reg':'', 'gstin':'','statu1':'','statu2':'','statu3':'','statu4':''}
    otlst = {'others':'/True', 'stockist_det':''}
    opdfsett = {'vat':4, 'vat1':4, 'sat':1, 'cst':2}
    ownerdict = {'billseries':'S', 'demochk':45, 'ownerinfo':{'owner':own, 'othersett':ostd, 'otlst':otlst, 'opdfsett':opdfsett},
                 'errorlist':[]}
    prpath = {}
    printerinfo = {'printer':{'pport':'USB001','pname':'myprinter'},'shareprinter':{'sprinter':'myprinter','sport':'LPT1','sname':'tvs'}}
    taxinfo = {'taxinfo':{'tax1name':'CGST', 'tax2name':'SGST','tax1lst':[], 'tax2lst':[], 'taxpayer':True},}
    conf = config.Configuration()
    cofdic ={'fare1':conf.FARE_MODE1(),'fare2':conf.FARE_MODE2(),
              'fare3':conf.FARE_MODE3(),'latefee':conf.LATE_FEE_DATE(),'an_hy_montn':conf.ANNUAL_HY_MONTH(),
              'headmargin':conf.HEAD_MARGIN(),'footmargin':conf.FOOT_MARGIN(),'leftmargin':conf.LEFT_MARGIN(),
              'rightmargin':conf.RIGHT_MARGIN(),'extendmargin':conf.EXTEND_MARGIN(),'subjecthigh':conf.SUBJECTS_HIGHER(),
              'subjectlow':conf.SUBJECTS_LOWER(),'subjectrowhigh':conf.SUBJECTS_ROW_HIGHER(), 'subjectrowlow':conf.SUBJECTS_ROW_LOWER(),   
              'fontsize_h':conf.HEIGHER_CLASS_FONT_SIZE(),'fontsize_l':conf.LOWER_CLASS_FONT_SIZE(),'outoff':conf.OUTOFF_LIST(),
              'session':conf.SESSION(),'feehead':conf.FEE_HEADINGS(),'pdfs1':conf.PRINT_PDF_STYLE(),
              'exportpath':conf.EXPORT_PATH(),'slogan':conf.SLOGAN(),
              'monthhead':config.MONTHS_HEADINGS(),'rvmonthhead':config.REVERSE_MONTHS_HEADINGS(),}
    rscr = {'sw':sw, 'sh':sh, 'font':fontd,'sysfontnum':int(sysfontnum), 'ownerdict':ownerdict, 'mycalendar':mycalendar,
            'fyear':'0', 'daterange':['2000-01-01','2021-03-31'],
            'ledgerid':'0','itemid':'0','transid':'0','spid':'0','csid':'0','csname':'',
            'rmspath':rmspath,'rmsicon':rmsicon, 'pardir': rmspath, 'prpath':prpath,'taxinfo':taxinfo,'printerinfo': printerinfo,
            'TABLENUM':'','today':today, 'today_db_format':today_db_f,'tax1':'0', 'tax2':'0',
            'the_time':'', 'itemidlist':[], 'spidlist':[],'renderlist':[],
            'taxinvoice':True,'stkmess':'YES','decimalval':'2','last_esti_no':None, 'last_sale_bill_no':None,
            'exp_alert':90,'estifilter':False,'sdc':'1','mysoft':'1','mysoftval':'1',
            'compbool':True, 'config':cofdic}
    buttonidx = 1
    parent = None
    sptag = 'Register Entry'
    spnum = 1
    whxy = (350, 350, 400, 200)
    app = RMSCalculator(root, sptag, spnum, buttonidx, parent, whxy, rscr=rscr)    
    root.mainloop()

if __name__ == '__main__':
    main()
"""
