import re, json, os, urllib2
from eztv import EztvMagnetProvider

def submit_to_transmission(transmission_location, link):
	url = transmission_location + '/rpc?method=torrent-add&filename=' + link
	urllib2.urlopen(url)

def parse_json_conf(fname):
	abspath = os.path.abspath(__file__)
	dname = os.path.dirname(abspath)
	os.chdir(dname)
	conf = {}
	if os.path.isfile(fname):
		conf = json.load(open(fname))
	return(conf)
	

conf = parse_json_conf('torrentdownloader.conf')


providers = list()
providers.append(EztvMagnetProvider())

search_text = "futurama"

eresults = dict()
episode_re = re.compile(".+([sS]\d+[eE]\d+).+")
for provider in providers:
	results = provider.search_magnets(search_text)
	for key in results.keys():
		episode_res = episode_re.search(key)
		if episode_res:
			eresults[episode_res.group(1)] = results[key]

last_episode = sorted(eresults.keys(), reverse=True)[0]
