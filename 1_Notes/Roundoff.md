# Rounding in Mathematics and Python

## What is Rounding?

Rounding means **replacing a number with a nearby, simpler number**. We do this to make numbers easier to read, write, remember, or calculate.

### Examples

```text
23.3478921 → 23.35
98 → 100
1998 → 2000
```

The rounded value is close to the original value but is simpler to understand.

---

# The Most Important Rule

Whenever someone says:

> **"Round this number."**

The first question should always be:

> **"Round it to what?"**

A number can be rounded to many different place values.

Examples:

* Nearest whole number (ones)
* Nearest ten
* Nearest hundred
* Nearest thousand
* One decimal place (tenths)
* Two decimal places (hundredths)
* Three decimal places (thousandths)

Without specifying the place value, the instruction is incomplete.

---

# Place Values

## Whole Numbers

| Place Value | Value |
| ----------- | ----: |
| Ones        |     1 |
| Tens        |    10 |
| Hundreds    |   100 |
| Thousands   |  1000 |

## Decimal Numbers

| Place Value | Value |
| ----------- | ----: |
| Tenths      |   0.1 |
| Hundredths  |  0.01 |
| Thousandths | 0.001 |

---

# The Golden Rule of Rounding

No matter what place value you are rounding to, the process is always the same.

### Step 1

Keep all digits up to the place value you are asked to round to.

### Step 2

Look at the **next digit** immediately after the last digit you kept.

### Step 3

Apply the rule:

* If the next digit is **0, 1, 2, 3, or 4**, keep the last digit unchanged.
* If the next digit is **5, 6, 7, 8, or 9**, increase the last kept digit by **1**.

This is the only rule you need to remember.

---

# Rounding Whole Numbers

## Example 1

Round **23** to the nearest **10**.

Keep the tens place:

```text
20
```

Look at the ones digit:

```text
23
 ^
 3
```

Since **3 < 5**, do not increase the tens digit.

Answer:

```text
23 → 20
```

---

## Example 2

Round **27** to the nearest **10**.

Keep:

```text
20
```

Look at the ones digit:

```text
27
 ^
 7
```

Since **7 ≥ 5**, increase the tens digit.

Answer:

```text
27 → 30
```

---

## Example 3

Round **149** to the nearest **100**.

Keep:

```text
100
```

Look at the tens digit:

```text
149
 ^
 4
```

Since **4 < 5**

Answer:

```text
149 → 100
```

---

## Example 4

Round **176** to the nearest **100**.

Keep:

```text
100
```

Look at the tens digit:

```text
176
 ^
 7
```

Since **7 ≥ 5**

Answer:

```text
176 → 200
```

---

# Rounding Decimal Numbers

The exact same rule applies.

The only difference is that you are keeping decimal places instead of tens or hundreds.

## Example 1

Round **2.22345** to **2 decimal places**.

Keep:

```text
2.22
```

Look at the next digit:

```text
2.22345
    ^
    3
```

Since **3 < 5**

Answer:

```text
2.22
```

---

## Example 2

Round **2.225** to **2 decimal places**.

Keep:

```text
2.22
```

Look at the next digit:

```text
2.225
    ^
    5
```

Since **5 ≥ 5**

Increase the last kept digit.

Answer:

```text
2.23
```

---

## Example 3

Round **23.347** to **2 decimal places**.

Keep:

```text
23.34
```

Look at the next digit:

```text
23.347
      ^
      7
```

Since **7 ≥ 5**

Answer:

```text
23.35
```

---

# School Mathematics vs Python

In school, you are often asked to round numbers to:

* Nearest 10
* Nearest 100
* Nearest 1000

Examples:

```text
23 → 20
27 → 30
149 → 100
176 → 200
```

In Python, the `round()` function is commonly used for:

* Nearest whole number
* Decimal places

Examples:

```python
round(3.7)
```

Output:

```text
4
```

```python
round(2.228, 2)
```

Output:

```text
2.23
```

The concept is exactly the same.

Only the place value changes.

---

# The Difference Between `round()` and `:.2f`

## `round()`

The `round()` function **changes the value** and returns a new rounded number.

Example:

```python
result = round(10 / 3, 2)

print(result)
```

Output:

```text
3.33
```

The variable now stores:

```text
3.33
```

---

## `:.2f`

Formatting with `:.2f` **does not change the original value**.

It only changes how the number is displayed.

Example:

```python
result = 10 / 3

print(f"{result:.2f}")
```

Output:

```text
3.33
```

But the variable still stores:

```text
3.3333333333333335
```

Proof:

```python
result = 10 / 3

print(f"{result:.2f}")
print(result)
```

Output:

```text
3.33
3.3333333333333335
```

Python internally rounds the number **only while displaying it**.

The original value remains unchanged.

---

# Key Difference

| `round()`                    | `:.2f` |       |
| ---------------------------- | ------ | ----- |
| Changes the stored value     | ❌ No   |       |
| Returns a rounded value      | ✅ Yes  |       |
| Used for future calculations | ✅ Yes  |       |
| Only formats the output      | ❌ No   | ✅ Yes |
| Rounds while displaying      | ✅      | ✅     |

---

# Important Things to Remember

* Rounding means replacing a number with a nearby, simpler number.
* Always ask **"Round to what place value?"**
* The rounding rule is the same for whole numbers and decimal numbers.
* The only difference is **which place value you keep**.
* `round()` returns a new rounded value.
* `:.2f` only formats the output and does not modify the original variable.
* In Python, `round(number)` rounds to the nearest whole number.
* `round(number, n)` rounds to **n decimal places**.
* `:.2f` always displays exactly **2 decimal places**, even if the original number has more.


<div style="border: 2px solid #444; border-radius: 8px; padding: 20px 24px; background-color: #f8f8f8;">

### Why does `round(2.225, 2)` sometimes return `2.22` instead of `2.23`?

You might expect:

```python
round(2.225, 2)
```

Output:

```text
2.23
```

However, Python often returns:

```text
2.22
```

While:

```python
round(2.235, 2)
```

returns:

```text
2.23
```

**This does not mean `round()` is broken.**

The reason is that computers store decimal numbers using **binary (base-2)**, not decimal (base-10). Many decimal values, such as `2.225`, **cannot be represented exactly in binary**. Instead, Python stores the closest possible binary approximation.

So, when `round()` performs the rounding, it rounds the value that is **actually stored in memory**, which may be slightly smaller or larger than the decimal number you typed.

Imagine the computer stores something conceptually similar to:

```text
2.224999999999...
```

*(This is only an example, not the exact stored value.)*

Since the stored value is slightly closer to `2.22` than `2.23`, the result becomes `2.22`.

---

**Flow of Events**

```
You type
   2.225
     │
     ▼
Computer stores the closest binary approximation
     │
     ▼
Example approximation
2.224999999999...
     │
     ▼
Python rounds the stored value
     │
     ▼
   Result
   2.22
```

This behavior is called **floating-point precision** and is a normal characteristic of almost every programming language, not just Python.

**Don't worry if this feels confusing right now.** Once you learn about binary numbers and floating-point representation, this behavior will make complete sense.

</div>

<img width="900" height="1474" alt="floating-point-note" src="https://github.com/user-attachments/assets/fcae51d9-3894-4385-8d09-8cad13703c38" />

