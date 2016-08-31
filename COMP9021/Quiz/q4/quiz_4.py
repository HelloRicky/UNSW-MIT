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
import re


filename = 'monthly.csv'

if not os.path.exists(filename):
    print('There is no file named {} in the working directory, giving up...'.format(filename))
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')

if source != 'GCAG' and source != 'GISTEMP':
    print('Wrong source, giving up...')
    sys.exit()

range_for_the_years = input('Enter a range for the years in the form XXXX--XXXX: ')
if not re.match(r'^[0-9]{4}--[0-9]{4}$', range_for_the_years):
    print('Wrong format, giving up...')
    sys.exit()

month = input('Enter a month in the form of a 2-digit number: ')
if not re.match(r'^[0-9]{2}$', month):
    print('Wrong format, giving up...')
    sys.exit()

average = 0
data_avg = []
data_year_fit = []
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE

src_key = 'Source'
mean_key = 'Mean'
date_key = 'Date'
date1 = int(range_for_the_years[:4])
date2 = int(range_for_the_years[6:])
startDate = min(date1, date2)
endDate = max(date1, date2)

with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        #check if source match up
        if row[src_key] == source:
            #check for year
            year = int(row[date_key][:4])
            if year >= startDate and year <= endDate:
                # check for month
                mth = row[date_key][-2:]
                if mth == month:
                    val = float(row[mean_key])
                    data_avg.append(val)
                    data_year_fit.append([val, year])
                    
if len(data_avg):
    average = sum(data_avg)/len(data_avg)
    for i in data_year_fit:
        if i[0] > average:
            years_above_average.append(i[1])
    years_above_average.sort()

print('The average anomaly for this month of those years is: {:.2f}.'.format(average))
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
