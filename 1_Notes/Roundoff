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
