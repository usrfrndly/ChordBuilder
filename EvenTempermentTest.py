"""

Jaclyn Horowitz
Music Software 2014
"""
import csv
import this

csv_list = []

# Change csv file to be compared to here
with open('even_temperment_sheet_phase4.csv', 'rU') as my_file:
    reader = csv.reader(my_file, skipinitialspace=True, delimiter=',', quoting=csv.QUOTE_NONE)
    # Skip all empty rows
    # for row in reader:
    row_count = 0
    cell_count = None
    found = False
    for row in reader:
        if len(row) != 0:
            csv_list.append(row)

my_file.close()

# Tests the pythag natural scale
def test_et_scale(et_scale):
    print("*** Beginning test_et_scale() tests ***")
    # How many tests failed
    failed = 0
    for interval in range(13):
        if float(et_scale.scale_intervals[interval].final_frequency) == float(csv_list[interval][0]):
            print("CORRECT: Interval " + str(interval) + ". ET Frequency = " + str(csv_list[interval][0]))
        else:
            print("INCORRECT: Interval " + str(interval) +". ET CSV Frequency =  " + str(csv_list[interval][0]) + " ET Calculated Frequency = " + str(et_scale.scale_intervals[interval].final_frequency))
            failed +=1
    print("*** test_et_scale() SUMMARY *** ")
    print("Failed: %d " % failed)

def eq(a, b, eps=0.01):
    return abs(a - b) <= eps


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False