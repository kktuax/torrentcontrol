import re
import requests
from bs4 import BeautifulSoup

class EztvMagnetProvider(object):
	
	SEARCH_URL = "https://eztv.it/search/"
	series = dict()		
		
	def __init__(self):   
		r = requests.get(self.SEARCH_URL)
		soup = BeautifulSoup(r.text)
		series_options = soup.findAll("option")
		for s in series_options:
			serie = s.contents[0]
			serie_id = s.attrs['value']
			if serie_id:
				self.series[serie] = serie_id

	def find_id(self, text):
		for serie,serie_id in self.series.items():
			if text.lower() in serie.lower():
				return serie_id
		print("Serie with name: " + text + " not found")
		return False
	
	def search_magnets(self, text):
		serie_id = self.find_id(text)
		if serie_id:
			payload = { 'SearchString': serie_id }
		else:
			payload = { 'SearchString1': text }	
		
		r = requests.post(self.SEARCH_URL, data=payload)
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
