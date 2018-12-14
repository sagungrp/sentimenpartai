import IR
from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

@app.route('/')
def start():
	button = "<div class='container'><button class='btn'>PKB</button><button class='btn'>GERINDRA</button><button class='btn'>PDIP</button><button class='btn'>GOLKAR</button><button class='btn'>NASDEM</button><button class='btn'>Partai BERKARYA</button><button class='btn'>PKS</button><br/><br/><button class='btn'>PERINDO</button><button class='btn'>PPP</button><button class='btn'>PSI</button><button class='btn'>PAN</button><button class='btn'>HANURA</button><button class='btn'>DEMOKRAT</button><button class='btn'>PARTAI BULAN BINTANG</button><button class='btn'>PKPI</button></div><a href='/PKB'><input type='button' value='PKB'></a>"

	

	return button
   
@app.route('/<partai>')
def hello_name(partai):
	return IR.main(partai)


if __name__ == '__main__':
   app.run()