try:
    a=int(input("Enter a number"))
    a=1/a
except Exception as e:
    print(e)
else:
    print("You are succesful")