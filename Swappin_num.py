
# swapping numbers using a temporary  variable

num1 = int(input("enter the number:"))

num2 = int(input("enter the number:"))

temp = num1

num1 = num2

num2 = temp

print("After swapping:")

print("num1 =", num1)

print("num2 =", num2)

# -----------------------------------------

# Without using a temporary variable

num_a = int(input("enter the number:"))
num_b = int(input("enter the number:"))

num_a , num_b = num_b ,num_a

print(f"After swapping: {num_a, num_b}")
