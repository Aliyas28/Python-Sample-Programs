

#spy number  is a number if the sum of the digits == products of the digit
"""
       # using for loop
  #------------------------------#
number = int(input("enter the number:"))

sum = 0 

products = 1

for i in str(number):
    
    sum +=int(i)
    
    products *=int(i)
    
print("spy number" if sum == products else "not spy number")     

"""

           #using while loop
      #------------------------------#
number = int(input("enter the number:"))

sum = 0 

digti = 0

products = 1

while(number > 0):
    
    digit = number % 10
    
    sum += digit
    
    products *=digit
    
    number = number // 10
    
print("spy number" if sum == products else "not spy number")    