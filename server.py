import http.server
import urllib.parse

import token_generation as g
import token_verification as v

class Handler(http.server.BaseHTTPRequestHandler):
    # Function for the headers
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # Display webpage on startup at localhost:8000 and verify JWT
    def do_GET(self):
        try:
            self._set_headers()
            if 'Authorization' in self.headers:
                try:
                    token = str(self.headers['Authorization'])
                    if v.verify_token(token) is True:
                        message = "Token was successfully verified"
                        self.wfile.write(message.encode())
                    else:
                        message = "Token could not be verified"
                        self.wfile.write(message.encode())
                    return
                except:
                    message = "Token could not be verified"
                    self.wfile.write(message.encode())
            else:
                try: 
                    f = open('client.html')
                    html_page = f.read()
                    f.close()
                    self.wfile.write(html_page.encode())
                except:
                    message = "An error has occured with returning the webpage"
                    self.wfile.write(message.encode())
        except:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return

    # How to handle the submitted form
    def do_POST(self):
        # Content length
        content_length = int(self.headers['Content-Length'])
        # Content data
        encoded_data = self.rfile.read(content_length)
        decoded_data = encoded_data.decode()
        # Isolating the user credentials
        credentials = dict(qc.split('=') for qc in decoded_data.split('&'))

        # Comparing the credentials to see if they are true
        # This is where it would query the database if I had one
        if credentials['username'] == 'user' and credentials['password'] == 'pass':
            # Actual generation of the token
            self._set_headers()
            token = g.generate_token(credentials['username'], credentials['password'])
            self.wfile.write(token)
            return
        else:
            self.send_response(401)
            self.end_headers()
            return
            
        return

# How to start the python server
def run(server_class=http.server.HTTPServer, handler_class=Handler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd on port: 8000")
    httpd.serve_forever()

run()