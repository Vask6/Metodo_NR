from math import*
x1= float(input("Introduza o termo inicial: "))
ni=int(input("introduza o número de iterações: "))
xn=0
def f(x):
  return exp(x)+x
def df(x):
  return exp(x)+1
for i in range(ni):
  xn=x1-(f(x1)/df(x1))
  x1=xn
print("A raíz aprox. de exp(x)+x é : ",xn)
