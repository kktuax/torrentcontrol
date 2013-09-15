#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, json, os
from eztv import EztvMagnetProvider
from apscheduler.scheduler import Scheduler
from transmissionremote import start_torrent, stop_torrent, add_torrent, get_ids

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

def stop_torrents():
	map( stop_torrent, get_ids() )

def start_torrents():
	map( start_torrent, get_ids() )

def add_new_serie_episodes():
	providers = list()
	providers.append(EztvMagnetProvider())
	history_fname = 'history.json'
	history = load_json(history_fname)
	episode_re = re.compile(".+([sS]\d+[eE]\d+).+")
	series = load_json('torrentdownloader.conf').get('series', [])
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
			
	with open(history_fname, 'w') as outfile:
		json.dump(history, outfile, indent=4)
		
sched = Scheduler()
conf = load_json('torrentdownloader.conf')
time_re = re.compile("(\d+):(\d+)")
start_res = time_re.search(conf.get('download-start-time', ""))
stop_res = time_re.search(conf.get('download-stop-time', ""))
if start_res and stop_res:
	start_hour = start_res.group(1)
	start_minute = start_res.group(2)
	stop_hour = stop_res.group(1)
	stop_minute = stop_res.group(2)
	print "Scheduling start at " + start_hour + ":" + start_minute
	sched.add_cron_job(start_torrents, hour=start_hour, minute=start_minute)
	print "Scheduling stop at " + stop_hour + ":" + stop_minute
	sched.add_cron_job(stop_torrents, hour=stop_hour, minute=stop_minute)

series_res = time_re.search(conf.get('series-search-time', "2:00"))
if series_res:
	series_hour = series_res.group(1)
	series_minute = series_res.group(2)
	print "Scheduling series search at " + series_hour + ":" + series_minute
	sched.add_cron_job(add_new_serie_episodes, hour=series_hour, minute=series_minute)

sched.start()

while True:
	pass
