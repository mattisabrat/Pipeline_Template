#!/usr/bin/env/python3
import getopt
import sys
from os import path

opts, args = getopt.getopt(sys.argv[1:], 'n:i:o:s:')

for opt, arg in opts:
    if   opt in ('-i'): input_foobar  = str(arg)
    elif opt in ('-o'): output_csv    = str(arg)
    elif opt in ('-n'): nThreads      = int(arg)
    elif opt in ('-s'): name          = str(arg)

#Read the string    
in_foobar = open(input_foobar,"r+")
foobar = in_foobar.read().rstrip()
in_foobar.close()

if (path.exists(output_csv)):
    #write it out
    out_foobar = open(output_csv, 'a')
    out_foobar.write(name + ',' + foobar + '\n')
    out_foobar.close()
else:
    out_foobar = open(output_csv, 'w+')
    out_foobar.write('SampleName, Foobar\n')
    out_foobar.write(name + ',' + foobar + '\n')
    out_foobar.close()
