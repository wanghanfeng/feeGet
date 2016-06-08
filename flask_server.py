# -*-encoding:utf-8-*-

from pytesser import *
from flask import Flask
from flask import flash
from flask import request
from flask import render_template
from flask import redirect, url_for
import urllib2
import getcookies_server


app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	flash('欢迎来到网卡查询....')
	return render_template('index.html',result = 'nicaichenggongfou?')

@app.route('/hello')
def hello():
	return 'hello world'

@app.route('/user/<username>')
def show_user_name(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_id(post_id):
	return 'Post id is : %d' % post_id
@app.route('/re')
def redirect():
	return redirect(url_for('index'))
@app.route('/code')
def show_result():
	impath = 'phototest.tif'
	im = Image.open(impath)
	text = image_to_string(im)
	return text

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug = True)
