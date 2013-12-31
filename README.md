torrentcontrol
==============

Torrentcontrol lets you automate usual tasks with [transmission BT client](http://www.transmissionbt.com/):

 * Automatic download of new episodes
 * Start and stop all downloads  

# Install the dependencies

    sudo apt-get install python-pip transmission-cli
    sudo pip install beautifulsoup4 requests

# Clone torrentcontrol

    sudo apt-get install git
    cd ~
    git clone git://github.com/kktuax/torrentcontrol.git
    
# Display help
    
	cd ~/torrentcontrol
    	./torrentcontrol.py -h
	
	usage: torrentcontrol.py [-h] [--start] [--stop] [--auto-series]
		                         [--conf-file CONF] [--history-file HISTORY]
		
		optional arguments:
		  -h, --help            show this help message and exit
		  --start               Starts all torrents
		  --stop                Stops all torrents
		  --auto-series         Searches for new episodes
		  --conf-file CONF      Location of configuration file
		  --history-file HISTORY
		                        Location of history file
		
	
# Configuration file

You can customize automatic serie's episode addition editing torrentcontrol.conf:

	{
	"series": [
		"game of thrones",
		"boardwalk empire",
		"it crowd"
		]
	}


# Search for new episodes and start downloads

    cd ~/torrentcontrol
    ./torrentcontrol.py --auto-series --start
	
