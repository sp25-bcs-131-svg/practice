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
