# ============================================
# PROBLEM 22: Percentage Calculator
# ============================================

# Taking input from the user
marks = float(input("Enter your marks obtained: "))
total = float(input("Enter the total marks: "))

# Calculating percentage
percentage = (marks / total) * 100

# Displaying the result
print(f"Percentage : {percentage:.2f}%")