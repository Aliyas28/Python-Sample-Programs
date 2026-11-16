""" 

A number is called a gold number if:
it is divisible by 3 
it is not divisible by 5

the sum of its digits is even

print all gold number from 1 to n"""


number = int(input("enter the number:"))

for i in range(1,number+1):
    
    sum = 0 
    
    digit = 0
    
    for digit in str(i):
        
        sum += int(digit)
        
    if i % 3 == 0 and i % 5 != 0 and sum % 2 ==0 :
            
        print(i) 
    
    
   