# Conditional Execution(II)

def input():
	score = float(input("Enter Score: "))
	return score
  
def scores(s):
	if s >= 0.9:
		return 'A'
	elif s >=0.8:
		return 'B'
	elif s >=0.7:
		return 'C'
	elif s >= 0.6:
		return 'D'
	elif s < 0.6:
		return 'F'
	else:
		return "Out of Range"
    
def main():
	scores()
  
main()  