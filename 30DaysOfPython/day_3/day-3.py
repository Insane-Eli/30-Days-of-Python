import math

# Data type examples
age = 16
height = 5.9
complex_num = 3 + 4j

# User-input computation examples
print("Triangle area calculation")
tri_base = float(input("Enter base: "))
tri_height = float(input("Enter height: "))
tri_area = tri_base * tri_height / 2
print("The area of the triangle is:", tri_area, "\n")

print("Triangle perimeter calculation")
tri_side_a = float(input("Enter side a: "))
tri_side_b = float(input("Enter side b: "))
tri_side_c = float(input("Enter side c: "))
tri_perimeter = tri_side_a + tri_side_b + tri_side_c
print("The perimeter of the triangle is:", tri_perimeter, "\n")

print("Rectangle area and perimeter calculation")
rect_base = float(input("Enter base: "))
rect_height = float(input("Enter height: "))
rect_area = rect_base * rect_height
print("The area of the rectangle is:", rect_area)
rect_perimeter = (rect_base + rect_height) * 2
print("The perimeter of the rectangle is:", rect_perimeter, "\n")

print("Circle area and circumference calculation")
radius = int(input("Enter a radius: "))
circle_area = math.pi * radius ** 2
print("Area of circle:", circle_area)
circumference = 2 * math.pi * radius
print("Circumference of circle:", circumference, "\n")

# Finding info about equations
coefficient_one = 2
constant_one = -2
print("y =", coefficient_one, "x", constant_one)
slope_one = coefficient_one
y_int_one = constant_one
x_int_one = -(constant_one)/coefficient_one
print("slope:", slope_one, "\ny-int:", y_int_one, "\nx-int:", x_int_one, "\n")

point1_two = (2, 2)
point2_two = (6, 10)
print("point1:", point1_two, "\npoint2:", point2_two)
slope_two = (point2_two[1]/point1_two[1])/(point2_two[0]/point1_two[0])
distance_two = math.sqrt((point2_two[1]-point1_two[1])**2 + (point2_two[0]-point1_two[0])**2)
print("slope:", slope_two, "\ndistance:", distance_two)
if slope_one > slope_two:
    print("slope one is bigger than slope two\n")
else:
    print("slope two is bigger than slope one\n")

print("x^2 + 6x - 9")
a_three = 1
b_three = 6
c_three = -9
discriminant = b_three**2 - 4*a_three*c_three
if discriminant >= 0:
    x1 = (-b_three + math.sqrt(discriminant)) / (2 * a_three)
    x2 = (-b_three - math.sqrt(discriminant)) / (2 * a_three)
    print("roots:", x1, "and", x2, "\n")
else:
    print("no real roots\n")

# Text comparisons
print("'python' is 'dragon':", "python" is "dragon")
print("'on' in 'python' and 'on' in 'dragon':", ("on" in "python") and ("on" in "dragon"))
print("I hope this course is not full of 'jargon':", "jargon" not in "I hope this course is not full of jargon")
print("'on' not in 'dragon' or 'python': ", ("on" not in "dragon") and ("on" not in "python"))
print("'python' char length:", str(len("python")))

# Number comparisons
def is_even(num):
    if num%2 == 0:
        return True
    if num%2 == 1:
        return False

print((7 // 3) == int(2.7))
print(type('10') == type(10))
print(int('9.8') == 10)

# Number calculations
hours = input("Enter hours:")
rate = input("Enter rate per hour:")
print("Your weekly earning is", hours*rate, "\n")

years = input("Enter number of years you have lived:")
if years > 100:
    years = 100 
print("You have lived for", 100*86400, "seconds\n")

col_one = 1
col_two = 1
col_four = 1
col_five = 1
for x in range(5):
    print(col_one + x, col_two, col_one + x, (col_four + x)**2, (col_five + x)**3)

