# dailyprogrammer-gameofthrees

i = int(raw_input())
while i>1:
	print i,
	r = i%3
	if r==0:
		print 0
		i/=3
	elif r==1:
		print -1
		i = (i-1)/3
	else: #r==2
		print 1
		i = (i+1)/3
print 1
