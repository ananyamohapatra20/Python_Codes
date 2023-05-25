def Readfile(Filename):
    try:
        with open (Filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {Filename} is not found")
Readfile("1.txt")
Readfile("2.txt")
Readfile("3.txt")