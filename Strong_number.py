#strong number 
  #  the sum of factorial of the digits equal to the  number
  
  
  
number = int(input("enter the number:"))

sum = 0

for num in str(number):
    
    fact = 1
    
    for i in range(1,int(num) +1):

        fact *= i
        
    sum += fact
    
print("strong number" if sum == number else "not strong number")          
  
    