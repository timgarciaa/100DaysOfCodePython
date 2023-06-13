print("Hello"[0])
print("Hello"[4])

print(123 + 456)

print(123_456)

#int
#float
#boolean

num_char = len(input("What is your name? "))
print(type(num_char))
print(num_char)

str_num_char = str(num_char)

print("Your name has " + str_num_char + " characters")

two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

print(10**3)

print(3*3+3/3-3)

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = float(weight) / (float(height)**2)
print(bmi)
print(f"your bmi is: {round(bmi, 2)}")

print("{:.2f}".format(bmi))