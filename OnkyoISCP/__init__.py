import eg
import socket

eg.RegisterPlugin(
    name = "Onkyo ISCP",
    author = "Alexander Hartmaier",
    version = "0.02",
    kind = "external",
    description = "Controls any Onkyo Receiver which supports the ISCP protocol."
)

class OnkyoISCP(eg.PluginBase):

    def __init__(self):
        self.AddAction(SendCommand)

    def __start__(self, ip, port):
        self.ip = ip
        self.port = int(port)
        self.socket = socket.socket()
	self.Connect()

    def __stop__(self):
    	self.socket.close()

    def Connect(self):
        s = self.socket
	ip = self.ip
	port = self.port
        try:
	    s.connect((ip, port))
        except:
            print "OnkyoISCP failed to connect to " + ip + ":" + str(port)
        else:
            print "OnkyoISCP connected to " + ip + ":" + str(port)
        

    def Configure(self, ip="", port=60128):
        panel = eg.ConfigPanel()
        textControl = wx.TextCtrl(panel, -1, ip)
        textControl2 = wx.TextCtrl(panel, -1, port)
        panel.sizer.Add(wx.StaticText(panel, -1, "IP address of Onkyo receiver"))
        panel.sizer.Add(textControl)
        panel.sizer.Add(textControl2)
        while panel.Affirmed():
            panel.SetResult(textControl.GetValue(), textControl2.GetValue())

class SendCommand(eg.ActionBase):

    def __call__(self, Command):
        length = len(Command) + 1
        code = chr(length)
        line = "ISCP\x00\x00\x00\x10\x00\x00\x00" + code + "\x01\x00\x00\x00!1" + Command + "\x0D"
    	s = self.plugin.socket
        try:
            s.send(line)
	    #data = s.recv(80)
        except socket.error, msg:
            # try to reopen the socket on error
            # happens if no commands are sent for a long time
            try:
		self.plugin.Connect()
                s.send(line)
            except socket.error, msg:
                print "Error " + msg

    def Configure(self, Command=""):
        panel = eg.ConfigPanel()
        textControl = wx.TextCtrl(panel, -1, Command)
        panel.sizer.Add(textControl)
        while panel.Affirmed():
            panel.SetResult(textControl.GetValue())
