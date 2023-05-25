list1=[2, 5,6,9,88]
list2=[]
'''for i  in list1:
    if i%2==0:
        list2.append(i)
print(list2)'''
#Shortcut to write the above code!!
list2=[ i for i in list1 if i%2==0] 
print(list2)
#List comprehension is an eleglant way to create a lists based on existing list.