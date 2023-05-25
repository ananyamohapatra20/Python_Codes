class Library:
    def __init__(self,ListofBooks):
        self.books = ListofBooks

    def displayAvailableBooks(self):
        print("The boooks present in this library are")
        for book in self.books:
           
            print("\t" +  book)



class Student:
    pass
if __name__=="__main__":
    centraLibrary=Library(["Algo","Flask","Django","Python","Cprog",])
    centraLibrary.displayAvailableBooks()