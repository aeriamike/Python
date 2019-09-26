#CMPT 120 Assignment #3
#Author: Wen Xuan Xie (wxxie@sfu.ca)
#Last Date of Revision: Oct 16, 2014
#Times used: Approximately 8 hours

import turtle as t
import random as ran

#functions with parameters
def balloon_size():
    radius = ran.randint(25,175)
    t.circle(radius,360)
    return

def balloon_colors():
    red   = ran.random()
    green = ran.random()
    blue  = ran.random()
    t.fillcolor(red, green, blue)
    return

def star_colors():
    purple  = ran.random()
    pink = ran.random()
    yellow = ran.random()
    t.fillcolor(purple, pink, yellow)
    t.pencolor(purple, pink, yellow)
    return

#loops
def squareloop():
    t.fillcolor("#000000")
    t.begin_fill()
    for i in range (4):
        t.left(90)
        t.forward(30)
    t.end_fill()
    return

def logosquareloop():
    for i in range (4):
        t.forward(30)
        t.left(90)
    return

def starloop():
    for i in range (5):
        t.right(30)
        print star_colors()
        t.begin_fill()
        t.forward(150)
        t.right(120)
        t.forward(150)
        t.end_fill()

#components
def crystals():
    t.fillcolor("white")
    t.begin_fill()
    t.circle(6,360)
    t.end_fill()
    
def pupils():
    
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(9,360)
    t.end_fill()
    return

def glasses_circle():
    t.pencolor("#A9A9A9")
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.right(90)
    t.pensize(10)
    t.circle(50)
    t.end_fill()
    return

def brown_eyeballs():
    t.fillcolor("#B8860B")
    t.begin_fill()
    t.circle(20,360)
    t.end_fill()
    return

def dark_gloves():
    t.fillcolor("black")
    t.begin_fill()
    t.circle(25,360)
    t.end_fill()
    return

#body parts (Subroutine)
def body():
    t.pencolor("yellow")
    t.fillcolor("#FFFF00")
    t.begin_fill()
    t.left(90)
    t.circle(120,180)
    t.forward(180)
    t.left(30)
    t.circle(140,120)
    t.left(30)
    t.forward(180)
    t.end_fill()
    return

def glasses_straps():
    t.pencolor("black")
    t.left(90)
    t.forward(20)
    print squareloop()
    t.penup()
    t.forward(226)
    t.pendown()
    print squareloop()
    t.penup()
    t.left(180)
    t.forward(28)
    t.pendown()
    return

def glasses_lens():
    print glasses_circle()
    t.penup()
    t.left(90)
    t.forward(100)
    t.pendown()
    print glasses_circle()

def eyes():
    t.pensize(1)
    t.pencolor("white")
    t.penup()
    t.forward(18)
    t.left(90)
    t.forward(40)
    t.pendown()

    print brown_eyeballs()

    t.penup()
    t.right(180)
    t.forward(90)
    t.right(180)
    t.pendown()

    print brown_eyeballs()

    t.penup()
    t.left(90)
    t.forward(10)
    t.pendown()
    t.pensize(10)
    
    t.right(90)
    
    print pupils()

    t.penup()
    t.forward(90)
    t.pendown()

    print pupils()

    t.pensize(1)
    t.forward(2)
    t.left(90)
    t.forward(12)
    print crystals()

    t.penup()
    t.left(90)
    t.forward(90)
    t.right(90)
    t.pendown()
    t.pensize(1)
    t.forward(2)
    print crystals()

def mouth():
    t.pensize(2)
    t.penup()
    t.right(180)
    t.forward(80)
    t.left(90)
    t.forward(12)
    t.right(90)
    t.left(30)
    t.pendown()
    t.circle(40,120)
    t.left(30)
    
def clothes ():
    t.penup()
    t.right(90)
    t.forward(82)
    t.right(90)
    t.forward(4)
    t.right(60)
    t.pendown()

    t.pensize(1)
    t.pencolor("blue")
    t.fillcolor("#1E90FF")
    t.begin_fill()
    t.forward(65)
    t.right(120)
    t.forward(10)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(10)
    t.right(110)
    t.forward(67)
    t.left(110)
    t.forward(25)
    t.left(65)
    t.forward(65)
    t.right(65)
    t.forward(40)
    t.right(90)
    t.forward(60)
    t.left(120)
    t.circle(140,120)
    t.left(120)
    t.forward(60)
    t.right(90)
    t.forward(40)
    t.right(65)
    t.forward(65)
    t.left(65)
    t.forward(25)
    t.end_fill()
    return

def logo ():
    t.penup()
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    t.pencolor("black")
    t.pensize(2)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(25,360)
    t.end_fill()

    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()

    t.left(90)
    t.forward(3)
    t.right(45)

    print logosquareloop()

    t.end_fill()

    t.pencolor("black")
    t.left(45)
    t.forward(10)
    t.right(90)
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10,360)
    t.end_fill()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pencolor("white")
    t.pensize(3)
    t.forward(25)
    t.left(90)
    t.forward(2)
    t.pencolor("black")
    t.left(90)
    t.forward(25)

    t.pensize(1)
    t.penup()
    t.right(90)
    t.forward(40)
    t.left(90)
    t.pendown()
    t.forward(40)
    t.left(90)
    t.forward(60)
    t.circle(40,180)
    t.forward(60)
    t.left(90)
    t.forward(40)
    return

def pants():
    t.penup()
    t.forward(70)
    t.left(90)
    t.forward(110)
    t.pendown()
    t.fillcolor("#1E90FF")
    t.begin_fill()
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(50)
    t.end_fill()

    t.penup()
    t.right(90)
    t.forward(20)
    t.pendown()
    t.pencolor("black")
    t.begin_fill()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(60)
    t.end_fill()

def shoes():
    t.penup()
    t.right(180)
    t.forward(60)
    t.pendown()
    t.fillcolor("#CD853F")
    t.begin_fill()
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.circle(10,180)
    t.end_fill()

    t.penup()
    t.forward(80)
    t.pendown()
    t.forward(60)
    t.begin_fill()
    t.circle(10,180)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.end_fill()
    
def arms_and_gloves():
    t.penup()
    t.forward(170)
    t.left(90)
    t.forward(100)
    t.pendown()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(40,90)
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.right(180)
    t.forward(60)
    t.right(90)
    t.forward(10)
    print dark_gloves()

    t.penup()
    t.right(180)
    t.forward(200)
    t.left(90)
    t.forward(110)
    t.right(90)
    t.forward(60)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.forward(80)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.right(180)
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.right(180)
    print dark_gloves()

#random components
def random_balloon():
    t.pencolor("black")
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(100)
    t.right(90)

    print balloon_colors()
    t.begin_fill()
    print balloon_size()
    
    t.end_fill()

def star():
    t.left(90)
    t.penup()
    t.forward(260)
    t.right(60)
    t.pendown()
    print starloop()
    
    
    
#TOP LEVEL

print body()

print glasses_straps()

print glasses_lens()

print eyes()

print mouth()

print clothes()

print logo()

print pants()

print shoes()

print arms_and_gloves()

print random_balloon()

print star()
