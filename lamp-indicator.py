#!/usr/bin/env python
# lamp-indicator v1.0
# GTK3 indicator for Ubuntu Unity

from gi.repository import Gtk, GLib
try: 
       from gi.repository import AppIndicator3 as AppIndicator  
except:  
       from gi.repository import AppIndicator
import os

FREQUENCY = 60 # seconds
PATH = os.path.abspath(__file__).split("/")
DELIMITER = "/"
BASEPATH = DELIMITER.join(PATH[0:len(PATH)-1])+"/pics/"

class LampIndicator:
    def __init__(self):
        self.ind = AppIndicator.Indicator.new(
            "lamp-indicator",
            "",
            AppIndicator.IndicatorCategory.OTHER)
       	self.ind.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self.icon_red()
        self.ind.set_attention_icon(BASEPATH+'green.png')
        self.setup_menu()

    def icon_orange(self):
        self.ind.set_icon(BASEPATH+'orange.png')
        self.ind.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    def icon_red(self):
        self.ind.set_icon(BASEPATH+'red.png')
        self.ind.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    def icon_green(self):
        self.ind.set_status(AppIndicator.IndicatorStatus.ATTENTION)

    def setup_menu(self):
        self.menu = Gtk.Menu()

        apacheStatus = os.system("service apache2 status")
        self.isRunning = apacheStatus == 0

        # Start
        if(not self.isRunning):
            item = Gtk.MenuItem()
            item.set_label("Start")
            item.connect("activate", self.handler_menu_start)
            item.show()
            self.menu.append(item)

        # Stop
        if(self.isRunning):
            item = Gtk.MenuItem()
            item.set_label("Stop")
            item.connect("activate", self.handler_menu_stop)
            item.show()
            self.menu.append(item)

        # Restart
        if(self.isRunning):
            item = Gtk.MenuItem()
            item.set_label("Restart")
            item.connect("activate", self.handler_menu_restart)
            item.show()
            self.menu.append(item)

        self.menu.show()
        self.ind.set_menu(self.menu)

    def handler_menu_start(self, evt):
        self.icon_orange()
        os.system("gksudo /etc/init.d/mysql start && gksudo /etc/init.d/apache2 start")
        self.checkStatus()

    def handler_menu_stop(self, evt):
        self.icon_orange()
        os.system("gksudo /etc/init.d/apache2 stop && gksudo /etc/init.d/mysql stop")
        self.checkStatus()

    def handler_menu_restart(self, evt):
        self.icon_orange()
        os.system("gksudo /etc/init.d/apache2 restart && gksudo /etc/init.d/mysql restart")
        self.checkStatus()

    def checkStatus(self):
        self.setup_menu()
        if self.isRunning:
            self.icon_green()
        else:
            self.icon_red()
        return 1

    def main(self):
        self.checkStatus()
        GLib.timeout_add(FREQUENCY * 1000, self.checkStatus)
        Gtk.main()

if __name__ == "__main__":
    ind = LampIndicator()
    ind.main()