# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx--xxxx, and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the second year can be anterior to the first year.
# - The month is a two digit number.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by Fu Zheng and Eric Martin for COMP9021


import sys
import os
import csv


filename = 'monthly.csv'
if not os.path.exists(filename):
    print('There is no file named {} in the working directory, giving up...'.format(filename))
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
range_for_the_years = input('Enter a range for the years in the form XXXX--XXXX: ')
month = input('Enter a month in the form of a 2-digit number: ')
average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE

with open(filename) as csvfile:
    pass
    # REPLACE pass ABOVE AND THIS COMMENT WITH YOUR CODE

print('The average anomaly for this month of those years is: {:.2f}.'.format(average))
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
