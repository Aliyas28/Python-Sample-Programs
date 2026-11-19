"""
        A YEAR is a leap year if it is evenly divisible by (4) , non century eg: 2020,1999,2022
    
       Century years(those ending in 00) are only leap year if they are evently divisible by (400)
       eg: 1900,
    """
    
    #leapyear code 
     
year = int(input("enter the year :"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
 print(f"{year} is leap year")    
    
else:
    print(f"{year} is non leap year")