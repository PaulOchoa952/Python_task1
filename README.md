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
Sure, here is an updated version of the 

README.md

 file with more detailed instructions and examples:

```markdown
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
```

#### Methods:

- `new_entry(name: str, description: str) -> None`: Prompts the user to enter a name and description, then adds the entry to the dictionary.
- `print_dict() -> None`: Prints the keys and values of the entries dictionary.
- `look(name: str) -> str`: Returns the description of the entry with the given name.

#### Running the Program:

To run the program, execute the `task1.py` file. You can add entries and look them up as shown in the example usage.

```sh
python 

task1.py


```

#### Running Unit Tests:

Unit tests are provided in the `test_task1.py` file. To run the tests, use the following command:

```sh
python -m unittest 

test_task1.py


```
