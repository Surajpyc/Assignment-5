
# Python List Manipulation Example

This script demonstrates basic list operations in Python.

## Description

The script performs the following tasks:

1. Creates an empty list.
2. Appends integers from 1 to 10 to the list.
3. Prints each appended value (which will be `None` because `list.append()` returns `None`).
4. Displays the original list.
5. Extracts the first five elements of the list.
6. Reverses the extracted elements.
7. Displays the reversed values.

## Code

```python
list = []
for i in range(1, 11):
    print(list.append(i))
print("original list is ", list)
b = list[0:5]
print("the first five extracted values are ", b)
b.reverse()
print("the reverse values of extracted values are ", b)
```

## Output Explanation

- The `print(list.append(i))` lines output `None` because `append()` modifies the list in place and returns `None`.
- The final output shows the list after all values are appended, the first five extracted values, and those five values reversed.

## Note

Avoid naming variables `list` as it shadows the built-in `list` type in Python. Use a different variable name like `my_list` instead.
