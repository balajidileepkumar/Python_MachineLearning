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

c = findfactorial(5)+findfactorial(4)+findfactorial(3)+findfactorial(8)
print("from function : ",c)

fact_5 = 0
a =5
x=1
y=a
result = 0
while a > 1 and x < a:
    result = y*(a-x)
    x = x +1
    y = result
else:
    fact_5 = result
    
    
fact_4=0
a =4
y=a
x=1
result = 0
while a > 1 and x < a:
    result= y*(a-x)
    x+=1
    y=result
else: 
    fact_4 = result
    
fact_3=0	
a =3
y=a
x=1
result = 0
while a > 1 and x < a:
    result= y*(a-x)
    x+=1
    y=result
else: 
    fact_3 = result
    
    
fact_8=0
a =8
y=a
x=1
result = 0
while a > 1 and x < a:
    result= y*(a-x)
    x+=1
    y=result
else: 
    fact_8 = result

print("without function : ",fact_5+fact_4+fact_3+fact_8)

