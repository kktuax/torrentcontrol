#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, json, os, argparse
from eztv import EztvMagnetProvider
from transmissionremote import start_torrent, stop_torrent, add_torrent, get_ids

def stop_torrents():
	map( stop_torrent, get_ids() )

def start_torrents():
	map( start_torrent, get_ids() )

def add_new_serie_episodes(series = [], history = {}):
	providers = list()
	providers.append(EztvMagnetProvider())
	episode_re = re.compile(".+([sS]\d+[eE]\d+).+")
	for serie in series:
		print "Searching for episodes of " + serie
		eresults = dict()
		for provider in providers:
			results = provider.search_magnets(serie)
			for key in results.keys():
				episode_res = episode_re.search(key)
				if episode_res:
					eresults[episode_res.group(1)] = results[key]
		
		if history.has_key(serie):
			for episode in sorted(eresults.keys()):
				if episode > history[serie]:
					print "Found new episode: " + episode
					history[serie] = episode
					add_torrent(eresults[episode])
		else:
			last_episode = sorted(eresults.keys(), reverse=True)[0]
			history[serie] = last_episode
			
	return history

def chdir():
	abspath = os.path.abspath(__file__)
	dname = os.path.dirname(abspath)
	os.chdir(dname)

def load_json(fname):
	conf = {}
	if os.path.isfile(fname):
		conf = json.load(open(fname))
	return conf

chdir()

parser = argparse.ArgumentParser()
parser.add_argument('--start', help='Starts all torrents', action='store_true')
parser.add_argument('--stop', help='Stops all torrents', action='store_true')
parser.add_argument('--auto-series', dest="series", help='Searches for new episodes', action='store_true')
parser.add_argument('--conf-file', dest="conf", help='Location of configuration file', default= os.path.join(os.getcwd(), 'torrentcontrol.conf'))
parser.add_argument('--history-file', dest="history", help='Location of history file', default= os.path.join(os.getcwd(), 'history.json'))
args = parser.parse_args()

if args.series:
	conf = load_json(args.conf)
	series = conf.get('series', [])
	history_fname = args.history
	history = load_json(history_fname)
	history = add_new_serie_episodes(series, history)
	with open(history_fname, 'w') as outfile:
		json.dump(history, outfile, indent=4)

if args.start:
	start_torrents()
	
if args.stop:
	stop_torrents()