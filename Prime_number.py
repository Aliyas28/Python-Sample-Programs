
#get the first 10 prime numbers from the range of 100 to 1000

number = 1000

count = 0

for number in range(100, 1000):

    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number)
        count += 1

    if count == 10:
        break
       