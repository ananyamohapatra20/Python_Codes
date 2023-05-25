try:
    a=int(input("Enter a number"))
    a=1/a
except Exception as e:
    print(e)
    exit()
finally:
    print("Finally you are done")
    #Irrespective of any error the program written in finally block will exceute
print("Thanks for using this program : ")
#In case amny error will occur in the program th this code will not get executed