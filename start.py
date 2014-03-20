from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, everyone on Earth!'

@app.route('/user/<user>')
def good_morning(user):
	app.logger.debug('Just checking')
	return render_template('user.html', username=user)

@app.route('/profile/<int:profile_id>')
def good_evening(profile_id):
	return 'Good evening, profile %d!' % profile_id

@app.route('/projects/')
def projects():
	return 'This is where you assign projects.'

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
