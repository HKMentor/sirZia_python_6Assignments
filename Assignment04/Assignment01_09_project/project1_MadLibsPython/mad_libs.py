# mad_libs.py

# Mad Libs Game - Simple Python Project

# Get user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")
verb = input("Enter a verb ending in -ing: ")

# Story using f-string
story = f"""
Once upon a time, there was a person named {name} who lived in {place}.
One day, they found a {animal} who looked very {emotion}.
They started {verb} together and became best friends!
"""

print("\nYour Mad Libs Story:")
print(story)
