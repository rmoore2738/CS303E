#Rebecca Moore RRM2738
#question 1
from random import randint
play_options = ["rock", "paper", "scissors"]   #the inputs accepted from the user
computer = play_options[randint(0,2)]
#the computer randomly selects an option, where rock is 0, paper is 1 and scissors
#is 2. this lets the computer always choose randomly and not keep the same choice

player = False    #begins loop

while player == False:
    player = input("Choose rock, paper, or scissors:")
    if player == computer:
        print("Computer is ",computer, ". You are ",player, ".\nDraw.")
        player = True   #ends loop to only play one game and then stop
    elif player == "rock":
        if computer == "paper":
            print("Computer is ",computer, "You are ",player, ".\nYou lose.")
            player = True
        else:
            print("Computer is ",computer, ". You are ",player, ".\nYou Win.")
            player = True
    elif player == "paper":
        if computer == "scissors":
            print("Computer is ",computer, "You are ",player, ".\nYou lose.")
            player = True
        else:
            print("Computer is ",computer, ". You are ",player, ".\nYou Win.")
            player = True
    elif player == "scissors":
        if computer == "rock":
            print("Computer is ",computer, "You are ",player, ".\nYou lose.")
            player = True
        else:
            print("Computer is ",computer, ". You are ",player, ".\nYou Win.")
            player = True
    else:
        print("invalid response")

    computer = play_options[randint(0,2)]
    #lets computer reset its choice for a new game

#Question 2
import turtle

turtle.pensize(3)    #sets thickness of line for all drawings
#input from the user to determine what shape and color the drawing will be
shape = input("Woiuld you like to draw a circle, square, or triangle?")
color = input("What color would you like?")


#to draw a circle
if shape == "circle":
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.color(color)     #the color the user inputs
    turtle.circle(100)
    turtle.hideturtle()
    turtle.done()
#to draw a square
if shape == "square":
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.color(color)   #the color the user inputs
    turtle.circle(100, steps = 4)
    turtle.hideturtle()
    turtle.done()
#to draw a triangle
if shape == "triangle":
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.color(color)   #the color the user inputs
    turtle.circle(100, steps = 3)
    turtle.hideturtle()
    turtle.done()
 #stops turtle without closing the window so you can see the shape
