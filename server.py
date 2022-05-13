import os
import http.server
import socketserver

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/drive":
            self.send_response(301)
            self.send_header('Location','https://drive.google.com/drive/folders/1EH-B_y-9JhCPLdEB7sAHNUU02QIkf-WB')
            self.end_headers()

        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello Shubham! you requested %s' % (self.path)
        self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
