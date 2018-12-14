import IR
from flask import Flask, request, Markup, render_template
from flask_restful import Resource, Api
import codecs

app = Flask(__name__)
api = Api(app)

labels = [
    'Positive Tweets','Neutral Tweets','Negative Tweets'
]

colors = [
    "#46BFBD", "#FEDCBA", "#FF4500"]

@app.route('/')
def start():
	# f=codecs.open("./index.html",'r')
	# button = f.read()
	button =  ('   <head>   '  + 
'       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">   '  + 
'       <link rel="stylesheet" type="text/css" href="sentimen-partai-frontend/css/main.css">   '  + 
'   </head>   '  + 
'        '  + 
'   <body>   '  + 
'       <header class="header">   '  + 
'           <script type="text/javascript" src="sentimen-partai-frontend/js/main.js"></script>   '  + 
'       </header>   '  + 
'       <div class="container">   '  + 
'           <br/>   '  + 
'           <br/>   '  + 
'           <br/>   '  + 
'           <br/>   '  + 
'           <table> '  + 
'               <tr> '  + 
'                   <td> '  + 
'                       <a href="/PKB">   '  + 
'                           <img border="0" alt="PKB" src="https://2.bp.blogspot.com/-zo6KAbLT6Ps/VcBsTo6Jq-I/AAAAAAAAAkA/pc8VrY9Mhfs/s1600/Logo%2BPKB.jpg" width="100" height="100">'  + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PKB"> '  + 
'                           </div>   '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/GERINDRA">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/1/18/Logo_Gerindra.svg/504px-Logo_Gerindra.svg.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="GERINDRA"> '  + 
'                           </div>  '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/PDIP">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/0/09/LOGO-_PDIP.svg/531px-LOGO-_PDIP.svg.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PDIP"> '  + 
'                           </div> '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/GOLKAR">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/f/f4/Logo_Golkar.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="GOLKAR"> '  + 
'                           </div> '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td>   '  + 
'                       <a href="/NASDEM">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/d/d1/NasDem_Logo.png/424px-NasDem_Logo.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="NASDEM"> '  + 
'                           </div> '  + 
'                       </a>   '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/Partai Garuda">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/5/59/Logo_Partai_Garuda.svg/640px-Logo_Partai_Garuda.svg.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="GARUDA"> '  + 
'                           </div> '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/Partai BERKARYA">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/c/cf/Logo_Partai_Berkarya.svg/600px-Logo_Partai_Berkarya.svg.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="BERKARYA"> '  + 
'                           </div> '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/PKS">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/5/5c/PKS_Logo.svg/453px-PKS_Logo.svg.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PKS"> '  + 
'                           </div>  '  + 
'                       </a>   '  + 
'                   </td> '  + 
'               </tr> '  + 
'               <tr> '  + 
'                   <td> '  + 
'                       <a href="/PERINDO">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/3/32/PartaiPerindo.png/499px-PartaiPerindo.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PERINDO"> '  + 
'                           </div> '  + 
'                       </a>   '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/PPP">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/7/73/Logo_PPP.svg/600px-Logo_PPP.svg.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PPP"> '  + 
'                           </div> '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td>   '  + 
'                       <a href="/PSI">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/LogoPSI.svg/474px-LogoPSI.svg.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PSI"> '  + 
'                           </div> '  + 
'                       </a>   '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/Partai PAN">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/2/2f/Logo_PAN.svg/426px-Logo_PAN.svg.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PAN"> '  + 
'                           </div> '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td>   '  + 
'                       <a href="/HANURA">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/thumb/2/24/Logo_Hanura.svg/640px-Logo_Hanura.svg.png" width="100" height="100"> ' + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="HANURA"> '  + 
'                           </div> '  + 
'                       </a> '  + 
'                   </td> '  + 
'                   <td>   '  + 
'                       <a href="/DEMOKRAT">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/commons/d/d6/Democratic_Party_%28Indonesia%29.svg" width="100" height="100">'    + 
'                           <div class="imgButton"> '  + 
'                                   <input class="btn" type="button" value="DEMOKRAT"> '  + 
'                           </div>  '  + 
'                       </a>   '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/PARTAI BULAN BINTANG">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Partai_Bulan_Bintang_Logo.jpg/640px-Partai_Bulan_Bintang_Logo.jpg" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PBB"> '  + 
'                           </div> '  + 
'                       </a>   '  + 
'                   </td> '  + 
'                   <td> '  + 
'                       <a href="/PKPI">   '  + 
'                           <img border="0" alt="PKB" src="https://upload.wikimedia.org/wikipedia/id/a/ad/Logo_PKPI.png" width="100" height="100">'   + 
'                           <div class="imgButton"> '  + 
'                               <input class="btn" type="button" value="PKPI"> '  + 
'                           </div>   '  + 
'                       </a> '  + 
'                   </td>   '  + 
'               </tr> '  + 
'           </table> '  + 
'       </div>   '  + 
'            '  + 
'       <nav class="navbar navbar-expand-lg fixed-top ">     '  + 
'           <a class="navbar-brand" href="#">Sentimen Partai</a>   '  + 
'       </nav>   '  + 
'   </body>    '  + 
'   <style>   '  + 
'       .navbar{  '  + 
'           background:#F97300; '  + 
'       } '  + 
'       .nav-link , .navbar-brand{  '  + 
'           color: #f4f4f4;  '  + 
'           cursor: pointer; '  + 
'       } '  + 
'       /*header style*/ '  + 
'       .header{ '  + 
'           background-attachment: fixed; '  + 
'           background-size: cover; '  + 
'           background-position: center; '  + 
'       } '  + 
'       .overlay{ '  + 
'           position: absolute; '  + 
'           min-height: 100%; '  + 
'           min-width: 100%; '  + 
'           left: 0; '  + 
'           top: 0; '  + 
'           background: rgba(244, 244, 244, 0.79); '  + 
'       }  '  + 
'       .imgButton, img{ '  + 
'           text-align:center; '  + 
'       } '  + 
'       table { '  + 
'           border-collapse: separate; '  + 
'           border-spacing: 30px 0; '  + 
'       } '  + 
'       td { '  + 
'           padding: 10px 0; '  + 
'       } '  + 
'       td:hover { '  + 
'           background: #F97300; '  + 
'           border-radius: 25px; '  + 
'       } '  + 
'  </style> ' )

	# button = "<div class='container'><a href='/PKB'><input type='button' value='PKB'></a><br/><br/><a href='/GERINDRA'><input type='button' value='GERINDRA'></a><br/><br/><a href='/PDIP'><input type='button' value='PDIP'></a><br/><br/><a href='/GOLKAR'><input type='button' value='GOLKAR'></a><br/><br/><a href='/NASDEM'><input type='button' value='NASDEM'></a><br/><br/><a href='/Partai BERKARYA'><input type='button' value='Partai BERKARYA'></a><br/><br/><a href='/PKS'><input type='button' value='PKS'></a><br/><br/><a href='/PERINDO'><input type='button' value='PERINDO'></a><br/><br/><a href='/PPP'><input type='button' value='PPP'></a><br/><br/><a href='/PSI'><input type='button' value='PSI'></a><br/><br/><a href='/PAN'><input type='button' value='PAN'></a><br/><br/><a href='/HANURA'><input type='button' value='HANURA'></a><br/><br/><a href='/DEMOKRAT'><input type='button' value='DEMOKRAT'></a><br/><br/><a href='/PARTAI BULAN BINTANG'><input type='button' value='PARTAI BULAN BINTANG'></a><br/><br/><a href='/PKPI'><input type='button' value='PKPI'></a><br/><br/></div>"

	return button
   
@app.route('/<partai>')
def showChart(partai):
	pie_labels = labels
	pos = IR.main(partai, "pos")
	neg = IR.main(partai, "neg")
	net = IR.main(partai, "net")
	values = [
    pos, neg, net
	]
	pie_values = values
	return (render_template('chart.html', sentiment=(IR.main(partai, 0)).decode('utf-8'), title='Analisa Sentimen Tweet mengenai' + partai, max=17000, set=zip(values, labels, colors)))



if __name__ =='__main__':
   app.run()