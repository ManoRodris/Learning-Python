year=int(input("Type a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That year is a leap year")
        else: 
            print("That year isn't a leap year")
    else:
        print("That year is a leap year")
else:
    print("That year isn't a leap year")