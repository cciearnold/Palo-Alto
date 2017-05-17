#!/usr/bin/env python

###########################################################
# Script: show_panos_app_versions
# Author: Arnold Batista
# Date: 05/14/2017
# Version 1.0
# Script to Show Palo Alto App,Av, and Wildfire versions
###########################################################

from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
from netmiko import ConnectHandler
import sys
import time
import select
import paramiko
import re

# Setting Netmiko to use built in Palo Alto Driver
platform = 'paloalto_panos'

#Uncheck below if you want to enter IP Address of the Palo Alto instead of using a host file.
#ip = raw_input("Enter the device IP Address: ")

#UnCheck below If you want to use a dictionary instead of using a host file.
#devices = [‘firewall1’, ‘firewall2’]

# Setting User Input for interactive prompt
username = raw_input('Enter username for device login:')
password = raw_input('Enter password for device login:')


def main():
    ip_add_file = open('hosts.txt','r')
    for host in ip_add_file:
        host = host.strip()
        device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        print "\n============================================================"
        print "Checking App,Av, and Wildfire Versions for:",host
        output = device.send_command('show system info | match app-')
        print(output)
        output = device.send_command('show system info | match av-')
        print (output)
        output = device.send_command('show system info | match wildfire-')
        print (output)
        print "============================================================\n"
        device.disconnect()
#
# __main__
if __name__ == '__main__':
    main()