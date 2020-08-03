#file read
f = open('test.txt')
r = f.read()

print(r)

f.close()
#file read
with open('test.txt', encoding='utf-8') as f:
    r = f.read()
    print(r)
    f.close()
#file readlines
with open('test.txt') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

#file write
with open('write_file.txt', 'w') as f:
    for i in range(10):
        f.write(f'newline_{i}\n')
    f.close()

#file append
with open('write_file.txt', 'a') as f:
    for i in range(10):
        f.write(f'append_mode_{i}\n')
    f.close()

#file write binary
f = open('binary_file', 'wb')
f.write('Text'.encode('utf-8'))
f.close()

#file read binary
f = open('binary_file', 'rb')
print(f.read())
f.close()

#Exercise
f = open("test.txt") 
Count = 0
Content = f.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Count += 1
          
print("Numarul de linii din fisier") 
print(Count)

# In Memmory files
import io

f = io.StringIO("Text")
print(f.getvalue())

f = io.StringIO("")
f.write("text")
print(f.getvalue())
print(f.getvalue())

f = io.BytesIO()
f.write(b'My binary data')
print(f.getvalue())

#import modules
import datetime
today = datetime.date.today()
now = datetime.datetime.now()

print(today)
print(now)

#import modules
from datetime import date, datetime

today = date.today()
now = datetime.now()

print(today)
print(now)

#import module math
import math

print(math.ceil(3.3))
print(math.floor(3.6))

log_e = math.log(math.e)
log_1 = math.log(1)
print(log_e, log_1)

#import module random
import random

rand = random.random()
print(rand)

print(random.randint(1, 5))

pets = ["cats", "dog", "fish"]
rand_choice = random.choice(pets)
print(rand_choice)

#import module urllib
from urllib.request import urlopen

response = urlopen('http://google.com/')
for line in response:
    print(line.decode('utf-8'), '\n')

#import function / modules
from base import base_function
from my_folder.utils import utils_function
base_function()
utils_function()
