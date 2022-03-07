def movatob(a):
    b = a+1
    return b   

def movbtoc(b):
    c = b+1
    return c

def movctod(c):
    d = c+1
    return d 

def movdtoe(d):
    e = d + 1
    return e

def movetof(e):
    f = e + 1
    return f

def movatof(a):
    x = movatob(a)
    y = movbtoc(x)
    z = movctod(y)
    i = movdtoe(z)
    j = movetof(i)
    return j

def factorial(x):
   while x>1:
      y = x*factorial(x-1)
      	



#a = factorial(5)+factorial(4)+fact(3)

fact_5 = 0
a =5
y=a
x=1
result = 0
while a > 1 and x < a:
    fact_5 = y*(a-x)
    x+=1
    fact_5 

fact_4=0
a =4
y=a
x=1
result = 0
while a > 1 and x < a:
    fact_4= y*(a-x)
    x+=1
    y=result

fact_3=0	
a =3


y=a
x=1
result = 0
while a > 1 and x < a:
    fact_3= y*(a-x)
    x+=1
    y=fact_3



def findfactorial(x):
   a =x
   y=a
   x=1
   result = 0
   while a > 1 and x < a:
       result = y*(a-x)
       x+=1
       y=result
   else:
      return result
