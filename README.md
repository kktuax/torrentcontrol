torrentcontrol
==============

Torrentcontrol lets you automate usual tasks with [transmission BT client](http://www.transmissionbt.com/):

 * Automatic download of new episodes
 * Schedule download times  

# Install the dependencies

    sudo apt-get install python-pip transmission-cli
    sudo pip install beautifulsoup4 apscheduler requests

# Clone torrentcontrol and launch

    sudo apt-get install git
    cd ~
    git clone git://github.com/kktuax/torrentcontrol.git
    cd ~/torrentcontrol
    nohup python torrentcontrol.py >/dev/null 2>&1 &
	
# Configuration file

You can customize download times and automatic serie's episode addition editing torrentcontrol.conf:

	{
	"download-start-time": "1:30",
	"download-stop-time": "8:30",
	"series-search-time": "2:00",
	"series": [
		"futurama",
		"game of thrones",
		"boardwalk empire",
		"dexter",
		"treme",
		"mad men",
		"big bang theory",
		"wallander",
		"true blood",
		"it crowd"
		]
	}
