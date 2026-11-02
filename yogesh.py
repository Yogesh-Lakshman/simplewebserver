from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Comp Device web page</title>
    </head>
    <body bgcolor="white">
    
        <table border="3" cellspacing="5" cellpadding="12" align="center" width="500" height="600">
            <caption>Laptop Config</caption>
            <caption><b>P.YOGESH LAKSHMAN</b></caption>
            <caption>26009783</caption>
            <tr bgcolor="cyan">
               <th>S.No.</th>
               <th>Device Type</th>
               <th>Device Info</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Device Name</td>
                <td>TL15-53M-G2

                </td>
            </tr>
                <td>2</td>
                <td>Processor</td>
                <td>Intel(R) Core(TM) 5 210H (2.20 GHz)

                </td>
            <tr>
                <td>3</td>
                <td>Installed RAM</td>
                <td>16.0 GB (15.7 GB usable)

                </td>

            </tr>
            <tr>
                <td>4</td>
                <td>Graphics card</td>
                <td>Intel(R) Graphics (128 MB)
                </td>
            </tr>
            <tr>
                <td>5</td>
                <td>Storage</td>
                <td>120 GB of 477 GB used
                </td>

            </tr>
            <tr>
                <td>6</td>
                <td>Device ID</td>
                <td>	C80D61B4-E391-40D8-BA6D-9D95B6F3A4FD
                </td>
            </tr>
            <tr>
                <td>7</td>
                <td>Product ID</td>
                <td>	00342-42954-08623-AAOEM
                </td>
            </tr>
            <tr>
                <td>8</td>
                <td>System Type</td>
                <td>	64-bit operating system, x64-based processor
                </td>

            </tr>
            <tr>
                <td>9</td>
                <td>Pen and touch</td>
                <td>No pen or touch input is available for this display
                </td>
            </tr>
            

        </table>
    
    
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()