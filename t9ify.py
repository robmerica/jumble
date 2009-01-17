import os
import string
import time
import sys

# turns a word (jumbled or not) into a key
def t9ify(letters):
	t9 		= ''
	letters = list(letters.lower())
	letters.sort()
	letters = string.join(letters,'')
	while (len(letters) > 0):
		t 		= letters[0]
		freq 	= letters.count(t)
		letters = letters.replace(t, '')
		t9  	+=	t + str(freq)
	return t9

# more compact/better version of t9ify, but slower
# for when I stick it into a DB
def t9minify(letters):
	map 	= {}
	t9 		= ''
	letters = list(letters.lower())
	letters.sort()
	letters = string.join(letters,'')
	while (len(letters) > 0):
		t 		= letters[0]
		freq 	= letters.count(t)
		letters = letters.replace(t, '')
		try:
			map[freq] 	+= t
		except KeyError:
			map[freq] 	= t
	for k, v in map.iteritems():
		t9 += str(v) + str(k)
	return t9


def scan(path = os.getcwd()+'/lists'): 
	index = []
	for x in os.listdir(path):
		current = path+'/'+x
		if os.path.isdir(current):
			scan(current)
		else:
			index.append(current)
	return index


start 		= time.time()
count 		= 0

try: 
	solve = t9minify(sys.argv[1])
except IndexError:
	solve = ''

lists = scan()

for x in lists:
	f = open(x,'r')
	for line in f:
		line = line.strip()
		if (line.isalpha() & (len(line) > 2)):
			#print line.lower()
			count += 1
			t9 = t9minify(line)
			#print t9
			if t9 == solve:
				print 'Possible Match: ' + line + ' (Key: ' +t9+ ')\n'
			#print '\n'
	f.close()
#print str(t9minify(sys.argv[1]))
print str(count) + ' words in word list\n'
print "Took " + (str((time.time() - start))) + ' seconds'
