import os
#File I/O

#Reading a file
file = open("demo.txt","r")
#data = file.read()
#print(data)
line1 = file.readline()
print(line1)
file.close()

#Writing in a file
file1 = open("demo.txt","w")
file1.write("this is a new  line\n") #overwrites the entire file
file1.close()

#Append 
file2 = open("demo.txt","a")
file2.write("this is a second new line") #adds to the file
file2.close()

#Read and overwrite (pointer at start , no truncate)
file3 = open("demo.txt","r+")
file3.write("  ")
print(file3.read)
file3.close()

#Truncate
"""/
file3 = open("demo.txt","w+")
print(file3.read)
file3.close()
"""       

#file = open("demo.txt","a+")
#read + append (pointer at end , no truncate) 

with open("demo1.txt","r") as f:
    data = f.read()
    print(data)

os.remove("sample.txt")