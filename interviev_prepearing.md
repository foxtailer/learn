## Table of Contents

### Beginner

- [Python Execution Pipeline](#python-execution-pipeline)
- [Variables](#variables)
- [Mutable / Immutable](#mutable--immutable)
- [Assignment in Python](#assignment-in-python)
- [Conditions (Bool Cond. Chain Cond.)](#conditions-bool-cond-chain-cond)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Try / Except](#try--except)
- [Iterables](#iterables)
- [Iterator](#iterator)
- [Generators](#generators)
- [Built-in Data Structures](#built-in-data-structures)
- [Functions](#functions)
- [Namespace](#namespace)
- [`*args` / `**kwargs`](#args--kwargs)
- [Common Methods](#common-methods)

### Intermediate

- [OOP](#oop)
- [Mixin](#mixin)
- [MRO (Method Resolution Order)](#mro-method-resolution-order--diamond-problem)
- [Comprehensions](#comprehensions)
- [Lambda / Map / Filter / Zip](#lambda--map--filter--zip)
- [Advanced Class](#advanced-class)
- [Dunder Methods](#dunder-methods)
- [Pip / PyPI](#pip--pypi)
- [Making Your Own Module](#making-your-own-module)
- [Virtual Environment](#virtual-environment)

### Advanced

- [Poetry](#poetry)
- [Big O Notation](#big-o-notation)
- [Closure](#closure)
- [Decorators](#decorators)
- [Context Manager (with)](#context-manager-with)
- [Metaclasses](#metaclasses)
- [Threads](#threads)
- [Concurrency](#concurrency)
- [Parallelism](#parallelism)
- [Multiprocessing](#multiprocessing)
- [GIL (Global Interpreter Lock)](#gil-global-interpreter-lock)
- [Race Condition](#race-condition)
- [Testing](#testing)
- [Build and Manipulate Packages](#build-and-manipulate-packages)
- [CPython](#cpython)

### Additional

- [Algorithms](#algorithms)
- [Data Structures](#data-structures)
- [Modules and Packages](#modules-and-packages)
- [Best Practices](#best-practices)
- [Anti-Patterns](#anti-patterns)
- [Problem Solving](#problem-solving)
- [Design Patterns](#design-patterns)
- [OSI Model](#osi-model)
- [TCP/IP Model](#tcpip-model)
- [HTTP / HTTPS](#http--https)
- [TCP / UDP](#tcp--udp)
- [Serialization](#serialization)
- [Git](#git)
- [Linux](#linux)
- [Common Ports and Protocols](#common-ports-and-protocols)
- [Regular Expressions](#regular-expressions)
- [Math](#math)
- [Statistics](#statistics)
- [Django](#django)
- [Flask](#flask)
- [Docker](#docker)
- [Logging](#logging)
- [Nginx](#nginx)
- [Gunicorn](#gunicorn)
- [REST API](#rest-api)
- [AJAX](#ajax)
- [ACID](#acid)
- [BASE](#base)
- [SQL](#sql)
- [SQLite](#sqlite)
- [PostgreSQL (PSQL)](#postgresql-psql)
- [Monolith vs Decomposed Monolith vs Microservices](#monolith-vs-microservices)
- [Pandas](#pandas)
- [Matplotlib](#matplotlib)
- [Ngrok](#ngrok)
- [Notes](#notes)

---

# **Python Interview Preparation**

---

## Python Execution Pipeline

The **Python Virtual Machine** (PVM) is the component of the Python interpreter that executes the compiled bytecode. When you write Python code, the process typically follows these steps:

1. **Parser**
   - **Role:** Converts your source code into an abstract syntax tree (AST).
   - **How It Works:** Reads and tokenizes the code (lexical analysis). Checks for syntax errors. Creates a tree structure representing the code's logic.
   - **Example:** `x = 5 + 3` — The parser creates a tree with nodes for:
     1. `=` (assignment)
     2. `x` (variable)
     3. `+` (addition)
     4. `5` and `3`

2. **Abstract Syntax Tree (AST)**
   - **Role:** A tree representation of the source code structure.
   - **Purpose:** Serves as an intermediate form for further processing.
   - **Usage:** Python provides a module (`ast`) to inspect and modify the AST.

3. **Compiler**
   - **Role:** Converts the AST into bytecode.
   - **Bytecode:** A lower-level, platform-independent representation of the code. Bytecode is stored in `.pyc` files in the `__pycache__` directory for reuse.
   - **Example Bytecode Instruction:**
     ```
     LOAD_CONST 5
     LOAD_CONST 3
     BINARY_ADD
     STORE_NAME x
     ```

4. **Python Virtual Machine (PVM)**
   - **Role:** Executes the bytecode.
   - **How It Works:** Reads one bytecode instruction at a time. Executes it using C-level functions. Manages Python's runtime features like memory allocation, function calls, and object operations.

5. **Garbage Collector**
   - **Role:** Automatically manages memory by removing unused objects.
   - **Key Features:**
     - Uses reference counting as the primary mechanism.
     - Handles cyclic references with a separate garbage collection process.
     - Controlled via the `gc` module.

6. **Global Interpreter Lock (GIL)**
   - **Role:** Ensures only one thread executes Python bytecode at a time.
   - **Purpose:** Simplifies memory management for CPython.
   - **Implication:** Limits true parallelism in multi-threaded Python programs.
   > However, the GIL is released during I/O operations — so threading is still useful and effective for I/O-bound tasks like network requests or file reading.

7. **Standard Library**
   - **Role:** Provides a rich set of built-in modules and tools (e.g., `os`, `sys`, `math`).
   - **How It Fits:** These modules are dynamically loaded as needed during execution.

8. **Built-in Functions and Objects**
   - **Role:** Provide essential functionality (e.g., `len`, `print`, `int`).
   - **Example:** Calling `len()` is directly handled by the interpreter as a special operation.

9. **C API**
   - **Role:** Allows the Python interpreter to interface with C extensions.
   - **Purpose:** Enables performance-critical tasks and native integrations.

```
    Python source code
        ↓
    Bytecode (.pyc)
        ↓
    PVM loop (written in C)
        ↓
    C functions
        ↓
    Machine instructions
        ↓
    CPU
```


---
# **BEGINNER**
---

## VARIABLES

Variables are containers for storing data values. A variable is created the moment you first assign a value to it (*name*).

> A *name* refers to or holds a reference to a concrete **object**. Python objects are concrete pieces of information that live in specific memory positions on the computer.

In Python, everything is treated as an object. Every object has these attributes:

**Identity (ID)** — This refers to the address that the object refers to in the computer's memory.
- Unique and constant for the object during its lifetime.
- You can obtain it using the `id()` function.
- The ID typically represents the memory address of the object in CPython, but this is not guaranteed in all Python implementations.

**Type (class)** — This refers to the kind of object that is created (e.g., integer, list, string).
- You can get the type of an object using the `type()` function.
- `type(x) == x.__class__  # True`

**Value** — This refers to the value stored by the object. For example, `List = [1, 2, 3]` would hold the numbers 1, 2, and 3.

**Reference counter** — Holds the number of links that point to an object.
- `x = 1; import sys; sys.getrefcount(x)`

> While ID and Type cannot be changed once created, values can be changed for **Mutable** objects.

> `(name)(variable) -> (reference)(id) -> (object)`

To sum up, every time we assign variables Python undertakes the three following steps:

1. Create an object in memory that holds the value.
2. If the variable name does not already exist in the namespace, go ahead and create it.
3. Assign the reference to the object to the variable name.

> A variable is a symbolic name in a system table that holds links (i.e., references) to objects. In other words, references are pointers from variables to objects (hold the location of objects). In Python though, variables do not have a type. Therefore, it is possible to assign objects of different type to the same variable name, as shown below. Behaves as a value that is contained.

*Object is a self-contained unit that bundles related data and behavior together.*
*Entity that lives in the computer's memory during execution.*

```
    x = 5
    y = "John"
    print(x)  # 5
    print(y)  # John
```

Variables do not need to be declared with any particular type, and can even change type after they have been set. Python makes extensive use of a type system known as **duck typing**. The system is based on objects' behaviors and interfaces.

> "If it walks like a duck and it quacks like a duck, then it must be a duck."

Duck typing is a type system where an object is considered compatible with a given type if it has all the methods and attributes (API) that the type requires.

```
    x = 4       # x is of type int
    x = "Sally" # x is now of type str
```

> If you want to specify the data type of a variable, this can be done with **casting**.

```
    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0
```

When we refer to objects we actually mean a piece of allocated memory that is capable of representing the value we wish. This value can be an integer, a string, or of any other type. Apart from the value, objects also come with a couple of header fields. These fields include the type of the object as well as its reference counter which is used by the Garbage Collector to determine whether it is fine to reclaim the memory of unused objects. And since Python objects are capable of knowing their own type, variables don't have to remember this piece of information.

**Reference Count:** Every object has a reference count, which tracks how many variables or objects are pointing to it.

**Tracking Reference Count:** The `sys` module provides the `getrefcount()` function, which can check the reference count of an object:

```
    import sys
    a = []
    print(sys.getrefcount(a))  # Output might be 2, as `a` and the argument in getrefcount both reference it
```

While the reference count is a key part of Python's memory management, Python also has a **cyclic garbage collector** to handle cases where objects reference each other in a cycle, which reference counting alone cannot handle.

```
    class Node:
        def __init__(self, name):
            self.name = name
            self.next = None

    # Create two objects referencing each other
    a = Node("A")
    b = Node("B")
    a.next = b
    b.next = a
```

The GC identifies these cycles and can clean them up, provided the objects are not reachable from the rest of the program.

The Python garbage collector (GC), which is part of the `gc` module, identifies circular references using a process called **tracing**. Here's how it works:

1. **Understanding Object Reachability**
   - The garbage collector differentiates between objects that are **reachable** and those that are **unreachable**.
   - **Reachable objects:** Can be accessed from active references in the program (e.g., global variables, local variables, or objects in use).
   - **Unreachable objects:** Are not directly or indirectly accessible from active references.

2. **Tracking Objects**
   - Python keeps track of all allocated objects in a structure called the **object graph**.
   - The GC maintains a list of all container objects (e.g., lists, dictionaries, and custom objects) that can potentially hold references to other objects.

**Weak References:**
Use weak references (`weakref` module) to break circular dependencies. Weak references do not increase the reference count.

```
    import weakref

    class Node:
        def __init__(self, name):
            self.name = name
            self.next = None

    a = Node("A")
    b = Node("B")
    a.next = weakref.ref(b)  # Weak reference prevents circular reference
    b.next = weakref.ref(a)
```

In Python, it is possible for multiple variables to reference the same object. This behavior is called a **"shared reference."** For example, consider the code below:

```
    a = 1
    b = a
    a = 'Hello World'
```

It is important to highlight that in this case, the value of variable `b` remains unchanged. Object `1` still exists because `b` refers to it. The reference from `a` to `1` is removed and `a` starts referring to `'Hello World'`.

**Note:**
As we have seen in the previous example, the last assignment `a = a - 1` won't modify the object itself since integer object type is **immutable**. This means that every time we want to change the value of an immutable object type (such as integer or string), Python is going to create a fresh object that holds the required value. For immutable types this is straightforward and makes altering variables quite safe since it does not impact the values of existing objects as in-place changes are not applicable on immutable object types.

**Mutable** object types enable in-place changes which means that when their value is modified, there is an impact on all variables referencing that object. Such object types include lists, dictionaries, and sets.

```
    list_1 = [1, 2, 3]
    list_2 = list_1
    list_1[0] = 0

    print(list_1)
    print(list_2)
    # >>> [0, 2, 3]
    # >>> [0, 2, 3]
```

### Copying Objects

Python comes with a built-in package called `copy` that offers functionality for copying objects. The two copy types are **shallow** and **deep**, and their difference relates to whether you have to deal with **compound objects** — that is, objects containing other objects — for instance a list of dictionaries, or a list of lists.

```
    import copy
    a = [1, 3, 4, 7]
    b = copy.copy(a)
    b[0] = -1
    print(a)
    print(b)
    # >>> [1, 3, 4, 7]
    # >>> [-1, 3, 4, 7]
```

> Slicing a mutable object (like a list) creates a shallow copy of the selected portion, not a deep copy. Same as:
> - `shallow_copy = list(original_list)`
> - `shallow_copy = original_list.copy()`
> - `shallow_copy = [*original_list]`
> - `shallow_copy = [i for i in original_list]`

However, shallow copies won't do the trick when you have a compound object with nested mutable types — for instance a list of lists. In the example below, we can see that if we take a shallow copy of a list of lists, a change of the original list `a` or the original compound object `c` will have an effect on the copied list `d`:

```
import copy
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [a, b]
d = copy.copy(c)
a[0] = -1
c[0][1] = -3
print(d)  # >>> [[-1, -3, 5, 7], [2, 4, 6, 8]]
```

This is because a shallow copy does not create a new object for the nested instances but instead copies their reference to the original object. In most cases we typically need to create a new object even for nested instances so that the copied compound object is completely independent from the old one. In Python this is called a **deep copy**.

```
import copy
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [a, b]
d = copy.deepcopy(c)
a[0] = -1
c[0][1] = -3
print(d)
# >>> [[1, 3, 5, 7], [2, 4, 6, 8]]
```

- `id()` — gives us the object identity.
- `is` — compares IDs.
- `==` — compares values.

```
import copy

some_list = [1, [2], 3]
print(some_list is copy.copy(some_list))                # False
print(some_list[1] is copy.copy(some_list)[1])          # True
```


## MUTABLE / IMMUTABLE

**Mutable** objects are those that allow you to change their value or data in place without affecting the object's identity. In contrast, **immutable** objects don't allow this kind of operation. You'll just have the option of creating new objects of the same type with different values.

### Objects of built-in type that are mutable:

- Lists
- Sets
- Dictionaries
- User-Defined Classes (it purely depends upon the user to define the characteristics)

> We can use `setdefault` in dict to avoid `KeyError`:
> ```
> numberOfPets.setdefault('cats', 0)  # Does nothing if 'cats' exists.
> ```

You can use the `collections.defaultdict` class to eliminate `KeyError` errors entirely.

```
import collections
scores = collections.defaultdict(int)
scores
# defaultdict(<class 'int'>, {})
scores['Al'] += 1  # No need to set a value for the 'Al' key first.
scores
# defaultdict(<class 'int'>, {'Al': 1})
scores['Zophie']  # >> 0 No need to set a value for the 'Zophie' key first.
scores['Zophie'] += 40
scores
# defaultdict(<class 'int'>, {'Al': 1, 'Zophie': 40})

import collections
booksReadBy = collections.defaultdict(list)
booksReadBy['Al'].append('Oryx and Crake')
booksReadBy['Al'].append('American Gods')
len(booksReadBy['Al'])
# 2
len(booksReadBy['Zophie'])  # The default value is an empty list.
# 0
```

### Objects of built-in type that are immutable:

- Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
- Strings
- Tuples
- Frozen Sets
- User-Defined Classes (it purely depends upon the user to define the characteristics)


## ASSIGNMENT IN PYTHON

### Basic Form
This form is the most common form.

```
student = 'Geeks'
print(student)  # >> Geeks
```

### Tuple Assignment

```
# equivalent to: (x, y) = (50, 100)
x, y = 50, 100

print('x = ', x)  # >> x = 50
print('y = ', y)  # >> y = 100
```

### List Assignment
This works in the same way as the tuple assignment.

```
[x, y] = [2, 4]

print('x = ', x)  # >> x = 2
print('y = ', y)  # >> y = 4
```

### Sequence Assignment

```
a, b, c = 'HEY'

print('a = ', a)  # >> a = H
print('b = ', b)  # >> b = E
print('c = ', c)  # >> c = Y
```

### Extended Sequence Unpacking
It allows us to be more flexible in how we select portions of a sequence to assign.

```
p, *q = 'Hello'

print('p = ', p)  # >> p = H
print('q = ', q)  # >> q = ['e', 'l', 'l', 'o']

*a, b = 'Hello'
# a >> ['H', 'e', 'l', 'l']
# b >> ['o']
```

### Multiple-Target Assignment

```
x = y = 75
print(x, y)  # >> 75 75
```

In this form, Python assigns a reference to the same object (the object which is rightmost) to all the targets on the left.

### Augmented Assignment
The augmented assignment is a shorthand assignment that combines an expression and an assignment.

```
x = 2
# equivalent to: x = x + 1
x += 1
print(x)  # >> 3
```

There are several other augmented assignment forms: `-=`, `**=`, `&=`, etc.


## CONDITIONS (BOOL COND. CHAIN COND.)

Python supports the usual logical conditions from mathematics:

| Operator | Description                  |
|----------|------------------------------|
| `a == b` | Equals                       |
| `a != b` | Not Equals                   |
| `a < b`  | Less than                    |
| `a <= b` | Less than or equal to        |
| `a > b`  | Greater than                 |
| `a >= b` | Greater than or equal to     |

Python compares lists by elements: `a[0]` compared to `b[0]`, `a[1]` compared to `b[1]`...
`[2] > [1, 1]` → `True` because `2 > 1`

These conditions can be used in several ways, most commonly in "if statements" and loops.

**Chained conditionals** are simply a "chain" or a combination of multiple conditions. We can combine conditions using the following three keywords:

- `and`
- `or`
- `not`

The `and` keyword allows us to check if two conditions are true. If they are both true then the entire condition is true. If one or both of them are false then the entire condition is false.

The `or` keyword allows us to check if one of two conditions is true. If one or both of the conditions are true then the entire condition will be true. If both of the conditions are false then the entire condition is false.

The `not` keyword allows us to check if an entire condition is false. If the condition is false it will result in a true value. If the condition is true it will give us a false value (you can think of it as reversing the condition).

```
True and False   # False
True and True    # True
False and False  # False

True or False    # True
True or True     # True
False or False   # False

not True         # False
not False        # True
```

Both the `and` and `or` operators in Python are **lazy (short-circuiting)**. This means they evaluate expressions only as far as needed to determine the result, potentially skipping the evaluation of subsequent expressions.

`and` evaluates its left operand first:
- If the left operand is falsy (e.g., `False`, `0`, `None`, `''`), it immediately returns the left operand without evaluating the right operand.
- If the left operand is truthy, it proceeds to evaluate the right operand and returns its result.

`or` evaluates its left operand first:
- If the left operand is truthy, it immediately returns the left operand without evaluating the right operand.
- If the left operand is falsy, it proceeds to evaluate the right operand and returns its result.

We can also combine the use of these keywords to create longer conditions:

```
(True or False) and False   # False
False and True and True     # False
(True or False) and True    # True
True and not(False)         # True

not(1 > 2 and 2-7 == -5)   # True
```


## OPERATORS

Operators are used to perform operations on variables and values. Python divides the operators into the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

### Arithmetic

| Operator | Name           | Example  |
|----------|----------------|----------|
| `+`      | Addition       | `x + y`  |
| `-`      | Subtraction    | `x - y`  |
| `*`      | Multiplication | `x * y`  |
| `/`      | Division       | `x / y`  |
| `%`      | Modulus        | `x % y`  |
| `**`     | Exponentiation | `x ** y` |
| `//`     | Floor division | `x // y` |

### Assignment

| Operator | Example    | Same As      |
|----------|------------|--------------|
| `=`      | `x = 5`    | `x = 5`      |
| `+=`     | `x += 3`   | `x = x + 3`  |
| `-=`     | `x -= 3`   | `x = x - 3`  |
| `*=`     | `x *= 3`   | `x = x * 3`  |
| `/=`     | `x /= 3`   | `x = x / 3`  |
| `%=`     | `x %= 3`   | `x = x % 3`  |
| `//=`    | `x //= 3`  | `x = x // 3` |
| `**=`    | `x **= 3`  | `x = x ** 3` |
| `&=`     | `x &= 3`   | `x = x & 3`  |
| `\|=`    | `x \|= 3`  | `x = x \| 3` |
| `^=`     | `x ^= 3`   | `x = x ^ 3`  |
| `>>=`    | `x >>= 3`  | `x = x >> 3` |
| `<<=`    | `x <<= 3`  | `x = x << 3` |

The `:=` symbol is the **walrus operator** in Python, introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression, meaning you can both assign and evaluate in a single line.

```
# Without :=
line = input("Enter text: ")
while line != "quit":
    print(line)
    line = input("Enter text: ")

# With :=
while (line := input("Enter text: ")) != "quit":
    print(line)

nums = [1, 3, 4, 5]
squares_over_10 = [square for num in nums if (square := num ** 2) > 10]
print(squares_over_10)  # Output: [16, 25]

import re
text = "Email: example@example.com"
if (match := re.search(r'\S+@\S+', text)):
    print("Found email:", match.group())
```

### Comparison

| Operator | Description                  |
|----------|------------------------------|
| `==`     | Equal                        |
| `!=`     | Not equal                    |
| `>`      | Greater than                 |
| `<`      | Less than                    |
| `>=`     | Greater than or equal to     |
| `<=`     | Less than or equal to        |

**Chain comparison:**

```
# Unpythonic Example
if 42 < spam and spam < 99:

# Pythonic Example
if 42 < spam < 99:

spam = eggs = bacon = 'string'
spam == eggs == bacon == 'string'  # True
```

> Whenever you compare a value to `None`, you should almost always use the `is` operator rather than the `==` operator. `==` can be overloaded. There is only one `None` object in any Python program.

### Logical

| Operator | Description                                                      |
|----------|------------------------------------------------------------------|
| `and`    | Returns `True` if both statements are true                       |
| `or`     | Returns `True` if one of the statements is true                  |
| `not`    | Reverse the result, returns `False` if the result is true        |

- `not` evaluates argument to boolean.
- `or` and `and` return one of the parameters.
- `or` — if first is `True` return first, else return second.
- `and` — if first is `False` return first, else return second.

### Identity

| Operator  | Description                                             |
|-----------|---------------------------------------------------------|
| `is`      | Returns `True` if both variables are the same object    |
| `is not`  | Returns `True` if both variables are not the same object |

### Membership

| Operator  | Description                                                              |
|-----------|--------------------------------------------------------------------------|
| `in`      | Returns `True` if a value is present in the object                       |
| `not in`  | Returns `True` if a value is not present in the object                   |

### Bitwise

| Operator | Description                                                           |
|----------|-----------------------------------------------------------------------|
| `&`      | AND — Sets each bit to 1 if both bits are 1                           |
| `\|`     | OR — Sets each bit to 1 if one of two bits is 1                       |
| `^`      | XOR — Sets each bit to 1 if only one of two bits is 1                 |
| `~`      | NOT — Inverts all the bits                                            |
| `<<`     | Zero fill left shift — Shift left by pushing zeros in from the right  |
| `>>`     | Signed right shift — Shift right by pushing copies of the leftmost bit |

### Precedence Order

The precedence order is described in the table below, starting with the highest precedence at the top:

| Operators                                                   | Description                                           |
|-------------------------------------------------------------|-------------------------------------------------------|
| `()`                                                        | Parentheses                                           |
| `**`                                                        | Exponentiation                                        |
| `+x`, `-x`, `~x`                                            | Unary plus, unary minus, and bitwise NOT              |
| `*`, `/`, `//`, `%`                                         | Multiplication, division, floor division, and modulus |
| `+`, `-`                                                    | Addition and subtraction                              |
| `<<`, `>>`                                                  | Bitwise left and right shifts                         |
| `&`                                                         | Bitwise AND                                           |
| `^`                                                         | Bitwise XOR                                           |
| `\|`                                                        | Bitwise OR                                            |
| `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons, identity, and membership operators |
| `not`                                                       | Logical NOT                                           |
| `and`                                                       | AND                                                   |
| `or`                                                        | OR                                                    |

If two operators have the same precedence, the expression is evaluated from left to right.

### Ternary Operator in Python

In Python, the Ternary Operator determines if a condition is `True` or `False` and then returns the appropriate value as the result.

```
# Syntax: true_value if condition else false_value
```

**Ternary Operator in Nested If-Else:**

```
# Syntax: true_value if condition1 else (true_value if condition2 else false_value)

a = 10
b = 20
print("Both are equal" if a == b else "a is greater" if a > b else "b is greater")
```

**Ternary Operator using Python Tuple:**

```
# Syntax: (false_value, true_value)[condition]

a = 10
b = 20
print(("b is minimum(0 False)", "a is minimum(1 True)")[a < b])
```

**Ternary Operator using Python Dictionary:**

```
print({True: "a is minimum", False: "b is minimum"}[a < b])
```

**Ternary Operator using Python Lambda:**

```
a = 10
b = 20
print((lambda: "b is minimum", lambda: "a is minimum")[a < b]())
```

**Shorthand Ternary:**
In Python there is also the shorthand ternary tag which is a shorter version of the normal ternary operator you have seen above.

```
>>> True or "Some"
True
>>> False or "Some"
'Some'

>>> def my_function(real_name, optional_display_name=None):
>>>     optional_display_name = optional_display_name or real_name
>>>     print(optional_display_name)
>>> my_function("John")
John
>>> my_function("Mike", "anonymous123")
anonymous123
```


## CONTROL FLOW

A program's control flow is the order in which the program's code executes. The control flow of a Python program is regulated by conditional statements, loops, and function calls.

Python has three types of control structures:

- **Sequential** — default mode
- **Selection** — used for decisions and branching
- **Repetition** — used for looping, i.e., repeating a piece of code multiple times.

**Sequential** statements are a set of statements whose execution process happens in a sequence. The problem with sequential statements is that if the logic has broken in any one of the lines, then the complete source code execution will break.

**Selection** statements allow a program to test several conditions and execute instructions based on which condition is true.

Some Decision Control Statements are:

- Simple `if`
- `if-else`
- Nested `if`
- `if-elif-else`

**Simple `if`:** If statements are control flow statements that help us to run a particular code, but only when a condition is met or satisfied. A simple `if` only has one condition to check.

```
n = 10
if n % 2 == 0:
    print("n is an even number")
print('end')
```

**`if-else`:** The `if-else` statement evaluates the condition and will execute the body of `if` if the test condition is `True`, but if the condition is `False`, then the body of `else` is executed.

```
n = 5
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")
print('end')
```

**Nested `if`:** Nested `if` statements are an `if` statement inside another `if` statement.

```
a = 5
b = 10
c = 15
if a > b:
    if a > c:
        print("a value is big")
    else:
        print("c value is big")
elif b > c:
    print("b value is big")
else:
    print("c is big")
```

**`if-elif-else`:** The `if-elif-else` statement is used to conditionally execute a statement or a block of statements.

```
x = 15
y = 12
if x == y:
    print("Both are Equal")
elif x > y:
    print("x is greater than y")
else:
    print("x is smaller than y")
```

A **repetition** statement is used to repeat a group (block) of programming instructions. In Python, we generally have two loops/repetitive statements:

- `for` loop
- `while` loop

#### Definite Loop
A definite loop is a loop that runs a predetermined number of times. The number of iterations is known before the loop starts.

**Characteristics:**
- Fixed iterations: The loop runs a set number of times.
- Example: `for` loops in many programming languages where the range is specified.

#### Indefinite Loop
An indefinite loop runs an unknown number of times. The number of iterations is not known beforehand and depends on some condition being met during the execution of the loop.

**Characteristics:**
- Condition-based: The loop runs based on a condition that is evaluated during each iteration.
- Example: `while` loops in many programming languages where the loop continues until the condition is false.

**`for` loop:** A `for` loop is used to iterate over a sequence that is either a list, tuple, dictionary, or a set. We can execute a set of statements once for each item in a list, tuple, or dictionary.

```
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    print(lst[i], end=" ")

for j in range(0, 10):
    print(j, end=" ")
else:
    # Else block runs if the loop completes without encountering a `break`.
    pass
```

**`while` loop:** In Python, `while` loops are used to execute a block of statements repeatedly until a given condition is satisfied. Then, the expression is checked again and, if it is still true, the body is executed again. This continues until the expression becomes false.

```
m = 5
i = 0
while i < m:
    print(i, end=" ")
    i = i + 1
print("End")
```

The `else` clause is only executed when your `while` condition becomes `False`. If you `break` out of the loop, or if an exception is raised, it won't be executed.

```
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")
```


## TRY / EXCEPT

| Block     | Description                                                              |
|-----------|--------------------------------------------------------------------------|
| `try`     | Lets you test a block of code for errors.                                |
| `except`  | Lets you handle the error.                                               |
| `else`    | Lets you execute code when there is no error.                            |
| `finally` | Lets you execute code, regardless of the result of the try- and except blocks. |

You can define as many exception blocks as you want, e.g., if you want to execute a special block of code for a special kind of error:

```
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except Exception as e:
    print(f"Something else went wrong {e}")
```

The `raise` keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.

```
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
```

Nested try-except with finally:

```
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
```

### Common Python Exceptions

| Exception           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `AssertionError`    | Raised when the `assert` statement fails.                                   |
| `EOFError`          | Raised when the `input()` function meets the end-of-file condition.         |
| `AttributeError`    | Raised when the attribute assignment or reference fails.                    |
| `TabError`          | Raised when the indentations consist of inconsistent tabs or spaces.        |
| `ImportError`       | Raised when importing a module fails.                                       |
| `IndexError`        | Occurs when the index of a sequence is out of range.                        |
| `KeyboardInterrupt` | Raised when the user inputs interrupt keys (Ctrl + C or Delete).            |
| `RuntimeError`      | Occurs when an error does not fall into any category.                       |
| `NameError`         | Raised when a variable is not found in the local or global scope.           |
| `MemoryError`       | Raised when programs run out of memory.                                     |
| `ValueError`        | Occurs when an argument has the right type but the wrong value.             |
| `ZeroDivisionError` | Raised when you divide a value or variable by zero.                         |
| `SyntaxError`       | Raised by the parser when the Python syntax is wrong.                       |
| `IndentationError`  | Occurs when there is a wrong indentation.                                   |
| `SystemError`       | Raised when the interpreter detects an internal error.                      |

All Python exceptions: https://docs.python.org/3/library/exceptions.html

**`assert`:**

```
>>> number = 42
>>> assert number > 0, f"number greater than 0 expected, got: {number}"

>>> number = -42
>>> assert number > 0, f"number greater than 0 expected, got: {number}"
Traceback (most recent call last):
    ...
AssertionError: number greater than 0 expected, got: -42
```


## ITERABLES

An **iterable** is an object capable of returning its members one by one. Said in other words, an iterable is anything that you can loop over with a `for` loop in Python.

**Sequences** are a very common type of iterable. Some examples for built-in sequence types are lists, strings, and tuples.

"Under the hood," an iterable is any Python object with an `__iter__()` method or with a `__getitem__()` method that implements Sequence semantics.

**How Traversal with `__getitem__` Works:**
When you traverse a collection using `__getitem__`, you typically use indexing like `obj[i]` to access elements. This approach requires that the entire data structure be present in memory and available for random access. Each call to `obj[i]` retrieves the element at index `i` directly from the collection.

**Sequence protocol:**
```
class CustomSequence:  # Sequence/Iterable
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")
```

**Iterator protocol:**
```
class CustomIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration
```

### Useful Built-in Functions That Accept Iterables

| Function   | Description                                                      |
|------------|------------------------------------------------------------------|
| `list()`   | Construct a list from an iterable.                               |
| `tuple()`  | Construct a tuple from an iterable.                              |
| `dict()`   | Construct a dictionary from an iterable.                         |
| `set()`    | Construct a set from an iterable.                                |
| `sum()`    | Sum the contents of an iterable.                                 |
| `sorted()` | Return a list of the sorted contents of an iterable.             |
| `any()`    | Returns `True` if `bool(item)` was `True` for any item.          |
| `all()`    | Returns `True` only if `bool(item)` was `True` for all items.    |
| `max()`    | Return the largest value in an iterable.                         |
| `min()`    | Return the smallest value in an iterable.                        |

Python provides an extremely useful functionality, known as **iterable unpacking**, which allows us to write simple, elegant code:

```
>>> my_list = [7, 9, 11]
>>> x, y, z = my_list
>>> print(x, y, z)
7 9 11
```

The built-in `enumerate` function allows us to iterate over an iterable, while keeping track of the iteration count.

```
>>> for entry in enumerate("abcd"):
        print(entry)

(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')

# Using `enumerate` to keep iteration count
none_indices = []

# note the use of iterable unpacking!
for iter_cnt, item in enumerate([2, None, -10, None, 4, 8]):
    if item is None:
        none_indices.append(iter_cnt)

# `none_indices` now stores: [1, 3]
```

> `range` returns an iterable.


## ITERATOR

Python's iterators and iterables are two different but related tools that come in handy when you need to iterate over a data stream or container. Iterators power and control the iteration process, while iterables typically hold data that you want to iterate over one value at a time.

An **iterator** is an object that can be iterated upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which implements the **iterator protocol**, which consists of the methods `__iter__()` and `__next__()`.

> `next()` with a second argument returns it when no more items in sequence:
> ```
> next(iterator, '@')
> ```

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from. All these objects have an `iter()` method which is used to get an iterator:

```
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry
```

The `for` loop actually creates an iterator object and executes the `next()` method for each loop.

> **Note:** Every iterator is also an iterable, but not every iterable is an iterator in Python.

```
import random
d = iter(lambda: random.randrange(10), 7)
list(d)  # >>> [3, 4, 6, 0, 9, 4, 8, 9, 8, 5, 8, 1, 1, 5, 1, 4, 4, 0, 3, 5, 6] or ...
```

- `lambda: random.randrange(10)`: This lambda function generates a random integer between 0 (inclusive) and 10 (exclusive) each time it is called.
- `iter(callable, sentinel)`: The `iter` function creates an iterator that repeatedly calls the provided callable. The iteration stops when the callable returns the sentinel value (7 in this case).
- `list(d)`: This converts the iterator `d` into a list by consuming all its values.

### Lazy Traversing

**Lazy traversing** (also known as lazy evaluation or lazy iteration) refers to a technique where elements of a sequence or collection are generated or accessed only as needed, rather than all at once. This approach is particularly useful when working with large data sets or potentially infinite sequences, as it avoids loading or processing everything in memory upfront.

**Characteristics of Lazy Traversing:**

- **On-Demand Computation:** Elements are produced one at a time when requested, instead of generating all elements at once. This means memory usage is minimized because only the required elements are in memory at any point.

- **Efficient Memory Usage:** Since data isn't stored all at once, you can work with huge (even infinite) data streams without running out of memory. For example, iterating over a generator yields one value at a time, without building a list of all elements.

- **Useful for Infinite Sequences:** Lazy traversing is especially effective for creating infinite sequences, as you only generate values as needed and can stop at any point, which wouldn't be possible with a fully evaluated sequence.


## GENERATORS

A **generator function** in Python is defined like a normal function, but whenever it needs to generate a value, it does so with the `yield` keyword rather than `return`. Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator. Generator objects are used either by calling the `next` method of the generator object or using the generator object in a "for in" loop.

```
    def fibonacci_gen():
        yield 0
        yield 1
        prev_prev, prev = 0, 1

        while True:
            result = prev + prev_prev
            prev_prev, prev = prev, result
            yield result

    g = fibonacci_gen()  # Return generator
    for i in g:
        print(i)
```

A generator enters the function, runs through lines until it meets `yield`. When `yield` occurs, the function returns some value and remembers the line of execution. After the next `next()` call, the generator returns to that line it remembers.

```
    def interleave_gen(a, b):
        a = iter(a)
        b = iter(b)
        while True:
            yield next(a)
            yield next(b)
```

**Embedded generator:**

```
    def join_Generator(a, b):
        # Enter 'a' and next generator call returns values from 'a' until 'a' is exhausted.
        yield from a
        yield from b

    j = join_Generator(range(2), range(3))  # 0, 1, 0, 1, 2, StopIteration

    # `yield from` is like:
    #     for item in iterable:
    #         yield item
```

```
    def flipper_Generator(a, b):
        while True:
            yield a
            yield b

    def counter_Generator():
        n = 0
        while True:
            yield n
            n += 1

    def cycler_Generator(maximum):
        n = 0
        while True:
            yield n
            n = n + 1
            if n >= maximum:
                n = 0
```

> `itertools` contains a lot of iterators and generators.

```
    def bgfun():
        res = 'Start'
        while res:
            res = yield f'/{res}/'
        yield 'Finish'

    ite = bgfun()
    next(ite)      # >>> '/Start/'
    ite.send(123)  # >>> '/123/'
    ite.send('qqq')# >>> '/qqq/'
    ite.send(0)    # >>> 'Finish'
```

### Generator Expression

In Python, a generator expression is another way of writing the generator function. It uses the Python list comprehension technique but instead of storing the elements in a list in memory, it creates generator objects.

```
    # Syntax: (expression for item in iterable)

    squares = (x * x for x in range(3))
    print(next(squares))  # Output: 0
    print(next(squares))  # Output: 1
    print(next(squares))  # Output: 4
```

> `g.send(None) <=> next(g) <=> g.__next__()`


### Generator with `send()`

```
    def responder():
        print("Ready to receive")
        while True:
            msg = yield  # waits here until .send(value) is called
            print("Received:", msg)

    g = responder()
    next(g)               # Prime the generator — starts and runs until first `yield`
    g.send("Hello")       # Output: Received: Hello
    g.send("Another one") # Output: Received: Another one
```

You must `next()` the generator once before the first `send()` to advance it to the first `yield`.

```
def running_average():
    total = 0
    count = 0
    average = None
    while True:
        num = yield average
        total += num
        count += 1
        average = total / count

avg_gen = running_average()
next(avg_gen)  # prime

print(avg_gen.send(10))  # 10.0
print(avg_gen.send(20))  # 15.0
print(avg_gen.send(30))  # 20.0
```

> `g.next() <=> g.send(None)`


## BUILT-IN DATA STRUCTURES

| Type          | Category       | Description                                  |
|---------------|----------------|----------------------------------------------|
| `int`         | Numeric        | Integer numbers                              |
| `float`       | Numeric        | Floating-point numbers                       |
| `complex`     | Numeric        | Complex numbers                              |
| `str`         | String         | Sequence of characters                       |
| `list`        | Sequence       | Ordered, mutable sequence                    |
| `tuple`       | Sequence       | Ordered, immutable sequence                  |
| `range`       | Sequence       | Arithmetic progression of numbers            |
| `bytes`       | Binary         | Immutable sequence of bytes                  |
| `bytearray`   | Binary         | Mutable sequence of bytes                    |
| `memoryview`  | Binary         | Memory view of a buffer                      |
| `dict`        | Mapping        | Key-value pairs                              |
| `bool`        | Boolean        | `True` or `False` (subclass of `int`)        |
| `set`         | Set            | Unordered collection of unique elements      |
| `frozenset`   | Set            | Immutable version of `set`                   |

> `bool` data type is a subclass of the `int` data type.

- **List** is an ordered sequence of some data written using square brackets `[]` and commas.
- **Tuple** is another data type which is a sequence of data similar to a list. But it is immutable. Data in a tuple is written using parentheses and commas.
- **Dictionary** is an unordered sequence of data of key-value pair form. It is similar to a hash table type. Dictionaries are written within curly braces in the form `key:value`.

> In Python, an object is considered **hashable** if it has a hash value that remains constant during its lifetime. Hashable objects must implement the `__hash__()` and `__eq__()` methods. The hash value of an object is used in hashing algorithms, such as those implemented by dictionaries and sets, to quickly compare keys and store/retrieve values.

```
    class HashList(list):
        def __hash__(self):
            return 1
        def __eq__(self, value):
            return True
```

### Hash Table

A **hash table** is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

Hash tables must support 3 fundamental operations:

| Operation                 | Description                                     |
|---------------------------|-------------------------------------------------|
| `Insert(key, value)`      | Adds an item to the hash table.                 |
| `get(key)`                | Fetches the value with the help of the given key. |
| `delete(key)`             | Removes a value with the help of the given key. |

These operations should ideally execute in **O(1)** time.

In a hash table, every key is unique. We should use this data structure when the ordering and sorting of data is not needed, because the order of data is not retained here.

The hash function can produce an index that has already been used in the table, which is called a **collision**.

```
index = hash(key) % table_size
```

A collision can be handled using various techniques:

#### Separate Chaining Technique

- **Insert:** Compute the index using the hash function. If the bucket at that index is empty, insert the element. If the bucket already contains elements, append the new element to the linked list.
- **Search:** Compute the index using the hash function. Search the linked list at the computed index for the desired key.
- **Delete:** Compute the index using the hash function. Search for the element in the linked list at that index, then remove it if found.

#### Open Addressing Technique

- **Hash Function:** Calculates the initial index for inserting a key.
- **Collision Handling:** If the calculated index is already occupied (collision), open addressing looks for the next available empty slot based on a probing technique.
- **Probing:** The process of finding the next open slot in the hash table by following a specific sequence. Different types: linear probing, quadratic probing, and double hashing.

> Function `hash(value)` returns the hash of a value.

### Set Operations

**Intersection:**
```
A = {'a', 'b', 'c'}   B = {'b', 'c', 'd'}
B & A = {'b', 'c'}
```

**Union:**
```
A = {'a', 'b', 'c'}   B = {'b', 'c', 'd'}
B | A = {'a', 'b', 'c', 'd'}
```

**Difference:**
```
A = {'a', 'b', 'c'}   B = {'b', 'c', 'd'}
A - B = {'a'}
B - A = {'d'}
```

**Symmetric Difference:**
```
A = {'a', 'b', 'c'}   B = {'b', 'c', 'd'}
A ^ B = {'a', 'd'}
```


## FUNCTIONS

A function is a block (callable object) of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

### Parameters or Arguments?

The terms **parameter** and **argument** can be used for the same thing: information that is passed into a function.

From a function's perspective:
- A **parameter** is the variable listed inside the parentheses in the function definition.
- An **argument** is the value that is sent to the function when it is called.

Python uses the mechanism of passing arguments **by sharing object reference** during function calls. The name of variable is reserved in local scope and refers to some object.

"**Scope**" generally refers to the set of variables, functions, and objects accessible at a given point in a program.

### Function Life Cycle

```
fu()
```
1. Matches Parameters
2. Create new namespace (local scope)
3. Execute function body until `return` statement or runs out of code.
4. Return result or `None`

### Function Side Effects

A function is said to have a **side effect** if it changes anything outside of its function definition, like changing arguments passed to the function or changing a global variable.

```
def fn_side_effects(fruits):
    print(f"Fruits before change - {fruits} id - {id(fruits)}")
    fruits += ["pear", "banana"]
    print(f"Fruits after change - {fruits} id - {id(fruits)}")

fruit_list = ["apple", "orange"]
print(f"Fruits List before function call - {fruit_list} id - {id(fruit_list)}")
fn_side_effects(fruit_list)
print(f"Fruits List after function call - {fruit_list} id - {id(fruit_list)}")

# Output
# Fruits List before function call - ['apple', 'orange'] id - 1904767477056
# Fruits before change - ['apple', 'orange'] id - 1904767477056
# Fruits after change - ['apple', 'orange', 'pear', 'banana'] id - 1904767477056
# Fruits List after function call - ['apple', 'orange', 'pear', 'banana'] id - 1904767477056
```

This function clearly has side effects due to:
- The ID of argument and parameter are exactly the same.
- The argument has additional values added after the function call.

**Function without side effect:**

```
def fn_no_side_effects(fruits):
    print(f"Fruits before change - {fruits} id - {id(fruits)}")
    fruits = fruits + ["pear", "banana"]
    print(f"Fruits after change - {fruits} id - {id(fruits)}")

fruit_list = ["apple", "orange"]
print(f"Fruits List before function call - {fruit_list} id - {id(fruit_list)}")
fn_no_side_effects(fruit_list)
print(f"Fruits List after function call - {fruit_list} id - {id(fruit_list)}")

# Output
# Fruits List before function call - ['apple', 'orange'] id - 2611623765504
# Fruits before change - ['apple', 'orange'] id - 2611623765504
# Fruits after change - ['apple', 'orange', 'pear', 'banana'] id - 2611625160320
# Fruits List after function call - ['apple', 'orange'] id - 2611623765504
```

### Order of Arguments

We have the following argument types at our disposal:

| Type                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Positional arguments | Matched from left to right                                                  |
| Keyword arguments   | Matched by name                                                             |
| Default arguments   | Assigned default values if omitted in function call                         |
| `*args`             | Iterables unpacked into individual positional arguments                     |
| `**kwargs`          | Dictionaries unpacked into individual keyword arguments                     |

The default values are evaluated at the point of function definition in the defining scope:

```
i = 5

def f(arg=i):
    print(arg)

i = 6
f()  # will print 5
```

**Important warning:** The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

```
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]
```

If you don't want the default to be shared between subsequent calls:

```
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```

### Function Annotations

Are completely optional metadata information about the types used by user-defined functions. Annotations are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on any other part of the function.

```
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

>>> f('spam')
# Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# Arguments: spam eggs
# 'spam and eggs'
```

### Documentation Strings

- The first line should always be a short, concise summary of the object's purpose. This line should begin with a capital letter and end with a period.
- If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.
- The following lines should be one or more paragraphs describing the object's calling conventions, its side effects, etc.


## NAMESPACE

Namespaces in Python use the **LEGB** (Local, Enclosing, Global, Built-in) rule.

```
str = 'global'
def outer():
    str = 'enclosing'
    def inner():
        str = 'local'
```

We use the `nonlocal` keyword to create nonlocal variables:

```
# outside function
def outer():
    message = 'local'

    # nested function
    def inner():
        # declare nonlocal variable
        nonlocal message
        print("inner:", message)  # inner: local
        message = 'nonlocal'

    inner()
    print("outer:", message)  # outer: nonlocal

outer()
```

Scopes aren't stored in a single physical location but exist in Python's **symbol tables**, which map variable names to their values.
- The **local symbol table** is created each time a function is called, mapping local variables within that function.
- The **global symbol table** maps global variables in the module.
- **Built-ins** are kept in the built-in namespace (usually loaded when Python starts).

You can view the names available in the current scope using the built-in functions `locals()` and `globals()`. The built-in scope can be accessed through the `__builtins__` module. You can list all built-in names by looking at `dir(__builtins__)`.

The `dir()` function is used to get a list of the names of attributes and methods associated with an object. Without arguments, `dir()` returns the list of names in the current local scope.

`__dict__` is a dictionary or mapping object that stores an object's (or class's) writable attributes. It essentially contains all the instance variables (attributes) of an object in the form of key-value pairs, where the key is the attribute's name (as a string), and the value is the corresponding data. (Contains only the object's instance attributes.)

1. If there is a global x declaration, x comes from and is assigned to the x global
variable module.4
2. If there is a nonlocal x declaration, x comes from and is assigned to the x local
variable of the nearest surrounding function where x is defined.
3. If x is a parameter or is assigned a value in the function body, then x is the local
variable.
4. If x is referenced but is not assigned and is not a parameter:
    - x will be looked up in the local scopes of the surrounding function bodies
    (nonlocal scopes).
    - If not found in surrounding scopes, it will be read from the module global
    scope.
    - If not found in the global scope, it will be read from __builtins__.__dict__.


## `*ARGS` / `**KWARGS`

`*args` is simply shortened for "arguments." It is used when we are not sure how many arguments we should pass to the function. By using `*args`, you are allowed to pass any number of arguments when calling a function.

```
def friends(*args):
    print(args)

friends("Sachin", "Rishu", "Yashwant", "Abhishek")
# >>> ('Sachin', 'Rishu', 'Yashwant', 'Abhishek')
```

We get a Tuple because when we use `*args`, the function will get the arguments as a tuple. There is one exception: when passing regular arguments and `*args` as parameters to a function, never pass `*args` before regular arguments.

Unlike `*args`, `**kwargs` takes keyword or named arguments. The type of `**kwargs` is Dictionary — the arguments are accepted as key-value pairs. We cannot pass `**kwargs` before `*args` in the function definition; otherwise, we'll get a `SyntaxError`.

```
def hello(write, **kwargs):
    print(write)
    for key, value in kwargs.items():
        print(f"{key} is {value}.")

write = "RGB stands for:"
hello(write, One="Red", two="Green", three="Blue")

# Output:
# RGB stands for:
# One is Red.
# two is Green.
# three is Blue.
```

```
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# with *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
# arg1: two
# arg2: 3
# arg3: 5

# with **kwargs
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
# arg1: 5
# arg2: two
# arg3: 3
```


## COMMON METHODS

<!-- Placeholder for common methods content -->


---
# **INTERMEDIATE**
---

## OOP

**Object-oriented programming (OOP)** is a method of structuring a program by bundling related properties and behaviors into individual objects. Conceptually, objects are like the components of a system.

### OOP Concepts in Python

- Class
- Objects
- Polymorphism
- Encapsulation
- Inheritance
- Data Abstraction

- A **class** contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.

- An **object** is an entity that has a state and behavior associated with it. It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.
  - **State:** Represented by the attributes of an object. It reflects the properties of an object.
  - **Behavior:** Represented by the methods of an object. It reflects the response of an object to other objects.
  - **Identity:** Gives a unique name to an object and enables one object to interact with other objects.

### Inheritance

**Inheritance** is the capability of one class to derive or inherit the properties from another class. The class that derives properties is called the **derived class** or **child class**, and the class from which the properties are being derived is called the **base class** or **parent class**. The benefits of inheritance are:

- It represents real-world relationships well.
- It provides reusability of code. We don't have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
- It is transitive in nature — if class B inherits from class A, then all subclasses of B would automatically inherit from class A.

#### Types of Inheritance

| Type                    | Description                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------|
| **Single**              | A derived class inherits from a single parent class.                                        |
| **Multilevel**          | A derived class inherits from a parent class, which in turn inherits from its parent class. |
| **Hierarchical**        | More than one derived class inherits from a single parent class.                            |
| **Multiple**            | One derived class inherits from more than one base class.                                   |

```
# Parent class
class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))

# Child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)  # or super().__init__(name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))

# Creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# Calling a function of the class Person using its instance
a.display()
a.details()

# Output:
# Rahul
# 886012
# My name is Rahul
# IdNumber: 886012
# Post: Intern
```

#### Subclassing (Calling Constructor of Parent Class)

Python program to demonstrate error if we forget to invoke `__init__()` of the parent:

```
class Person(object):
    # Constructor
    def __init__(self, name):
        self.name = name
    # To get name
    def getName(self):
        return self.name
    # To check if this person is an employee
    def isEmployee(self):
        return False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    # Here we return true
    def isEmployee(self):
        return True

# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee)
```

The `super()` function is a built-in function that returns the objects that represent the parent class. It allows access to the parent class's methods and attributes in the child class.

```
# Parent class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

# Child class
class Student(Person):
    def __init__(self, name, age, dob):
        self.sName = name
        self.sAge = age
        self.dob = dob
        # inheriting the properties of parent class
        super().__init__("Rahul", age)

    def displayInfo(self):
        print(self.sName, self.sAge, self.dob)

obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()
```

#### Private Members of the Parent Class

We don't always want the instance variables of the parent class to be inherited by the child class. We can make some of the instance variables of the parent class **private**, which won't be available to the child class.

```
class C(object):
    def __init__(self):
        self.c = 21
        # d is private instance variable
        self.__d = 42

class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)

object1 = D()
# produces an error as d is private instance variable
print(object1.c)
# print(object1.__d)  # ❌ AttributeError
```

To access private members: `self._Base__c`

```
# f"_{self.__class__.__name__}__c"          >> "_Derived__c"
# f'_{type(self).__mro__[1].__name__}__c'
```

> `type(self).__mro__[0] == self.__class__  # is True`

### Composition

**Composition** is often used to model "has-a" relationships between objects, as opposed to inheritance, which models "is-a" relationships. Composition is a design principle where a class contains instances of other classes to reuse their functionality, rather than inheriting from them. It is an alternative to inheritance and is often preferred because it promotes flexibility, modularity, and maintainability.

```
class Engine:
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def drive(self):
        self.engine.start()
        print("Car is driving")

# Using composition
my_car = Car()
my_car.drive()
```

You can pass different objects dynamically to customize behavior:

```
class PetrolEngine:
    def start(self):
        print("Petrol engine starts")

class ElectricEngine:
    def start(self):
        print("Electric engine starts")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Inject the engine dynamically

    def drive(self):
        self.engine.start()
        print("Car is driving")

# Using composition with different engines
petrol_car = Car(PetrolEngine())
electric_car = Car(ElectricEngine())

petrol_car.drive()
# Output:
# Petrol engine starts
# Car is driving

electric_car.drive()
# Output:
# Electric engine starts
# Car is driving
```

### Polymorphism

**Polymorphism** simply means "having many forms." It is the opportunity to apply one common function to objects with different types. In Python, polymorphism allows objects of different classes to be treated as objects of a common superclass. It is the ability to present the same interface for differing underlying forms (data types).

- **Method Overriding:** Occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. The method in the subclass overrides the method in the superclass.
- **Method Overloading:** The ability to define multiple methods with the same name but different parameters. Python does not support method overloading in the same way as languages like Java or C++. Instead, it uses default arguments and variable-length arguments.
- **Duck Typing:** Python follows the principle of "duck typing" where the type or class of an object is less important than the methods it defines. If an object implements the necessary methods, it can be used in that context.
- **Polymorphic Functions:** Functions that can take objects of different types and apply the same operation on them.

```
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# Output:
# There are many types of birds.
# Most of the birds can fly but some cannot.
# There are many types of birds.
# Sparrows can fly.
# There are many types of birds.
# Ostriches cannot fly.
```

### Encapsulation

**Encapsulation** is one of the fundamental concepts in OOP.
- Minimization of necessary information space.
- Wrapping one namespace by another (create hierarchy: `obj1.param.name.set()`).
- It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object's variable can only be changed by an object's method. Those types of variables are known as **private variables**.

```
# Python program to demonstrate private members
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"

class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # print(self.__c)  # self._Base__c

        # or
        # super().__init__()
        # private_name = [name for name in dir(self) if name.endswith("__c")][0]
        # print(getattr(self, private_name))  # Still prints "GeeksforGeeks"

        # f"_{self.__class__.__name__}__c"          >> "_Derived__c"
        # f'_{type(self).__mro__[1].__name__}__c'

# Driver code
obj1 = Base()

print(obj1.a)  # GeeksforGeeks
# print(self.__c)  # ❌ AttributeError
```

> `type(self).__mro__[0] == self.__class__  # is True`

### Data Abstraction

It hides unnecessary code details from the user. Also, when we do not want to give out sensitive parts of our code implementation, this is where data abstraction comes in. Data Abstraction in Python can be achieved by creating **abstract classes**.

- Abstract classes provide a way to define common interfaces for a group of related classes. They serve as blueprints for other classes and enforce the implementation of certain methods in derived classes.
- Abstract classes **cannot** be instantiated directly. They are designed to be subclassed.
- Enforce a contract for subclass implementation, ensuring consistency across all derived classes.
- Python provides the `abc` (Abstract Base Classes) module to define abstract classes.

```
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def speak(self):
        """This method must be implemented by subclasses."""
        pass

class Dog(Animal):  # Subclass of Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):  # Subclass of Animal
    def speak(self):
        return "Meow!"

# dog = Animal()  # This will raise an error: Can't instantiate abstract class

dog = Dog()
print(dog.speak())  # Output: Woof!
cat = Cat()
print(cat.speak())  # Output: Meow!
```

**Example of an Error:**

```
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Incorrect subclass: does not implement the abstract method `speak`
class Dog(Animal):
    pass

# Attempting to instantiate `Dog` will raise an error
dog = Dog()  # TypeError: Can't instantiate abstract class Dog with abstract method speak
```

### Descriptors

In Python, a **descriptor** is an object attribute with "binding behavior," meaning it can control how an attribute is accessed, modified, or deleted. Descriptors are a way to customize the behavior of attributes through methods implemented in a separate class. The descriptor protocol consists of three methods: `__get__`, `__set__`, and `__delete__`.

| Method                               | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| `__get__(self, instance, owner)`     | Called when the attribute is accessed.                        |
| `__set__(self, instance, value)`     | Called when a value is assigned to the attribute.             |
| `__delete__(self, instance)`         | Called when the attribute is deleted.                         |

- `instance` → the actual object you're accessing the attribute from (obj, p).
- `owner` → the class the descriptor is defined on (MyClass, Person).

```
class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"Getting {self.name}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Setting {self.name} to {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Deleting {self.name}")
        del instance.__dict__[self.name]

class MyClass:
    attribute = Descriptor('attribute')

obj = MyClass()
obj.attribute = 10  # Output: Setting attribute to 10
print(obj.attribute)  # Output: Getting attribute \n 10
del obj.attribute  # Output: Deleting attribute
```

```
class UpperCase:
    def __get__(self, instance, owner):
        return instance.__dict__['name'].upper()
    def __set__(self, instance, value):
        instance.__dict__['name'] = value

class Person:
    name = UpperCase()  # ← descriptor
    def __init__(self, name):
        self.name = name

p = Person("harry")
print(p.name)  # HARRY

# self (descriptor) = <__main__.UpperCase object at 0x7f8e59f5cf40>
# instance (object) = <__main__.Person object at 0x7f8e59f5cfd0>
# owner (class) = <class '__main__.Person'>
```

### `@property`

In Python, the `@property` decorator is used to define methods in a class that act like attributes, allowing for controlled access to instance variables. This allows you to implement getter, setter, and deleter methods for an attribute without directly exposing the attribute itself. It is a way to encapsulate and manage access to the attributes of a class.

```
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """The getter method"""
        return self._value

    @value.setter
    def value(self, new_value):
        """The setter method"""
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value

    @value.deleter
    def value(self):
        """The deleter method"""
        del self._value

# Usage
obj = MyClass(10)
print(obj.value)  # Output: 10

obj.value = 20
print(obj.value)  # Output: 20

# obj.value = -5  # Raises ValueError: Value cannot be negative

del obj.value
# print(obj.value)  # Raises AttributeError: 'MyClass' object has no attribute '_value'
```

**Benefits of Using `@property`:**

- **Encapsulation:** You can hide the internal representation of an attribute and control how it is accessed and modified.
- **Validation:** You can add validation logic in the setter method to ensure that the data is in the expected format.
- **Read-only Attributes:** By only defining a getter method, you can make an attribute read-only.

### `__slots__`

The `__slots__` mechanism is used to restrict the attributes that an object can have, allowing for more memory-efficient objects. By default, Python objects use a dictionary to store instance attributes, which can take up a lot of memory, especially if many instances are created. When `__slots__` is defined in a class, Python doesn't create the usual dictionary for storing instance attributes, but instead creates a more memory-efficient internal structure. You can define a set of attributes that instances of the class are allowed to have. Any attempt to assign an attribute not listed in `__slots__` will result in an `AttributeError`.

```
class A:
    __slots__ = ['a', 'b', 'c']
    a = 1  # read-only attribute

a = A()
a.b = 2
# a.d = 3  # AttributeError
```

### `@classmethod`

A class method in Python is a method that is bound to the class, rather than an instance of the class. This means it receives the class itself as its first argument, rather than an instance of the class. It is defined using the `@classmethod` decorator, and the first parameter is typically named `cls` (for class), rather than `self` (which is used for instance methods).

```
class Dog:
    species = "Canis familiaris"  # Class-level attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species

# Calling class method on the class
print(Dog.get_species())  # Output: Canis familiaris

# Calling class method on an instance (not recommended)
dog = Dog("Buddy")
print(dog.get_species())  # Output: Canis familiaris
```

Class methods are often used to create **alternative constructors** for a class.

```
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @classmethod
    def from_string(cls, car_string):
        brand, model = car_string.split('-')
        return cls(brand, model)

# Using the class method as an alternative constructor
car = Car.from_string("Toyota-Camry")
print(car.brand)  # Output: Toyota
print(car.model)  # Output: Camry
```

### `@staticmethod`

A static method in Python is a method that is bound to a class rather than an instance of the class, but unlike a `classmethod`, it does not take the class (`cls`) or instance (`self`) as its first argument. It behaves just like a regular function, but it belongs to the class's namespace and can be called on the class itself or on an instance.

```
class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        # Function logic
        print(f"Static method called with {arg1} and {arg2}")
```

### `__new__` — Singleton Pattern

Use case of `__new__`: Singleton pattern when we need to allow creation of only one instance of an object.

```
class Singleton:
    _instance = None  # class-level cache

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

a = Singleton(10)
b = Singleton(20)

print(a.value)  # 20
print(b.value)  # 20
print(a is b)   # True — both are the same instance
```


## MIXIN

A **mixin** is a class that provides method implementations for reuse by multiple related child classes. However, the inheritance is not implying an "is-a" relationship.

- A mixin doesn't define a new type. Therefore, it is not intended for direct instantiation.
- A mixin bundles a set of methods for reuse. Each mixin should have a single specific behavior, implementing closely related methods.
- Typically, a child class uses multiple inheritance to combine the mixin classes with a parent class.
- Since Python doesn't define a formal way to define mixin classes, it's a good practice to name mixin classes with the suffix `Mixin`.

```
class Person():
    pass

class SomeMixin():  # Adds functionality to class
    pass

class Employee(Person, SomeMixin):
    pass
```


## MRO (Method Resolution Order / Diamond Problem)

1. The class of the object itself.
2. The first parent class (from left to right in the inheritance declaration).
3. If the attribute is not found, Python checks the next parent class in the MRO.
4. If still not found, it continues up through the ancestors (i.e., parents of parents) in the MRO.

```
class A:
    def method(self):
        print("Method from A")

class B(A):  # B inherits from A
    pass

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):  # D inherits from both B and C
    pass

d = D()
d.method()

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

List of object fields/members populated from:
1. Object fields.
2. Class fields.
3. Parent class fields (recursively).


## COMPREHENSIONS

Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, sets, dictionaries, etc.) using previously defined sequences. Python supports the following 4 types of comprehension:

- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions
- Generator Comprehensions

```
# List comprehension
output_list = [output_exp for var in input_list if (var satisfies this condition)]

# Dictionary comprehension
dict_using_comp = {key: value for (key, value) in zip(state, capital)}
```

### Nested List Comprehension

**Example: Flattening a List of Lists**

```
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6]
```

**Creating a Multiplication Table**

```
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(multiplication_table)
# Output:
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]
```


## LAMBDA / MAP / FILTER / ZIP

### Lambda

A **lambda function** is a small anonymous function. Meaning they are not given a specific name unless assigned to a variable. A lambda function can take any number of arguments, but can only have one expression.

```
# Syntax: lambda arguments: expression

>>> lambda x: x + 1
# <function <lambda> at 0x...>
>>> (lambda x: x + 1)(2)
3

>>> add_one = lambda x: x + 1
>>> add_one(2)
3

>>> full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
>>> full_name('guido', 'van rossum')
'Full name: Guido Van Rossum'

x = {1: 3, 2: 2, 3: 1}
max(x, key=lambda y: x[y])  # Max item not by keys but by values — returns 1
```

### `map()`

`map()` applies a function to each element in a collection and returns a generator.

### `filter()`

`filter()` applies a function to each element in a collection. If the function returns `True`, the element stays in the collection; otherwise, it is removed. Returns a generator.

### `zip()`

`zip()` runs through collections at the same time until one of them doesn't have any items left, creating a tuple on each iteration.


## ADVANCED CLASS


## DUNDER METHODS


## PIP / PYPI


## MAKING YOUR OWN MODULE


## VIRTUAL ENVIRONMENT

A **virtual environment** is (amongst other things):

- Used to contain a specific Python interpreter and software libraries and binaries which are needed to support a project (library or application). These are by default isolated from software in other virtual environments and Python interpreters and libraries installed in the operating system.
- Contained in a directory, conventionally either named `venv` or `.venv` in the project directory, or under a container directory for lots of virtual environments, such as `~/.virtualenvs`.
- Not checked into source control systems such as Git.
- Considered as **disposable** — it should be simple to delete and recreate it from scratch. You don't place any project code in the environment.
- Not considered as movable or copyable — you just recreate the same environment in the target location.

```bash
pip freeze > requirements.txt
pip freeze | xargs pip uninstall -y

python -m venv /path/to/new/virtual/environment
python3 -m venv myenv --python=/usr/bin/python3.8
source vnv/bin/activate
pip install -r requirements.txt
```


---
# **ADVANCED**
---


## POETRY

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. An alternative to `pip` package manager. Pip downloads packages from PyPI.


## BIG O NOTATION

An algorithm is little more than a series of steps required to perform some task. If we treat each step as a basic unit of computation, then an algorithm's execution time can be expressed as the number of steps required to solve the problem. Two factors that computer scientists love to model mathematically, though, are how long a program will take to run, and how much space (typically, memory) it will use. We call these **time** and **space efficiency**.

| Notation  | Name          |
|-----------|---------------|
| `1`       | Constant      |
| `log n`   | Logarithmic   |
| `n`       | Linear        |
| `n log n` | Log Linear    |
| `n²`      | Quadratic     |
| `n³`      | Cubic         |
| `2ⁿ`      | Exponential   |

### Operation Performance

#### List

| Operation          | Big O     |
|--------------------|-----------|
| `index[]`          | `O(1)`    |
| Index assignment   | `O(1)`    |
| `append`           | `O(1)`    |
| `pop()`            | `O(1)`    |
| `pop(i)`           | `O(n)`    |
| `insert(i, item)`  | `O(n)`    |
| `del` operator     | `O(n)`    |
| Iteration          | `O(n)`    |
| Contains (`in`)    | `O(n)`    |
| Get slice `[x:y]`  | `O(k)`    |
| Del slice          | `O(n)`    |
| Reverse            | `O(n)`    |
| Concatenate        | `O(k)`    |
| Sort               | `O(n log n)` |
| Multiply           | `O(nk)`   |

#### Dictionary

| Operation          | Big O     |
|--------------------|-----------|
| `copy`             | `O(n)`    |
| Get item           | `O(1)`    |
| Set item           | `O(1)`    |
| Delete item        | `O(1)`    |
| Contains (`in`)    | `O(1)`    |
| Iteration          | `O(n)`    |


## CLOSURE

In Python, a **closure** is a function that retains access to its lexical scope, even after the scope has finished executing. In simpler terms, a closure "remembers" the variables that were in its surrounding scope when it was created, even if that scope no longer exists.

When Python analyzes inner function code and 'sees' a variable that refers to the parent function scope (nonlocal/enclosing), it saves the value of this variable in `__closure__` of the child function.

```
    returned_inner_fu.__closure__[0].cell_contents

    import inspect
    inspect.getclosurevars(fu)
```

### How Closures Work

Closures are created when a nested function captures variables from its enclosing scope.

```
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello, World!")
closure()  # Output: Hello, World!
```

- The `outer_function` creates a variable `msg` and a function `inner_function` that uses `msg`.
- `inner_function` is returned as a function object.
- When `outer_function` is called with the argument `"Hello, World!"`, it returns `inner_function`, which retains the value of `msg`.
- The variable `msg` remains in memory even after `outer_function` has finished executing.
- When `closure()` is called, it executes `inner_function`, which uses the saved value of `msg`.

### Modifying Enclosed Variables

To modify values of variables within a closure, use the `nonlocal` keyword:

```
    def outer_function(msg):
        count = 0
        def inner_function():
            nonlocal count
            count += 1
            print(f"{msg}, called {count} times")
        return inner_function

    closure = outer_function("Hello")
    closure()  # Output: Hello, called 1 times
    closure()  # Output: Hello, called 2 times
```

```
    def make_averager():
        series = []

        # The closure for averager extends the scope of that function 
        # to include the binding for the free variable series.
        def averager(new_value):
            series.append(new_value)
            total = sum(series)
            return total / len(series)
        return averager

    avg = make_averager()

    avg(10)
    avg(11)

    series = avg.__closure__[0].cell_contents
    print("outside:", sys.getrefcount(series))
```

> Within averager, series is a `free variable`. This is a technical term meaning a variable that is not bound in the local scope

```
    avg.__code__.co_varnames  # ('new_value', 'total')
    avg.__code__.co_freevars  # ('series',)
```

### Function Factories

Closures are often used to create functions with fixed parameters.

```
def power_factory(exp):
    def power(base):
        return base ** exp
    return power

square = power_factory(2)
cube = power_factory(3)

print(square(4))  # Output: 16
print(cube(2))    # Output: 8
```

### Decorators

Decorators in Python also use closures to add functionality to functions.

```
def simple_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```


## DECORATORS

A Python **decorator** is a function or a class that modifies the behavior of another function or method. Decorators are a way to "wrap" a function or a method in additional functionality without changing its actual code. They use the `@decorator_name` syntax just before a function definition, allowing you to add reusable features or behaviors to existing code in a clean, readable way. In Python, functions are **first class objects**, which means that functions in Python can be used or passed as arguments.

> A decorator is a callable that takes another function as an argument.
>A decorator may perform some processing with the decorated function, and returns it or replaces it with another function or callable object.
> Decorators run right after the decorated function is defined. That is usually at import time 

> The target(funnction) name is bound to whatever function is returned by decorator
```
    # When we use @decorator sintax we replase teh name of defining function
    # by result of call the decorator with this function as argument.
    @gfg_decorator
    def hello_decorator():
        print("Gfg")

    '''Above code is equivalent to:
    def hello():
        print("Gfg")

    hello_decorator = gfg_decorator(hello)
    '''
```

```
    # Defining a decorator
    def hello_decorator(func):
        # inner1 is a Wrapper function in which the argument is called
        # inner function can access the outer local functions like in this case "func"

        def inner1():
            print("Hello, this is before function execution")

            # calling the actual function now inside the wrapper function.
            func()

            print("This is after function execution")

        return inner1

    # defining a function, to be called inside wrapper
    def function_to_be_used():
        print("This is inside the function !!")

    # passing 'function_to_be_used' inside the decorator to control its behaviour.
    function_to_be_used = hello_decorator(function_to_be_used)

    # calling the function
    function_to_be_used()

    # Output:
    # Hello, this is before function execution
    # This is inside the function !!
    # This is after function execution
```

```
    def hello_decorator(func):
        def inner1(*args, **kwargs):
            print("before Execution")

            # getting the returned value
            returned_value = func(*args, **kwargs)
            print("after Execution")

            # returning the value to the original frame
            return returned_value

        return inner1

    # adding decorator to the function
    @hello_decorator
    def sum_two_numbers(a, b):
        print("Inside the function")
        return a + b

    a, b = 1, 2

    # getting the value through return of the function
    print("Sum =", sum_two_numbers(a, b))

    # Output:
    # before Execution
    # Inside the function
    # after Execution
    # Sum = 3
```

Sinse decorator bind name of function to inner wraper and it masks the __name__ and __doc__ of the decorated function. This behavior can be changed this way:

```
    import time
    import functools

    def clock(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = [repr(arg) for arg in args]
            arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
            arg_str = ', '.join(arg_lst)
            print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
            return result
        return clocked
```

### Decorator Chaining

```
    def decor1(func):
        def inner():
            x = func()
            return x * x
        return inner

    def decor(func):
        def inner():
            x = func()
            return 2 * x
        return inner

    @decor1  # applied second
    @decor   # applied first
    def num():
        return 10

    @decor
    @decor1
    def num2():
        return 10

    print(num())   # Output: 400
    print(num2())  # Output: 200
```

```
    def green(fu):
        fu.green = True
        return fu

    @green
    def add(a, b):
        return a + b

    add.green  # >> True
```

```
    def to_float(fu):
        def wrapper(a, b):
            a = float(a)
            b = float(b)
            return fu(a, b)
        return wrapper

    @to_float
    def add(a, b):
        return a + b

    add(1, 2)  # >> 3.0
```

```
    from functools import wraps

    def repeater(n):
        def dec(fu):
            @wraps(fu)
            def wrapper(*args):
                return [fu(*args) for i in range(n)]
            return wrapper
        return dec

    @repeater(4)
    def multi(a, b):
        return a * b

    multi(2, 4)  # [8, 8, 8, 8]
```

```
    class repeater4:
        def __init__(self, fu):
            self.fu = fu
        def __call__(self, *args):
            return [self.fu(*args) for i in range(4)]

    @repeater4
    def multi(a, b):
        return a * b

    multi(2, 4)  # [8, 8, 8, 8]
```

### Decorator with Parameters

A decorator with parameters is not a decorator itself; it is a **decorator factory** that returns a decorator.

- Regular decorator: `fu = decorator(fu)`
- Decorator with parameters: `fu = dec_factory(param)(fu)`

```
    registry = set()
    
    def register(active=True):
        def decorate(func):
            print('running register'
            f'(active={active})->decorate({func})')

            if active:
                registry.add(func)
            else:
                registry.discard(func)

            return func
        return decorate

    @register(active=False)
    def f1():
        print('running f1()')

    @register()
    def f2():
        print('runningf2()')

    def f3():
        print('runningf3()')
```


## CONTEXT MANAGER (WITH)


## METACLASSES


## THREADS

The threads may be running on different processors, but with the GIL they will only be running one at a time. Tasks that spend much of their time waiting for external events are generally good candidates for threading. Problems that require heavy CPU computation and spend little time waiting for external events might not run faster at all.

### 1. Threads

**Definition:** A thread is the smallest unit of a process that can be scheduled for execution. Threads allow a program to perform multiple operations concurrently in the same process space.

**Key Points:**
- **Lightweight:** Threads share the same memory space, making them lightweight compared to processes.
- **Shared Resources:** Since threads share memory and other resources, they can communicate more efficiently than processes. However, this can also lead to issues like race conditions and deadlocks.
- **Concurrency:** Threads enable concurrent execution of tasks within the same program.

### 2. Process

**Definition:** A process is an instance of a program that is being executed. It contains the program code and its current activity.

**Key Points:**
- **Isolation:** Each process has its own memory space, which isolates it from other processes. This makes processes more secure but more resource-intensive.
- **Context Switching:** Switching between processes is more costly in terms of resources than switching between threads.
- **Parallelism:** Processes can run in parallel on multi-core systems.

### 3. Thread Pool

**Definition:** A thread pool is a collection of pre-initialized threads that stand ready to be given work. This approach helps manage a large number of concurrent tasks efficiently.

**Key Points:**
- **Resource Management:** Thread pools manage the allocation of threads, reducing the overhead of creating and destroying threads frequently.
- **Concurrency:** Thread pools improve performance by reusing existing threads instead of creating new ones.
- **Examples:** Thread pools are often used in server applications to handle incoming requests.

### 4. Parallelism

**Definition:** Parallelism involves executing multiple tasks simultaneously to increase performance. It leverages multiple processors or cores to perform computations more quickly.

**Key Points:**
- **True Parallelism:** Requires hardware with multiple processing units (e.g., multi-core processors).
- **Task Parallelism:** Different tasks or threads are executed simultaneously.
- **Data Parallelism:** The same task is executed on different chunks of data simultaneously.

Yes, concurrency and threading are indeed ways to achieve the simulation of parallelism in a single-CPU environment.

**Time-Slicing:** The operating system divides CPU time into slices and allocates these slices to various tasks. By rapidly switching between tasks, it creates the illusion that tasks are running at the same time.

**Task Switching:** The system saves the state of a task before switching to another, allowing it to resume where it left off later.

**Context Switching:** The CPU switches between different tasks or threads very quickly, saving and restoring their states. This switching happens so rapidly that it appears as if tasks are running in parallel.

**Non-blocking I/O:** For I/O-bound tasks, using asynchronous programming or non-blocking I/O operations allows the CPU to switch to another task while waiting for I/O operations to complete.

### 5. Multiprocessing

**Definition:** Multiprocessing refers to using two or more CPUs within a single computer system to perform tasks simultaneously.

**Key Points:**
- **Process-based Parallelism:** Involves running multiple processes in parallel, each on different CPU cores.
- **Isolation:** Processes do not share memory, which prevents interference but requires inter-process communication mechanisms.
- **Scalability:** Multiprocessing can efficiently utilize multiple CPUs for parallel execution of tasks.

### Relative Terms and Concepts

- **Concurrency vs. Parallelism:** Concurrency refers to the execution of multiple tasks in overlapping time periods (not necessarily simultaneously), while parallelism refers to tasks running at the same time.
- **GIL (Global Interpreter Lock):** In CPython, the GIL prevents multiple native threads from executing Python bytecodes at once. This means Python threads are not fully parallel and are more suited for I/O-bound tasks rather than CPU-bound tasks.
- **Asyncio:** A Python library for writing concurrent code using the `async`/`await` syntax, designed for I/O-bound and high-level structured network code.

### Example in Python

```
import threading
import multiprocessing

# Function to be executed by threads/processes
def worker(name):
    print(f'Worker {name}')

# Using threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Using processes
processes = []
for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()
```


## CONCURRENCY

Python with GIL limits the amount of concurrency on a single thread on a single process.

### Asyncio

**Asynchronous execution** — parallel execution of different code blocks. Asynchronous functions are defined using the `async def` syntax. Instead of blocking the execution (like a normal function), an async function allows other tasks to run while it waits for an operation to complete.

```
async def my_async_function():
    print("Start")
    await asyncio.sleep(1)
    print("End")
```

**`await` Keyword:**
The `await` keyword is used to call an asynchronous function and wait for its result without blocking the event loop. It can only be used inside `async` functions.

```
async def my_async_function():
    print("Start")
    await asyncio.sleep(1)  # Waits for 1 second without blocking
    print("End")
```

**Event Loop:**
The event loop is the core of the `asyncio` module, responsible for scheduling and running async functions. You can get the event loop using `asyncio.get_event_loop()` and run tasks using `loop.run_until_complete()` or `asyncio.run()`.

```
async def my_async_function():
    print("Start")
    await asyncio.sleep(1)
    print("End")

# Run the async function
asyncio.run(my_async_function())
```

**Tasks:**
Tasks are used to schedule coroutines (async functions) concurrently. They are created using `asyncio.create_task()`. This allows multiple async functions to run "at the same time," meaning they can execute concurrently.

```
async def task1():
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    task_1 = asyncio.create_task(task1())
    task_2 = asyncio.create_task(task2())

    await task_1  # Wait for task 1 to finish
    await task_2  # Wait for task 2 to finish

asyncio.run(main())
```

**Coroutines:**
Coroutines are the result of a call to an asynchronous function. A coroutine is a function that can pause and resume execution, usually using `await`. When you use `async def`, you're defining a coroutine.

```
async def my_coroutine():
    await asyncio.sleep(1)
    return "Finished"
```

**Running Multiple Tasks:**
You can run multiple coroutines concurrently using `asyncio.gather()` or `asyncio.wait()`.

```
async def task1():
    await asyncio.sleep(2)
    return "Task 1 finished"

async def task2():
    await asyncio.sleep(1)
    return "Task 2 finished"

async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)

asyncio.run(main())
```

**Example Scenario: Web Scraper**

```
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['http://example.com', 'http://example.org', 'http://example.net']
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())
```

**Summary:**

- Use `async def` to define an async function.
- Use `await` to pause execution within an async function until the awaited task is complete.
- Use `asyncio.run()` to run your async function.
- Create tasks with `asyncio.create_task()` to run multiple coroutines concurrently.
- Use `asyncio.gather()` to wait for multiple tasks to complete and collect their results.

In Python, asynchronous programming (using `asyncio` and coroutines) can indeed be a more efficient way to achieve concurrency than threading, especially when dealing with I/O-bound tasks. The key reason is that context switching between coroutines is typically lighter than switching between threads. Coroutine switching occurs within the same thread and is managed by the Python runtime, so it doesn't require the operating system to get involved. Thread switching, on the other hand, involves OS-level threads, which come with additional overhead for context switching.


## PARALLELISM


## MULTIPROCESSING


## GIL (Global Interpreter Lock)

Python Global Interpreter Lock (GIL) is a type of process lock which is used by Python whenever it deals with processes. Generally, Python only uses one thread to execute the set of written statements. This means that in Python only one thread will be executed at a time. The performance of the single-threaded process and the multi-threaded process will be the same in Python, and this is because of GIL in Python. We cannot achieve multithreading in Python because we have a global interpreter lock which restricts the threads and works as a single thread — only one thread can execute Python bytecode at a time. This lock is necessary because Python's memory management is not thread-safe.

### What problem did the GIL solve for Python?

Python has something that no other language has: a **reference counter**. With the help of the reference counter, we can count the total number of references that are made internally in Python to assign a value to a data object. Due to this counter, we can count the references, and when this count reaches zero, the variable or data object will be released automatically. The GIL prevents multiple threads from executing simultaneously in the interpreter, which avoids race conditions and data corruption. Without the GIL, every object access would need to be protected by locks, which would significantly complicate the interpreter's implementation and potentially degrade performance.

**Multiprocessing:** One common workaround is to use the `multiprocessing` module instead of `threading`. The `multiprocessing` module creates separate processes, each with its own Python interpreter and memory space, bypassing the GIL and allowing true parallelism.

1. **GIL Blocks True Parallelism with Threads:** The GIL prevents true parallel execution of threads because it only allows one thread to execute Python bytecode at a time, even if there are multiple CPU cores available.

2. **Threads Still Achieve Concurrency:** Even with the GIL, Python threads can achieve concurrency by rapidly switching between tasks, giving the illusion that multiple tasks are happening simultaneously. This is especially effective for I/O-bound tasks (like waiting for network responses, file reads/writes) where the GIL is released while waiting, allowing another thread to run in the meantime.

3. **Concurrency Without Parallelism:** Threads in Python can still make progress on multiple tasks concurrently, but they're not truly executing at the same time on different CPU cores (i.e., not in parallel). They appear to run "at the same time" through task switching, but only one thread executes Python code at any given moment.


## RACE CONDITION

A **race condition** happens when two or more threads (or processes) access shared resources concurrently and the final outcome of the execution depends on the specific timing or interleaving of their execution. This can lead to inconsistent or incorrect results, especially if the shared resources are not properly synchronized.


## TESTING

- `pytest`
- `unittest`


## BUILD AND MANIPULATE PACKAGES


## CPYTHON

When Python code is executed, it goes through a multi-step process:

### Syntax Analysis (Parsing)
Python first parses the code, checking its syntax for correctness. This step involves generating an **Abstract Syntax Tree (AST)** from the source code, ensuring that the code conforms to Python's grammar. If there are syntax errors, Python raises a `SyntaxError` and stops execution.

### Bytecode Compilation
After syntax analysis, the code is compiled into **bytecode**, an intermediate, platform-independent representation of the code. Bytecode is a lower-level, optimized version of the original code, which allows Python to run more efficiently. Python stores the compiled bytecode in `.pyc` files (in the `__pycache__` directory), so it doesn't need to recompile unchanged code in future executions.

### Interpretation (Execution)
Finally, the Python interpreter executes the bytecode line by line. This is done by the **Python Virtual Machine (PVM)**, which interprets and runs the bytecode.


---
# **ADDITIONAL**
---


## ALGORITHMS


## DATA STRUCTURES

"A **data structure** is a collection of data values, the relations among them, and functions that can be applied to them."

### Queue

Operations associated with a queue:

| Operation  | Description                                                        | Time Complexity |
|------------|--------------------------------------------------------------------|-----------------|
| `Enqueue`  | Adds an item to the queue. Overflow if full.                       | `O(1)`          |
| `Dequeue`  | Removes an item from the queue. Underflow if empty.                | `O(1)`          |
| `Front`    | Get the front item from queue.                                     | `O(1)`          |
| `Rear`     | Get the last item from queue.                                      | `O(1)`          |

**FIFO (First In, First Out):**
```
enqueue -> (rear) | | | | | | | (front) -> dequeue
```

```
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)
```

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A class to represent a queue
# The queue, front stores the front node of LL and rear stores the last node of LL
class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from queue
    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.DeQueue()
    print("Queue Front : " + str(q.front.data if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))
```


## MODULES AND PACKAGES

A **module** is a simple Python file that contains collections of functions and global variables and has a `.py` extension. It is an executable file, and to organize all the modules we have the concept called **Package** in Python. There are actually three different ways to define a module in Python:

- A module can be written in Python itself.
- A module can be written in C and loaded dynamically at run-time, like the `re` (regular expression) module.
- A built-in module is intrinsically contained in the interpreter, like the `itertools` module.

A module's contents are accessed the same way in all three cases: with the `import` statement.

The cool thing about modules written in Python is that they are exceedingly straightforward to build. All you need to do is create a file that contains legitimate Python code and then give the file a name with a `.py` extension. That's it! No special syntax is necessary.

When the interpreter executes the above `import module` statement, it searches for `mod.py` in a list of directories assembled from the following sources:

1. The directory from which the input script was run or the current directory if the interpreter is being run interactively.
2. The list of directories contained in the `PYTHONPATH` environment variable, if it is set. (The format for `PYTHONPATH` is OS-dependent but should mimic the `PATH` environment variable.)
3. An installation-dependent list of directories configured at the time Python is installed.

The resulting search path is accessible in the Python variable `sys.path`, which is obtained from a module named `sys`:

```
>>> import sys
>>> sys.path
['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
'C:\\Python36', 'C:\\Python36\\lib\\site-packages']
```

You can modify `sys.path` at run-time so that it contains your module directory:

```
>>> sys.path.append(r'C:\Users\john')
```

Once a module has been imported, you can determine the location where it was found with the module's `__file__` attribute:

```
>>> import mod
>>> mod.__file__
# 'C:\\Users\\john\\mod.py'
```

```
>>> python -c 'import aiogram; print(aiogram.__file__)
```

```
>>> import mod
>>> mod
# <module 'mod' from 'C:\\Users\\john\\Documents\\Python\\doc\\mod.py'>
```

A **package** is a simple directory having collections of modules. This directory contains Python modules and also has an `__init__.py` file by which the interpreter interprets it as a Package. The package is simply a namespace. The package also contains sub-packages inside it. Packages allow for a hierarchical structuring of the module namespace using dot notation.

`__all__ = [module1, module2]` — defines a list of modules that will be imported when: `from package/module import *`


## BEST PRACTICES

### DRY
**Don't Repeat Yourself**

### KISS
**Keep It Simple, Smart**

### YAGNI
**You Ain't Gonna Need It**

- Change is inevitable in software.
- "Programs must be written for people to read, and only incidentally for machines to execute."

### SOLID Principles

| Principle                       | Description                                                                                  |
|---------------------------------|----------------------------------------------------------------------------------------------|
| **S**ingle Responsibility (SRP) | A class should have only one reason to change.                                               |
| **O**pen/Closed (OCP)           | Software entities should be open for extension, but closed for modification.                 |
| **L**iskov Substitution (LSP)   | Derived classes must be substitutable for their base classes.                                |
| **I**nterface Segregation (ISP) | Many client-specific interfaces are better than one general-purpose interface.               |
| **D**ependency Inversion (DIP)  | Depend on abstractions, not on concrete implementations. Favor composition over inheritance. |

#### 1. Single Responsibility Principle (SRP)
This principle states that "a software entity should have only one reason to change," which means every class should have a single responsibility or single job or single purpose.

- One component = one task.
- One component = one responsibility.
- One component = one usage scenario.
- Don't create god objects.

#### 2. Open/Closed Principle (OCP)
This principle states that "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification," which means you should be able to extend a class's behavior without modifying it.

- Separate parts of the program that change from those that stay the same.
- Program to interfaces. The interface stays the same; implementations change.
- Behavior is controlled by an interface.

#### 3. Liskov Substitution Principle (LSP)
This principle states that "derived or child classes must be substitutable for their base or parent classes." This ensures that any class that is the child of a parent class should be usable in place of its parent without any unexpected behavior.

- Child instead of a parent changes nothing.
- Children's behavior is the same as the parent's behavior.

#### 4. Interface Segregation Principle (ISP)
This principle states "do not force any client to implement an interface which is irrelevant to them." Your main goal is to focus on avoiding fat interfaces and give preference to many small client-specific interfaces.

#### 5. Dependency Inversion Principle (DIP)
This principle states that "high-level modules should not depend on low-level modules. Both should depend on abstractions." Additionally, "abstractions should not depend on details. Details should depend on abstractions."

- **Favor composition over inheritance.**
- High-level modules (domain) should not depend on low-level modules (infrastructure).

### Other Principles

- **Identify aspects of the application that can change** and separate/encapsulate them from those that always remain constant.
- **Program at the interface level,** not at the implementation level.
- **Strive for loose coupling** of interacting objects.


## ANTI-PATTERNS

### ITM (Initiate Then Modify)


## PROBLEM SOLVING


## DESIGN PATTERNS

### Creational Patterns
These patterns provide various object creation mechanisms that increase flexibility and reuse of existing code.

**Factory Method (Virtual Constructor):**
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

### Strategy Pattern
**Strategy Pattern** is a behavioral design pattern that defines a family of algorithms, encapsulates each one in a separate class, and makes them interchangeable at runtime. This allows a client (such as an object) to select a specific algorithm dynamically without altering its own code.

### Observer Pattern
**Observer Pattern** is a behavioral design pattern that establishes a one-to-many dependency between objects, ensuring that when one object (the subject) changes its state, all its dependent objects (the observers) are notified and updated automatically.

- **Subject:** The object being observed. It maintains a list of its observers and provides methods to add, remove, or notify them.
- **Observer:** The object that wants to be notified of changes in the subject. It defines an interface for updating in response to changes. Can subscribe or unsubscribe to the subject.

### Decorator Pattern
**Decorator Pattern** is a structural design pattern that allows you to dynamically add or modify behavior to an object without changing its structure or modifying its code. It involves wrapping an object with another object (called a decorator) that provides the additional behavior.

- **Component:** The original object interface or abstract class.
- **ConcreteComponent:** The core object whose behavior you want to extend.
- **Decorator:** An abstract wrapper that follows the same interface as the component.
- **ConcreteDecorator:** The specific wrapper that adds or modifies behavior.


## OSI MODEL

| Layer | Name            | Examples                                           | Purpose                                                                 |
|-------|-----------------|----------------------------------------------------|-------------------------------------------------------------------------|
| 7     | **Application** | HTTP, FTP, SMTP, DNS, POP3                         | Provides network services to end-user applications.                     |
| 6     | **Presentation**| SSL/TLS, ASCII, JPEG, MPEG                         | Data formatting, encryption/decryption, compression, translation.       |
| 5     | **Session**     | NetBIOS, RPC, PPTP                                 | Manages and controls connections (sessions) between applications.       |
| 4     | **Transport**   | TCP, UDP, SCTP                                     | Ensures reliable data delivery, flow and congestion control.            |
| 3     | **Network**     | IP, ICMP, ARP, RIP, OSPF                           | Logical addressing, routing, and forwarding of packets.                 |
| 2     | **Data Link**   | Ethernet, PPP, HDLC, MAC                           | Node-to-node data transfer, error detection in frames.                  |
| 1     | **Physical**    | Ethernet (cables), USB, Bluetooth, DSL, Wi-Fi      | Transmission of raw binary data over a physical medium.                 |

**PDU (Protocol Data Unit) by Layer:**
- Layer 4 (Transport): **Segment**
- Layer 3 (Network): **Packet**
- Layer 2 (Data Link): **Frame**
- Layer 1 (Physical): **Bit**

**Key Identifiers by Layer:**
- Layer 4: Applications identified by **ports**
- Layer 3: Computers identified by **IP addresses**
- Layer 2: Devices identified by **MAC addresses**


## TCP/IP MODEL

| Layer              | Corresponding OSI Layers |
|--------------------|--------------------------|
| **Application**    | 7, 6, 5 (Application, Presentation, Session) |
| **Transport**      | 4 (Transport)            |
| **Internetwork**   | 3 (Network)              |
| **Network Access** | 1, 2 (Physical, Data Link) |


## HTTP / HTTPS

**HTTP (Hypertext Transfer Protocol)** is the foundation of data communication on the web. It is a protocol used for transferring data between a client (usually a web browser) and a server (hosting a website).

### Key Points

1. **Stateless Protocol:** HTTP is stateless, meaning each request made by a client to the server is independent of any previous request. The server doesn't retain any knowledge of past requests.
2. **Request-Response Model:** A client sends an HTTP request (e.g., to load a webpage), and the server processes the request and sends an HTTP response.

### HTTP Methods

| Method    | Description                                                    |
|-----------|----------------------------------------------------------------|
| `GET`     | Retrieves data from the server.                                |
| `POST`    | Sends data to the server, often used for submitting forms.     |
| `PUT`     | Updates data on the server.                                    |
| `DELETE`  | Deletes data from the server.                                  |
| `HEAD`    | Retrieves headers (but not the body of the response).          |
| `OPTIONS` | Describes the communication options for the target resource.   |
| `PATCH`   | Applies partial modifications to a resource.                   |

### HTTP vs HTTPS

- **HTTP:** Not encrypted. Data is sent in plain text, making it vulnerable to eavesdropping and modification.
- **HTTPS:** Adds a layer of security by using SSL/TLS encryption, ensuring data is encrypted and secure.

### HTTP Status Codes

#### 1xx — Informational

| Code | Description                  |
|------|------------------------------|
| 100  | Continue                     |
| 101  | Switching Protocols          |
| 102  | Processing                   |

#### 2xx — Successful

| Code | Description                  |
|------|------------------------------|
| 200  | OK                           |
| 201  | Created                      |
| 202  | Accepted                     |
| 204  | No Content                   |

#### 3xx — Redirection

| Code | Description                  |
|------|------------------------------|
| 301  | Moved Permanently            |
| 302  | Found (Temporary Redirect)   |
| 304  | Not Modified                 |

#### 4xx — Client Error

| Code | Description                  |
|------|------------------------------|
| 400  | Bad Request                  |
| 401  | Unauthorized                 |
| 403  | Forbidden                    |
| 404  | Not Found                    |
| 405  | Method Not Allowed           |
| 408  | Request Timeout              |

#### 5xx — Server Error

| Code | Description                  |
|------|------------------------------|
| 500  | Internal Server Error        |
| 501  | Not Implemented              |
| 502  | Bad Gateway                  |
| 503  | Service Unavailable          |
| 504  | Gateway Timeout              |


## TCP / UDP


## SERIALIZATION

**Serialization** is the process of converting an object into a format that can be easily stored or transmitted. This format is typically a byte stream or a string. The serialized data can then be saved to a file, sent over a network, or stored in a database.

### Common Serialization Formats

| Format          | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **JSON**        | Lightweight data interchange format, easy to read and write.                |
| **XML**         | Markup language that is both human-readable and machine-readable.           |
| **YAML**        | Human-readable data serialization standard, often used for config files.    |
| **Binary**      | Protocol Buffers, Apache Avro, MessagePack — more efficient for size/speed. |

**Deserialization** is the reverse process: it converts the byte stream or string back into a copy of the original object.


## GIT

### Help
```bash
git <command> --help              # Opens help for the specified command
git --help --all                  # Lists all commands
```

### Init
```bash
git init                          # Create a repository in current folder
git init <name>                   # Create a repository in directory <name>
```

### Clone
```bash
git clone <remote-url>
git clone https://github.com/user/repo.git    # via HTTP
git clone git@github.com:user/repo.git        # via SSH
```

### Remote
- `origin` — Name of a remote repo
- `main` (or `master`) — A branch
- `HEAD` — Pointer to your current branch
- `origin/main` — Remote branch snapshot

```bash
git remote set-url origin https://github.com/user/repo.git
git remote add test https://github.com/user/repo.git
git remote -v                         # List all remote addresses

git rm -r --cached *.sqlite3          # Remove files from tracking
git rm -r --cached **/__pycache__/

git status --ignored
```

### Config
```bash
git config -l                         # List current settings
git config --global -l                # List global settings
git config --local -l                 # List local settings
git config --global user.name Name
git config --global user.email email@example.com
git config --unset <var>              # Remove a variable from config
git config alias.<alias> <command>    # Create an alias
git config alias.st status            # Now use `git st` instead of `git status`
git config --global core.autocrlf <input|false|true>
```

### Status
```bash
git status
git status -s              # Short form
# Flags: ?? - Untracked, A - Added, M - Modified, D - Deleted
```

### Add / Restore / Rm
```bash
git add <path>
git add . | add --all | add -A
git restore --staged <path>
git restore <path>
git rm
```

### Stash
```bash
git stash -m 'my stash name'
git stash pop                     # Apply and remove last stash
git stash apply                   # Apply and keep stash
git stash list
git stash show <stash>
git stash drop <stash>
```

### Commit
```bash
git commit -m 'Title'
git commit -m 'Title' -m 'Description'
git commit <path> -m 'Title'
git commit --amend [-m]
git commit --amend --no-edit
git commit -a -m                  # Add and commit without explicit add
```

### Log
```bash
git log
git log <branch-name>
git log --grep <pattern>
git log --invert-grep <pattern>
git log --oneline
git log --graph --all --oneline
```

### Revert / Reset
```bash
git revert <commit>
git revert -n <commit>
git reset <commit>
git reset --soft HEAD~
git reset --hard HEAD~4
```

### Cherry-pick
```bash
git cherry-pick <commit>
git cherry-pick -n <commit>
```

### Branch / Switch / Checkout
```bash
git branch
git branch <branch-name>
git branch -a                     # List all branches including remotes
git branch -m                     # Rename branch
git branch -d / -D                # Delete branch

git checkout <branch> | <commit>
git checkout -b <new_branch>

git switch <branch> | <commit>
git switch -c <new_branch>
```

### Merge
```bash
git merge <branch>
git merge --continue
git merge --abort
```

### Rebase
```bash
git rebase <commit>
git rebase <branch>
git rebase --continue
git rebase --abort
```

### Fetch / Pull / Push
```bash
git fetch
git fetch <remote>
git fetch <remote> --prune

git pull origin <branch>
git pull origin <branch> --rebase

git push <remote> <branch>
git push -f <remote> <branch>
git push -u <remote> <branch>     # Set upstream tracking
```

### Reflog
```bash
git reflog
git reflog <branch>
```

### Common Workflow Commands
```bash
git init
git push -u origin master
git reflog
git reset --hard [hash]
git reset HEAD~1
git restore .
git checkout master
git diff branch-name
git diff commit1 commit2
git stash
git stash pop
```


## LINUX

### Directory Structure

| Directory | Description                                                  |
|-----------|--------------------------------------------------------------|
| `/bin`    | Essential binary executables (ls, cp, mv, bash)              |
| `/boot`   | Boot files: kernel, GRUB, initrd                             |
| `/dev`    | Device files (e.g., /dev/sda, /dev/null)                     |
| `/etc`    | System-wide configuration files (/etc/passwd, /etc/hostname) |
| `/home`   | Users' personal directories                                  |
| `/lib`    | Shared libraries and kernel modules                          |
| `/lib64`  | 64-bit shared libraries                                      |
| `/media`  | Temporary mount point for removable media                    |
| `/mnt`    | Temporary mount point for file systems                       |
| `/opt`    | Optional software packages                                   |
| `/proc`   | Virtual file system for process and kernel info              |
| `/root`   | Home directory for the root user                             |
| `/run`    | Runtime information for processes and services               |
| `/sbin`   | System binaries (requires root privileges)                   |
| `/srv`    | Service data (web servers, FTP)                              |
| `/sys`    | Virtual file system for hardware/kernel info                 |
| `/tmp`    | Temporary files (usually cleared on reboot)                  |
| `/usr`    | User-installed applications and libraries                    |
| `/var`    | Variable data (logs: /var/log, queues: /var/spool)           |

### Common Commands

```bash
# System
shutdown now / poweroff / halt / init 0 / systemctl poweroff -i
uptime / cat /etc/os-release / uname -a

# Environment
env / printenv / export MY_VAR="value"

# File Operations
ls -l -a / ls -ld . / tree
touch / mkdir / rm / cp / mv
head / tail file.log -n 5
cat file-name.txt / cat >> file-name.txt

# Permissions
chmod 400 key.pem
chmod a+w file / chmod -R a+w directory
chmod g+w, o-rw, a+x file
chown :group something
groups user-name
visudo

# Find
find . -name "*.exmpl"
find . -type d -name dir-name
find / -perm x
locate something

# Users
adduser name / deluser name / passwd name
cat /etc/passwd
addgroup group-name / delgroup group-name
usermod -a -G group-name user-name
gpasswd -d user-name group-name

# Processes
top / htop / ps aux
kill id / killall name

# Network
ifconfig / ip -4 addr / netstat
curl ifconfig.me / wget -qO- ifconfig.me
curl adress / curl -X POST --data "key=value" adress
ping adress / dig adress
sudo lsof -i :<port_number>

# SSH
ssh -V
ssh -p 2220 user@host
ssh -i ~/sshkey.private -p 2220 user@host
ssh-keygen -b 4096 / ssh-keygen -t rsa -b 4096 -C "email"
ssh-copy-id root@000.000.000.000

# Screen
screen / screen -ls / screen -r <id>
# Ctrl + A, then D to detach
```

### Reset Forgotten Root Password (Debian)
1. Reboot and press `e` on GRUB menu.
2. Find the line beginning with `linux`, go to end after `ro quiet`, append `init=/bin/bash`.
3. Press `Ctrl + X`.
4. Run: `mount -n -o remount,rw /`, then `passwd`.
5. Press `Ctrl + Alt + Del` to reboot.


## COMMON PORTS AND PROTOCOLS

| Protocol | Port(s)       | Transport |
|----------|---------------|-----------|
| FTP      | 21            | TCP       |
| SSH      | 22            | TCP       |
| Telnet   | 23            | TCP       |
| SMTP     | 25            | TCP       |
| DNS      | 53            | UDP       |
| DHCP     | 67, 68        | UDP       |
| TFTP     | 69            | UDP       |
| HTTP     | 80            | TCP       |
| POP3     | 110           | TCP       |
| IMAP     | 143           | TCP       |
| SNMP     | 161           | UDP       |
| SMB      | 139, 445      | TCP       |
| HTTPS    | 443           | TCP       |


## REGULAR EXPRESSIONS

### Basic Characters

| Pattern  | Legend                                            | Example             | Match           |
|----------|---------------------------------------------------|---------------------|-----------------|
| `\d`     | One digit (0-9)                                   | `file_\d\d`         | `file_25`       |
| `\w`     | Word character (letter, digit, underscore)        | `\w-\w\w\w`         | `A-b_1`         |
| `\s`     | Whitespace (space, tab, newline)                  | `a\sb\sc`           | `a b c`         |
| `\D`     | One non-digit                                     | `\D\D\D`            | `ABC`           |
| `\W`     | One non-word character                            | `\W\W\W\W\W`        | `*-+=)`         |
| `\S`     | One non-whitespace                                | `\S\S\S\S`          | `Yoyo`          |

### Quantifiers

| Pattern  | Legend                          | Example            | Match              |
|----------|---------------------------------|--------------------|--------------------|
| `+`      | One or more                     | `Version\w-\w+`    | `Version A-b1_1`   |
| `{3}`    | Exactly three times             | `\D{3}`            | `ABC`              |
| `{2,4}`  | Two to four times               | `\d{2,4}`          | `156`              |
| `{3,}`   | Three or more times             | `\w{3,}`           | `regex_tutorial`   |
| `*`      | Zero or more times              | `A*B*C*`           | `AAACC`            |
| `?`      | Once or none                    | `plurals?`         | `plural`           |

### Special Characters

| Pattern  | Legend                            | Example        | Match       |
|----------|-----------------------------------|----------------|-------------|
| `.`      | Any character except line break   | `a.c`          | `abc`       |
| `\`      | Escapes a special character       | `\.\*\+\?`     | `.*+?`      |
| `|`      | Alternation / OR                  | `22|33`        | `33`        |
| `(...)`  | Capturing group                   | `A(nt\|pple)`  | `Apple` (captures `pple`) |
| `\1`     | Contents of Group 1               | `r(\w)g\1x`    | `regex`     |
| `\2`     | Contents of Group 2               | `(\d\d)\+(\d\d)=\2\+\1` | `12+65=65+12` |
| `(?:...)`| Non-capturing group               | `A(?:nt\|pple)` | `Apple`     |

### Character Classes

| Pattern    | Legend                                          | Example      | Match              |
|------------|-------------------------------------------------|--------------|--------------------|
| `[...]`    | One of the characters in brackets               | `T[ao]p`     | `Tap` or `Top`     |
| `-`        | Range indicator                                 | `[a-z]`      | One lowercase letter |
| `[x-y]`    | One character in range x to y                   | `[A-Z]+`     | `GREAT`            |
| `[^x]`     | One character that is not x                     | `[^a-z]{3}`  | `A1!`              |
| `[\d\D]`   | One character: digit or non-digit               | `[\d\D]+`    | Any character including new lines |

### Anchors

| Pattern  | Legend                                             | Example              |
|----------|-----------------------------------------------------|----------------------|
| `^`      | Start of string or line                             | `^abc.*`             |
| `$`      | End of string or line                               | `.*?the end$`        |

### Greedy vs Lazy

| Pattern    | Type     | Legend                    | Example | Match            |
|------------|----------|---------------------------|---------|------------------|
| `+`        | Greedy   | One or more               | `\d+`   | `12345`          |
| `+?`       | Lazy     | Makes quantifiers lazy    | `\d+?`  | `1` in `12345`   |
| `*`        | Greedy   | Zero or more              | `A*`    | `AAA`            |
| `*?`       | Lazy     | Makes quantifiers lazy    | `A*?`   | empty in `AAA`   |
| `{2,4}`    | Greedy   | Two to four times         | `\w{2,4}` | `abcd`         |
| `{2,4}?`   | Lazy     | Makes quantifiers lazy    | `\w{2,4}?` | `ab` in `abcd` |

### Usage in Python

```
re.findall(r'\b\w+\b', line)  # -> list of words without punctuation
```


## MATH


## STATISTICS


## DJANGO

### Model

Object-Relational Mapping (ORM) system. Allows you to define models as Python classes, which are then mapped to database tables. This system abstracts away much of the complexity of database access, letting you interact with data using Python objects and methods instead of raw SQL queries.

A **Model** is a Python class that defines the structure and behavior of the data you work with in your application. It represents a table in the database and maps to fields (columns) in that table.

```
from django.db import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
```

### Authentication vs Authorization

- **Authentication:** The process of verifying the identity of a user or system. Confirms *who* someone is (e.g., username and password).
- **Authorization:** The process of determining what actions, resources, or services a user or system is permitted to access after authentication. Determines *what* an authenticated user can do.

### Common Commands

```bash
django-admin startproject mysite
python manage.py startapp <name>
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
python manage.py runserver 8001

python manage.py dumpdata app_name.ModelName --output=data.json
python manage.py loaddata data.json
```

### Key Components

- **View**
- **Template**
- **URLs and Routing**
- **Forms**
- **Admin Interface**
- **Middleware**
- **Authentication and Permissions**
- **Signals**
- **Testing**


## FLASK


## DOCKER

Docker is a platform that uses **containers** to run applications. Containers are lightweight, standalone, and executable units that include everything needed to run a piece of software.

### Key Concepts

- **Images:** Read-only templates containing instructions to create a container.
- **Containers:** Instances of Docker images that run applications in an isolated environment.
- **Dockerfile:** A text file with instructions to build a Docker image.
- **Docker Engine:** Core part responsible for running and managing containers.
- **Docker Hub:** Cloud-based registry for storing and sharing images.

### Basic Commands

```bash
docker version
docker images

docker run hello-world
docker run -d -p 127.0.0.1:8000:80 --name server nginx
docker run -it ubuntu
docker start -i container

# Cleanup
docker rm container1 container2
docker container prune
docker rm $(docker ps -aq)
docker system prune -a --volumes
docker builder prune -a
docker rmi image

# Containers
docker pull image
docker ps -a
docker stop $(docker ps -q)
docker kill container
docker pause / unpause container
docker logs -f container
docker inspect container
docker stats

# Network
docker network ls
docker network create network_name

# Execute
docker exec -it server sh /bin/bash

# Volumes
docker volume ls / prune / rm
docker run --rm -v /host/folder:/app counter:01
docker run -d -p 8000:80 -v ${PWD}/site:/usr/share/nginx/html --name server nginx
docker run -v folder_name:/app/in_container/folder name image
docker volume create v_name
```

### Docker Compose

```bash
docker compose build
docker compose up -d
docker compose up -d --scale service_name=3
docker compose start / stop / restart
docker compose down --remove-orphans
docker compose down --volumes
docker compose ps / top
docker compose logs
docker compose exec container_id command
```

### Networks

- `bridge`: Default network (172.17.0.0/16)
- `host`: Uses host's network
- `none`: No networking

### PostgreSQL Docker

```bash
docker run --name my-postgres \
    -e POSTGRES_PASSWORD=pass123 \
    -e POSTGRES_USER=user1 \
    -e POSTGRES_DB=testdb \
    -p 5432:5432 \
    -d postgres
```


## LOGGING

### Log Levels

| Level       | Value | Description                                                      |
|-------------|-------|------------------------------------------------------------------|
| `NOTSET`    | 0     | All events are logged (when set on handler) or check ancestors.  |
| `DEBUG`     | 10    | Detailed information, typically for diagnosing problems.         |
| `INFO`      | 20    | Confirmation that things are working as expected.                |
| `WARNING`   | 30    | Something unexpected happened or might occur soon.               |
| `ERROR`     | 40    | More serious problem, software couldn't perform some function.   |
| `CRITICAL`  | 50    | A serious error, program may be unable to continue running.      |

**Flow:**
```
Logger receives log request → creates log record → sends to handler → formatter transforms data → sends to target
```

> Logger and handler can have filters.


## NGINX

Is a high-performance web server and reverse proxy server. It's widely used for various purposes in modern web applications due to its efficiency, scalability, and versatility.

- Web Server
- Reverse Proxy
- Load Balancer
- HTTPS Termination
- Caching
- WebSocket Proxying
- Content Compression
- Security Features
- Serving as a Gateway for Microservices

**Benefits:**
- Hide backend server details from clients.
- Provide a single entry point for requests.
- Enable features like HTTPS termination, caching, and compression.
- Handle high traffic efficiently.
- Improve fault tolerance by distributing load.
- Increase application scalability and reliability.


## GUNICORN

Is a Python WSGI (Web Server Gateway Interface) server that runs Python web applications, such as Django or Flask. It acts as a bridge between your Python application and a web server like Nginx or Apache, handling incoming requests and sending responses back to the client.

### Key Features

- **WSGI Compatibility:** Compatible with any Python web framework following WSGI (Django, Flask, FastAPI with adapters).
- **Concurrency:** Uses a pre-fork worker model to handle multiple requests simultaneously.
- **Flexibility:** Supports various worker types (sync, async, and others).
- **Ease of Deployment:** Lightweight and easy to integrate into existing projects.


## REST API

**Representational State Transfer (REST)** is an architectural style that defines a set of constraints to be used for creating web services. REST API is a way of accessing web services in a simple and flexible way without having any processing.

REST technology is generally preferred over SOAP because REST uses less bandwidth, is simple and flexible, making it more suitable for internet usage. All communication done via REST API uses only HTTP requests.

### HTTP Methods (CRUD)

| HTTP Method | CRUD Operation | Description                    |
|-------------|----------------|--------------------------------|
| `POST`      | Create         | Create a new resource          |
| `GET`       | Read           | Retrieve a resource            |
| `PUT/PATCH` | Update         | Update an existing resource    |
| `DELETE`    | Delete         | Remove a resource              |


## AJAX


## ACID

| Property     | Description                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------|
| **Atomicity**| A transaction is treated as a single, indivisible unit. Either all operations complete or none.  |
| **Consistency**| A transaction takes the database from one consistent state to another. Constraints must hold.  |
| **Isolation**| Multiple transactions can execute concurrently without interfering with each other.              |
| **Durability**| Once a transaction is committed, its changes are permanent and survive system failures.         |


## BASE


## SQL

### Data Querying

```sql
-- Basic SELECT
SELECT * FROM employees;
SELECT name FROM employees;
SELECT DISTINCT department FROM employees;

-- Filtering
SELECT * FROM employees WHERE department = 'Sales';
SELECT * FROM employees WHERE department IN ('Sales', 'Marketing');
SELECT * FROM employees WHERE salary BETWEEN 50000 AND 100000;
SELECT * FROM employees WHERE name LIKE 'J%';
SELECT * FROM employees WHERE commission IS NULL;

-- Sorting
SELECT * FROM employees ORDER BY salary DESC;
SELECT * FROM employees ORDER BY salary DESC LIMIT 5 OFFSET 10;

-- Aggregation
SELECT department, COUNT(*) FROM employees GROUP BY department;
SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 50000;

-- Joins
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;

SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id;

-- Subquery
SELECT employee.first_name, employee.last_name
FROM employee
WHERE employee.emp_id IN (
    SELECT works_with.emp_id
    FROM works_with
    WHERE works_with.total_sales > 30000
);

-- EXISTS
SELECT * FROM employees
WHERE EXISTS (SELECT * FROM sales WHERE sales.employee_id = employees.id);
```

### Data Manipulation

```sql
INSERT INTO employees (name, department, salary) VALUES ('John Doe', 'HR', 60000);
UPDATE employees SET salary = 70000 WHERE name = 'John Doe';
DELETE FROM employees WHERE name = 'John Doe';
TRUNCATE TABLE employees;
```

### Data Definition

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

ALTER TABLE employees ADD email VARCHAR(100);
ALTER TABLE employees DROP COLUMN phone;

DROP TABLE employees;
CREATE DATABASE company;
DROP DATABASE company;

CREATE INDEX idx_department ON employees (department);
DROP INDEX idx_department;
```

### Constraints and Keys

| Constraint      | Description                                                     |
|-----------------|-----------------------------------------------------------------|
| `PRIMARY KEY`   | Uniquely identifies each record.                                |
| `FOREIGN KEY`   | Ensures referential integrity by linking two tables.            |
| `UNIQUE`        | Ensures all values in a column are distinct.                    |
| `NOT NULL`      | Ensures a column cannot contain NULL values.                   |
| `CHECK`         | Ensures values satisfy a specific condition.                    |
| `DEFAULT`       | Sets a default value for a column.                             |

**Types of Keys:**
- **Primary Key:** Unique identifier for a record.
- **Surrogate Key:** Artificially created key (e.g., auto-incrementing integer).
- **Natural Key:** Key derived from data itself (e.g., SSN, email).
- **Composite Key:** Primary key consisting of two or more columns.
- **Foreign Key:** Primary key from another table.

### Transactions

```sql
BEGIN TRANSACTION;
COMMIT;
ROLLBACK;
SAVEPOINT my_savepoint;
RELEASE SAVEPOINT my_savepoint;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

### Functions

```sql
SELECT COUNT(*) FROM employees;
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary), MAX(salary) FROM employees;
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;
SELECT SUBSTRING(name, 1, 3) FROM employees;
SELECT ROUND(salary, 2) FROM employees;
SELECT NOW();
SELECT COALESCE(phone, 'Not Provided') FROM employees;
```

### Set Operations

```sql
SELECT name FROM employees WHERE department = 'Sales'
UNION
SELECT name FROM employees WHERE department = 'HR';

SELECT name FROM employees WHERE department = 'Sales'
INTERSECT
SELECT name FROM employees WHERE salary > 50000;

SELECT name FROM employees WHERE department = 'Sales'
EXCEPT
SELECT name FROM employees WHERE salary < 50000;
```

### Views & Indexes

```sql
CREATE VIEW employee_view AS SELECT name, department FROM employees WHERE salary > 50000;
DROP VIEW employee_view;
SHOW INDEX FROM employees;
```

### PostgreSQL Specific

```sql
-- JSON operators
json_column->'key'               -- Extract JSON field
json_column->>'key'              -- Extract as text
json_column#>'{path,to,key}'     -- Extract sub-object
json_column#>>'{path,to,key}'    -- Extract sub-object as text

-- Array operators
'{1,2,3}' @> '{1}'              -- Contains (true)
'{1}' <@ '{1,2,3}'              -- Contained by (true)
'{1,2}' || '{3,4}'              -- Concatenate
'{1,2}' && '{2,3}'              -- Overlap (true)
```


## SQLITE

```bash
sqlite3 <path to db>
```

```sql
.tables
.schema table_name

SELECT name FROM sqlite_master WHERE type = 'table';
SELECT sql FROM sqlite_master WHERE name = 'crime_scene_report';

ALTER TABLE users ADD COLUMN bot_lang TEXT DEFAULT 'ENG';
UPDATE users SET bot_lang = 'ENG' WHERE bot_lang IS NULL;

INSERT INTO tasks (user, text, active) VALUES (1, 'user 1 task', TRUE);
```


## POSTGRESQL (PSQL)

### Installation & Service

```bash
sudo apt install postgresql postgresql-contrib
sudo systemctl status/start/stop/enable/disable postgresql
```

### Connection

```bash
sudo -i -u postgres psql
psql -U username -d mydatabase -W
psql -h pg.pg4e.com -p 5432 -U pg4e_c952d0d873 pg4e_c952d0d873
```

### Meta-Commands

```bash
\l          # List databases
\du         # List users
\dt         # List tables
\d / \d+ <table_name>   # Describe table
\c dbname   # Connect to database
\i file.sql # Run SQL from file
\q          # Exit
```

### DDL (Data Definition Language)

```sql
CREATE USER username WITH PASSWORD 'password';
CREATE DATABASE db_name WITH OWNER username;

CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

ALTER TABLE student ADD gpa DECIMAL(3,2) UNIQUE;
ALTER TABLE student ADD age INT DEFAULT 0;
ALTER TABLE student DROP COLUMN gpa;
ALTER TABLE users RENAME TO customers;
ALTER TABLE automagic ALTER COLUMN name TYPE char(32);

ALTER USER new_username WITH SUPERUSER;
ALTER USER new_username WITH CREATEDB;
ALTER USER django_user WITH PASSWORD 'django_pass';

DROP USER username;
DROP DATABASE database_name;
DROP TABLE IF EXISTS table_name;
```

### DML (Data Manipulation Language)

```sql
INSERT INTO student(student_id, name) VALUES (3, 'Ivan');
UPDATE student SET major = 'bio' WHERE major = 'biology';
DELETE FROM student WHERE email = 'some@email.com';
```

### DCL (Data Control Language)

```sql
GRANT ALL PRIVILEGES ON DATABASE database_name TO new_username;
SET ROLE username;
```

### Triggers

```sql
CREATE OR REPLACE FUNCTION log_new_employee()
RETURNS trigger AS $$
BEGIN
    INSERT INTO trigger_test VALUES ('New employee added');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER my_trigger
BEFORE INSERT ON employee
FOR EACH ROW
EXECUTE FUNCTION log_new_employee();
```

### Prompt Indicators

- `home=:` — Ready for new command
- `home->:` — Command continued on next line
- `home'>:` — Open quote in command
- `*#` instead of `>` means logged in as admin

### Change Auth Method

```bash
# Before: local   all   django_user   peer
# After:  local   all   django_user   md5
```

### Reinstall PostgreSQL

```bash
sudo systemctl stop postgresql
sudo apt remove --purge postgresql postgresql-* -y
sudo rm -rf /etc/postgresql /var/lib/postgresql /var/log/postgresql
sudo apt autoremove -y && sudo apt autoclean
sudo apt install postgresql -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
```


## MONOLITH vs MICROSERVICES

| Aspect                 | Monolith                              | Decomposed Monolith                | Microservices                         |
|------------------------|---------------------------------------|-------------------------------------|---------------------------------------|
| Deployment             | Single deployable unit                | Single deployable unit              | Independent services                  |
| Independence           | Tightly coupled                       | Loosely decoupled                   | Fully decoupled                       |
| Communication          | In-memory function calls              | In-memory or internal APIs          | Network-based (HTTP, gRPC, etc.)      |
| Database               | Shared monolithic database            | Shared database, modularized        | Separate databases per service        |
| Scaling                | Scale entire system                   | Scale entire system                 | Scale individual services             |
| Failure Isolation      | Whole system can fail                 | Improved but still risks            | Failures isolated to service          |
| Team Autonomy          | Tight coordination required           | Some independence                   | Independent teams                     |
| Operational Complexity | Low                                   | Moderate                            | High                                  |
| Technology Choices     | Single stack                          | Usually single stack                | Different stacks allowed               |
| Development Speed      | Fast initially, slower as system grows| Improved modularity                 | Faster iteration per service          |
| Testing Complexity     | Simpler as a single unit              | Requires modular testing            | Each service tested individually      |

**Summary:**
- **Monolith:** Tightly coupled, deployed together, simple but hard to scale.
- **Decomposed Monolith:** Refactored into modular components, deployed as one unit.
- **Microservices:** Fully decoupled, independent services, scalable but operationally complex.


## PANDAS


## MATPLOTLIB


## NGROK

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
ngrok http 8001
```


---
## NOTES

- **Hardcode** — to put information into a software program so that it cannot be easily changed by a user. Write value just in code instead of using a variable.
- **Pseudocode** is an artificial and informal language that helps programmers develop algorithms. Pseudocode is a "text-based" detailed (algorithmic) design tool.

### VS Code Shortcuts

| Shortcut                | Action                          |
|-------------------------|---------------------------------|
| `Ctrl + Shift + E`      | Select sidebar                  |
| `Ctrl + B`              | Close sidebar                   |
| `Ctrl + 1/2/3`          | Swap or open group              |
| `Ctrl + F4`             | Close last group                |
| `Ctrl + J`              | Show/hide terminal              |
| `Ctrl + L`              | Select current line             |
| `Ctrl + Shift + L`      | Select all instances of selection |
| `Ctrl + F2`             | Select all instances of word    |
| `Alt + Enter`           | Select all results after find   |
| `Ctrl + G`              | Go to line                      |
| `Alt + Click`           | Add additional cursor           |
| `Ctrl + Alt + Up/Down`  | Add cursor                      |
| `Ctrl + U`              | Undo cursor insertion           |
| `Alt + Up/Down`         | Move current line               |
| `Shift + Alt + Up/Down` | Copy line/block                 |

### Windows Shortcuts

| Shortcut | Action        |
|----------|---------------|
| `Win + D`| Show desktop  |

### Python Notes

- Constant integers between -5 and 256 in Python are already cached.
- `type(obj)` returns the constructor of the object. `obj2 = type(obj)()` creates a new object of the same type.
- `from inspect import signature; signature(fu)` — inspect function signature.
