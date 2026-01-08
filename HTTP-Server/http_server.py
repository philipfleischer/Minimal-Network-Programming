# In terminal run: python3 -m https.server
# Serving HTTP on :: port 8000
# Made serverdir and inside: test1.txt and test2.xlsx in the HTTP-Server directory
# bruker@MacBook-Pro-2 serverdir % ipconfig getifaddr en0
# 192.168.1.11
# python3 -m http.server 8000 -b 192.168.1.11
# RESULT: Serving HTTP on 192.168.1.11 port 8000 (http://192.168.1.11:8000/) ...
# bruker@MacBook-Pro-2 serverdir % curl 192.168.1.11:8000
# <html><body>Hello World!</body></html>%

from email.policy import HTTP
from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.1.11"
PORT = 8000


class PhilipefHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body>Hello World!</body></html>", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time":"' + date + '"}', "utf-8"))


server = HTTPServer((HOST, PORT), PhilipefHTTP)
print(f"Server now running...\nHOST={HOST}\nPORT={PORT}")
server.serve_forever()
server.server_close()
print("Server Stopped!")
