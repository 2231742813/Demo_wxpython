# coding=utf-8
import wx


class MaimFrame(wx.Frame) :
    def __init__(self, parent, id) :
        wx.Frame.__init__(self, parent, id, title = "Demo_wxpython V1.0.0", pos = (100, 100), size = (860, 845))
        # 创建第一个面板
        panel = wx.Panel(self, pos = (0, 0), size = (160, 190))
        # 控件
        self.text_ip = wx.StaticText(panel, label = "IP", pos = (5, 10))
        self.text_port = wx.StaticText(panel, label = "port", pos = (5, 40))
        self.text_username = wx.StaticText(panel, label = "username", pos = (5, 70))
        self.text_password = wx.StaticText(panel, label = "password", pos = (5, 100))

        # 控件
        self.label_ip = wx.TextCtrl(panel, pos = (65, 10), size = (85, 20), style = wx.TE_LEFT)
        self.label_port = wx.TextCtrl(panel, pos = (65, 40), size = (85, 20), style = wx.TE_LEFT)
        self.label_username = wx.TextCtrl(panel, pos = (65, 70), size = (85, 20), style = wx.TE_LEFT)
        self.label_password = wx.TextCtrl(panel, pos = (65, 100), size = (85, 20), style = wx.TE_LEFT)

        # 设置控件默认值
        self.label_ip.SetValue('1111')
        self.label_port.SetValue('1111')
        self.label_username.SetValue('1111')
        self.label_password.SetValue('1111')


        # 创建第二个面板（----------------测试结果显示框-----------------------------）
        panel1 = wx.Panel(self, pos = (162, 0), size = (698, 800))
        self.show_text = wx.TextCtrl(panel1, id = -1, value = '', pos = (0, 0), size = (680, 790),
                                     style = wx.TE_MULTILINE | wx.TE_READONLY)

        # 获取按钮
        panel5 = wx.Panel(self, pos = (0, 191), size = (160, 80))
        self.get_lst = wx.Button(panel5, label = '获取', pos = (20, 35), size = (100, 30))
        self.get_lst.Bind(wx.EVT_BUTTON, self.get_lsts)


    # 获取按钮的Demo函数
    def get_lsts(self,event) :
        self.show_text.AppendText('\n-------------------------------你好-------------------------------\n')

def main() :
    app = wx.App()
    win = MaimFrame(parent = None, id = -1)  # 创建窗体
    win.Show()  # 显示窗体
    app.MainLoop()  # 运行程序


if __name__ == "__main__" :
    main()
