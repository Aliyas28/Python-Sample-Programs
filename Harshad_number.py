
# A Harshad Number is a positive integer that is divisible by the sum of its digits.

# example : 18 ---> sum of digits = 1 + 8 = 9 ---> 18 / 9 = 2

n = int(input("Enter the number: "))

temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

if temp % sum == 0:
    print("Harshad Number")
    
else:
    print("Not a Harshad Number")
