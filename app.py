# coding: utf-8
from flask import Flask, request, session, g, redirect, url_for, \
		abort, render_template, flash
import utils, config

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	url = None
	if request.method == 'POST':
		url = r'http://osapi.dmm.com/gadgets/'
	else:
		pass
	print url
	return render_template('index.html', play_url=url)

if __name__ == '__main__':
	app.debug = config.DEBUG
	app.run(host=config.HOST, port=config.PORT)