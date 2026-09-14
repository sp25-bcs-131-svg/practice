# This is my revision for python
""" Comments 
which are 
multilined """


print("Hello , World")
print(23)
print(40+60)

name = "Talha"
age = 21
old = False
print("My name is",name,"and age is",age,"and it is",old,"that i am old")

price = 500.00

print(type(name))
print(type(age))
print(type(price))

a = 10
b = 20
sum = a + b
diff = a - b
product = a * b
div = b / a
exp = a ** b
mod = b % a
int_div = b // a
print(int_div)
print(sum)
print(diff)
print(product)
print(div)
print(exp)
print(mod)

A = 2
B = 3
Txt = "$"
print(A*Txt*B)
D = "2"
print((D+Txt)*B)

x = 10
y = 5.0
print(x*y)
print(x/y)
print(x//y)

name = input("name: ")
age = int(input("age: "))
price = float(input("price: "))

light = input("What colour is the light? : ")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Get ready")
elif(light == "green"):
    print("Go")
else:
    print("Light is broken")

#Ternary operator
sports = input("Which sports sre you gonna play? :")
play = "Yes I will play" if sports == "football" else "No I dont play it"
print(play)

school = input("Which school do you go to? : ")
print("I also went there") if school == "lgs" else print("Ok , nice school")
