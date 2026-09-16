#Strings

str1 = "Hello My name is Talha,\n whats yours"
str2 = "Hello My name is Talha,\t whats yours"
print(str1)
print(str2)

name1 = "Talha"
name2 = "Munir"
full = name1 + " " + name2
print(full)
print(len(full))
print(full[0])
print(full[0:5])
print(full[6:])
print(full[-5:-1])
print(full[:8])

str = "coder"
print(str.endswith("er"))
print(str.startswith("co"))
print(str.capitalize())
print(str.upper())
print(str.replace("co","mo"))
print(str.find("d"))
print(str.count("o"))

age = int(input("Enter your age: "))
if(age >= 45):
    print("OLD")
elif(age > 18 and age < 45):
    print("ADULT")
elif(age <= 18 and age > 13):
    print("TEENAGER")
elif(age <= 13 and age > 3):
    print("CHILD")
else:
    print("NEW BORN")