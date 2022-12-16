#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import wx
import sys
import wx.calendar
import wx.combo
import datetime
from datetime import date as dt
import config


TEXTCTRL_FILED_COLOUR = (255,255,200)
text = [255,255,200]
class MyDateCtrl(wx.combo.ComboCtrl):
    def __init__(self, parent, size, pos, title):
        wx.combo.ComboCtrl.__init__(self, parent, size=size, pos=pos,
                                    style=wx.TE_PROCESS_ENTER | wx.NO_BORDER)
        self.title = title
        self.SetBackgroundColour(TEXTCTRL_FILED_COLOUR)
        self.TextCtrl.SetBackgroundColour(TEXTCTRL_FILED_COLOUR)
        self.TextCtrl.Bind(wx.EVT_SET_FOCUS, self.on_got_focus)
        self.TextCtrl.Bind(wx.EVT_KILL_FOCUS, self.on_lost_focus)
        self.TextCtrl.Bind(wx.EVT_CHAR, self.on_char)
        self.nav = False
        self.setup_button()
        #self.SetFocus()
    def setup_button(self):  # copied directly from demo
        # make a custom bitmap showing "..."
        bw, bh = 14, 16
        bmp = wx.EmptyBitmap(bw, bh)
        dc = wx.MemoryDC(bmp)

        # clear to a specific background colour
        bgcolor = wx.Colour(int(text[0]),int(text[1]),int(text[2]))
        dc.SetBackground(wx.Brush(bgcolor))
        #dc.SetBackground(wx.Brush(TEXTCTRL_FILED_COLOUR))
        dc.Clear()

        # draw the label onto the bitmap
        label = "..."
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        dc.SetFont(font)
        tw, th = dc.GetTextExtent(label)
        dc.DrawText(label, (bw-tw)/2, (bw-tw)/2)
        del dc

        # now apply a mask using the bgcolor
        bmp.SetMaskColour(bgcolor)

        # and tell the ComboCtrl to use it
        self.SetButtonBitmaps(bmp, True)

    # Overridden from ComboCtrl, called when the combo button is clicked
    def OnButtonClick(self):
        text_ctrl = self.TextCtrl
        date = text_ctrl.Value
        if date in ('', '  /  /    '):
            wx_date = wx.DateTime()
        else:
            try:
                d, m, y = map(int, date.split('/'))
            except ValueError:
                today = wx.DateTime.Today().Format("%d/%m/%Y")
                tday = str(today).split('/')
                d, m ,y = int(tday[0]),int(tday[1]),int(tday[2])
            try:
                wx_date = wx.DateTimeFromDMY(d, m-1, y)
            except :
                wx_date = wx.DateTime.Today().Format("%d/%m/%Y")
        try:
            dlg = MyCalendarDlg(self, wx_date)
        except:
            return
        dlg.CentreOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            cal_date = dlg.cal.Date
            text_ctrl.Value = '{0:02}/{1:02}/{2:04}'.format(
                cal_date.Day, cal_date.Month+1, cal_date.Year)
            self.nav = True
        dlg.Destroy()
        self.SetFocus()

    # Overridden from ComboCtrl to avoid assert since there is no ComboPopup
    def DoSetPopupControl(self, popup):
        pass

    def on_got_focus(self, evt):
        if self.nav:  # user has made a selection, so move on
            self.nav = True #False
            wx.CallAfter(self.Navigate)
        else:
            text_ctrl = self.TextCtrl
            if text_ctrl.Value == '':
                a = wx.Locale(wx.LANGUAGE_ENGLISH)
                b = wx.DateTime.Today()
                date_value_now = b.Format("%d/%m/%Y")
                text_ctrl.Value = date_value_now #'  /  /    '
            text_ctrl.InsertionPoint = 0
            text_ctrl.SetSelection(-1, -1)
            text_ctrl.pos = 0
        evt.Skip()

    def on_lost_focus(self, evt):
        value = self.Value
        a = wx.Locale(wx.LANGUAGE_ENGLISH)
        b = wx.DateTime.Today()
        date_value_now = b.Format("%x")
        #if value == date_value_now : #'  /  /    ':  # ) remove these lines
        #    self.Value = ''        # ) if you want a blank
        #    evt.Skip()             # ) entry to default to
        #    return                 # ) today's date
        today = dt.today()
        date = value.split('/')
        day = date[0].strip()
        if day == '':
            day = today.day
        else:
            day = int(day)
        month = date[1].strip()
        if month == '':
            month = today.month
        else:
            month = int(month)
        year = date[2].strip()
        if year == '':
            year = today.year
        elif len(year) == 2:
            # assume year is in range (today-75) to (today+25)
            year = int(year) + int(today.year/100)*100
            if year - today.year > 25:
                year -= 100
            elif year - today.year < -75:
                year += 100
        else:
            try:
                year = int(year)
            except ValueError as e:
                wx.MessageBox("INVALID ENTRY >> \n %s" % e, "WARNING !!", wx.ICON_WARNING)
                wx.CallAfter(self.SetFocus)
        try:
            try:
                date = dt(year, month, day)
                self.Value = '{0:02}/{1:02}/{2:04}'.format(day, month, year)
            except TypeError as e:
                wx.MessageBox("INVALID ENTRY >> \n %s" % e, "WARNING !!", wx.ICON_WARNING)
                wx.CallAfter(self.SetFocus)
        except ValueError as error:
            #dlg = wx.MessageDialog(
            #    self, str(error), self.title, wx.OK | wx.ICON_INFORMATION)
            #dlg.ShowModal()
            #dlg.Destroy()
            self.Value = '  /  /    '
            wx.CallAfter(self.SetFocus)

        self.TextCtrl.SetSelection(0, 0)
        evt.Skip()

    def on_char(self, evt):
        text_ctrl = self.TextCtrl
        code = evt.KeyCode
        if code in (wx.WXK_SPACE, wx.WXK_F4) and not evt.AltDown():
            self.OnButtonClick()
            return
        if code in (wx.WXK_LEFT, wx.WXK_RIGHT, wx.WXK_HOME, wx.WXK_END):
            if text_ctrl.Selection == (0, 10):
                text_ctrl.SetSelection(0, 0)
            if code == wx.WXK_LEFT:
                if text_ctrl.pos > 0:
                    text_ctrl.pos -= 1
                    if text_ctrl.pos in (2, 5):
                        text_ctrl.pos -= 1
            elif code == wx.WXK_RIGHT:
                if text_ctrl.pos < 10:
                    text_ctrl.pos += 1
                    if text_ctrl.pos in (2, 5):
                        text_ctrl.pos += 1
            elif code == wx.WXK_HOME:
                text_ctrl.pos = 0
            elif code == wx.WXK_END:
                text_ctrl.pos = 10
            text_ctrl.InsertionPoint = text_ctrl.pos
            return
        if code in (wx.WXK_BACK, wx.WXK_DELETE):
            if text_ctrl.Selection == (0, 10):
                text_ctrl.Value = '  /  /    '
                text_ctrl.SetSelection(0, 0)
            if code == wx.WXK_BACK:
                if text_ctrl.pos == 0:
                    return
                text_ctrl.pos -= 1
                if text_ctrl.pos in (2, 5):
                    text_ctrl.pos -= 1
            elif code == wx.WXK_DELETE:
                if text_ctrl.pos == 10:
                    return
            curr_val = text_ctrl.Value
            text_ctrl.Value = curr_val[:text_ctrl.pos]+' '+curr_val[text_ctrl.pos+1:]
            text_ctrl.InsertionPoint = text_ctrl.pos
            return
        if code in (wx.WXK_TAB, wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER) or code > 255:
            evt.Skip()
            return
        if text_ctrl.pos == 10:
            wx.Bell()
            return
        ch = chr(code)
        if ch not in ('0123456789'):
            wx.Bell()
            return
        if text_ctrl.Selection == (0, 10):
            a = wx.Locale(wx.LANGUAGE_ENGLISH)
            b = wx.DateTime.Today()
            date_value_now = b.Format("%x")
            curr_val = '  /  /    ' #date_value_now #
        else:
            curr_val = text_ctrl.Value
        text_ctrl.Value = curr_val[:text_ctrl.pos]+ch+curr_val[text_ctrl.pos+1:]
        text_ctrl.pos += 1
        if text_ctrl.pos in (2, 5):
            text_ctrl.pos += 1
        text_ctrl.InsertionPoint = text_ctrl.pos

class MyCalendarDlg(wx.Dialog):
    def __init__(self, parent, date):
        wx.Dialog.__init__(self, parent, title=parent.title)
        panel = wx.Panel(self, -1)

        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        cal = wx.calendar.CalendarCtrl(panel, date=date)

        if sys.platform != 'win32':
            # gtk truncates the year - this fixes it
            w, h = cal.Size
            cal.Size = (w+25, h)
            cal.MinSize = cal.Size

        sizer.Add(cal, 0)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add((0, 0), 1)
        btn_ok = wx.Button(panel, wx.ID_OK)
        btn_ok.SetDefault()
        button_sizer.Add(btn_ok, 0, wx.ALL, 2)
        button_sizer.Add((0, 0), 1)
        #btn_can = wx.Button(panel, wx.ID_CANCEL)
        #button_sizer.Add(btn_can, 0, wx.ALL, 2)
        #button_sizer.Add((0, 0), 1)
        sizer.Add(button_sizer, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Fit(panel)
        self.ClientSize = panel.Size

        cal.Bind(wx.EVT_KEY_DOWN, self.on_key_down)
        cal.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        cal.SetFocus()
        self.cal = cal

    def on_key_down(self, evt):
        code = evt.KeyCode
        if code == wx.WXK_TAB:
            self.cal.Navigate()
        elif code in (wx.WXK_RETURN, wx.WXK_NUMPAD_ENTER):
            self.EndModal(wx.ID_OK)
        elif code == wx.WXK_ESCAPE:
            self.EndModal(wx.ID_CANCEL)
        else:
            evt.Skip()
    def on_left_down(self, evt):
        self.EndModal(wx.ID_OK)
        evt.Skip()
