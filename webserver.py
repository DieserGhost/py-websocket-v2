import http.server
import socketserver
import json
import os

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Get the port from the configuration file, default to 8000 if not specified
port = config.get('port', 8000)

# Print message indicating the WebSocket has started on the specified port
purple_text = "\033[95mWEBSOCKET: Started on port {}\033[0m".format(port)

# Define the request handler class
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        cwd = os.getcwd()
        web_dir = os.path.join(cwd, 'web')
        if not os.path.isdir(web_dir):
            os.makedirs(web_dir)
        return os.path.join(web_dir, path.lstrip('/'))

# Create and start the HTTP server
with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(purple_text)
    httpd.serve_forever()
