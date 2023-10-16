import math
from datetime import timedelta
PI = math.pi

# 1
name = input("What's your name? ")
print("Hello" , name)
print("Hello " + name)

#2
age = int(input("What is your age? "))
birth_year = 2023 - age
print("So, you were born in " + str(birth_year))

#3
celsius_degree = int(input("What is the celsius degree? "))
fahrenheit_degree = (celsius_degree*9/5) + 32
print("Weather is " + str(fahrenheit_degree) + " fahrenheit degree")

#4
print("Enter a, b and c values for the equation ax + b = c.")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
x = (c - b) / a
print("X is: " + str(x))

#5
side1 = int(input("What is the length of side 1? "))
side2 = int(input("What is the length of side 2? "))
side3 = math.sqrt(side1**2 + side2**2)
print("Hyphotenus length is: " + str(side3))

#6
homework_grade = int(input("What is your homework grade: "))
midterm_grade = int(input("What is your midterm grade: "))
final_grade = int(input("What is your final grade: "))
course_grade = (homework_grade + 3*midterm_grade + 6*final_grade)/10
print("Your course grade:" , course_grade)

#7
r1 = int(input("What is radius 1? "))
r2 = int(input("What is radius 2? "))
r3 = (r1 + r2)*2
r1_area = PI*r1**2 
r2_area = PI*r2**2
r3_area = PI*r3**2 
blue_area = r3_area - r1_area - r2_area
print(blue_area)

#8
radius = int(input("What is the radius? "))
area = PI*radius**2
circumference = 2*PI*radius
smallest_squre_that_covers_circle = (2*radius)**2
largest_square_that_can_fit_in = ((2*radius)**2)/2
print(area,circumference,smallest_squre_that_covers_circle,largest_square_that_can_fit_in)

#9
y = int(input("a number between 0 and 10.000: "))

thousands = y // 1000
y -= 1000*thousands

hundreds = y // 100
y -= 100*hundreds

tens = y // 10
y-= 10*tens

ones = y

print(thousands,hundreds,tens,ones, sep = ' | ')

#10
sec = int(input("seconds? : "))

time = timedelta(seconds = sec)

print(time)