#Gulzat Kaipova
#8/4/2023

# The program iterates through the numbers from 1 to 50, replacing multiples of three with "Divisible by three,
# " multiples of five with "Divisible by five," and multiples of both three and five with "Divisible by both."

for number in range(1, 51):
    # all numbers divisible by both 3 and 5 are divisble by 15
    # and all numbers divisible by 15 are divisible by both 3 and 5
    if number % 15 == 0: 
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)

