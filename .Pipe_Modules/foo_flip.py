#!/usr/bin/env/python3
import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], 'i:o:f:n:')

for opt, arg in opts:
    if opt in ('-i'):   input_foo  =  str(arg)
    elif opt in ('-o'): output_foo =  str(arg)
    elif opt in ('-f'): config_text = str(arg)
    elif opt in ('-n'): nThreads = int(arg)

#Read the string    
in_foo = open(input_foo,"r+")
foo = in_foo.readline().rstrip()
in_foo.close()

print(foo)

#flip the string
foo = foo[::-1]

print(foo)

#Append the text from config_text
foo = config_text + ' ' + foo

print(foo)

#write it out
out_foo = open(output_foo, 'w+')
out_foo.write(foo)
out_foo.close()
