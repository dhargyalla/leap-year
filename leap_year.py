#To check whether the input year is leap year or not
#the condition of the leap year is, the number should either divisible by 4, or divisible by 400 except the number divisible by 100
# Ask the user to input random year

year = int(input("Enter any valid year "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
