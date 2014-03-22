from flask import Flask, render_template
from crawler import crawl

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Nothing here.'

@app.route('/symbol/<symbol>')
def show_stock_price(symbol):
	price = crawl.fetch_price(symbol)
	app.logger.debug("Price is %s" % price)
	return render_template('stock_price.html', symbol=symbol, price=price)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
