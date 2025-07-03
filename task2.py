list=[]
for i in range(1,11):
    print(list.append(i))
print("original list is ", list)
b=list[0:5]
print("the first five extracted values are ", b)
b.reverse()
print("the reverse values of extracted values are ", b)
