# Write a program to display all the numbers between m and n input from the keyboard 
# (where m<n, m>0, n>0), check and print the numbers that are perfect square.
# e.g. 25, 36, 49, are said to be perfect square numbers. Use this ,Math.sqrt() , int

import math

m = int(input("enter a number = "))
n = int(input("enter a number = "))

for i in range(m,n+1):
	s = int(math.sqrt(i))

	if s * s == i:
		print(i,end = " ") 
    