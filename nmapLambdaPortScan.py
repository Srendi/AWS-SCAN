#!/bin/env python
import timeit
import nmap
import sys
import socket
from multiprocessing import Process, freeze_support
from slacker import Slacker
	
def Send2Slack(message, channel='#General'):
	slack = Slacker('xoxp-77218513845-77163231587-77222556855-ec5a052950')
	slack.chat.post_message(channel, message)
	
def scan(scanhost):
	output = ""
	tic = timeit.default_timer()
	print "Port scan of " + scanhost + " begining...\n"
	nm = nmap.PortScanner()
	nm.scan(scanhost, arguments='-sT')
	for host in nm.all_hosts():
		output += ('Host : %s (%s)\n' % (host, nm[host].hostname()))
		output += ('State : %s\n' % nm[host].state())
		for proto in nm[host].all_protocols():
			output += ('----------\n')
			output += ('Protocol : %s\n' % proto)
			lport = nm[host][proto].keys()
			lport.sort()
			for port in lport:
				output += ('port : %s\tstate : %s\n' % (port, nm[host][proto][port]['state']))
	toc =  timeit.default_timer()
	sumt = toc - tic
	output += "\nTime taken to scan host " + host + ": " + str(sumt) + " seconds\n"
	#print('%s' % (output))
	Send2Slack(output)
	
def lambdaHandler(event, context):
	#We need to pull the external address of the hostname to be port scanned from the AWS event.
	scan(hostArg)
	
def scanWrapper():
	#maintic = timeit.default_timer()
	for arg in sys.argv[1:]:
		try:
			scanhost = socket.gethostbyname(arg)
			#print"Host: " + arg + " resolves to: " + scanhost
		except socket.gaierror:
			sys.exit("Hostname: %s could not be resolved. Does the host exist? Exiting" % arg)

		except socket.error:
			sys.exit("Couldn't connect to server")
	
	for arg in sys.argv[1:]:
		scan(arg)
		
	#maintoc = timeit.default_timer()
	#mainsumt = maintoc - maintic
	#print "\nTime taken to scan all hosts: " + str(mainsumt) + " seconds\n"
	
def main ():
	if (len(sys.argv) < 2):
		print('Usage: %s host [host]...' % sys.argv[0])
		sys.exit()
	scanWrapper()
	

if __name__ == "__main__":
	freeze_support()
	
	main()
