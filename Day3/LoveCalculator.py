# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

score1 = 0
score2 = 0

score1 += name1_lowercase.count("t")
score1 += name1_lowercase.count("r")
score1 += name1_lowercase.count("u")
score1 += name1_lowercase.count("e")

score2 += name1_lowercase.count("l")
score2 += name1_lowercase.count("o")
score2 += name1_lowercase.count("v")
score2 += name1_lowercase.count("e")

score1 += name2_lowercase.count("t")
score1 += name2_lowercase.count("r")
score1 += name2_lowercase.count("u")
score1 += name2_lowercase.count("e")

score2 += name2_lowercase.count("l")
score2 += name2_lowercase.count("o")
score2 += name2_lowercase.count("v")
score2 += name2_lowercase.count("e")

score = int(str(score1) + str(score2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")



