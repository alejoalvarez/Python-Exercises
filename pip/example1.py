# pip install wxPython
import wx


app = wx.App()
window = wx.Frame(parent=None,title="Hello World")
window.Show()
app.MainLoop()

#Example 2
class Window(wx.Frame):

    def __init__(self, *args, **kw):
        super(Window, self).__init__(*args, **kw)
        self.button1 = wx.Button(self, label="Press button")
        self.Bind(wx.EVT_BUTTON, self.press_button, self.button1)


    def press_button(self, event):
        wx.MessageBox("Hello World")


app1 = wx.App()
frm = Window(None, title='Test')
frm.Show()
app1.MainLoop()

