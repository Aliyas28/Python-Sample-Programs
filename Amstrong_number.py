# check whether a number is amstrong number or not

number = int(input("enter the number:"))

temp = number 
length = 0
total = 0
digit = 0
num = number
while number > 0: #finding the length
    length +=1 
    number = number //10
print(length)    

while temp >0:
    
    digit = temp % 10
    total += digit **length
    temp = temp // 10
    
print(total)    

print("amstrong number " if total == num else " not amstrong" )