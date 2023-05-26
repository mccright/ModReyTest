import random
import time
import os

def get_words(filename: str, numberofwords: int) -> list:
    # Read the contents of the file then load them into a list
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]

    # 'Randomly' select twenty words from the list
    selected_words = random.sample(words, numberofwords)
    return selected_words

def print_words(present_these_words: list, seconds_on_screen: int):
    # Print one of the selected words every 'seconds_on_screen' seconds
    for word in present_these_words:
        print(f"\n\n\n\t\t{word}\n\n\n")
        time.sleep(seconds_on_screen)
        # Clear the screen before the next word
        os.system('cls' if os.name == 'nt' else 'clear')

# Word list from Google: 
# https://github.com/first20hours/google-10000-english/blob/master/20k.txt 
# ToDo: I need a list better taylored to a ModRey test -- where using 
# semantically and phonemically unrelated words improves the 
# quality of test results 
filename = '20k.txt'
numberofwords = 20
seconds_on_screen = 3

# Clear the screen to start
os.system('cls' if os.name == 'nt' else 'clear')

present_these_words = get_words(filename, numberofwords)

print_words(present_these_words, seconds_on_screen)

# Ask the user to input the words they remember 
user_input = input("Enter as many of the words you just saw as you can, separated by spaces: ")

# Compare the user input with the 'present_these_words' words and print matches
matches = [word for word in user_input.split() if word in present_these_words]
print(f"\n{str(len(matches))} of your words matched one of the {str(len(present_these_words))} words we presented:")
print(f"\nYou matched: {matches}")
print(f"\nWe had presented: {present_these_words}")
