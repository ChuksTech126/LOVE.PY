print("Hello, greetings from ChuksTech")
a=100
print(a)
a="Coming"
print(a)
ABS="Apple"
print(ABS)
d, t, y = "Dotun", 20, "Ade"
print(d, t, y)
is_student= False
print(is_student)
result = 10+10
print(result)
product = 7 - 5
print(product)
quotient = 20/4
print(quotient)
power = 2 ** 3
print (power)
power = 2 * 3
print(power)
g=f=t="Life Racing"
print("Life Racing")
int = 60
string = "Python is prefectly easy"
print(int)
print(string)
stay = "In Python, life is cool for programmer"
print(stay)
age = 50

if age <= 30:
    print("you are an adult")
else:
    print("you are a minor")   

simi_age = 56

if simi_age <= 54:
    print("I am matured")
else:
    print("You are not matured")
    
bimpe = 18
    #bimpe is a girl 
    #She is born on the street
    #I know of this
if bimpe >= 31:
    print("is married lady who is well known for promiscuity")
else:
    print("is promiscous and has not gotten a man")
Count = 10
while Count < 15:
    print(f"Count = {Count}")
    Count +=1
Score = 13
while Score > 9:
    print(f"Score = {Score}")
    Score -=1


    
fruits = ["banana", "EGG", "MANGO"]
for index,  fruit in enumerate(fruits):
    print(f"{index}.fruit: {fruit}")
    

for number in range(6):
    print(f"{number}")
    
for letter in range( 9, 29):
    print(f"{letter}")
    """
    Hello world, I am here again just as you have always wanted to show up every fucking day
    I will continually show up irrespective of what happens 
    not minding what happens i will show up for what i do
    Thanks for being yo
    """
#print("Hello, PLS God help me")

x = 10
y = "Love"
print(x)


z ='love'
z ='great'
print(z)


y, u, p = 10, 7, 9
print(y)
print(u)
print(p)


g = l = d = "Great Man"
print(g)
print(l)
print(d)


#Unpacking a list
fruits = ['grape', 'apple', 'orange']
g, a, o = fruits
print(g)
print(a)
print(o)


"""
I learn about outputting a multiple variable
with each value forming a single result
"""
x = "mango "
y = "is " 
z = "good"
print(x+y+z)


#Mathematical additions in python
s = 15
r = 40
print(s+r)

#defining a function and calling it
#global variable concept
q = "Awesome"

def my_func():
    print("Python is", q)
my_func()


#displacing a global variable and using a variable within function
#for clarity sake 
q = "Awesome"

def my_func():
    q = "coding fans"
    print("python is ", q)
my_func()

#global variable continues 
q = "Awesome"

def my_func():
    e = "fanstatical"
    print("python is", e)
my_func()

print("python is ", q)

#making a function variable global
def my_some():
    global t
    t = "Major"
my_some()

print("python is", t)

#NUMBER CONVERSION IN PYTHON
#THE FIRST IS #INT
#THE SECOND IS #FLOAT
#THE THIRD IS #COMPLEX
t = 4
u = 3.8
y = 4j

i = complex(t)
o = float(t)
print(i, o,)

#A start at random from previous- Number
from ast import Break
import random 
e = range(1,9)
print(random.randrange(1, 9))

y = float("56")
u = float("8.9")
i = float("7")
print(y, u, i)


r = str(56)
print(r)


#BOOLEAN RETURNS TRUE OR FALSE MOSTLY DEPENDING ON CONDITION
W = 20
i = 40

if W < i:
    print('TRUE')
else :
    print('FALSE')
    
def Func():
    return True
if Func():
    print('yes')
else:
    print('no')

#multiline string
a = """ i love  God
tthe Lord is Goood
he is A great God
"""
print(a)

w = " he is 'Johnny'"
print(w[13])


#loop thru String
for s in "bananas":
    print(s)
    
e = 'Hello, World'
print(len(e))
print(e[4])

#this search for a keyword in string and specifies whether present or not 
txt = "The best things in life are free!"
if "free" in txt:
  print('True'.lower())
  
txt = "The Best Things in life are free"
if "love" not in  txt:
    print('false'.upper())
    
    
y =  "hello, World"
print(y[2:5])

print(y[:-1])

t = 'hello world'
print(t.split())

u = "heloo, myG"
print(u.upper())

y = "hello daddy"
print(y.lower())

e = " great man "
u = (e.replace("a", "e",))
print(u.strip())

print( y, u)

age = 36
myself = f"my name is Nwachukwu Abraham Ikechukwu, I am {age}"
print (myself)

litre = f"the price per is {age:.2f}"
print(litre)

mine = 80
you =  f"i like me {age + mine}"
print(you)

#The IF statements
a = 40
b = 30
if b > a:
    print("The greater value")
elif b == a:
    print("same value")
else:
    print("The lesser value")
    
c = 30
d = 30
if d > c:
    print("The greater value")
elif d == c:
    print("same value")
else:
    print("The lesser value")
#Assignment for if condition
A = 600
d= 50
if d > A:
    print("The greater Number")
elif A == d:
    print("The Equal")
else:
    print("you are alone")
    
c = 55
e = 60
if d < A and e > c:
    print("True condition")

if A > d or e > c:
    print("Truth of it")
else:
    print("possibility")
    
if  not d > A and e > c:
    print("Not variable")
else:
    print("god of python")
    
if A > d:
    pass

A = 600
d= 50
c = 55
e = 60
if A > d:
    print("True")
if e > 55:
    print("Truth")
else:
    print("lost")

  
u = 10
z = 3
while z < u:
      print(z)
      if z == 10:
        continue
      z += 1
else:
      print("The Truth")
      
qwerty = ["love", "great", "You"]
for y in qwerty:
    print(y)
    if y == "great":
      continue
else:
    print('none')
    
esther = ['Joy', 'Thomas', 'Ruth']
micah  = ['white', 'Yellow', 'green']
for e in esther:
 for m in micah:
    print(e, m)
    
mine = ['mikel', 'obi', 'josiah']
football = ['jay', 'okocha', 'martins']
female = ['asisat', 'yemi', 'Simi']
for n in mine:
 for b in football:
  for l in female :
      print(n, b, l)
      
      
#Functions RELOOK
def my_func(fname):
    print(fname)
my_func('Emily') 
my_func('Tobias')
my_func('Nwachuwku Abraham Ikechukwu')

#FUNCTION CONTINUATION
def your_func(fname, lname):
    print(fname, '', lname)
your_func('Abraham',  'Nwachukwu')

y = "kids"
def their_function(*name):
   print(f"my name is ", name[0].capitalize(), 'I am a proud father of three wonderful {y}')
   print(f"my {y} are ", name[1]. capitalize(),"", name[2]. capitalize(),"", name[3].capitalize())
   print(f"the youngest of my {y} is", name[2]. upper())
    
their_function('abraham,', 'favour,', 'divine,', 'maduabuchi')