# Python List Operations Example

This script demonstrates simple list operations in Python:

1. Creating a list of numbers from 1 to 10.
2. Extracting the first five elements from the list.
3. Reversing the extracted elements.

## Code

```python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list is ", list)

# Extract the first five elements
b = list[0:5]
print("The first five extracted values are ", b)

# Reverse the extracted values
b.reverse()
print("The reverse values of extracted values are ", b)
```

## Output

```
Original list is  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
The first five extracted values are  [1, 2, 3, 4, 5]
The reverse values of extracted values are  [5, 4, 3, 2, 1]
```
