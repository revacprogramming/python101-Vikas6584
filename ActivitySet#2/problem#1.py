def add(a, b):
    c = float(a)+float(b) 
    return c
  
def main():
    a = input("Enter the first number")
    b = input("Enter the second number")
    c = add(a, b)
    print ("The Sum =",c)
  
main()       