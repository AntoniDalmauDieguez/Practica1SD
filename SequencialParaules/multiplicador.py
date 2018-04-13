with open('Sherlock.txt') as f:
	s=f.read()

vegades=2
with open('Sherlock'+str(vegades)+'.txt', 'w') as f:
	i=0
	while i<vegades:
		f.write(s)
		i=i+1
