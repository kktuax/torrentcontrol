import subprocess, re

def get_ids():
    p = subprocess.Popen( ["transmission-remote", "--list"], stdout=subprocess.PIPE )
    p.wait()
    out, err = p.communicate()
    return re.findall(r'\s(\d+)\s', out)

def start_torrent(pk):
    p = subprocess.Popen( ["transmission-remote", "--torrent", pk, "--start"] )
    p.wait()

def stop_torrent(pk):
    p = subprocess.Popen( ["transmission-remote", "--torrent", pk, "--stop"] )
    p.wait()

def add_torrent(link):
    p = subprocess.Popen( ["transmission-remote", "--add", link] )
    p.wait()
