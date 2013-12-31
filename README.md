torrentcontrol
==============

Torrentcontrol lets you automate usual tasks with [transmission BT client](http://www.transmissionbt.com/):

 * Automatic download of new episodes
 * Start and stop all downloads  

# Install the dependencies

    sudo apt-get install python-pip transmission-cli
    sudo pip install beautifulsoup4 requests

# Clone torrentcontrol and display help

    sudo apt-get install git
    cd ~
    git clone git://github.com/kktuax/torrentcontrol.git
    cd ~/torrentcontrol
    ./torrentcontrol.py -h
	
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
	