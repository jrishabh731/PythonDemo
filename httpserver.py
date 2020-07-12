## HTTP Server Code
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from io import BytesIO


class WebServerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            print(dir(self))
            print(self.path)
            if self.path.endswith("/hello"):
                self.send_response(200, "OK")
                self.send_header('Content-type', 'application-json')
                self.end_headers()
                self.wfile.write(b'Hello World')
        except IOError:
            self.send_error(401, 'File not found')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        send_response = self.send_response(200, "OK")
        response = send_response
        # self.send_header('Content-type', 'application-json')
        self.end_headers()
        resp = BytesIO()
        resp.write(body)
        self.wfile.write(resp.getvalue())

def run(server_class=HTTPServer,
        handler_class=WebServerHandler):
    server_address = ('localhost', 8080)
    try:
        print("Starting server")
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard Interrrupt")
        httpd.socket.close()

run()