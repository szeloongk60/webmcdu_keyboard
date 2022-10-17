import SimpleHTTPServer
import SocketServer
import xpc

client=xpc.XPlaneConnect()
class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
      #  if(self.path =="/M.html"): 
      #      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
       # gear_dref = "sim/custom/xap/mcdu/click_" + self.path[1:]
        #client.sendDREF(gear_dref, 1)
        #self.path="M.html"
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        gear_dref = "sim/custom/xap/mcdu/click_" + post_body
        client.sendDREF(gear_dref, 1)
        print gear_dref
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
    def do_action(self, path, args):
        print "ATC"
        print path
        print args
        
PORT = 110
 
Handler = ServerHandler
 
httpd = SocketServer.TCPServer(("", PORT), Handler)
 
print "serving at port", PORT
httpd.serve_forever()
      
