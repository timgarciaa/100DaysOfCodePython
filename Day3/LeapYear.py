# Don't change the code below
year = int(input("Which year do you want to check? "))
# Don't change the code above

#Write your code below this line

cond1 = year % 4
cond2 = year % 100
cond3 = year % 400

if cond1 >= 1:
    print("Not leap year.")
else:
    if cond2 == 0:
        if cond3 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
