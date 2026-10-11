# Python Learning Journey

A beginner-friendly collection of Python lesson notes and small practice scripts. The material starts with Python fundamentals and builds toward working with variables, data types, type conversion, and user input.

## Lessons

Follow the lessons in order:

1. [Python Fundamentals](Lessons/01.%20Python%20Fundamentals.md) — learn what Python is, how programming works, how to install Python, and how to run your first script.
2. [Printing & Variables](Lessons/02.%20Printing%20%26%20Variables.md) — practice `print()`, variables, naming rules, f-strings, and importing modules.
3. [Data Types](Lessons/03.%20Data%20Types.md) — explore strings, integers, floats, booleans, lists, tuples, sets, and dictionaries.
4. [Type Checking](Lessons/04.%20Type%20Checking.md) — inspect values with `type()` and check types with `isinstance()`.
5. [Typecasting](Lessons/05.%20Typecasting.md) — convert values between types, including strings and bytes.
6. [User Input](Lessons/06.%20User%20Input.md) — read input with `input()`, convert it, and handle invalid values.

## Practice scripts

The [`Practice`](Practice) directory contains short examples that complement the lessons:

| Script | What it demonstrates |
| --- | --- |
| [hello.py](Practice/hello.py) | Printing a greeting |
| [variable.py](Practice/variable.py) | Storing and displaying example connection details |
| [type.py](Practice/type.py) | Comparing the types of values |
| [typecast.py](Practice/typecast.py) | Converting a string to a number and combining values |
| [conversion.py](Practice/conversion.py) | Encoding text as bytes and decoding it back |
| [input.py](Practice/input.py) | Reading a name, target, and port from the user |
| [ip_conversion.py](Practice/ip_conversion.py) | Converting an IPv4 address to its packed byte representation |
| [modules.py](Practice/modules.py) | Exploring modules and making an HTTP request |

## Running an example

Install Python 3, then run a script from the repository root:

```bash
python3 Practice/hello.py
```

On systems where Python 3 is available as `python`, you can use:

```bash
python Practice/hello.py
```

`Practice/modules.py` also imports the third-party `requests` package and makes a network request; the other examples use Python's standard library.

## Repository layout

- [`Lessons`](Lessons) — lesson notes and study material
- [`Practice`](Practice) — runnable example scripts
- [`LICENSE`](LICENSE) — repository license
