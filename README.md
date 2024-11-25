## Python Tasks

### Task 1: Create a Class Dictionary

This task involves creating a class `Dictionary` which can add words and their entries. The class provides methods to add new entries, print the dictionary, and look up entries by name.

#### Example Usage:

```python
d = Dictionary()
d.new_entry('apple', 'fruit that grows on trees')
d.print_dict()
# Output:
# apple: fruit that grows on trees

print(d.look('apple'))
# Output:
# fruit that grows on trees

print(d.look('banana'))
# Output:
# Entry not found.

#### Running Unit Tests:

python -m unittest [test_task1.py]


```
```
