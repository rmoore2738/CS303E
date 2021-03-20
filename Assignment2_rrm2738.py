#Rebecca Moore RRM2738
#CS303E Assignment 2
import math

#1
length = input("Enter the length from the center to a vertex:")
sine = math.sin(math.pi/5)
side = (2 * float(length)) * sine
area = (3 * math.sqrt(3))/2  * math.pow(side,2)
print("The area of the pentagon is " +(format(area,".2f")))


#2
name = input("Enter employee’s name:")
hours = float(input("Enter number of hours worked this week:"))
rate = float(input("Enter hourly pay rate:"))
gross_pay = hours * rate

federal_tax = float(input("Enter federal tax withholding rate (%):"))
federal = federal_tax / 100
state_tax = float(input("Enter state tax withholding rate (%):"))
state = state_tax / 100
federal_withholding = gross_pay * federal
state_withholding = gross_pay * state



net_pay = gross_pay - federal_withholding - state_withholding
print(" ")
print("Weekly pay statement for",name)
print("Hours Worked:    ",hours)
print("Pay Rate:       $" + format(rate,".2f"))
print("Gross Pay:     $" + format(gross_pay,".2f"))
print("Deductions:")
print("  Federal Withholding","(",federal_tax,"%):  $" + format(federal_withholding,".1f"))
print("  State Withholding","(" , state_tax,"%):   $"  + format(state_withholding,".2f"))
print("Net Pay: $" + format(net_pay,".2f"))




#3
import turtle
turtle.speed(3)

turtle.penup()
turtle.goto(0,250)
turtle.begin_fill()
turtle.color("dark green")
turtle.circle(40, steps = 4)
turtle.end_fill()




turtle.penup()
turtle.goto(8,-40)
turtle.pendown()
turtle.begin_fill()
turtle.color("orange")
turtle.circle(150)
turtle.end_fill()

turtle.pensize(8)

turtle.penup()
turtle.goto(-60,150)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(30, steps = 3)
turtle.end_fill()



turtle.penup()
turtle.goto(60,150)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(30, steps =3)
turtle.end_fill()

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("black")
turtle.circle(100,90)

turtle.penup()
turtle.setheading(180)
turtle.goto(0,0)
turtle.pendown()
turtle.circle(-100,90)

turtle.penup()
turtle.goto(10,100)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(15, steps = 3)
turtle.end_fill()



turtle.hideturtle()


turtle.done()
