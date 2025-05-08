
#testing for loop in iterating through a string
text = "anaconda"
for char in text: 
    print(char)

#testing for loop in iterating through a list
colors = ["red", "blue", "green"]
for color in colors: 
    print(color)
    
#testing for loop in iterating through a tuple 
shapes = ("circle", "square", "triangle")
for shape in shapes: 
    print(shape)
    
#testing for loop in iterating through a dictionary
# person = {"name": "John", "age": 30, "city": "New York"}
# for key, value in person: 
#     print(key, value)
    
#Iterating over a list of names and send a greeting to each friend on the list
friends = ["Alice", "Bob", "Charlie"]
for friend in friends: 
    print("Hello, " + friend + "!")
    
#Building a countdown timer using a while loop
countdown = 10
while countdown > 0: 
    print("time left", countdown, "seconds")
    countdown -= 1
print("Event starts now!")

#generating a multiplication table using a nested loop
for i in range(1,6):
    for j in range(1,11):
        print(i * j, end="\t")
    print()
    
#testing the use of a function to calculate division of two numbers
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block always executes.")
    
#testing a function call
    
def calculate_sum(a, b):
    return a + b

result = calculate_sum(5, 10)
print("The sum is:", result)

#testing block statements in python
x = 10

x = 5

if x > 3:
    print("x is greater than 3")
    
    if x > 5:
        print("x is also greater than 5")
    else:
        print("x is not greater than 5")
else:
    print("x is not greater than 3")
    
#testing the use of functions in python
def person (name, age):
    print("Name:", name, "Age:", age)

person("Alice", 30)
person("Bob", 25)

    