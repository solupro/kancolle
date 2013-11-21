# coding: utf-8
from flask import Flask, request, render_template
import utils, config

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	url = None
	if request.method == 'POST':
		account = request.form['account']
		password = request.form['password']

		url = 'Empty!!'
		helper = utils.Helper()
		try:
			token = helper.get_token()
			if token != '':
				helper.login(account, password, token)
				url = helper.get_play_url()
		except Exception, e:
			raise e

	return render_template('index.html', play_url=url)

if __name__ == '__main__':
	app.debug = config.DEBUG
	app.run(host=config.HOST, port=config.PORT)