from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

if __name__ == '__main__':
    server = ThreadingSimpleServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)
    print("Serving HTTP on 127.0.0.1:3000...")
    server.serve_forever()
