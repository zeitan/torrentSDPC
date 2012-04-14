#!/usr/bin/python2.6
from deluge.ui.client import client
from twisted.internet import reactor
import dbus
import time

def on_connect_success(result):
    print "Connection was successful!"
    def on_get_torrent_value(value):
	apagar=1
	for torrent in value:
		if value[torrent]["progress"] <>100 :
	        	apagar=0
			print value[torrent]["name"]
			break
	if apagar==1:
		#print "apague"
		bus = dbus.SystemBus()
		shut = bus.get_object('org.freedesktop.Hal','/org/freedesktop/Hal/devices/computer')
		shutr =  dbus.Interface(shut , 'org.freedesktop.Hal.Device.SystemPowerManagement')
		shutr.Shutdown()
        client.disconnect()
        reactor.stop()
        
    client.core.get_torrents_status({}, ["progress","name"]).addCallback(on_get_torrent_value)

def on_connect_fail(result):
    print "Connection failed!"
    print "result:", result


d = client.connect()
d.addCallback(on_connect_success)
d.addErrback(on_connect_fail)
reactor.run()
	#print "Start : %s" % time.ctime()
	#time.sleep( 60 )
	#print "End : %s" % time.ctime()
