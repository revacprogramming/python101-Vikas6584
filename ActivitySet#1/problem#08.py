# Files
def file():
  f = open("dataset/mbox-short.txt")
  count, sum = 0,0
  for line in f:
    if line.startswith('X-DSPAM-Confidence'):
      count += 1
      x = float(line[20::1])
      sum += x
  print('There were', count, 'subject lines in', "dataset/mbox-short.txt" )
  avg=sum/(count)
  print("Average spam confidence :", avg)

file()