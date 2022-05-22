# Dictionaries
#'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer'''

filename = "dataset/mbox-short.txt"
filehandle =open(filename)
count={}

for line in filehandle :
	if line.startswith("From "):
		email=line.split()[1]
		count[email]=count.get(email,0)+1
max_count=0
max_emails=0
for email in count:
	if count[email]>max_count:
		max_count=count[email]
		max_emails=email
print(max_emails,max_count)			