# if / else example
a = input()
a = a.split('.')

if len(a) == 2 and a[-1] == 'py':
    print("Extensia este py")
elif len(a) == 2:
    print("Extensia este: ", a[-1])
else:
    print("Fisierul nu are extensie")

a = 5

# while
while True:
    print(a)
    a -=1

#while break
while True:
    print("Please enter your password\n")
    password = input()
    if password == "youshallnotpass":
        break

#for loop
a = [1,2,3,4]
for i in a:
    print(i)

#for loop text
a = "spam"
for i in a:
    print(i)

#for loop range
for i in range(10):
    print(i)

a = range(10)
print(a)
print(list(a))

#for loop continue
count = 0
for i in range(10):
    if i % 2 == 0:
        continue
    count += i
    print(i)
print(count)

#for loop break
count = 0
for i in range(10):
    print(i)
    if i % 2 != 0:
        break
    count += i

#for loop enumerate
s = "spam"

for index, element in enumerate(s):
    print(index, element)

for i in enumerate([7,6,5,4]):
    print(i)

#for loop tuples
t = ((1,2), (3,4), (5,6))

for i in t:
    print(i)

for i, j in t:
    print(i, j)
    
#for loop dictionary
d = {'name': 'Alice', 'age': 33}

for i in d:
    print(i, d[i])

for key in d.keys():
    print(key)

for key, value in d.items():
    print(key, value)

#exercise count sum number less than 1000
count = 0
sum = 0
while count < 1000:
    if count % 2 == 0:
        sum += count
    count += 1

for i in range(1000):
    if i % 2 == 0:
        sum += i
print(sum)

#functions
def hello():
    print("Hello")

hello()

#functions parameters
def hello(name):
    print("Hello", name)

hello('Bob') 

#functions default parameters
def hello(name='Alice'):
    print("Hello", name)

hello()
hello('Bob')

#function return None
def add(x, y=10):
    print(x + y)

add(5)

#function return 
def hello(name='Alice'):
    return "Hello " + name

a = hello()
print(a)

#function return multiple values
def double(x, y, z):
    return x * 2, y * 2, z * 2

a = double(10, 20, 30)
print(a)

#function scope
a = 10

def double():

    a = 20
    print(a)

double()
print(a)

#function scope
def double():
    global a
    a = 10
    
double()
print(a)

#function scope
def double(a, *args):
    print(a)
    print(args)

double(20)

#function args
def multiply_list(coeficient, *args):
    l = []
    for element in args:
        l.append(element * coeficient)
    return l

print(multiply_list(10, 20, 30, 40, 50, 60))

#function kwargs
def double(x, **kwargs):
    print(x)
    print(kwargs)

double(10, a=10, b=20, c=30, d=10)

#function kwargs
def double(x, **kwargs):
    print(x)
    print(kwargs)

double(10, **{'a':10, 'b':20, 'c':30, 'd':10})

#function kwargs
def concatenate(**kwargs):
    result = ''
    for word in kwargs.values():
        result += ' ' + word
    return result
print(concatenate(**{'a':'Python', 'b':'is', 'c':'great', 'd': '!'}))

#function parameters, default parameters, args, kwargs
def my_function(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)

my_function(1)
my_function(2, 20)
my_function(3, 30, 50, 10, 40, 100, x=101, y=202)
my_function(3, 30, 50, 10, 40, 100, **{'x': 303, 'y': 404})

#exeptions
def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Cannot divide by 0')
    except TypeError:
        print('Unsuported types')
    

divide(10, 2)
divide(10, 0)
divide(10, 'a')


def divide(a, b):
    if b == 0:
        raise Exception('Cannot divide by 0')
    print(a / b)
divide(10, 0)
