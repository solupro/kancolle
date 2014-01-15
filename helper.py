# coding: utf-8
import requests
import re
import config

class Helper(object):
	def __init__(self):
		self.s = requests.Session()

	def get_token(self):
		r = self.s.get(config.LOGIN_URL, headers=config.HEADERS)
		html = r.text
		token = {}
		try:
			m = re.search('"DMM_TOKEN",\W+"([\d|\w]+)"', html)
			dmm_token = m.group(1)
			m = re.search('"token":\W+"([\d|\w]+)"', html)
			req_token = m.group(1)

			hs = dict(r.headers)
			hs['Content-Type'] = 'pplication/x-www-form-urlencoded; charset=UTF-8'
			hs['X-Requested-With'] = 'XMLHttpRequest'
			hs['DMM_TOKEN'] = dmm_token
			data = {
				"token" : req_token,
			}

			r = self.s.post(config.TOKEN_URL, data=data, headers=hs)
			token = r.json()
		except Exception, e:
			pass
		return token

	def login(self, account, password, token):
		data = {
			token.get("login_id") : account,
			token.get("password") : password,
			"login_id" : account,
			"password" : password,
			"path" : '',
			"save_login_id" : '0',
			"save_password" : '0',
			"token" : token.get("token"),
		}
		r = self.s.post(config.POST_URL, data=data)
		#print r.text


	def get_play_url(self):
		r = self.s.get(config.GAME_URL)
		html = r.text
		play_url = ''
		try:
			m = re.search('URL\W+:\W+"(.*)",', html)
			play_url = m.group(1)
		except Exception, e:
			pass
		return play_url

if __name__ == '__main__':
	h = Helper()
	token = h.get_token()
	h.login('account', 'password', token)
	print h.get_play_url()
