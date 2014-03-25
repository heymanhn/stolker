# Fetch a stock price from Google Finance's website
import urllib2, locale
from bs4 import BeautifulSoup

locale.setlocale( locale.LC_ALL, '' )
GOOGLE_FINANCE_URL = 'http://www.google.com/finance?q='

def fetch_price(ticker_symbol):
	# We know the fixed URL pattern for Google Finance	
	url = GOOGLE_FINANCE_URL + ticker_symbol.upper()
	response = urllib2.urlopen(url)
	html = response.read()

	html_tree = BeautifulSoup(html, "lxml")
	price = html_tree.find(class_='pr')

	if price:
		return locale.atof(price.get_text())
	else:
		return None
