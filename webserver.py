import http.server
import socketserver
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

port = config.get('port', 8000)

purple_text = "\033[95mWEBSOCKET: Started on port {}\033[0m".format(port)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        return "web/index.html"

with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(purple_text)
    httpd.serve_forever()