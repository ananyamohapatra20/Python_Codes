while(True):
    print("Press Q to quit")
    a=input("Enter a number ")
    
    if a=="Q":
        break
    try:
        a=int(a)
        if a>10:
            print("You enterd a number greater than 10")
    except Exception as e:
        print(e)
print("Thanks for playing this game")


