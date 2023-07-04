import random
import time
import os

# See the readme.md at:
# https://github.com/mccright/ModReyTest/blob/main/README.md


# Implementing a strict function signature may help to
# ensure code written by any users will look recognizable
# to future developers/reviewers
def get_words(file_name: str, number_of_words: int, encoding="utf-8") -> list:
    # Read the contents of the file then load them into a list
    with open(file_name, 'r', encoding="utf-8") as file:
        words = [line.strip() for line in file]

    # 'Randomly' select twenty words from the list
    selected_words = random.sample(words, number_of_words)
    return selected_words


def print_words(present_these_words: list, seconds_on_screen: int, encoding="utf-8"):
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
FILENAME = '20k.txt'
NUMBEROFWORDS = 5
SECONDSONSCREEN = 3

# Clear the screen to start
os.system('cls' if os.name == 'nt' else 'clear')

presentthesewords = get_words(FILENAME, NUMBEROFWORDS, encoding="utf-8")

print_words(presentthesewords, SECONDSONSCREEN, encoding="utf-8")

# Ask the user to input the words they remember
user_input = input("Enter as many of the words you just saw as you can, separated by spaces: ")

# Compare the user input with the 'present_these_words' words and print matches
matches = [word for word in user_input.split() if word in presentthesewords]
print(f"\n{str(len(matches))} of your words matched one of \
the {str(len(presentthesewords))} words we presented:")
print(f"\nYou matched: {matches}")
print(f"\nWe had presented: {presentthesewords}")
