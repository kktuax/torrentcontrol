import re
from eztv import EztvMagnetProvider

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
