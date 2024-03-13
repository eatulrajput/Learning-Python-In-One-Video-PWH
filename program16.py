# Date: 13th March, 2024
# Author: Atul Rajput
# Place: Library

'''
Problem Statement: Write a program to accept marks of 6 students and display them in a sorted manner.
'''
marks1 = int(input("Enter marks of student 1: "))
marks2 = int(input("Enter marks of student 2: "))
marks3 = int(input("Enter marks of student 3: "))
marks4 = int(input("Enter marks of student 4: "))
marks5 = int(input("Enter marks of student 5: "))
marks6 = int(input("Enter marks of student 6: "))

marks_board = [marks1, marks2, marks3, marks4, marks5, marks6]

print("Showing Original Marks", marks_board)
marks_board.sort()
print("Sorted Marks Board", marks_board)