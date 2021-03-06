# coding: utf-8
import urllib2, urllib, cookielib
import re
import config
import json

class Helper(object):
	def __init__(self):
		cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
		self.opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)

	def get_token(self):
		req = urllib2.Request(url=config.LOGIN_URL, headers=config.HEADERS)
		resp = self.opener.open(req)
		html = resp.read()
		token = ''
		try:
			m = re.search('<input.*name="token".*value="([\d|\w]+)"', html)
			token = m.group(1)
		except Exception, e:
			pass
		return token

	def get_new_token(self):
		#req = urllib2.Request(url=config.LOGIN_URL, headers=config.HEADERS)
		#req = urllib2.Request(url=r'http://solupro.org/login.html', headers=config.HEADERS)
		#resp = self.opener.open(req)
		#html = resp.read()
		token = {}
		try:
		#	m = re.search('"DMM_TOKEN",\W+"([\d|\w]+)"', html)
		#	dmm_token = m.group(1)
		#	m = re.search('"token":\W+"([\d|\w]+)"', html)
		#	req_token = m.group(1)

		#	hs = config.HEADERS
		#	hs['Content-Type'] = 'pplication/x-www-form-urlencoded; charset=UTF-8'
		#	hs['X-Requested-With'] = 'XMLHttpRequest'
		#	hs['DMM_TOKEN'] = dmm_token
		#	data = {
		#		"token" : req_token,
		#	}
		#	data = urllib.urlencode(data)

		#	req = urllib2.Request(url=config.TOKEN_URL, data=data, headers=hs)
			req = urllib2.Request(url=config.TOKEN_URL) #nothing to do, just request
			resp = self.opener.open(req)
			#resp = urllib2.urlopen(req)
			token = json.loads(resp.read())

		except Exception, e:
			pass
		#print dmm_token, req_token
		return token

	def login(self, account, password, token):
		data = {
			"login_id" : account,
			"password" : password,
			"path" : '',
			"save_login_id" : '0',
			"save_password" : '0',
			"token" : token,
		}
		data = urllib.urlencode(data)

		req = urllib2.Request(url=config.POST_URL, data=data, headers=config.HEADERS)
		resp = self.opener.open(req)
		#print resp.read()

	def new_login(self, account, password, token):
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
		data = urllib.urlencode(data)

		req = urllib2.Request(url=config.POST_URL, data=data, headers=config.HEADERS)
		resp = self.opener.open(req)
		#print resp.read()


	def get_play_url(self):
		req = urllib2.Request(url=config.GAME_URL, headers=config.HEADERS)
		resp = self.opener.open(req)
		html = resp.read()
		play_url = ''
		try:
			m = re.search('URL\W+:\W+"(.*)",', html)
			play_url = m.group(1)
		except Exception, e:
			pass
		return play_url

if __name__ == '__main__':
	h = Helper()
	token = h.get_new_token()
	h.new_login('account', 'password', token)
	print h.get_play_url()
