"""
Program: payroll2.py
Chapter 4 Practice Project (page 133)
7/31/24
Dennis Schauf 

Payroll application that reads employee data from a text file and outputs payroll info in tabular format. 
"""

import os.path 
import time

# input phase
fileName = input("Please type the name of the payroll file that you would like to process >> ")

while os.path.isfile(fileName) == False:
     fileName = input("Sorry! Please enter a valid payroll file name >> ")

print("Processing file data...")
time.sleep(3)

# processing phase 
data = open(fileName, "r")

print()
print("%-18s%9s%9s%11s" % ("Last Name", "Wage", "Hours", "Earnings"))
print("-" * 50)

# Loop through the file data line by line. Split up the data in each line. Place each component into tabular format and calculate the earnings. 
for line in data: 
     # Break the line into individual string values
     dataArray = line.split()
     # Extract the last name from that array and store it
     name = dataArray[0]
     # Extract the wage from the array, convert it to a float and store it
     wage = float(dataArray[1])
     # Extract the hours from the array, convert it to a float and store it
     hours = float(dataArray[2])
     # Extract the earnings from the array, convert it to a float and store it
     earnings = wage * hours
     print("%-18s%9.2f%9.2f%11.2f" % (name, wage, hours, earnings))

# Final sign-off message
input("\n\nEnd of file. Press ENTER to quit.")