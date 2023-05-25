class MyList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList([1, 2, 3, 4])
print(my_list[0]) # 1
my_list[0] = 10
print(my_list[0]) # 10
