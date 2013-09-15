import re, json, os
from eztv import EztvMagnetProvider
from apscheduler.scheduler import Scheduler
from transmissionremote import start_torrent, stop_torrent, get_ids

def chdir():
	abspath = os.path.abspath(__file__)
	dname = os.path.dirname(abspath)
	os.chdir(dname)

def load_json(fname):
	conf = {}
	if os.path.isfile(fname):
		conf = json.load(open(fname))
	return(conf)

sched = Scheduler()

def stop_torrents():
	map( stop_torrent, get_ids() )

def start_torrents():
	map( start_torrent, get_ids() )

chdir()
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


sched.start()
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
