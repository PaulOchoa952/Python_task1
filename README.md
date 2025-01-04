### Task 1: Create a Class Dictionary

Create a class dictionary to which you can add words and their entries.

**Example Usage:**

```python
class Dictionary:
    def __init__(self):
        self.entries = {}

    def add_word(self, word, definition):
        self.entries[word] = definition

    def get_definition(self, word):
        return self.entries.get(word, "Word not found")

# Example
my_dict = Dictionary()
my_dict.add_word("apple", "A fruit that is sweet and crisp")
print(my_dict.get_definition("apple"))  # Output: A fruit that is sweet and crisp
```

### Task 2: Calculate Total Cost with Tax

Given a dictionary of items and their costs and an array specifying the items bought, calculate the total cost of the items plus a given tax.

**Example Usage:**

```python
def calculate_total_cost(items, bought_items, tax_rate):
    total_cost = sum(items[item] for item in bought_items)
    total_cost_with_tax = total_cost * (1 + tax_rate)
    return total_cost_with_tax

# Example
items = {"apple": 1.00, "banana": 0.50, "orange": 0.75}
bought_items = ["apple", "banana", "orange"]
tax_rate = 0.07
print(calculate_total_cost(items, bought_items, tax_rate))  # Output: 2.35
```

### Task 3: Concatenate nth Letters from Each Word

Concatenate the nth letters from each word in a list of words.

**Example Usage:**

```python
def concatenate_nth_letters(words, n):
    result = ''.join(word[n] for word in words if len(word) > n)
    return result

# Example
words = ["apple", "banana", "cherry"]
n = 1
print(concatenate_nth_letters(words, n))  # Output: "pah"
```

#### Running Unit Tests:

Unit tests are provided in the `test_task3.py` file. To run the tests, use the following command:

```sh
python -m unittest test_task1.py
```
```sh
python -m unittest test_task2.py
```
```sh
python -m unittest test_task3.py
```