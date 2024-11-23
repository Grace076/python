mylist=[]
mylist.append([10,20,30,40])
print(mylist)
mylist[0][1] =15
print(mylist)
list = [50,60,70]
mylist.extend(list)
print(mylist)
del mylist[-1]
print(mylist)
mylist.sort()
print(mylist)
print(mylist.index(30))