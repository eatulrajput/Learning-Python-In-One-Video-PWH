# Date: 14th March, 2024
# Author: Atul Rajput
# Place: Library

'''
Problem Statement: Write  a program to creat a dictionary of hindi words with values as their English translation. Provide the user an option to look it up.
'''
oxford = {
    "ladki" : "wood",
    "kursi" : "chair",
    "chaku" : "knife"
}

key = input("Enter the key\n")
if(oxford.get(key)==None):
    print("Value not found")
else:
    print("The value corresponding to the key:",oxford.get(key))    