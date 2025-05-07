# Age of a person and its categories:
age = int(input("Enter your age:"))
if age < 13:
    print("child")
elif 13 <= age <= 19:
    print("teenager")   
elif 20 <= age <=59:
    print("elder")
else:
    print("senior") 
# Check if number is Positive,Negative or Zero:  
num = int(input("Enter a number:"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero") 
# Operations on a list of numbers:
numbers=[54,87,98,43,76]
print("First item:",numbers[0])
print("Last item:",numbers[-1])
print("Maximum value:",max(numbers))
# Modify dictionary value:
car = {"brand": "toyota","model": "corolla", "year": 2021}
car["year"] = 2022
print("updated dictionary:",car)             