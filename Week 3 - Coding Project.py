########################################
# Script Name: Assignment3.py
# Title: Assignment 3 Code File
# Author: Vincent Marks
# Date: Feb 3rd 2023
########################################

payRates = [15.80, 16.00, 17.45, 15.80, 20.20]
timeCards = [35.75, 42.00, 41.0, 40.00, 39.50]

# Remove the five zeroes from the example.
# Append to the empty list later on.
# This will coincide with the count and..
# .. ensure proper recording of data.
payAmounts = []


count = 0

while count < len(payRates):
    if timeCards[count] <= 40:
# Append the calculated pay to the payAmounts list
        payAmounts.append(payRates[count] * timeCards[count])
        count += 1
    elif timeCards[count] > 40:
        payAmounts.append((payRates[count] * 40) + (1.5 * payRates[count]) * (timeCards[count] - 40))
        count += 1 

# Begin the priting portion of program once the..
# .. length of payAmounts list is equal to the length of payRates.
# This ensures all employees' paychecks have been calculated.
if len(payAmounts) == len(payRates):
    print('\n============Payroll Calculator=============')

count = 0

# Utilize a Counter Controlled loop until all employee..
# pay information is printed.
while count != len(payRates):

    payR = "${:.2f}".format(payRates[count])
    payA = "${:.2f}".format(payAmounts[count])

    print('\nEmployee', count,':', 
    '\n\nRate:', f"{payR:>16}",
    '\nHours Worked: ', f"{timeCards[count]:>7,.2f}",
    '\nCheck Amount: ', f"{payA:}")
    count += 1





