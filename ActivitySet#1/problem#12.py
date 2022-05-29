# Regular Expressions
# https://www.py4e.com/lessons/regex

import re
def file():
  file=open("dataset/regex.txt")
  s=[]
  sum=0
  for check in file:
    check=check.rstrip()
    main=re.findall('[0-9]+',check)
    if s!=main:
      s=s+main
  for n in s:
    sum=sum+int(n)
  print(sum)



file()