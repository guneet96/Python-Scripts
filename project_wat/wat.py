from pos_ex import posl
from neg import negl
import random
import time
import os

#print posl
#print negl

print "--------------------------------------------------------------------Welcome to WAT Exercise---------------------------------------------------------------------"

print "\n\n\n\n"
inp = raw_input("Enter y to start, n to exit")

if str(inp) == "n":
	exit()

for i in range(1,61):
	random.shuffle(posl)
	print str(i) + " " + posl[0]
	posl.pop(0)
	time.sleep(15)
	duration = 0.5  # second
	freq = 440  # Hz
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
