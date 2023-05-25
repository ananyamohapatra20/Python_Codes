a=67#global variable
def func1():
    global a
    print(f"print statement 1:{a}")
    a=8 #local variable
    print(f"print statement2 :{a}")
func1()
print(f"print statement3 :{a}")