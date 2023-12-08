# Bookbot
Bookbot is my first git project!

# Learned
## String Manipulation
### White Space Errors
The difference between text.split() and text.split(' ') lies in how Python's split() function handles whitespace.

text.split() with no arguments splits the string at whitespace characters such as space, tab, newline, return, and formfeed. It also treats consecutive whitespace characters as a single separator. So, if you have multiple spaces or a combination of spaces and tabs between words, split() will treat them as a single separator.

On the other hand, text.split(' ') splits the string at space characters only and treats each space as a separate separator. This means if you have multiple consecutive spaces between words, split(' ') will count each space as a separate split, resulting in extra empty strings in the resulting list.

In the context of counting words in a text, text.split() is generally more accurate because it handles multiple consecutive spaces and different types of whitespace characters correctly.

Next steps:

Use text.split() for a more accurate word count.
If you have any other questions about Python string methods or text processing, feel free to ask.

### Removing Spaces
You can remove spaces from a string in Python using the `replace()` method. Here's how you can do it:

```python
text = text.replace(' ', '')
```

This line of code will replace all spaces in the string with nothing, effectively removing them.

## Dictionaries
### Default Value for Missing Keys
Both `counter.get()` and `defaultdict` are valid ways to handle missing keys in a dictionary, and the choice between them often comes down to personal preference and the specific requirements of your code.

`defaultdict` can make your code cleaner and easier to read when you're frequently dealing with missing keys, as it automatically provides a default value for missing keys. This can be particularly useful in more complex scenarios where you're dealing with nested dictionaries or other data structures.

On the other hand, `counter.get()` gives you more flexibility, as you can specify a different default value for each key lookup. This can be useful if you need to handle missing keys in different ways in different parts of your code.

In terms of performance, both methods are generally quite fast, but `defaultdict` can be slightly faster in some cases because it doesn't need to check if a key exists before accessing it.

Next steps:
- Consider the specific requirements of your code to decide which method to use.
- If you're still unsure, you could try implementing your code both ways and see which you prefer.
- If you have any other questions about Python dictionaries or other data structures, feel free to ask.
### Conversion to List
You can convert a dictionary into a list in Python using the `items()` method, which returns a list of tuples where each tuple is a key-value pair. Here's how you can do it:

```python
def dict_to_list(dictionary):
    return list(dictionary.items())
```

This function takes a dictionary as an argument and returns a list of tuples.

You can use this function in your `print_report` function like this:

```python
def print_report(text):
    character_dictionary = get_character_dict(text)
    character_list = dict_to_list(character_dictionary)
    print(character_list)
```
## Lambda Functions
### Filtering
In Python, `filter()`, `map()`, and `reduce()` are built-in functions that operate on lists (and other iterable objects). Here's how you can use them:

1. `filter()`: This function constructs a list from elements of an iterable for which a function returns true.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```

2. `map()`: This function applies a given function to each item of an iterable and returns a list of the results.

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
```

3. `reduce()`: This function applies a rolling computation to sequential pairs of values in a list. For example, if you wanted to compute the product of a list of integers.

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce((lambda x, y: x * y), numbers)
```

Next steps:
- Using `filter()`, `map()`, and `reduce()` in my code.

### Sorting
**Sort()** will sort the list in-place, mutating its indexes and returning None , whereas **sorted()** will return a new sorted list leaving the original list unchanged. Another difference is that sorted() accepts any iterable while list. sort() is a method of the list class and can only be used with lists.

The `sort()` method in Python sorts the elements of a given list in a specific order - either ascending (default) or descending.

Here's how you can use it:

```python
# For a list of numbers
numbers = [5, 1, 9, 3, 7]
numbers.sort()
print(numbers)  # Output: [1, 3, 5, 7, 9]

# For a list of strings
words = ['apple', 'banana', 'cherry', 'date']
words.sort()
print(words)  # Output: ['apple', 'banana', 'cherry', 'date']
```

If you want to sort in descending order, you can use the `reverse` parameter:

```python
numbers = [5, 1, 9, 3, 7]
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 7, 5, 3, 1]
```

For a list of tuples or lists, you can use the `key` parameter to specify a function of one argument that is used to extract a comparison key from each element:

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

### Example Solution for Sorting

```python
def sort_on(d):
    return d["num"] # where num is the index of the value we are using to are a key for sorting
...
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
```
The sort() method in Python accepts a key parameter, which should be a function that takes a single argument and returns a key to use for sorting purposes. When you pass sort_on as the key argument to sort(), Python will call sort_on with each element of the list to determine its sort order.

In my code, sort_on is not used. Instead, a lambda function is used as the key for sorting: key=lambda char: char[1]. This lambda function takes each element (which is a tuple) and returns the second element of the tuple (at index 1) as the key for sorting.