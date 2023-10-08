import http.server
import socketserver
directory = ""  # Set the the path of your directory
ip = '127.0.0.1'#Set the ip address
port = 8000 # Set the port number
#server
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
#client
with socketserver.TCPServer((ip, port), MyHandler) as httpd:
    print(f"Serving at http://{ip}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
