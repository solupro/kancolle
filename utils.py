# coding: utf-8
import urllib2, urllib, cookielib
import re
import config

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
	print h.get_play_url()
