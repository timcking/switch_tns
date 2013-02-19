#!/usr/bin/env python
import string
import re
import sys

USAGE = 'Usage: ' + sys.argv[0] + ' [rocky|xps]'

if len(sys.argv) == 1:
   print USAGE
   exit()

env = sys.argv[1]

if env == 'rocky':
   replace_string = 'rocky'
elif env == 'xps':
   replace_string = 'xps'
else:
   print USAGE
   exit()

FILE_NAME = 'C:\\oracle\\product\\11.2.0\\client_1\\network\\admin\\tnsnames.ora'
   
# Read the file
tns_file = open(FILE_NAME, 'r')
the_text = tns_file.read()
tns_file.close()

# Replace
match_str = re.compile('HOST = \S*.\)')
the_text = match_str.sub('HOST = ' + replace_string + ')', the_text)

# Write the file`
tns_file = open(FILE_NAME, 'w')
tns_file.write(the_text)
tns_file.close()
