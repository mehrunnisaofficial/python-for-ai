# Smart Name Formatter
name = input("Enter your full name: ").strip().title()
print(f"Hello, {name}!")

# Smart Salary Formatter
salary = float(input("Enter your salary: "))
print(f"Your Salary is ₹{salary:,.2f}")

# Mini Banking App
current_balance = float(input("Enter your current balance: "))

deposit_amount = salary * 20 / 100
total_balance = current_balance + deposit_amount

print(f"Deposit Amount : ₹{deposit_amount:,.2f}")
print(f"Total Balance  : ₹{total_balance:,.2f}")
