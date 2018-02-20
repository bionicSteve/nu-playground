from http.server import BaseHTTPRequestHandler, HTTPServer

class myHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        msg = '<h1>Hello World!</h1>'
        
        self.wfile.write(bytes(msg, 'utf8'))
        return


def run():
    print("Starting Web Server...")
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myHTTPServer)
    print(f"Running server http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
