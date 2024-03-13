# Date: 12th March, 2024
# Author: Atul Rajput
# Place: Library
'''
# Problem Statement: Write a program to fill in a letter template given below with name and date; 
Letter = Dear <|Name|>
You are selected!
<Date!>
'''
name = input("Enter name here: ")
date = input("Enter date here: ")

template = '''
Letter = Dear <|Name|>,
You are selected!
<|Date|>
'''
print(template.replace('<|Name|>', name).replace('<|Date|>', date))
