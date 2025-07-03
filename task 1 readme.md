
# Student Marks Dictionary Program

## Problem Statement
Write a Python program that:

1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student's name is not found, display an appropriate message.

## Code

```python
dict = {
    "Suraj": 75,
    "Shyam": 85,
    "Suryanshu": 95,
    "Dhruv": 62
}

user_input = input("enter a name to get their marks: ")
a = dict.get(user_input)
if user_input in dict:
    print("marks of {} is {}".format(user_input, a))
else:
    print("name not found")
```

## How to Use
1. Run the program in a Python environment.
2. Enter the student name when prompted.
3. The program will display the marks if the name exists, or show "name not found".

