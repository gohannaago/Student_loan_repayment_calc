# Written by Hanna Go 8/3/2022
# based on Student loan company repayment scheme

from time import sleep
from header import yn_to_bool, calc

# Initialize variables
# List that appends payments
payments = []
# threshold values hardcoded for each plan
th_1 = 19895
th_2 = 27295
th_4 = 25000
th_p = 21000
#repayment rates in percentage
rate = 9
rate_p = 6

print("Welcome to the Student loan repayment calculator.")
print("Calculated amount is what you need to repay per month.")
sleep(3)

# Ask user for Annual Income
income = float(input("Please enter your annual income: "))

# Check which plan is used
bool_1 = yn_to_bool("Are you on Plan 1? Answer either (y/n)")
bool_2 = yn_to_bool("Are you on Plan 2? Answer either (y/n)")
bool_4 = yn_to_bool("Are you on Plan 4? Answer either (y/n)")
bool_p = yn_to_bool("Are you on Postgraduate Loan repayment plan? Answer either (y/n)")

# Calculate for each plan
if bool_1:
    payments.append(calc(income, th_1, rate))
if bool_2:
    payments.append(calc(income, th_2, rate))
if bool_4:
    payments.append(calc(income, th_4, rate))
if bool_p:
    payments.append(calc(income, th_p, rate_p))

total = sum(payments)

print(f"You will repay total of £{total} per month. ")