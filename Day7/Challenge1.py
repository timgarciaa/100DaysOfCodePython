import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, 3)]
print(chosen_word)
chosen_word2 = random.choice(word_list)
print(chosen_word2)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letter_guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for x in range(len(chosen_word) - 1):
    if letter_guess == chosen_word[x]:
        print(chosen_word[x])

for letter in chosen_word:
    print(letter)