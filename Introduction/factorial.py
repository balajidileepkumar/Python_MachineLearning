import os
import sys
#x = int(input("Enter the number?"))
x = int(sys.argv[1])
output =1
for n in range(x+1):
	if(n!=0):
		print(n)	
		output = output * n
print(output)