print(12 + 25)

x = 25
y = "34"
z = 10.5

# grades is type of list here
grades = [5, 5.9, 8, 9.6]

# range() : generate range of given number , output: beginNumber , ....., endNumber-1
# lis() : convert range in list
numbers = list(range(0, 11))

# type() return type of variable
print(type(x), type(y), type(z), type(grades), type(numbers))

print(numbers)

odd_numbers = range(1, 11, 2)

print(odd_numbers, type(odd_numbers))
print(list(odd_numbers))

# The dir() function in python is an in-built function
# used on an object to look at all the properties / attributes
# and methods of that object,
# without its values (if the values of the attributes are given)
print(dir(odd_numbers))

# help() : If argument is given, it returns its documentation
# along with modules, keywords, and attributes
help(range.count)
