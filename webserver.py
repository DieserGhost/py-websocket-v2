import http.server
import socketserver
import json
import os
import ssl

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

port = config.get('port', 8000)
use_https = config.get('use_https', True)
ssl_cert = config.get('ssl_cert')
ssl_key = config.get('ssl_key')

purple_text = "\033[95mWEBSOCKET: Started on port {}\033[0m".format(port)

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        cwd = os.getcwd()
        web_dir = os.path.join(cwd, 'web')
        if not os.path.isdir(web_dir):
            os.makedirs(web_dir)
        return os.path.join(web_dir, path.lstrip('/'))

if use_https and ssl_cert and ssl_key:
    with socketserver.TCPServer(("", port), MyHandler) as httpd:
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile=ssl_cert, keyfile=ssl_key, server_side=True)
        print(purple_text)
        httpd.serve_forever()
else:
    with socketserver.TCPServer(("", port), MyHandler) as httpd:
        print(purple_text)
        httpd.serve_forever()
