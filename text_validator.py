#!/usr/bin/python
# -*- coding: UTF-8 -*-


import wx,string

class Rmss_TextCtrl(wx.TextCtrl):
    def __init__(self, parent, *args, **kwargs):
        super(Rmss_TextCtrl, self).__init__(parent, *args, **kwargs)
        self.Bind(wx.EVT_TEXT, self.OnText)
    def Clone(self):
        return Rmss_TextCtrl(self.flag)

    def OnText(self, event):
        val = self.GetValue()
        uval = val.upper()
        if val != uval:
                pos = self.GetInsertionPoint()
                self.ChangeValue(uval)
                self.SetInsertionPoint(pos)
        return
    
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
