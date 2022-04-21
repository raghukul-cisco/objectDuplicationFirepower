import re
import getpass
import sys
import warnings
import requests
import time
import json
from fireREST import FMC
from netaddr import *
import ipaddress
import datetime


#Global variables

nObjects = {}
hObjects = {}
gObjects = {}
rObjects = {}
expGroup = {}
literalsGroup = {}
dupHost = {}
dupNet = {}
overlapNet = {}

def objectGuide(fmc):
	print ("Inside Object Pull")
	netObjects = fmc.object.network.get()
	hostObjects = fmc.object.host.get()
	groupObjects = fmc.object.networkgroup.get()
	netAddObjects = fmc.object.networkaddress.get()
	rangeObjects = fmc.object.range.get()

	
	for item in netObjects:
		nObjects[item['name']] = [item['id'], IPNetwork(item['value'])]

	for item in hostObjects:
		hObjects[item['name']] = [item['id'], IPNetwork(item['value'])]

	for item in groupObjects:
		if ('literals' in item.keys()):
			temp = item['literals']
			vList = []
			for local in temp:
				vList.append(local['value'])
			literalsGroup[item['name']] = [vList, item['id']]
		else:
			try:
				expandG = item['objects']
			except KeyError:
				pass
			gList = []
			for local in expandG:
				gList.append(local['name'])
			gObjects[item['name']] = gList

	for item in rangeObjects:
		rObjects[item['name']] = item['value']


def detectDuplicates():
	#Host Duplication block
	for key, value in hObjects.items():
		res = []
		for key1, value1 in hObjects.items():
			if (key == key1):
				pass
			else:
				if (value[1] == value1[1]):
					res.append(key1)
		if (res):
			res.append(key)
			dupHost[value[1]] = res

	#Network Duplication block
	for key,value in nObjects.items():
		res = []
		overlap = []
		for key1, value1 in nObjects.items():
			keyFlag = 1
			if (key == key1):
				keyFlag = 0
				pass
			else:
				if (value[1] == value1[1]):
					res.append(key1)

			if (keyFlag):
				if ((value[1] == IPNetwork('0.0.0.0/0')) or (value1[1] == IPNetwork('0.0.0.0/0'))):
					pass
				else:
					if (value1[1] in value[1]) and (value[1] != value1[1]):
						#overlap.append(key1 + "::" + str(value1[1]))
						overlap.append(key1)
						

		if (res):
			res.append(key)
			dupNet[value[1]] = res

		if (overlap):
			overlap.append(key)
			overlapNet[key] = overlap


def writeResults():
	hostFile = open("hostDuplicates" + ".csv", "w")
	hostFile.write("IP Address, Duplicates, Count of Duplicates\n")
	print ("Total Host Duplicates", len(dupHost))
	pos =0
	for key, value in dupHost.items():
		pos = pos + 1
		print("Writing host duplicate {0} to CSV...".format(pos))
		hostFile.write("{0}, {1}, {2}\n".format(key,';'.join(value), len(value)))
	
	networkFile = open("networkDuplicates" + ".csv", "w")
	networkFile.write("IP Network, Duplicates, Count of Duplicates\n")	
	print ("Total Network Duplicates", len(dupNet))	
	pos =0
	for key,value in dupNet.items():
		pos = pos + 1
		print ("Writing network duplicates {0} to CSV ...".format(pos))
		networkFile.write("{0}, {1}, {2}\n". format(key,";".join(value), len(value)))

def getInput():
	
	hostname = input("Enter the IP Address of the FMC: ")
	username = input("Enter the username for the FMC: ")
	password = getpass.getpass("Enter the password associated with the username entered: ")
	fmc = FMC(hostname=hostname, username=username, password=password, domain='Global')

	objectGuide(fmc)


getInput()
detectDuplicates()
writeResults()