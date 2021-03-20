#Rebecca Moore RRM2738
#Assignment 1 CS303E


#1
name = input("What is your name? ")
print("Hello " + name + "! You\'ve just delved into Python. ")

#2
celsius = float(input("Enter a degree in Celsius: "))
Fahrenheit = (float(9/5) * celsius + 32)
print(celsius, "Celsius is", Fahrenheit, "Fahrenheit")

#3
bill, gratuity  = input("Enter the bill and gratuity rate: ").split(',')
Tip = eval(bill) * (eval(gratuity) / 100)
Total = Tip + eval(bill)
print("The gratuity is $" + format(Tip,".2f"),"and the total is $" + format(Total,".2f"))



#4
user_number = int(input("Enter a number between 0 and 1000: "))
sum = 0
for number in range(0,3):
    sum += user_number % 10
    user_number // 10

print("The sum of the digits is " + str(sum))


#5
seconds_year = 365*24*60*60
number_births_year = seconds_year // 7
number_deaths_year = seconds_year // 13
number_immigrants_year = seconds_year // 45

population = int(input("Enter the current population: "))

population += number_births_year - number_deaths_year + number_immigrants_year
print("The population in 1 year will be: " + str(population))


population += number_births_year - number_deaths_year + number_immigrants_year
print("The population in 2 years will be: " + str(population))


population += number_births_year - number_deaths_year + number_immigrants_year
print("The population in 3 years will be: " + str(population))


population += number_births_year - number_deaths_year + number_immigrants_year
print("The population in 4 years will be: " + str(population))


population += number_births_year - number_deaths_year + number_immigrants_year
print("The population in 5 years will be: " + str(population))



#6
weight_p = input("Enter your weight in pounds: ")
feet, inches = input("Enter your height (feet, inches): ").split(',')
weight_kg = eval(weight_p) * 0.454
height_total = eval(feet) + (eval(inches) / 12)
height_m = height_total * 0.3048
height_squared = height_m ** 2
BMI = (weight_kg / height_squared)
print("Your BMI is " + format(BMI,".2f"))
