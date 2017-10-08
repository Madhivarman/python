#famous 99 beer bottle song

import os

def child(pipeout):
	bottles = 99

	while True:
		bob = "bottle  of beer"
		otw = "on the wall"
		take1 = "Take one down and pass it around"
		store = "Go to store and buy some more"

		if bottles > 0:
			#song rythm
			values = (bottles,bob,otw,bottles,bob,take1,bottles-1,bob,otw)
			verse = "%2d %s %s ,\n %2d %s.\n%s,\n%2d %s %s.\n" % values
			os.write(pipeout,verse)
			bottles -= 1
		else:
			#last rythm
			bottles = 99 
			values = (bob,otw,bob,store,bottles,bob,otw)
			verse = "No More %s %s,\n no more %s.\n%s,\n%2d %s %s.\n" % values
			os.write(pipeout,verse)

def parent():
	pipein,pipeout = os.pipe()

	if os.fork() == 0:
		os.close(pipein)
		child(pipeout)
	else:
		os.close(pipeout)
		counter = 1
		pipein = os.fdopen(pipein)

		while True:
			print "Verse %d" % (counter)

			for i in range(4):
				verse = pipein.readline()[:-1]
				print '%s' % (verse)
			counter +=1
			print

parent()