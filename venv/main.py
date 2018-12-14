import IR
from flask import Flask, request, Markup, render_template
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

labels = [
    'Positive Tweets', 'Neutral Tweets', 'Negative Tweets'
]

colors = [
    "#46BFBD", "#FEDCBA", "#FF4500"]

@app.route('/')
def start():
	button = "<div class='container'><a href='/PKB'><input type='button' value='PKB'></a><br/><br/><a href='/GERINDRA'><input type='button' value='GERINDRA'></a><br/><br/><a href='/PDIP'><input type='button' value='PDIP'></a><br/><br/><a href='/GOLKAR'><input type='button' value='GOLKAR'></a><br/><br/><a href='/NASDEM'><input type='button' value='NASDEM'></a><br/><br/><a href='/Partai BERKARYA'><input type='button' value='Partai BERKARYA'></a><br/><br/><a href='/PKS'><input type='button' value='PKS'></a><br/><br/><a href='/PERINDO'><input type='button' value='PERINDO'></a><br/><br/><a href='/PPP'><input type='button' value='PPP'></a><br/><br/><a href='/PSI'><input type='button' value='PSI'></a><br/><br/><a href='/PAN'><input type='button' value='PAN'></a><br/><br/><a href='/HANURA'><input type='button' value='HANURA'></a><br/><br/><a href='/DEMOKRAT'><input type='button' value='DEMOKRAT'></a><br/><br/><a href='/PARTAI BULAN BINTANG'><input type='button' value='PARTAI BULAN BINTANG'></a><br/><br/><a href='/PKPI'><input type='button' value='PKPI'></a><br/><br/></div>"

	

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
	return (render_template('chart.html', sentiment=(IR.main(partai, 0)).decode('utf-8'), title='Analisa Sentimen Tweet mengenai ' + partai, max=17000, set=zip(values, labels, colors)))



if __name__ == '__main__':
   app.run()