# Lecture 1: Python Basics

Welcome to your very first Python lecture. You do not need to know anything about programming before starting this. We are going to build everything from the ground up — one small idea at a time — so that by the end of this lecture, you will be able to read and write real Python code with confidence.

Think of this document as a patient teacher sitting next to you, explaining every single detail, even the ones that seem "obvious." Nothing is assumed. Nothing is skipped.

Let's begin.

---

## Table of Contents

1. [Functions](#1-functions)
2. [Parameters and Arguments](#2-parameters-and-arguments)
3. [Return Values](#3-return-values)
4. [Variables](#4-variables)
5. [Strings](#5-strings)
6. [Output Formatting](#6-output-formatting)
7. [`print()` Parameters](#7-print-parameters)
8. [String Methods](#8-string-methods)
9. [`split()`](#9-split)
10. [Lists (Introduction)](#10-lists-introduction)
11. [Unpacking](#11-unpacking)
12. [Common Errors](#12-common-errors)
13. [Practice Problems](#13-practice-problems)
    - [Problem 1: Ask the user for their name](#problem-1-ask-the-user-for-their-name)
    - [Problem 2: Print the user's name](#problem-2-print-the-users-name)
    - [Problem 3: Different ways to format strings](#problem-3-different-ways-to-format-strings)
    - [Problem 4: What whitespace does `print()` add?](#problem-4-what-whitespace-does-print-add)
    - [Problem 5: Using `sep`](#problem-5-using-sep)
    - [Problem 6: Using `end`](#problem-6-using-end)
    - [Problem 7: Quotes inside quotes](#problem-7-quotes-inside-quotes)
    - [Problem 8: Using f-strings](#problem-8-using-f-strings)
    - [Problem 9: Removing whitespace using `strip()`](#problem-9-removing-whitespace-using-strip)
    - [Problem 10: Capitalising text](#problem-10-capitalising-text)
    - [Problem 11: Capitalising every word](#problem-11-capitalising-every-word)
    - [Problem 12: Method chaining](#problem-12-method-chaining)
    - [Problem 13: Using `split()`](#problem-13-using-split)
    - [Problem 14: List indexing](#problem-14-list-indexing)
    - [Problem 15: Unpacking](#problem-15-unpacking)
    - [Problem 16: Understanding common errors](#problem-16-understanding-common-errors)
- [Final Recap](#final-recap)

---

## 1. Functions

### What is a function?

A **function** is a named, reusable block of instructions that performs a specific task. You "call" (use) a function by writing its name followed by parentheses `()`.

**Real-life analogy:** Think of a function like a coffee machine. You don't need to know exactly how the coffee is brewed inside the machine — you just press a button (call the function), maybe tell it how much sugar you want (give it an argument), and it hands you a cup of coffee (the result). The machine hides the complicated part and gives you a simple button to press.

### Why do functions exist?

Imagine if, every single time you wanted to display something on the screen, you had to write ten lines of complicated low-level code. That would be exhausting and error-prone. Functions exist so that:

- Common tasks can be **packaged once** and reused forever.
- Code becomes **shorter and easier to read**.
- You don't need to know *how* something works internally — only *what* it does.

This idea is called **abstraction** — hiding complexity behind a simple interface.

### Built-in functions

Python comes with many functions already built in, ready to use immediately. Today, we will focus on three of them:

| Function  | Purpose                                             |
| --------- | ---------------------------------------------------- |
| `print()` | Displays (shows) information on the screen           |
| `input()` | Asks the user to type something and captures it      |
| `len()`   | Tells you how many characters/items are in something |

### User-defined functions (Introduction only)

Python also allows *you* to create your own functions using the `def` keyword. We are not going deep into this today — just know that it exists, and we will study it fully in a future lecture. For now, we will only *use* the functions Python already gives us.

### `print()`

**What?** `print()` is a function that displays text or values on the screen.

**Why?** Without a way to display information, a program would run silently and we'd have no idea what it's doing. `print()` is our window into the program.

**How?** You write `print()` followed by whatever you want to show, inside the parentheses.

**Syntax:**

```python
print(value)
```

**Example:**

```python
print("Hello, World!")
```

**Output:**

```text
Hello, World!
```

**Line-by-line explanation:**

- `print` is the name of the function.
- `(` and `)` are parentheses — they tell Python "I am calling this function, and here is what I'm giving it."
- `"Hello, World!"` is the value we are giving to `print()`. It is text, so it must be inside quotes.

```
print("Hello, World!")
   │         │
   │         └──► the value passed into the function
   └──► the function being called
```

> **Common Mistake**
> Forgetting the quotes around text:
> ```python
> print(Hello)   # ❌ Error! Python thinks "Hello" is a variable name, not text.
> ```

> **Best Practice**
> Always double-check that text is wrapped in quotes before running your code.

### `input()`

**What?** `input()` is a function that pauses the program, waits for the user to type something, and then hands that typed text back to your program.

**Why?** Programs often need information *from* the person using them — a name, an age, a choice. `input()` is how a program listens.

**How?** You call `input()` and can optionally put a message inside the parentheses — this message is called a **prompt**, and it's shown to the user so they know what to type.

**Syntax:**

```python
input("Your message here: ")
```

**Example:**

```python
name = input("Enter your name: ")
print(name)
```

**Output:**

```text
Enter your name: David
David
```

**Line-by-line explanation:**

- `input("Enter your name: ")` displays the text `Enter your name: ` on the screen, then waits.
- The user types something — let's say `David` — and presses Enter.
- Whatever the user typed becomes the **return value** of `input()` (more on return values in Section 3).
- `name = ...` stores that returned text inside a variable called `name` (more on variables in Section 4).
- `print(name)` displays the value stored in `name`.

```
input("Enter your name: ")
         │
         ▼
   user types "David"
         │
         ▼
    returns "David"
         │
         ▼
   name = "David"
```

**Important detail — why does `input()` always return a string?**

Even if the user types numbers, like `25`, `input()` will always give it back as **text** (a string), not as a number. This is because Python has no way of knowing in advance whether you plan to use the input as a number, a word, a sentence, or something else. Treating everything as text is the safest, most predictable default. If you need it as a number later, you must explicitly convert it — but that is a topic for another day.

> **Common Mistake**
> Beginners often try to do math directly with `input()` results:
> ```python
> age = input("Enter your age: ")
> print(age + 1)   # ❌ Error! age is text, not a number.
> ```

> **Note**
> We are not fixing this today — just be aware that `input()` always gives you a string.

### `len()`

**What?** `len()` tells you the length of something — for example, how many characters are in a piece of text.

**Why?** Sometimes your program needs to know *how much* data it's dealing with — like checking if a password is long enough, or how many letters are in a name.

**How?** You pass the thing you want measured inside the parentheses, and `len()` returns a number.

**Syntax:**

```python
len(value)
```

**Example:**

```python
word = "Python"
print(len(word))
```

**Output:**

```text
6
```

**Line-by-line explanation:**

- `word = "Python"` stores the text `"Python"` in a variable called `word`.
- `len(word)` counts the characters in `word`: P-y-t-h-o-n = 6 characters.
- `print(...)` displays that count.

```
"Python"
   │
   ▼
 len() counts: P y t h o n
   │
   ▼
    6
```

> **Common Mistake**
> Forgetting that spaces count as characters too:
> ```python
> print(len("hi there"))   # 8, not 7 — the space counts!
> ```

### Small Summary — Section 1

- A function is a reusable block of code that performs a task.
- `print()` shows information on the screen.
- `input()` asks the user for information and always returns it as text.
- `len()` tells you the length (number of characters or items) of something.

---

## 2. Parameters and Arguments

### What is a parameter?

A **parameter** is a placeholder name that a function uses internally to refer to whatever value you give it. Think of it as a labeled slot waiting to be filled.

### What is an argument?

An **argument** is the actual value you place into that slot when you call the function.

**Real-life analogy:** Imagine a form with a blank labeled "Name: ____". The blank labeled "Name" is like the **parameter** — it exists on the form before anyone fills it in. When you actually write "David" in that blank, "David" is the **argument** — the real value being supplied.

**Example:**

```python
print("Hello")
```

Here, `"Hello"` is the **argument** being passed into `print()`. Internally, `print()` has a parameter (a slot) that receives whatever text you give it.

### Positional arguments

A **positional argument** is one where the *order* you place values in matters — Python matches each value to a slot based on its position (1st, 2nd, 3rd...).

**Example:**

```python
print("Hello", "World")
```

**Output:**

```text
Hello World
```

Here, `"Hello"` fills the first slot and `"World"` fills the second slot, purely based on the order they appear.

### Keyword arguments

A **keyword argument** is one where you explicitly name which parameter you're filling, using `parameter_name=value`. Order no longer matters because you're labeling each value directly.

**Example:**

```python
print("Hello", "World", sep="-")
```

**Output:**

```text
Hello-World
```

Here, `sep="-"` explicitly tells `print()`: "use `-` as the separator parameter," regardless of where it appears in the parentheses.

### Comparing them side by side

| Type               | How it works                          | Example                     |
| ------------------ | -------------------------------------- | ---------------------------- |
| Positional argument | Matched by order                       | `print("Hello", "World")`   |
| Keyword argument    | Matched by explicit name               | `print("Hello", sep="-")`   |

> **Tip**
> You can mix both — positional arguments first, keyword arguments after:
> ```python
> print("Hello", "World", sep="-", end="!\n")
> ```

> **Common Mistake**
> Putting a positional argument *after* a keyword argument causes an error:
> ```python
> print(sep="-", "Hello")   # ❌ Error!
> ```

### Small Summary — Section 2

- A parameter is the named slot defined by the function.
- An argument is the actual value you supply.
- Positional arguments rely on order; keyword arguments rely on explicit names.

---

## 3. Return Values

### What is a return value?

A **return value** is the result a function hands back to you after it finishes its work. Not every function displays something — some quietly *compute* something and give it back so you can store or use it.

**Real-life analogy:** Think of asking a friend "What's 5 plus 3?" Your friend doesn't just think about it silently forever — they *tell you* the answer: "8." That spoken answer is like a return value — a result handed back to you so you can use it.

### How `input()` returns a value

We already saw this in Section 1: when the user types something and presses Enter, `input()` **returns** that typed text back to wherever you called it.

```python
name = input("Enter your name: ")
```

```
input(...) runs
     │
     ▼
user types "David"
     │
     ▼
returns "David"   ◄── this is the return value
     │
     ▼
stored in: name
```

### How `len()` returns a value

`len()` doesn't display anything by itself — it silently computes a number and returns it. That's why we often wrap it in `print()`:

```python
print(len("Python"))
```

Here, `len("Python")` returns `6`, and then `print()` displays that returned value.

> **Note**
> `print()` itself does **not** return anything useful (technically it returns a special empty value called `None`, which we won't worry about today). Its job is to *display*, not to *return* something usable.

> **Best Practice**
> If you want to use a function's result later (store it, do math with it, pass it elsewhere), make sure the function actually returns a value — don't assume every function does.

### Small Summary — Section 3

- A return value is the result a function hands back after running.
- `input()` returns whatever the user typed (always as text).
- `len()` returns a number representing a length.
- Return values are useless unless you store them or use them immediately.

---

## 4. Variables

### What is a variable?

A **variable** is a named container that stores a value in the computer's memory so you can use it later.

**Real-life analogy:** A variable is like a labeled box. You can put something inside the box (a value), label the box (give it a name), and later look inside the box just by referring to its label — without needing to remember exactly where the box physically is.

### Assignment

**Assignment** is the act of putting a value into a variable. In Python, this is done using the `=` sign.

> **Important:** In Python, `=` does **not** mean "equals" like in math. It means **"store the value on the right into the name on the left."**

**Syntax:**

```python
variable_name = value
```

**Example:**

```python
age = 20
```

```
   age
    │
    ▼
   20
```

**Line-by-line explanation:**

- `age` is the variable name — the label on the box.
- `=` performs the assignment — "put this value into that box."
- `20` is the value being stored.

### Storing return values

Instead of just printing a function's result immediately, we can **store** it in a variable to use later.

```python
name = input("Enter your name: ")
```

Here, the value returned by `input()` doesn't disappear — it gets stored inside `name`, so we can use `name` again and again throughout our program.

### Naming variables

Variable names in Python must follow certain rules:

| Rule                                   | Valid Example | Invalid Example |
| --------------------------------------- | -------------- | ----------------- |
| Must start with a letter or underscore | `name`, `_age` | `1name`          |
| Can contain letters, numbers, underscores | `user_name1` | `user-name`      |
| Cannot use Python keywords              | `my_input`     | `print` (used as a variable name) |
| Case-sensitive                          | `Name` ≠ `name` | —                 |

> **Best Practice**
> Use clear, descriptive names. `name` is better than `x`. `user_age` is better than `a`.

### Printing variables

Once a value is stored in a variable, you can display it using `print()`:

```python
name = "David"
print(name)
```

**Output:**

```text
David
```

**Line-by-line explanation:**

- `name = "David"` stores the text `"David"` inside the variable `name`.
- `print(name)` — notice there are **no quotes** around `name` here. This tells Python "display the *value stored inside* the variable called `name`," not the literal word "name."

> **Common Mistake**
> Confusing a variable with a string:
> ```python
> name = "David"
> print("name")   # Output: name   (the literal word, not David!)
> print(name)     # Output: David  (the value stored inside the variable)
> ```

### Small Summary — Section 4

- A variable is a named container for a value.
- `=` assigns a value to a variable name (it does not mean mathematical equality).
- Variable names should be descriptive and follow Python's naming rules.
- Quotes around a name mean "literal text"; no quotes means "look up the variable's value."

---

## 5. Strings

### What is a string?

A **string** is a sequence of characters — letters, numbers, symbols, spaces — treated as text. In Python, any text wrapped in quotes is a string.

**Real-life analogy:** A string is like a string of beads threaded together, where each bead is one character. `"cat"` is three beads: `c`, `a`, `t`, threaded in that exact order.

```
"cat"
 │ │ │
 c a t
```

### Quotes

Strings must always be wrapped in quotes so Python knows "this is text, not code."

### Single vs. double quotes

Python allows both single quotes `'...'` and double quotes `"..."` to create strings — they work identically.

```python
print('Hello')
print("Hello")
```

**Output:**

```text
Hello
Hello
```

> **Note**
> There is no functional difference between single and double quotes in Python — pick one style and be consistent. Most style guides prefer double quotes, but either is correct.

### Quotes inside quotes

Sometimes your text itself needs to contain a quote character. The trick is to use the *other* type of quote as the outer wrapper.

**Example:**

```python
print("It's a sunny day")
```

**Output:**

```text
It's a sunny day
```

Here, the outer quotes are double quotes `"..."`, so the single quote `'` inside `It's` is treated as just a regular character, not the end of the string.

```python
print('She said "hello"')
```

**Output:**

```text
She said "hello"
```

> **Common Mistake**
> Using the same quote type inside and outside without escaping:
> ```python
> print('It's a sunny day')   # ❌ Error! Python thinks the string ends after "It"
> ```

### Escape characters

An **escape character** is a special code, starting with a backslash `\`, that lets you insert characters that would otherwise be difficult or impossible to type directly into a string — like a literal quote mark, a new line, or a tab space.

**Why do escape characters exist?** Because sometimes you need to include a character (like a quote) that would normally *end* the string early, or a character that can't be typed as a visible symbol (like "start a new line"). The backslash tells Python: "the next character is special — treat it differently."

| Escape Sequence | Meaning              |
| ---------------- | --------------------- |
| `\n`              | New line              |
| `\t`              | Tab (horizontal space) |
| `\"`              | A literal double quote |
| `\\`              | A literal backslash    |

**Example — `\n` (new line):**

```python
print("Hello\nWorld")
```

**Output:**

```text
Hello
World
```

**Example — `\t` (tab):**

```python
print("Name:\tDavid")
```

**Output:**

```text
Name:	David
```

**Example — `\"` (literal quote):**

```python
print("She said \"hello\"")
```

**Output:**

```text
She said "hello"
```

**Example — `\\` (literal backslash):**

```python
print("C:\\Users\\David")
```

**Output:**

```text
C:\Users\David
```

> **Best Practice**
> If your string needs many literal quotes, it's often easier to just switch to the other quote style instead of escaping.

### Small Summary — Section 5

- A string is text wrapped in quotes.
- Single and double quotes behave identically.
- Use the opposite quote type to include a quote character inside a string.
- Escape characters (`\n`, `\t`, `\"`, `\\`) let you insert special characters into strings.

---

## 6. Output Formatting

There are several ways to combine text and variables when printing. We will look at all of them for awareness, but **as a beginner, you really only need to remember two: commas and f-strings.**

### Commas

Separate multiple values with commas inside `print()`. Python automatically inserts a single space between each value.

```python
name = "David"
print("Hello,", name)
```

**Output:**

```text
Hello, David
```

### The `*` operator (repeat/unpack) — for awareness only

The `*` symbol can be used in advanced ways related to lists (which we'll cover in future lectures). For now, just know it exists — we won't use it today.

### `.format()` — for awareness only

An older way to insert values into text:

```python
name = "David"
print("Hello, {}".format(name))
```

**Output:**

```text
Hello, David
```

### f-strings

An **f-string** (formatted string) lets you insert variables *directly* inside a string by placing an `f` before the opening quote and wrapping variable names in curly braces `{}`.

```python
name = "David"
print(f"Hello, {name}")
```

**Output:**

```text
Hello, David
```

**Line-by-line explanation:**

- The `f` right before the opening quote tells Python: "this string contains placeholders that should be replaced with real values."
- `{name}` is a placeholder — Python replaces it with the current value stored in `name`.

```
f"Hello, {name}"
              │
              ▼
       replaced with "David"
              │
              ▼
      "Hello, David"
```

### `%` formatting — for awareness only

An old-style formatting method inherited from the C programming language:

```python
name = "David"
print("Hello, %s" % name)
```

### `+` Concatenation method

```python
name = "Noor"
print("Hello " + name)
```

**->** ***Most common way for output is comma(,) and concatenation***

#### Difference Between `,` and `+` in `print()`

This was confusing to me at first, so here's the simplest way to remember it.

---

##### Using `,` (Comma)

```python
name = "David"

print("Hello,", name)
```

Output:

```text
Hello, David
```

###### What's happening?

When we use a comma, we are giving **multiple arguments** to the `print()` function.

```python
print("Hello,", name)
```

Here, `print()` receives:

- `"Hello,"`
- `name`

The `print()` function has a **default separator** (`sep=" "`), so it automatically places **one space** between each argument.

You can think of it like this (only as a mental model):

```text
"Hello," + " " + "David"
```

> **Note:** Python is **not actually using `+` internally**. This is just an easy way to understand why a space appears.

###### Memory Trick

> **Comma = Let `print()` do the work.**

---

##### Using `+` (Concatenation)

```python
name = "David"

print("Hello, " + name)
```

Output:

```text
Hello, David
```

###### What's happening?

The `+` operator joins (**concatenates**) two strings **before** `print()` receives them.

Python first creates:

```text
"Hello, David"
```

Then `print()` simply prints that one complete string.

Unlike commas, `+` **does not add spaces automatically**.

For example:

```python
print("Hello," + name)
```

Output:

```text
Hello,David
```

If we want a space, we must write it ourselves.

```python
print("Hello, " + name)
```

Notice the space after the comma.

---

### Simple Difference

**Using `,`**

```python
print("Hello,", name)
```

- Gives **two separate arguments** to `print()`.
- `print()` automatically adds a space between them.
- Easier for beginners.

Think:

> **"I'm letting `print()` handle the spacing."**

---

**Using `+`**

```python
print("Hello, " + name)
```

- Joins strings into **one string** first.
- `print()` receives only one argument.
- No spaces are added automatically.

Think:

> **"I'm doing the joining myself before `print()` prints it."**

---

**Easy Way to Remember**

#### `,`

```python
print("Hello,", name)
```

🧠 Let **`print()`** handle the spacing.

---

#### `+`

```python
print("Hello, " + name)
```

🧠 I handle the joining and spacing myself.

---

# One-Line Summary

- **`,` = Multiple arguments → `print()` adds spaces automatically.**
- **`+` = Join strings yourself → You must add spaces yourself.**



**Output:**

```text
Hello, David
```

### Comparison table

| Method       | Beginner-friendly? | Example                          |
| ------------ | ------------------- | ---------------------------------- |
| Commas       | ✅ Yes               | `print("Hello,", name)`           |
| f-strings    | ✅ Yes               | `print(f"Hello, {name}")`         |
| `.format()`  | ⚠️ Awareness only    | `"Hello, {}".format(name)`       |
| `%` formatting | ⚠️ Awareness only  | `"Hello, %s" % name`             |
| `*`          | ⚠️ Awareness only (advanced, list-related) | —          |

> **Remember**
> As a complete beginner, focus only on **commas** and **f-strings**. The rest exist in real-world code you might encounter, but you don't need to write them yet.

### Small Summary — Section 6

- Commas in `print()` join values with an automatic space.
- f-strings let you embed variables directly inside text using `{}`.
- `.format()` and `%` formatting are older styles you should recognize but not worry about using yet.

---

## 7. `print()` Parameters

### `sep`

**What?** `sep` (short for "separator") controls what character(s) Python places *between* multiple values in a `print()` call.

**Why does `print()` automatically insert spaces?** When you write `print("Hello", name)`, Python needs *some* way to join these two separate pieces together into one line of output. By default, it chooses a single space, because that's the most natural, readable default for human language — nobody wants `HelloDavid` mashed together. That default space is exactly what the `sep` parameter controls, and you can override it any time.

**Default value:** `sep=" "` (a single space) — this is why `print("Hello", "World")` shows `Hello World`.

**Internal behavior — conceptually:**

```python
print("Hello", name)
```

Behaves conceptually like:

```
"Hello" + " " + name
```

Python isn't literally doing string addition internally, but *conceptually*, it's stitching the pieces together using whatever `sep` is set to — by default, a space.

**Changing the separator:**

```python
print("Hello", "World", sep="-")
```

**Output:**

```text
Hello-World
```

**Removing the separator (empty string):**

```python
print("Hello", "World", sep="")
```

**Output:**

```text
HelloWorld
```

**Custom separator (multiple characters):**

```python
print("2024", "01", "15", sep="/")
```

**Output:**

```text
2024/01/15
```

> **Common Mistake**
> Forgetting that `sep` only affects the space *between* arguments — it does nothing if you only pass one argument:
> ```python
> print("Hello", sep="-")   # Output: Hello   (no effect — only one value!)
> ```

### `end`

**What?** `end` controls what Python adds *after* the entire `print()` output finishes — by default, a new line character `\n`.

**Why?** Every time you call `print()`, the cursor needs to know where to go next. By default, Python moves to a new line after printing, so that the *next* `print()` call starts fresh on its own line. This default is stored in the `end` parameter.

**Default value:** `end="\n"` (a new line).

**Example showing the default behavior:**

```python
print("Hello")
print("World")
```

**Output:**

```text
Hello
World
```

Each `print()` ends with an invisible `\n`, pushing the next output to a new line.

**Changing `end` to print on the same line:**

```python
print("Hello", end=" ")
print("World")
```

**Output:**

```text
Hello World
```

**Line-by-line explanation:**

- `print("Hello", end=" ")` displays `Hello`, but instead of moving to a new line, it adds a single space and stays on the same line.
- `print("World")` then continues right there, producing `Hello World` on one line.

```
print("Hello", end=" ")      print("World")
        │                          │
        ▼                          ▼
      "Hello "  ───────────────►  "World"
                (same line)
```

**Another example — no line break at all:**

```python
print("Loading", end="")
print("...")
```

**Output:**

```text
Loading...
```

> **Best Practice**
> Use `end=""` or `end=" "` when you want to build up a single line of output across multiple `print()` calls — for example, showing progress like `Loading...`.

### Small Summary — Section 7

- `sep` controls what goes *between* multiple values (default: a single space).
- `end` controls what goes *after* the entire print output (default: a new line).
- Both can be customized using keyword arguments.

---

## 8. String Methods

A **method** is a special kind of function that "belongs to" a value and is called using a dot `.` after that value, like `text.method()`.

**Real-life analogy:** Think of a string as an object that comes with a built-in toolbox of the actions it can perform on itself — like a smartphone that has a "screenshot" button built in. You don't build the camera yourself; you just call `.screenshot()` and it happens.

### `strip()`

**What?** `strip()` removes whitespace (spaces, tabs, new lines) from the **beginning and end** of a string. It does **not** touch whitespace in the middle.

**Why does this exist?** User input often accidentally contains extra spaces (someone types `"  David  "` instead of `"David"`). `strip()` cleans this up so your program isn't confused by invisible extra characters.

**Syntax:**

```python
text.strip()
```

**Example:**

```python
name = "   David   "
print(name.strip())
```

**Output:**

```text
David
```

**Diagram — before and after:**

```
before:  "   David   "
                │
                ▼  strip()
after:   "David"
```

> **Common Mistake**
> Thinking `strip()` removes spaces from the *middle* of a string too:
> ```python
> print("da vid".strip())   # Output: "da vid"  — middle space untouched!
> ```

### `capitalize()`

**What?** `capitalize()` makes the **first letter** of the string uppercase, and forces **every other letter** to lowercase.

**Example:**

```python
text = "hello WORLD"
print(text.capitalize())
```

**Output:**

```text
Hello world
```

**Diagram:**

```
before:  "hello WORLD"
                │
                ▼ capitalize()
after:   "Hello world"
```

> **Common Mistake**
> Expecting every word to be capitalized:
> ```python
> print("hello world".capitalize())   # Output: "Hello world" — only the FIRST letter!
> ```

### `title()`

**What?** `title()` capitalizes the **first letter of every word** in the string.

**Example:**

```python
text = "hello world"
print(text.title())
```

**Output:**

```text
Hello World
```

**Diagram:**

```
before:  "hello world"
                │
                ▼ title()
after:   "Hello World"
```

### Comparison table

| Method          | Effect                                    | Example Input | Example Output |
| ---------------- | ------------------------------------------ | -------------- | --------------- |
| `strip()`         | Removes leading/trailing whitespace       | `"  hi  "`     | `"hi"`         |
| `capitalize()`   | Capitalizes only the first letter overall | `"hello WORLD"` | `"Hello world"` |
| `title()`         | Capitalizes the first letter of every word | `"hello world"` | `"Hello World"` |

### Method chaining

**What?** Method chaining means calling one method directly after another, on the same line, because each method returns a *new string* that the next method can immediately act on.

**Why does this work?** Every string method we've seen returns a brand-new string as its result. Since that result is itself a string, you can immediately call *another* string method on it — chaining them together like links.

**Example:**

```python
text = "   hello world   "
result = text.strip().title()
print(result)
```

**Output:**

```text
Hello World
```

**Line-by-line explanation:**

- `text.strip()` runs first, removing the outer spaces: `"hello world"`.
- `.title()` is then called immediately on *that result*, capitalizing each word: `"Hello World"`.
- The final result is stored in `result` and printed.

**Diagram:**

```
"   hello world   "
         │
         ▼ .strip()
"hello world"
         │
         ▼ .title()
"Hello World"
```

> **Best Practice**
> Method chaining keeps code short, but if a chain gets too long, it can become hard to read. Break it into steps if needed for clarity.

### Small Summary — Section 8

- Methods are functions that belong to a value, called with a dot.
- `strip()` removes outer whitespace; `capitalize()` capitalizes only the first letter; `title()` capitalizes every word.
- Method chaining lets you apply multiple methods in sequence, left to right.

---

## 9. `split()`

### What does `split()` do?

**What?** `split()` breaks a string apart into a **list** of smaller strings, based on a separator.

**Why does `split()` return a list?** Splitting text naturally produces *multiple* pieces — not just one. Python needs a way to hold multiple pieces together as a single result, in order, so you can access each piece individually. A **list** (introduced properly in Section 10) is exactly that: an ordered collection. So `split()` hands back a list because "multiple pieces of text" is precisely what a list is designed to hold.

### Default whitespace splitting

By default, `split()` breaks a string apart wherever there is whitespace (spaces, tabs, new lines), and ignores any extra whitespace.

**Example:**

```python
full_name = "John Doe"
parts = full_name.split()
print(parts)
```

**Output:**

```text
['John', 'Doe']
```

**Diagram:**

```
"John Doe"
     │
     ▼ split()
["John", "Doe"]
```

### Custom separators

You can tell `split()` exactly which character to split on, by passing it as an argument.

**Example:**

```python
date = "2024-01-15"
parts = date.split("-")
print(parts)
```

**Output:**

```text
['2024', '01', '15']
```

**Another example:**

```python
csv_line = "apple,banana,cherry"
fruits = csv_line.split(",")
print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry']
```

> **Common Mistake**
> Assuming `split()` without arguments splits on commas or other punctuation — by default it only splits on whitespace unless you tell it otherwise.

> **Note**
> Multiple consecutive spaces are treated as one when using default `split()`:
> ```python
> print("hello     world".split())   # ['hello', 'world']
> ```

### Small Summary — Section 9

- `split()` breaks a string into a list of pieces.
- By default, it splits on whitespace.
- You can specify a custom character to split on.
- It returns a list because splitting naturally produces multiple ordered pieces.

---

## 10. Lists (Introduction)

### What is a list?

A **list** is an ordered collection of values, stored together under a single variable name. Lists are written using square brackets `[ ]`, with items separated by commas.

**Real-life analogy:** A list is like a numbered row of lockers. Each locker holds one item, and each locker has a number so you can find exactly what's inside.

**Example:**

```python
parts = ["John", "Doe"]
print(parts)
```

**Output:**

```text
['John', 'Doe']
```

### Indexing

**What is indexing?** Indexing means accessing a specific item inside a list (or string) using its position number, written in square brackets right after the list's name.

**Why does indexing start from zero?** This feels strange at first, but here's the reasoning: an index doesn't represent "the 1st, 2nd, 3rd item" — it represents **how far you have to move from the very first item to reach the item you want**. The first item requires *zero* steps to reach it, because you're already there. This is a core convention across most programming languages, and it becomes natural with practice.

**Diagram:**

```
parts = ["John", "Doe"]

index:     0        1
          "John"   "Doe"
```

### `[0]` — first item

```python
parts = ["John", "Doe"]
print(parts[0])
```

**Output:**

```text
John
```

### `[1]` — second item

```python
parts = ["John", "Doe"]
print(parts[1])
```

**Output:**

```text
Doe
```

> **Common Mistake**
> Trying to access an index that doesn't exist:
> ```python
> parts = ["John", "Doe"]
> print(parts[2])   # ❌ IndexError! There is no item at position 2.
> ```
> (We'll explain this error properly in Section 12.)

### Small Summary — Section 10

- A list is an ordered collection of values written with `[ ]`.
- Each item has a position, called an index, starting from `0`.
- `list[0]` gets the first item, `list[1]` gets the second item, and so on.

---

## 11. Unpacking

### What is unpacking?

**Unpacking** means assigning each item of a list directly to its own variable, all in a single line, by matching positions.

**Example:**

```python
parts = ["John", "Doe"]
first, last = parts
print(first)
print(last)
```

**Output:**

```text
John
Doe
```

### What exactly does Python do internally?

When Python sees `first, last = parts`, it looks at how many variable names are on the left (`first` and `last` — two names) and how many items are inside `parts` (two items). Since the counts match, Python assigns them **in order**:

- The item at index `0` (`"John"`) goes into `first`.
- The item at index `1` (`"Doe"`) goes into `last`.

**Diagram:**

```
parts = ["John", "Doe"]
            │        │
            ▼        ▼
         first     last
         "John"    "Doe"
```

### Comparing unpacking with manual indexing

Unpacking:

```python
first, last = parts
```

is exactly equivalent to writing this manually, item by item:

```python
first = parts[0]
last = parts[1]
```

Both approaches produce identical results — unpacking is simply a shorter, cleaner way to write multiple indexing assignments at once.

| Approach          | Code                          | Result                          |
| ------------------ | ------------------------------ | --------------------------------- |
| Manual indexing    | `first = parts[0]` <br> `last = parts[1]` | Two lines, explicit             |
| Unpacking          | `first, last = parts`          | One line, same result           |

> **Common Mistake**
> The number of variable names on the left **must exactly match** the number of items in the list, or you'll get a `ValueError` (explained in Section 12).

### Small Summary — Section 11

- Unpacking assigns each list item to its own variable in one line, based on position.
- It behaves exactly like indexing each item manually — just written more concisely.
- The number of variables must match the number of items exactly.

---

## 12. Common Errors

### `IndexError`

**When does it happen?** An `IndexError` occurs when you try to access an index that does not exist in a list (or string) — for example, asking for the 5th locker when there are only 2 lockers.

**Why does it happen?** Python cannot return a value that isn't there. Rather than silently giving you something incorrect, Python stops the program and reports the exact problem, so you can fix your code.

**Example:**

```python
parts = ["John", "Doe"]
print(parts[5])
```

**Output:**

```text
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    print(parts[5])
IndexError: list index out of range
```

**Explanation:** `parts` only has indexes `0` and `1`. Index `5` simply does not exist, so Python raises (reports) an `IndexError`.

```
parts = ["John", "Doe"]

index:     0        1        2   3   4   5
          "John"   "Doe"    ❌  ❌  ❌  ❌ ← doesn't exist!
```

> **Common Mistake**
> Forgetting that indexing starts at `0`, so a list with 2 items only has valid indexes `0` and `1` — not `1` and `2`.

### `ValueError`

**When does unpacking fail?** A `ValueError` occurs during unpacking when the number of variable names on the left does **not** match the number of items being unpacked.

**Example — too many values:**

```python
parts = ["John", "Middle", "Doe"]
first, last = parts
```

**Output:**

```text
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    first, last = parts
ValueError: too many values to unpack (expected 2)
```

**Example — too few values:**

```python
parts = ["John"]
first, last = parts
```

**Output:**

```text
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    first, last = parts
ValueError: not enough values to unpack (expected 2, got 1)
```

**Explanation:** Python needs an *exact* match between the number of names you're assigning to and the number of items available — otherwise it doesn't know what to do with the leftover names or leftover values.

> **Best Practice**
> Before unpacking, make sure you know exactly how many items the list contains — for example, by printing `len(parts)` first if you're unsure.

### Small Summary — Section 12

- `IndexError` happens when you access a position that doesn't exist in a list.
- `ValueError` happens during unpacking when the number of variables doesn't match the number of items.
- Both errors exist so Python can clearly tell you what went wrong instead of guessing.

---

## 13. Practice Problems

### Problem 1: Ask the user for their name

**Problem statement:** Write code that asks the user to type their name and stores it.

```python
name = input("Enter your name: ")
```

**Line-by-line explanation:**

- `input("Enter your name: ")` displays the prompt and waits for the user to type something.
- `name = ...` stores whatever the user typed inside the variable `name`.

**Output (example run, user types "David"):**

```text
Enter your name: David
```

**What is happening internally:** Python pauses program execution at the `input()` call. The moment the user presses Enter, the typed text is captured as a string and returned, then stored in `name`.

> **Common Mistake:** Forgetting to store the result — calling `input()` without `name = ` discards the typed value instantly.

**Key takeaway:** `input()` captures user text and always returns it as a string.

---

### Problem 2: Print the user's name

**Problem statement:** Display the name that was collected in Problem 1.

```python
name = input("Enter your name: ")
print(name)
```

**Output:**

```text
Enter your name: David
David
```

**Line-by-line explanation:**

- Line 1 collects the name as before.
- `print(name)` displays the *value* stored in `name` (no quotes, so Python looks up the variable).

**What is happening internally:** Python retrieves the value currently stored in the `name` box and sends it to the screen.

> **Common Mistake:** Writing `print("name")` instead of `print(name)` — the quoted version prints the literal word "name," not the value.

**Key takeaway:** No quotes around a variable name means "use its stored value."

---

### Problem 3: Different ways to format strings

**Problem statement:** Show the same greeting using commas and f-strings.

```python
name = "David"
print("Hello,", name)
print(f"Hello, {name}")
```

**Output:**

```text
Hello, David
Hello, David
```

**Line-by-line explanation:**

- Line 2 uses a comma to separate two values, letting `print()`'s default `sep=" "` join them.
- Line 3 embeds the variable directly inside the string using an f-string.

**What is happening internally:** Both approaches produce identical final text, but through different mechanisms — one joins separate arguments, the other substitutes a placeholder inside one string.

> **Common Mistake:** Forgetting the `f` before the quotes — without it, `{name}` is treated as literal text, not a placeholder.

**Key takeaway:** Multiple techniques can achieve the same output; f-strings are usually the cleanest for beginners.

---

### Problem 4: What whitespace does `print()` add?

**Problem statement:** Demonstrate the default space `print()` inserts between comma-separated values.

```python
print("Hello", "World")
```

**Output:**

```text
Hello World
```

**Line-by-line explanation:** With two comma-separated arguments and no custom `sep`, Python uses its default separator — a single space — between them.

**What is happening internally:** Conceptually, Python joins the arguments as `"Hello" + " " + "World"`.

> **Common Mistake:** Assuming there's no space unless you add one yourself — the space is automatic by default.

**Key takeaway:** `print()`'s default `sep` is a single space, automatically inserted between multiple arguments.

---

### Problem 5: Using `sep`

**Problem statement:** Join values with a custom separator instead of a space.

```python
print("2024", "01", "15", sep="/")
```

**Output:**

```text
2024/01/15
```

**Line-by-line explanation:** The keyword argument `sep="/"` overrides the default space, so `/` is placed between each value instead.

**What is happening internally:** Python joins the three arguments using `/` wherever it would normally use a space.

> **Common Mistake:** Placing `sep` before the values it applies to and forgetting it must be a keyword argument (`sep=`), not just a plain value.

**Key takeaway:** `sep` customizes what goes *between* printed values.

---

### Problem 6: Using `end`

**Problem statement:** Print two things on the same line instead of separate lines.

```python
print("Hello", end=" ")
print("World")
```

**Output:**

```text
Hello World
```

**Line-by-line explanation:** The first `print()` normally ends with a new line (`\n`), but `end=" "` replaces that with a single space, so the next `print()` continues on the same line.

**What is happening internally:** Python does not move the cursor to a new line after the first call; it stays on the current line, letting the second call's output attach right after.

> **Common Mistake:** Forgetting that `end` still applies even if you don't set it — its default value is `"\n"`, which is why prints normally appear on separate lines.

**Key takeaway:** `end` controls what happens *after* a print statement finishes; the default is a new line.

---

### Problem 7: Quotes inside quotes

**Problem statement:** Print a sentence containing a quotation.

```python
print("She said \"hello\" to me")
```

**Output:**

```text
She said "hello" to me
```

**Line-by-line explanation:** The backslash before each inner `"` tells Python "this is a literal quote character, not the end of the string."

**What is happening internally:** Python reads `\"` as a single escaped character, inserting a literal `"` into the output rather than terminating the string.

> **Common Mistake:** Using the same quote type inside and outside without escaping, which ends the string early and causes an error.

**Key takeaway:** Use escape characters (`\"`) or switch quote styles to include quotes inside a string.

---

### Problem 8: Using f-strings

**Problem statement:** Greet a user by embedding their name and the length of their name in one f-string.

```python
name = "David"
print(f"Hello, {name}! Your name has {len(name)} letters.")
```

**Output:**

```text
Hello, David! Your name has 5 letters.
```

**Line-by-line explanation:** `{name}` is replaced with `"David"`, and `{len(name)}` is replaced with the result of calling `len(name)`, which is `5`.

**What is happening internally:** Python evaluates whatever is inside each pair of curly braces (even a function call) and substitutes the result directly into the string.

> **Common Mistake:** Forgetting curly braces around the variable — without `{}`, the variable name is treated as plain text.

**Key takeaway:** f-strings can contain not just variables, but any expression, including function calls like `len()`.

---

### Problem 9: Removing whitespace using `strip()`

**Problem statement:** Clean up a name that has extra spaces around it.

```python
name = "   David   "
clean_name = name.strip()
print(clean_name)
```

**Output:**

```text
David
```

**Line-by-line explanation:** `.strip()` removes the leading and trailing spaces from `name`, returning a new cleaned string stored in `clean_name`.

**What is happening internally:** Python scans from both ends of the string inward, removing whitespace characters until it hits a non-whitespace character on each side.

> **Common Mistake:** Expecting `strip()` to remove spaces in the middle of a string — it only removes them from the edges.

**Key takeaway:** `strip()` is essential for cleaning up messy user input before using it.

---

### Problem 10: Capitalising text

**Problem statement:** Fix the capitalization of a messy string.

```python
text = "hello WORLD"
print(text.capitalize())
```

**Output:**

```text
Hello world
```

**Line-by-line explanation:** `.capitalize()` makes the very first character uppercase and forces every other character to lowercase.

**What is happening internally:** Python rebuilds the string, capitalizing only the character at index `0`, and lowercasing everything from index `1` onward.

> **Common Mistake:** Expecting every word to be capitalized — `capitalize()` only affects the first letter of the *entire string*.

**Key takeaway:** `capitalize()` affects only the first character of the whole string, not each word.

---

### Problem 11: Capitalising every word

**Problem statement:** Format a name properly so each word starts with a capital letter.

```python
text = "david michael doe"
print(text.title())
```

**Output:**

```text
David Michael Doe
```

**Line-by-line explanation:** `.title()` scans the string and capitalizes the first letter of *every* word, lowercasing the rest of each word.

**What is happening internally:** Python identifies word boundaries (spaces) and capitalizes the character immediately following each boundary, plus the very first character of the string.

> **Common Mistake:** Confusing `title()` with `capitalize()` — only `title()` affects every word.

**Key takeaway:** Use `title()` when you want every word capitalized, such as for full names.

---

### Problem 12: Method chaining

**Problem statement:** Clean and format a messy full name in a single line.

```python
raw_name = "   david michael doe   "
formatted_name = raw_name.strip().title()
print(formatted_name)
```

**Output:**

```text
David Michael Doe
```

**Line-by-line explanation:** `.strip()` runs first, removing outer whitespace, producing `"david michael doe"`. `.title()` then runs on *that* result, capitalizing each word.

**What is happening internally:** Each method returns a brand-new string, and the next method in the chain operates on that returned result — like passing a baton from one runner to the next.

> **Common Mistake:** Calling methods in the wrong order can produce different intermediate results — always think about what each step produces before the next one runs.

**Key takeaway:** Method chaining applies multiple transformations to a string in a single readable line, left to right.

---

### Problem 13: Using `split()`

**Problem statement:** Break a full name into separate first and last name pieces.

```python
full_name = "John Doe"
parts = full_name.split()
print(parts)
```

**Output:**

```text
['John', 'Doe']
```

**Line-by-line explanation:** `.split()` with no arguments breaks the string apart wherever whitespace occurs, producing a list of the separate pieces.

**What is happening internally:** Python scans the string, treats each run of whitespace as a boundary, and collects everything between boundaries into a list of substrings.

> **Common Mistake:** Assuming `split()` requires an argument — it works fine with no arguments, defaulting to whitespace.

**Key takeaway:** `split()` transforms one string into a list of smaller strings, which is essential before we can access individual pieces.

---

### Problem 14: List indexing

**Problem statement:** Access the first and second items of a list directly.

```python
parts = ["John", "Doe"]
print(parts[0])
print(parts[1])
```

**Output:**

```text
John
Doe
```

**Line-by-line explanation:** `parts[0]` retrieves the item at position `0` (the first item); `parts[1]` retrieves the item at position `1` (the second item).

**What is happening internally:** Python counts positions starting from `0`, then jumps directly to the requested slot in memory and returns whatever value is stored there.

> **Common Mistake:** Thinking `parts[1]` means "the first item" — it actually means "the item at position 1," which is the *second* item, since counting starts at 0.

**Key takeaway:** List indexing always starts counting from `0`, not `1`.

---

### Problem 15: Unpacking

**Problem statement:** Split a full name and assign each piece directly to its own variable.

```python
full_name = "John Doe"
parts = full_name.split()
first, last = parts
print(first)
print(last)
```

**Output:**

```text
John
Doe
```

**Line-by-line explanation:** After `split()` produces `["John", "Doe"]`, the line `first, last = parts` assigns `"John"` to `first` and `"Doe"` to `last`, matching by position.

**What is happening internally:** Python checks that there are exactly two names on the left and exactly two items in `parts`, then assigns index `0` to the first name and index `1` to the second name.

> **Common Mistake:** Trying to unpack into the wrong number of variables — this raises a `ValueError` if the counts don't match.

**Key takeaway:** Unpacking is a shortcut for assigning each list item to its own variable, based on matching positions.

---

### Problem 16: Understanding common errors

**Problem statement:** Trigger and understand an `IndexError` and a `ValueError`.

```python
parts = ["John", "Doe"]
print(parts[5])
```

**Output:**

```text
Traceback (most recent call last):
IndexError: list index out of range
```

```python
parts = ["John", "Doe", "Smith"]
first, last = parts
```

**Output:**

```text
Traceback (most recent call last):
ValueError: too many values to unpack (expected 2)
```

**Line-by-line explanation:** The first example asks for index `5`, which does not exist in a 2-item list, so Python raises `IndexError`. The second example tries to unpack 3 items into only 2 variable names, so Python raises `ValueError`.

**What is happening internally:** Python always checks bounds and counts before performing an operation. When something doesn't line up — a missing index, or a mismatched count — it stops immediately and reports exactly what went wrong, rather than guessing or silently failing.

> **Common Mistake:** Ignoring error messages instead of reading them — Python's error messages usually tell you *exactly* what's wrong (e.g., "expected 2, got 3").

**Key takeaway:** `IndexError` means "that position doesn't exist"; `ValueError` (in unpacking) means "the number of variables doesn't match the number of values." Reading the error message carefully is the fastest way to fix your code.

---

## Final Recap

| Concept          | Key Idea                                             |
| ----------------- | ------------------------------------------------------ |
| Functions         | Reusable blocks of code, e.g. `print()`, `input()`, `len()` |
| Parameters/Arguments | Parameters are slots; arguments are the values filling them |
| Return values     | The result a function hands back after running        |
| Variables         | Named containers that store values using `=`           |
| Strings           | Text wrapped in quotes; escape characters add special symbols |
| Output formatting | Commas and f-strings are the beginner-friendly go-tos  |
| `sep` / `end`     | Control what goes between/after printed values         |
| String methods    | `strip()`, `capitalize()`, `title()` transform strings  |
| `split()`         | Breaks a string into a list of pieces                   |
| Lists             | Ordered collections accessed by index, starting at `0`  |
| Unpacking         | Assigns list items to variables by matching position    |
| `IndexError`      | Accessing a position that doesn't exist                |
| `ValueError`      | Mismatched count during unpacking                       |

> **Tip**
> Re-read this lecture slowly, and actually *type out* every example yourself. Programming is a skill built through practice, not just reading.

Congratulations — you've completed Lecture 1: Python Basics!


---

## 🐾 Thanks for studying with me! 🐾

That wraps up **Lecture 1 — Python Basics** all in one cozy little `.md` file. 🖤🤍 Hope it made things click a little easier. See you in the next one! 👋

📌 **Follow for more notes & updates:**
- 📸 Insta: [@mehrunnisa.ai](https://www.instagram.com/mehrunnisa.ai/)
- ✍️ Substack: [The Epoch](https://theepoch.substack.com/)
- 🎥 YouTube: [@mehrunnisa.ai](https://www.youtube.com/@Mehrunnisa-ai)

---