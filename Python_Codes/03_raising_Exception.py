def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not valid")
a=increment(89)
print(a)
num=99
print(increment(num))
