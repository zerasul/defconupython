import network
import machine
import usocket

class WebController:
    fcontroller=None
    dcontroller=None
    TEMPLATE="template.html"
    def __init__(self,fcontroller,dcontroller):
        self.fcontroller=fcontroller
        self.dcontroller=dcontroller

    def initServer(self, port):
        server = usocket.socket()
        server.bind(('0.0.0.0', 80))
        server.listen(1)
        while True:
            try:
               (socket, sockaddr) = server.accept()
               self.__handle__(socket)
            except Exception as e:
              print(e)
              socket.write("HTTP/1.1 500 Internal Server Error\r\n\r\n")
              socket.write("<h1>Internal Server Error</h1>")
            socket.close()

    def __handle__(self,socket):
        (method, url, version) = socket.readline().split(b" ")
        print(method, url, version)
        print(socket.readline())
        if b"?" in url:
            (path, query) = url.split(b"?", 2)
            listquery = query.split(b"=",2)
            if listquery[0] == b"defcon":
                nextstate = int(listquery[1])
        else:
             (path, query) = (url, b"")
             nextstate = self.dcontroller.get_current_state()
        while True:
            header = socket.readline()
            if header == b"":
                return
            if header == b"\r\n":
                break
        if version != b"HTTP/1.0\r\n" and version != b"HTTP/1.1\r\n":
            self.err(socket, "505", "Version Not Supported")
        elif method == b"GET":
            if path == b"/":
                self.fcontroller.write_2_flash(nextstate)
                self.dcontroller.changestate(nextstate)
                self.ok(socket, query)
            else:
             self.err(socket, "404", "Not Found")
        else:
            self.err(socket, "501", "Not Implemented")
    
    def ok(self,socket, query):
        f = open(self.TEMPLATE,'r')
        html=f.readlines()
        socket.write("HTTP/1.1 OK\r\n")
        socket.write("Content-Type: text/html\r\n\r\n")
        for strhtml in html:
            strhtml=strhtml.replace("#{defcon}",str(self.dcontroller.get_current_state()))
            socket.write(strhtml)

    def err(self, socket, code, message):
        socket.write("HTTP/1.1 OK\r\n\r\n")
        mesage = "<html><head><title>Error {}</title></head><body><h1>Error {}</h1><p>{}".format(code,code,message)
        socket.write(mesage)
