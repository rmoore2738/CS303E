#Rebecca Moore RRM2738
#Question 1
print("I’m thinking of a number from 1 to 10000. Try to guess my \nnumber! (Enter 0 to stop playing.)")
guess = input("Please enter your guess:")
guess = int(guess)
number = 1458
if guess == number:
    print("That's correct! You win! You guessed my number in X guesses.")

while guess != number:
    if guess < number:
        print("Your guess is too low.")
        guess = input("Please enter your guess:")
        guess = int(guess)
    elif guess > number:
        print("Your guess is too high.")
        guess = input("Please enter your guess:")
        guess = int(guess)
    elif guess > 10000:
        guess = input("Please enter your guess:")
        guess = int(guess)

    elif guess == 0:
        print("Goodbye!")
    else:
        break


#question 2
spaces = 4 #number of spaces before stars
for i in range(1,6,1): #loop to draw stars
    print(" "*spaces + i*"*")
    spaces= spaces - 1

#question 3
import turtle #allows the use of turtle graphics
turtle.speed(10)
width=7
height=10
distance=30
for i in range (height):
    for i in range(width):
        turtle.circle(15)   # This line creates a circle with a diameter of 30
        turtle.penup()      # This lifts the pen up so that when the turtle moves it does not draw.
        turtle.forward(distance)  # Moves the turtle forward 30
        turtle.pendown()    # Puts the pen back down ready to draw the next time we go through the loop
    turtle.penup()
    turtle.back(distance*width)
    turtle.right(90)
    turtle.forward(distance)
    turtle.left(90)
    turtle.pendown()
turtle.done()
