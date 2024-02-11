import math
import circle
import polygon
import time


# Function to add two numbers
def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2


# Function to Raise to the power
def square(num1: object) -> object:
    return num1 ** number_2


# Function to find Sine of number 1
def sin(num_1=None):
    return math.sin(num_1)


# Function to find Cosine of number 1
def cosine(num_1=None):
    return cosine(num_1)


# Function to determine tangent of number 1
def tan(num_1=None):
    return math.tan(num_1)


# Function to convert miles to kilometres
def mile_to_kilometer(mile):
    return mile / 0.62137119


# Function to convert kilometres to miles
def kilometre_to_mile(kilometre):
    return kilometre * 0.62137119


# Function to find area of a circle
def area_of_circle(radius):
    return radius ** 2 * 3.14


# Function to compute radius of circle from circumference

def radius_of_circle(circumference):
    return circumference / 3


# Function to get circumference from radius
def circumference(radius):
    return radius * 6.28


# Function to convert kilograms to pounds


def kilograms_to_pounds(kilogram):
    return kilogram * 2.2


# Function to convert pounds to kilograms


def pounds_to_kilograms(pounds):
    return pounds / 2.2


print("Please select operation -\n")
print(
    "1. Add\n""2. Subtract\n""3. Multiply\n""4. Divide\n""5. x to the power of\n""6. Sine\n""7. Cosine\n""8. Tangent\n""9. Miles to kilometers\n""10. kilometre to miles\n""11. Area of circle\n""12. Find Radius from Circumference\n""13. Kilograms to pounds\n""14. Pounds to kilograms\n""15. Draw polygon\n""")

single_param_func = [6, 7, 8, 9, 10, 13, 14]
second_param_func = [15]
third_param_func = [11]
fourth_param_func = [12]

# Take input from the user
select = int(input("Select operations from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15: "))

if select in single_param_func:
    number_1 = float(input('Enter the value: '))
elif select in second_param_func:
    number_1 = float(input("Enter the amount of sides for polygon: "))
    number_2 = float(input('Enter the length of the sides for polygon: '))
elif select in third_param_func:
    number_1 = float(input("Input the Radius: "))
elif select in fourth_param_func:
    number_1 = float(input("Input Circumference: "))


else:
    number_1 = float(input('Enter first value: '))
    number_2 = float(input("Enter second value: "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
    print("Successfully Calculated")
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
    print("Successfully Calculated")
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    print("Successfully Calculated")
elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
    print("Successfully Calculated")
elif select == 5:
    print(number_1, '**', number_2, "=", square(number_1))
    print("Successfully Calculated")
elif select == 6:
    print(number_1, "sin", "=", math.sin(number_1))
    print("Successfully Calculated")
elif select == 7:
    print(number_1, "cosine", "=", math.cos(number_1))
    print('Successfully Calculated')
elif select == 8:
    print(number_1, "tan", "=", math.tan(number_1))
    print("Successfully Calculated")
elif select == 9:
    print(number_1, " miles is equal to"" ", mile_to_kilometer(number_1), " kilometres")
    print("Successfully Calculated")
elif select == 10:
    print(number_1, "kilometres is equal to"" ", kilometre_to_mile(number_1), " miles")
    print("Successfully Calculated")
elif select == 11:
    print(number_1, "Area of circle is equal to ", area_of_circle(number_1))
    print("Successfully Calculated")
elif select == 12:
    print(number_1, "has a radius of", radius_of_circle(number_1))
    print("Successfully Calculated")
elif select == 13:
    print(number_1, "Pounds is equal to", kilograms_to_pounds(number_1))
elif select == 14:
    print(number_1, "kilograms is equal to", pounds_to_kilograms(number_1))
elif select == 15:
    polygon.draw(number_1, number_2)
else:
    print('Invalid input')

time.sleep(5)




