# coding: utf-8

HOST = '0.0.0.0'
PORT = 8677
DEBUG = True

LOGIN_URL = 'https://www.dmm.com/my/-/login/'
TOKEN_URL = 'https://www.dmm.com/my/-/login/ajax-get-token/'
POST_URL = 'https://www.dmm.com/my/-/login/auth/'
GAME_URL = 'http://www.dmm.com/netgame/social/-/gadgets/=/app_id=854854/'

HEADERS = {
	"User-Agent" 	: "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:26.0) Gecko/20100101 Firefox/26.0",
	#"Host" 			: "www.dmm.com",
	#"Referer" 		: "https://www.dmm.com/my/-/login/",
	#"X-Forwarded-For" : IPADDR,
}
