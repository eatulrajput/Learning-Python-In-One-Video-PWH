# Date: 12th March, 2024
# Author: Atul Rajput
# Place: Library

MyListOfNumbers = [1, 8, 7, 2, 21, 15]
print("Original list:", MyListOfNumbers)

MyListOfNumbers.sort()
print("Sorted list:", MyListOfNumbers)

MyListOfNumbers.reverse()
print("Reversed list:", MyListOfNumbers)

MyListOfNumbers.append(100) # It will add 100 at the end of the list
print("Appended List:", MyListOfNumbers)

MyListOfNumbers.insert(3,200) # It will insert 200 at index 3
print("List after insertion:", MyListOfNumbers)

MyListOfNumbers.pop(2) # It will remove the element at index 2
print("List after pop:", MyListOfNumbers)

MyListOfNumbers.pop() # It will remove the element from the end of the list
print("List after pop:", MyListOfNumbers)

MyListOfNumbers.remove(2) # It will remove the element 2 from the list
print("List after using remove:", MyListOfNumbers)

