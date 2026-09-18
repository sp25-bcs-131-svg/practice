#Loops

#qs1
i = 1
while i <= 100:
    print(i)
    i += 1

#qs2
i = 100
while i >= 1:
    print(i)
    i -= 1

#qs3
n = 3
j = 1
while j <= 10:
    print(n,"*",j,"=",n*j)
    j += 1

#qs4
list = [1,4,9,16,25,36,49,64,81,100]
k = 0
while k <= (len(list)-1):
    print(list[k])
    k += 1

#qs5
tuple = (1,4,9,16,25,36,49,64,81,100)
x = 81
y = 0
while y <= (len(tuple)-1):
    if x == tuple[y]:
        print("Number found at index",y)
        break
    else:
        print("Number not found")
    y += 1

h = 1
while h <= 10:
    if( h%2 != 0):
       h += 1
       continue
    print(h) 
    h += 1

#For Loops             
list = ["talha", 1, 2, 3, 5.55]
for el in list:
    print(el)

tuple1 = (1, 2, 3, 4, 5, 6, 7)
for val in tuple1:
    print(val)

str = "metamorphasis"
for char in str:
    print(char)
