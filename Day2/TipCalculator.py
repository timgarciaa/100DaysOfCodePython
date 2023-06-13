#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

bill = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_count = input("How many people to slip the bill? ")

tip = float(tip_percentage) / 100
total_bill = float(bill) * tip + float(bill)
ambagan = total_bill / int(split_count)

print(f"Each person should pay: {round(ambagan, 2)}")