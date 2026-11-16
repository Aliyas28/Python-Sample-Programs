"""
    A perfect  number is a positive
"""


n = int(input("enter the number:"))

sum = 0

for i in range(1,n):
    
    if n % i == 0:
        
        sum += i
print("perfect number" if sum == n  else "not perfect number")


