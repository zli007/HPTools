"""!@mainpage HPTools

@section intro_sec Introduction

Python Tools to manipulate, analyze and plot DNA helical parameter data
    TcB @ Louisiana Tech 2018
    contributions from Zilong Li, Ran Sun
    @page HPTools HPTools
    Usage:  HPTools.py
    
    @page Run-Me RunMe
    Usage:  Run-Me.py
    

"""

import sys
import os
import urllib2
import twobitreader

####################
### Check valid url
####################

def _CHECKURL(url):
	"""Check whether the url is valid"""
	try:
		urllib2.urlopen(url)
		return True
	except urllib2.URLError:
		return False

####################
### Check valid file
####################

def _CHECKFILE(fp):
	"""Check whether the file is valid"""
	if os.path.isfile(fp) == True:
		return True
	else:
		return False

#################################
### Read sequence from 2bit files
#################################

def Read_sequence_2bit(fp,chromatin,start,end):
	"""
	Given 2bit file, chromatin e.g. chrIII, start position and end position
	Return sequence(string) with uppercase 'ACGT's
	Tested that url for 2bit will not work, need to be 2bit file.
	"""
	if _CHECKFILE(fp)==True:
		tbf = twobitreader.TwoBitFile(str(fp))
		seq = tbf[str(chromatin)][int(start):int(end)]
		seq = seq.upper()
	else:
		print "Provide a valid file"
		sys.exit(0)
	return seq
	
#############################
### Read sequence from txt files
#############################

def Read_sequence_txt(fp):
	"""
	Given seqin.txt, either with one column of sequence or one/several rows of sequence
	Return sequence(string) with uppercase 'ACGT's
	"""
	if _CHECKFILE(fp)==True:
		with open(fp) as f:
			seq=''.join(line.replace('\n', '') for line in f)
		seq = seq.upper()
	else:
		print "Provide a valid file"
		sys.exit(0)
	return seq
	