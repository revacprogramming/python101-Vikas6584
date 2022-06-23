# Tuples

filename = "dataset/mbox-short.txt"
filehandle=open(filename)
counts={}

for line in filehandle:
	if line.startswith("From "):
		time=line.split()[5].split(":")
		counts [time[0]] = counts.get(time[0], 0) + 1


lst = list()

for key, value in counts.items():
    lst.append( (key,value) )
lst.sort()

for hour, counts in lst:
    print (hour, counts)   
  