import IR
from flask import Flask, request
from flask_restful import Resource, Api
import codecs

app = Flask(__name__)
api = Api(app)

@app.route('/')
def start():
	# f=codecs.open("./index.html", 'r')
	# button = f.read()
	button =  ('   <!-- navbar -->    '  + 
'   <head>  '  + 
'           <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">  '  + 
'       <link rel="stylesheet" type="text/css" href="sentimen-partai-frontend/css/main.css">  '  + 
'   </head>  '  + 
'     '  + 
'   <body>  '  + 
'       <header class="header">  '  + 
'           <script type="text/javascript" src="sentimen-partai-frontend/js/main.js"></script>  '  + 
'       </header>  '  + 
'       <div class="container">  '  + 
'           <br/>  '  + 
'           <br/>  '  + 
'           <br/>  '  + 
'           <br/>  '  + 
'           <a href="/PKB">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PKB">  '  + 
'           </a>  '  + 
'           <a href="/GERINDRA">  '  + 
' 				<img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/1/18/Logo_Gerindra.svg/504px-Logo_Gerindra.svg.png" width="100" height="100"> ' +
'               <input class="btn" type="button" value="GERINDRA">  '  + 
'           </a>  '  + 
'           <a href="/PDIP">  '  + 
' 				<img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/0/09/LOGO-_PDIP.svg/531px-LOGO-_PDIP.svg.png" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PDIP">  '  + 
'           </a>  '  + 
'           <a href="/GOLKAR">  '  + 
' 				<img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/f/f4/Logo_Golkar.png" width="100" height="100"> ' +
'               <input class="btn" type="button" value="GOLKAR">  '  + 
'           </a>  '  + 
'           <a href="/NASDEM">  '  + 
' 				<img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/d/d1/NasDem_Logo.png/424px-NasDem_Logo.png" width="100" height="100"> ' +
'               <input class="btn" type="button" value="NASDEM">  '  + 
'           </a>  '  + 
'           <a href="/Partai BERKARYA">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PartaiBERKARYA">  '  + 
'           </a>  '  + 
'           <a href="/PKS">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PKS">  '  + 
'           </a>  '  + 
'           <a href="/PERINDO">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PERINDO">  '  + 
'           </a>  '  + 
'           <a href="/PPP">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PPP">  '  + 
'           </a>  '  + 
'           <a href="/PSI">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PSI">  '  + 
'           </a>  '  + 
'           <a href="/PAN">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PAN">  '  + 
'           </a>  '  + 
'           <a href="/HANURA">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="HANURA">  '  + 
'           </a>  '  + 
'           <a href="/DEMOKRAT">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="DEMOKRAT">  '  + 
'           </a>  '  + 
'           <a href="/PARTAI BULAN BINTANG">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PARTAI BULAN BINTANG">  '  + 
'           </a>  '  + 
'           <a href="/PKPI">  '  + 
' 				<img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100"> ' +
'               <input class="btn" type="button" value="PKPI">  '  + 
'           </a>  '  + 
'       </div>  '  + 
'         '  + 
'       <nav class="navbar navbar-expand-lg fixed-top ">    '  + 
'           <a class="navbar-brand" href="#">Sentimen Partai</a>  '  + 
'       </nav>  '  + 
'  </body>  ')
	return button
   
@app.route('/<partai>')
def hello_name(partai):
	return IR.main(partai)


if __name__ == '__main__':
   app.run()