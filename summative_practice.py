
def word_frequency(text: str) -> dict:
    pass

    """
    It should:

    Ignore case

    Remove punctuation

    Return a dictionary of word counts

    Example
    word_frequency("Hello hello world!")


    Returns:

    {"hello": 2, "world": 1}
    """


def flatten_list(data: list) -> list:
    pass

    """
    Flatten a nested list of arbitrary depth.
    Example

    flatten_list([1, [2, [3, 4], 5]])

    Returns:

    [1, 2, 3, 4, 5]
    """


def group_by_key(data: list, key: str) -> dict:
    pass

    """
    Given a list of dictionaries, group them by a specified key.
    Example

    data = [
        {"name": "Alice", "department": "IT"},
        {"name": "Bob", "department": "HR"},
        {"name": "Charlie", "department": "IT"},
    ]

    group_by_key(data, "department")

    Returns:

    {
        "IT": [
            {"name": "Alice", "department": "IT"},
            {"name": "Charlie", "department": "IT"}
        ],
        "HR": [
            {"name": "Bob", "department": "HR"}
        ]
    """

def top_n(numbers: list, n: int) -> list:
    pass

    """
    Return the top n largest unique numbers sorted descending.
    Example

    top_n([5, 1, 5, 3, 9, 9], 2)

    Returns:

    [9, 5]
    """

def merge_dicts(d1: dict, d2: dict) -> dict:
    pass

    """
    Rules:
    If key exists in both, sum the values.

    Otherwise include normally.
    """



def cache_results(func):
    pass

    """
    Write a decorator:

    That caches function results based on arguments.

    Test it on a slow recursive Fibonacci function.
    """


"""
Given:

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30}
]


Write a list comprehension to get names of people over 18.

Convert this list into a dictionary where name is the key and age is the value.

Sort by age descending.
"""

#What is __name__ == "__main__" used for?

"""
🔹 Question 7 — Linux Terminal Knowledge
1️⃣ What does this command do?
ls -la

2️⃣ What does this command do?
cat file.txt | grep "ERROR"


Explain:

What is a pipe (|)?

What is grep?

3️⃣ What does this do?
wc -l file.txt

4️⃣ How would you:

Redirect output to a file?

Append output to a file?

Redirect errors?

Give Linux examples.

5️⃣ Explain the difference between:
> 
>>

4️⃣ How do you make a Python script executable in Linux?

Assume you have a file myscript.py.

Write the steps using:

Shebang (#!)

chmod

Direct execution

5️⃣ What does this command do?
chmod +x myscript.py


What does +x mean?

6️⃣ What is the difference between these?
./myscript.py
python3 myscript.py


When would you use each?
"""