from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<table border="5" cellpadding="20" >
            
    <th bgcolor="Pink">
        S.no
    </th>
    <th bgcolor="Cyan">
        Ram
    </th>
    <th bgcolor="brown">
        VRam
    </th>

    <tr>
        <td>1</td>
        <td>16</td>
        <td>4</td>
    </tr>

    <tr>
        <td>2</td>
        <td>24</td>
        <td>8</td>
    </tr>

    <tr>
        <td>3</td>
        <td>32</td>
        <td>12</td>
    </tr>
            
</table>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()