#Lists
name = ["Talha","Munir","Ali","Ahmed"]
print(name)
print(name[0])
print(len(name))
print(name[0:3])
print(name[-3:-1])
print(name[:4])

list = [2,1,3,5,4]
list.append(6)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(2,7)
print(list)
list.remove(3)
print(list)
list.pop(2)
print(list)

#Tuples
tuple = (1, 2, 3, 4, 5)
print(tuple)
print(tuple[0])
print(len(tuple))
print(tuple[0:3])
print(tuple.index(3))
print(tuple.count(2))

list1 = [1, 2, 3, 2, 1]
list2 = list1.copy()
list2.reverse
if(list1 == list2):
    print("Palindrome")
else:
    print("Not Palindrome")

