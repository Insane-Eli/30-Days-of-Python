# Day 2: 30 Days of python programming

import math

# Strings
first_name = 'Giannis'
last_name = 'Antetokounmpo'
full_name = first_name + ' ' + last_name
country = 'Greece'
city = 'Athens'

# Ints
age = 29
year = 2024

# Bools
is_married = True
is_true = True
is_light_on = False

# Multiple variables at same time
real_name, real_age, real_country = 'Eli', 16, 'America'

# Check data type
first_name_type = type(first_name)
age_type = type(age)
is_married_type = type(is_married)

# Find length of names
first_name_length = len(first_name)
last_name_length = len(last_name)
first_name_longer_by = first_name_length - last_name_length

# Math stuff
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Circle stuff
radius = 5
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

# User input stuff
radius = int(input("Enter a radius: "))
area_of_circle = math.pi * radius ** 2
print("Area of circle:", area_of_circle)
first_name = input("First name: ")
last_name = input("Last name: ")
country = input("Country: ")
age = int(input("Age: "))

# Keywords
help('keywords')


