# Date: 14th March, 2024
# Author: Atul Rajput
# Place: Library

'''
Problem Statement: Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique.
'''
# Create an empty dictionary
friends_languages = {}

# Allow each friend to enter their favorite language
name = input("Enter the name of the first friend: ")
language = input("Enter their favorite language: ")
friends_languages[name] = language

name = input("Enter the name of the second friend: ")
language = input("Enter their favorite language: ")
friends_languages[name] = language

name = input("Enter the name of the third friend: ")
language = input("Enter their favorite language: ")
friends_languages[name] = language

name = input("Enter the name of the fourth friend: ")
language = input("Enter their favorite language: ")
friends_languages[name] = language

# Print the dictionary
print("Friend's favorite languages:")
for name, language in friends_languages.items():
    print(f"{name}: {language}")
