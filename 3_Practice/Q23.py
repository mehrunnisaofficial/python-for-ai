# Age Calculator

import sys


# calculating age of a person
current_year = int(input("Enter Current Year: "))
current_month = int(input("Enter Current Month: "))
todays_date = int(input("Enter today's day number: "))

user_name = sys.argv[1]
user_birth_year = int(sys.argv[2])
user_birth_month = int(sys.argv[3])
user_birth_day = int(sys.argv[4])



year = current_year - user_birth_year
month = current_month - user_birth_month
day = todays_date - user_birth_day

print(f"{user_name} is exactly: {year} years {month} months {day} days old")
