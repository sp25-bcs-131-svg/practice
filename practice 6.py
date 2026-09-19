#Functions
def calc_sum(a, b):
    sum = a + b
    print(sum)
calc_sum(2,3)
calc_sum(4,5)
calc_sum(9,6)

def hello():
    print("hello")
hello()

def average(a,b,c):
    avg = (a+b+c)/3
    return avg
print(average(3,4,5))

#Default Parameters          
def calc_product(a=2,b=4):
    print(a*b)
calc_product()

#qs1
def calc_len(list1):
    return len(list1)
print(calc_len([1,2,3,4,5]))

#qs2
def print_elements(list1):
    i = 0
    while i <= (len(list1)-1):
        print(list1[i] , end=" ") 
        i += 1           
print_elements(["t","a","l","h","a"])
print()

#qs3
def exchange_rate(usd):
    pkr = usd * 276.82 
    print(pkr)
exchange_rate(5500)

#qs4
def odd_even(a):
    if( a%2 == 0):
        print("Even number")
    else:
        print("Odd number")
odd_even(9)

#Recursion
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
show(4)

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return (n * fact(n-1))
print(fact(5))

def calculate_sum(n):
    if(n == 0):
        return 0
    return calculate_sum(n-1) + n
print(calculate_sum(5))

def print_list(list1 , index=0):
    if(index == len(list1)):
        return
    print(list1[index])
    print_list(list1 , index+1)
print_list(["m","u","n","i","r"])