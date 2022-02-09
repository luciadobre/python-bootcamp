#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to Tip Calculator!")
total = float(input("What's the bill total?"))
people = float(input("How many people have to split the bill?"))

tip = round((round(total))/people * 1.12, 2)


print(f"Adding the 12% tip, each of you has to pay {tip}$")