def square(num):
    return num*num
#Method 1
l1=[6,7,8]
l2=[]
#for i in l1:
  #  l2.append(square(i))
#print(l2)
#Method 2
print(list(map(square,l1)))