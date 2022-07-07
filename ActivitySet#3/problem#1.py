def rect():
  n=int(input("how many rectangles area do you want?"))
  i=0
  while n>i:
      area()
      i=i+1


def area():
  x1=eval(input("enter value for x1"))
  y1=eval(input("enter value for y1"))
  x2=eval(input("enter value for x2"))
  y2=eval(input("enter value for y2"))
  x3=eval(input("enter value for x3"))
  y3=eval(input("enter value for y3"))

  area=(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y3))
  print("Area of rectangle with vertices","(",x1,",",y1,")"",""(",x2,",",y2,")"",""(",x3,",",y3,")","is","=",area)

rect()         hdhdh