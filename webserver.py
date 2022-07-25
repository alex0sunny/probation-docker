from http.server import BaseHTTPRequestHandler, HTTPServer
from os.path import curdir, sep
from os import system
from subprocess import run

from calc import calculate

PORT_NUMBER = 3000

CALC_PATH = 'calc'
HOOK_PATH = 'hook'


class CustomHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            if self.path.endswith(".html"):
                mimetype = 'text/html'
            elif self.path.endswith(".js"):
                mimetype = 'application/javascript'
            else:
                return

            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(f.read().encode())
            f.close()

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self._set_headers()

    # Handler for the POST requests
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode()
        path = self.path[1:]
        if path == CALC_PATH:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(calculate(post_data)).encode())
        if path == HOOK_PATH:
            print(system('git pull origin main'))


try:
    server = HTTPServer(('', PORT_NUMBER), CustomHandler)
    print('Started httpserver on port ', PORT_NUMBER)

    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
