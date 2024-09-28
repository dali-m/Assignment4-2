# This program calculates an employee's productivity bonus.

employeeName=str(input("Enter Employee's name: "))
numShifts=int(input("Enter Number of Shifts: "))
numTransactions=int(input("Enter Number of Transactions: "))
tranValue=float(input("Enter transaction dollar value: "))

bonus=0.00

score=(tranValue/numTransactions)/numShifts
if score <= 30:
    bonus = 50.00
elif score >= 31 and score <= 69:
    bonus = 75.00
elif score >= 70 and score <= 199:
    bonus = 100.00
elif score >= 200:
    bonus = 200.00

print("Employee Name: ",employeeName)
print("Employee Bonus: ",bonus)