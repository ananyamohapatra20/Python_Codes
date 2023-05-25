try:
    a=int(input("Enter a number "))
    c=1/a
    print(c)
except ValueError as e:
    print("Enter a valid value!! ")
    print(e)
except ZeroDivisionError as e:
    print("Make sure you are dividing by zero!!! ")
    print(e)
    
print("Thanks for using this code")