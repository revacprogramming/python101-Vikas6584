# Files
#use file name as dataset/mbox-short.txt

def filehandle():
	fname = input("Enter file name: ")
	fhand = open(fname)
	count,average = 0,0
	for line in fhand:
	    line=line.rstrip()
	    if not line.startswith("X-DSPAM-Confidence:") : 
	        continue
	    average += float(line[20:])
	    count = count + 1
	final=average/count
	return final
  
def output(final):		
	print("Average spam confidence:", final)
  
def main():
	final=filehandle()
	output(final)
  
main()	   








 
  