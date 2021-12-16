import os
import logging

logging.basicConfig(level=logging.NOTSET)

from http.server import BaseHTTPRequestHandler,HTTPServer

hostName = "localhost"
serverPort = 8080 

class sojernWebServer(BaseHTTPRequestHandler):      

    def do_GET(self):   
        try:            
            print ('Get request received')  
            
            path = self.path
            cwd = os.getcwd()
            fullpath = cwd+path
            

            if self.path.endswith("/tmp"):            
                if os.path.exists(fullpath):                        
                    self.send_response(200, "OK")                
                    self.send_header("Content-type", "text/html")
                    self.end_headers() 
                    self.wfile.write(bytes("<html><head><title>https://sojerntrackingwebserver.com</title></head>", "utf-8"))
                    self.wfile.write(bytes("<p> Request sent : %s</p>" % path, "utf-8"))
                    self.wfile.write(bytes("<body>", "utf-8"))                
                    self.wfile.write(bytes("<p> OK </p>", "utf-8"))
                    self.wfile.write(bytes("</body></html>", "utf-8"))
                    return               
                else:                                            
                    self.send_error(503, 'Service Unavailable: %s' % path)                                                
            elif self.path.endswith("/img"):                
                if os.path.exists(fullpath):                  
                    print("Gif Image")
                    self.send_response(200, "OK")
                    self.send_header("Content-Type", "image/gif")
                    self.end_headers()                    
                    logging.info("Request logged")            

                    self.wfile.write(open(fullpath + '/error_3x3.gif','rb').read())                    
                    return
                else:                                            
                    self.send_error(503, 'Image File Not Found: %s' % path)      
            else:
                print("Request fullpath ELSE : ", fullpath)                                            
                self.send_error(404, 'Bad Request : %s' % path)                 
        except IOError:
            self.send_error(503, 'File Not Found Exception: %s' % path)            

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), sojernWebServer)       
    print("Sojern Server started http://%s:%s" % (hostName, serverPort))    
    
try:    
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
webServer.server_close()  
print("Server stopped.")