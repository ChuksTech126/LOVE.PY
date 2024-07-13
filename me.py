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