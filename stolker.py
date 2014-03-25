from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime
from crawler import crawl

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/stolker'
db = SQLAlchemy(app)

# Stock Price class for db model
class StockPrice(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	symbol = db.Column(db.String(10))
	price = db.Column(db.Float)
	fetch_date = db.Column(db.DateTime)

	def __init__(self, symbol, price):
		self.symbol = symbol
		self.price = price
		self.fetch_date = datetime.utcnow()

	def __repr__(self):
		return 'Symbol: {0} | Price: {1} | Time: {2}'.format(self.symbol, self.price, self.fetch_date) 

@app.route('/')
def hello_world():
	return 'Nothing here.'

@app.route('/add/<symbol>')
def store_price(symbol):
	price = crawl.fetch_price(symbol)

	if price:
		price_entry = StockPrice(symbol.upper(), price)
		db.session.add(price_entry)
		db.session.commit()
		return 'Added stock price for {0}.'.format(symbol.upper())
	else:
		return 'Symbol {0} doesn''t exist.'.format(symbol.upper())

@app.route('/symbol/<symbol>')
def show_stock_price(symbol):
	price = StockPrice.query.filter_by(symbol=symbol.upper()).order_by(desc(StockPrice.fetch_date)).first()
	return render_template('stock_price.html', symbol=symbol, price=price)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
