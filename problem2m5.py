#Gulzat Kaipova
#8/4/2023

#The program prints each number from the list on a new line and, in a separate loop, 
#prints each number and its square on a new line as well.

# List of numbers
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a. Print each number on a new line
print("a. Numbers:")
for number in numbers:
    print(number)

# b. Print each number and its square on a new line
print("\nb. Numbers and Their Squares:")
for number in numbers:
    print(f"{number} - {number ** 2}")
