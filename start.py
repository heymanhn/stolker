from flask import Flask
app = Flask(__name__)

@app.route('/')
def good_evening():
	return 'Good evening sir!'

if __name__ == '__main__':
	app.debug = True
	app.run()
