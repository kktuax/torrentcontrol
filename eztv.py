import re
import requests
from bs4 import BeautifulSoup

class EztvMagnetProvider(object):
	def search_magnets(self, text):
		SEARCH_URL = "http://eztv.it/search/"
		payload = {
			'SearchString1': text
		}
		r = requests.post(SEARCH_URL, data=payload)
		soup = BeautifulSoup(r.text)
		results = dict()
		for result in soup.findAll('tr', class_='forum_header_border'):
			amagnet = result.find('a', href=re.compile(r'^magnet'))
			magnet_url = None
			if amagnet is not None and 'href' in amagnet.attrs:
				magnet_url = amagnet.attrs['href']
			info = result.find('a', class_='epinfo')
			if info and magnet_url:
				results[info.text] = magnet_url
		return results
