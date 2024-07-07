##########################################################
# Script Name: Coding Project 1 Final.py
# Title: Assignement 5 Code File
# Author: Vincent Marks
# Date: Feb 17th 2023

standard1 = [12.250, 18.000, 27.125]
standard2 = [22.4, 60.0, 98.5]
metric1 = []
metric2 = []
## Imports
from os import system, name


## Functions
def clearScreen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def standardToMetric3(x, y):
    for i in x:
        miliMetric1 = (i * 25.400)
        y.append(miliMetric1)
def printData(chosenList1, chosenList2):
    n = len(chosenList1)
    print(f"{'Standard':<}", f"\t{'Metric':>}")
    for x in range(n):
        inch = chosenList1[x]
        mili = chosenList2[x]
        print(f"{inch:<,.2f}", f"{mili:>16,.2f}")
def main():
    clearScreen()
    standardToMetric1()
    printData1()
    standardToMetric2()
    printData2()
def main2(x, y):
    standardToMetric3(x, y)
    printData(x, y)


# ====================================================
# todo 1.1
def standardToMetric1():
    for i in standard1:
        miliMetric1 = (i * 25.400)
        metric1.append(miliMetric1)
# todo 2.1
def printData1():
    n = len(standard1)
    print(f"{'Standard':<}", f"\t{'Metric':>}")
    for x in range(n):
        inch = standard1[x]
        mili = metric1[x]
        print(f"{inch:<,.2f}", f"{mili:>16,.2f}")
# todo 3.1
def standardToMetric2():
    global standard2
    global metric2
    for i in standard2:
        miliMeter = i * 25.40
        metric2.append(miliMeter)
# todo 3.3
def printData2():
    n = len(standard2)
    print(f"{'Standard':<}", f"\t{'Metric':>}")
    for x in range(n):
        inch = standard2[x]
        mili = metric2[x]
        print(f"{inch:<,.2f}", f"{mili:>16,.2f}")
#=========================================================
## Program
clearScreen()
main()
main2(standard1, metric1)
main2(standard2, metric2)

