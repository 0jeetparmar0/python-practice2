# Hello World
**************************************************************************
print('Hello, World!')
name = input('What is your Name? ')
print('Hello, ' + name + '.')

#Temp_Conversion
**************************************************************************
def convertToFahrenheit(degreesCelsius):
    Fahrenheit = degreesCelsius * (9/5) + 32
    return Fahrenheit

def convertToCelsius(degreesFahrenheit):
    Celsius = (degreesFahrenheit - 32) * (5/9)
    return Celsius

print(convertToCelsius(0))
print(convertToCelsius(180))
print(convertToFahrenheit(0))
print(convertToFahrenheit(100))
print(convertToCelsius(convertToFahrenheit(15)))
print(convertToCelsius(convertToFahrenheit(42)))


#Odd_Even
**************************************************************************
def isOdd(number):
    return number%2 == 1

def isEven(number):
    return number%2 == 0

print(isOdd(42))
print(isOdd(9999))
print(isOdd(-10))
print(isOdd(-11))
print(isOdd(3.1415))
print(isEven(42))
print(isEven(9999))
print(isEven(-10))
print(isEven(-11))
print(isEven(3.1415))


#Area_Volume
**************************************************************************
def area(length,width):
    return (length * width)

def perimeter(length,width):
    return 2 * (length + width)

def volume(length,width,height):
    return (length * width * height)

def surfaceArea(length,width,height):
    return 2 * (length*width + length*height + width*height)

print(area(10, 10))
print(area(0, 9999))
print(area(5, 8))
print(perimeter(10, 10))
print(perimeter(0, 9999))
print(perimeter(5, 8))
print(volume(10, 10, 10))
print(volume(9999, 0, 9999))
print(volume(5, 8, 10))
print(surfaceArea(10, 10, 10))
print(surfaceArea(9999, 0, 9999))
print(surfaceArea(5, 8, 10))


#Fizz_Buzz
**************************************************************************
def fizzBuzz(upTo):
    for i in range(1,upTo+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz',end=' ')
        elif i%3==0:
            print('Fizz',end=' ')
        elif i%5==0:
            print('Buzz',end=' ')
        else:
            print(i,end=' ')

fizzBuzz(35)


#Ordinal_Sufix
**************************************************************************
def ordinalSuffix(number):
    numberStr = str(number)

    if numberStr[-2:] in ['11','12','13']:
        return numberStr +'th'
    elif numberStr[-1] == '1':
        return numberStr + 'st'
    elif numberStr[-1] == '2':
        return numberStr + 'nd'
    elif numberStr[-1] == '3':
        return numberStr + 'rd'
    else:
        return numberStr +'th'

print(ordinalSuffix(0))
print(ordinalSuffix(1))
print(ordinalSuffix(2))
print(ordinalSuffix(3))
print(ordinalSuffix(4))
print(ordinalSuffix(10))
print(ordinalSuffix(11))
print(ordinalSuffix(12))
print(ordinalSuffix(13))
print(ordinalSuffix(14))
print(ordinalSuffix(101))


#Ascii_Table
**************************************************************************
def printASCIITABLE():
    for i in range(32,127):
        print(i,chr(i))

printASCIITABLE()


#Character_Swap
**************************************************************************
import string
s=input("Enter String: ")
print(s.lower())

**********************
import string
x=input("Enter String: ")
print(s.swapcase())


#MenuDriven Temperature Conversion
**************************************************************************
ch = 0

def ctof():
    c = int(input("Enter Celsius: "))
    print("Fahrenheit: ",c*(9/5)+32)

def ftoc():
    f = int(input("Enter Fahrenheit: "))
    print("Celsius: ",(f-32)*(5/9))

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit")
while ch !=3:
    ch = int(input("Enter Choice: "))
    if ch==1:
        ctof()
    elif ch==2:
        ftoc()
    elif ch==3:
        break
    else:
        print("Enter Correct Choice")


#Total_Marks
**************************************************************************
sub1 = int(input("Enter Marks Subject 1: "))
sub2 = int(input("Enter Marks Subject 2: "))
sub3 = int(input("Enter Marks Subject 3: "))

tm = sub1+sub2+sub3
per = (tm/3)
print("Total Marks:",tm,"Out of 300")
print("Percentage:",per)

if(per>=80):
    print("Grade A")
elif(per>=70 and per<80):
    print("Grade B")
elif(per>=60 and per<70):
    print("Grade C")
elif(per>=40 and per<60):
    print("Grade D")
else:
    print("Grade E")


#AreaofRectangle_Square_Circle_Triangle
**************************************************************************
import math

def rectangle():
 length = float(input("Enter the length: "))
 width = float(input("Enter the width: "))
 print("The area of the rectangle is", length*width)

def square():
  side = float(input("Enter the side: "))
  print("The area of the square is", side*side)

def circle():
  radius = float(input("Enter the radius: "))
  print("The area of the circle is", math.pi*radius*radius)

def triangle():
  base = float(input("Enter the base: "))
  height = float(input("Enter the height: "))
  print("The area of the triangle is", 0.5*base*height)

print("1. Area of rectangle")
print("2. Area of square")
print("3. Area of circle")
print("4. Area of triangle")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
  rectangle()
elif choice == 2:
  square()
elif choice == 3:
  circle()
elif choice == 4:
  triangle()
elif choice==5:
  break
else:
  print("Invalid choice")


#fibonacci
**************************************************************************
def fibonacci(a):
    n1, n2 = 0, 1
    count = 0
    while count < a:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

x = int(input("Enter Number: "))
fibonacci(x)


#factorial
**************************************************************************
def factorial(a):
    x = 1
    for i in range(1,a+1):
        x*=i
        return x

n = int(input("Enter Number: "))
print("Factorial of",n,"is",factorial(n))


#sum of nth term
**************************************************************************
n = int(input("Enter the number of terms"))
sum1=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum1=sum1+(i/fact)
print(round(sum1,2))


#sumandproductofmatrix
**************************************************************************
import numpy as np

#creating two compatible matrices
matrix1 = np.array([[1, 2], [3, 4]]) 
matrix2 = np.array([[5, 6], [7, 8]])

#sum of two matrices
sum_matrix = np.add(matrix1, matrix2)
print("Sum of two matrices: \n", sum_matrix)

#product of two matrices
product_matrix = np.multiply(matrix1, matrix2)
print("Product of two matrices: \n", product_matrix)

#Kite (pygame)
**************************************************************************
import pygame
from sys import exit

pygame.init()
X = 600
Y = 600

scrn = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
pygame.display.set_caption('image')

imp = pygame.image.load("C:\\Users\kamal\Downloads\kite.png").convert()
#scrn.blit(imp, (-100,300))
imp_pos_x = -100
imp_pos_y = 300
status = True
while (status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    imp_pos_x += 1
    imp_pos_y -= 1
    scrn.blit(imp,(imp_pos_x,imp_pos_y))
    
    pygame.display.update()
    clock.tick(60)


#Kite Turtle
**************************************************************************
from turtle import *

color('red', 'yellow')

speed(10)

up()
left(-90)
forward(325)
left(-90)
forward(400)
left(180)
down()

left(45)
speed(0)
pensize(10)

for j in range(0,75):
    for i in range(0,4):
        forward(100)
        left(90)

    left(-90)
    forward(25)
    left(-135)
    forward(35)
    left(-135)
    forward(25)
    up()
    forward(10)
    down()
    clear()
done()


#fuctionsum
**************************************************************************
a = int(input("Enter Number one: "))
b = int(input("Enter Number two: "))

def sum():
    print("Sum Of Two Number:",(a+b))

def diff(a,b):
    print("Difference Of Two Number:",a-b)

def div():
    return a/b

def mul(a,b):
    return a*b

sum()
diff(a,b)
print("Division Of Two Number:",div())
print("Multiplication Of Two Number:",mul(a,b))


#Buy8get1
**************************************************************************
def freecoffee(amtcoffees,price):
    nofreecoffee = amtcoffees//9
    nopaidcoffee = amtcoffees - nofreecoffee
    return nopaidcoffee * price
printfreecoffee(7,2.50)
printfreecoffee(8,2.50)
printfreecoffee(9,2.50)
printfreecoffee(10,2.50)


#LeapYear
**************************************************************************
def isLeapYear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


#Validate date
**************************************************************************
import leapyear

def isValidDate(year, month, day):
    if not (1 <= month <= 12):
        return False

    if leapyear.isLeapYear(year) and month == 2 and day == 29:
        return True

    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <= 31):
        return False

    elif month in (4, 6, 9, 11) and not (1 <= day <= 30):
        return False

    elif month == 2 and not (1 <= day <= 28):
        return False

    return True

print(isValidDate(1999, 12, 31))
print(assert isValidDate(2000, 2, 29))
print(assert isValidDate(2001, 2, 29))
print(assert isValidDate(2029, 13, 1))
print(assert isValidDate(1000000, 1, 1))
print(assert isValidDate(2015, 4, 31))
print(assert isValidDate(1970, 5, 99))
print(assert isValidDate(1981, 0, 3))
print(assert isValidDate(1666, 4, 0))


#RockPaperScissors
**************************************************************************
def rpsWinner(move1, move2):
    if move1 == 'rock' and move2 == 'paper':
        return 'player two'
    elif move1 == 'rock' and move2 == 'scissors':
        return 'player one'
    elif move1 == 'paper' and move2 == 'scissors':
        return 'player two'
    elif move1 == 'paper' and move2 == 'rock':
        return 'player one'
    elif move1 == 'scissors' and move2 == 'rock':
        return 'player two'
    elif move1 == 'scissors' and  move2 == 'paper':
        return 'player one'
    else:
        return 'tie'


#Tutle: Square_Rectangle_Circle
**************************************************************************
#square
from turtle from *
for i in range(4):
    forward(100)
    left(90) 

#rectangle
from turtle from *
for i in range(2):
    forward(200)
    left(90)
    forward(100)
    left(90) 

#Circle
from turtle import *
circle(100)

#Shape1
**************************************************************************
from turtle from *
for i in range(5):
    for i in range(4):
	forward(100)
	left(90)
    penup()
    forward(50)
    left(90)
    forward(35)
    right(90)
    pendown()
    left(360/5)

#Shape2
**************************************************************************
from turtle import *

speed(1)
#1.two diamond
penup()
goto(-200,200)
pendown()
left(45)
angle = 90
for i in range(4):
    left(90)
    forward(100)
for i in range(4):
    forward(100)
    right(90)

#2.two triangle
right(45)
penup()
goto(125,125)
pendown()
for i in range(3):
    forward(100)
    left(120)
left(45)
forward(70)
right(90)
forward(70)
left(45)

#3. circle
penup()
goto(125,-125)
pendown()
y = 35
for i in range(5):
    circle(30)
    penup()
    if i%2==1:
        y = -35
    else:
        y = 35
    forward(35)
    right(90)
    forward(y)
    pendown()
    left(90)

#4. iso rectangle
penup()
goto(-250,-100)
pendown()

for i in range(4):
    forward(50)
    left(90)
forward(50)
for i in range(4):
    forward(50)
    right(90)
penup()
goto(-250,-100)
pendown()
goto(-200,-150)
penup()
goto(-150,-100)
pendown()
goto(-200,-50)
goto(-250,-50)
goto(-150,-150)


#Menu3DShape
**************************************************************************
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Curve():
    t = np.linspace(0, 2*np.pi, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, z)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Curve')

    plt.show()
   
def Sphere():
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='y')
    plt.show()
   
def Cone():
    r = 1
    h = 2
    n = 50
    theta = np.linspace(0, 2*np.pi, n)
    z = np.linspace(0, h, n)
    theta, z = np.meshgrid(theta, z)
    x = r * z/h * np.cos(theta)
    y = r * z/h * np.sin(theta)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='b')
    plt.show()
   
def Ring():
    r1, r2 = 1, 2
    n = 50
    theta = np.linspace(0, 2*np.pi, n)
    phi = np.linspace(0, 2*np.pi, n)
    theta, phi = np.meshgrid(theta, phi)
    x = (r2 + r1 * np.cos(theta)) * np.cos(phi)
    y = (r2 + r1 * np.cos(theta)) * np.sin(phi)
    z = r1 * np.sin(theta)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='r')
    plt.show()
   
def Cylinder():    
    r = 1
    h = 2
    n = 50
    theta = np.linspace(0, 2*np.pi, n)
    z = np.linspace(0, h, n)
    theta, z = np.meshgrid(theta, z)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='g')
    ax.plot_surface(x, y, -z, color='g')
    plt.show()
   
def menu():
    print('1. Curve\n2. Sphere\n3. Cone\n4. Ring\n5. Cylinder')
    choice = int(input('Enter your choice :'))
    if choice == 1:
        Curve()
    elif choice == 2:
        Sphere()
    elif choice == 3:
        Cone()
    elif choice == 4:
        Ring()
    elif choice == 5:
        Cylinder()
       
menu()


