"""

Jaclyn Horowitz
Music Software 2014
"""
import csv

csv_list = []

# Change csv file to be compared to here
with open('Interval_Spacing_csv.csv', 'rU') as my_file:
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
def test_interval_spacing(pythag_scale):
    print("*** Beginning test_interval_spacing() tests ***")
    # How many tests failed
    failed = 0
    # The csv file is in sorted order, so we should begin by sorting our own collection to compare
    numerator_row = 2
    col = 1
    for interval_left in range(1, 8):
        tempcol = col
        calculated_intv_spacing = pythag_scale.get_spacing(interval_left,interval_left+1)
        while csv_list[numerator_row][tempcol+1]!="":
            tempcol +=1
        csv_intv_spacing = str(csv_list[numerator_row][tempcol]) + "/" + str(csv_list[numerator_row+1][tempcol])

        if calculated_intv_spacing == csv_intv_spacing:
            print("CORRECT: Interval left= " + str(interval_left) + " Interval Right= " + str(interval_left+1) + " CSV Interval Spacing = " + str(csv_intv_spacing) + " Calculated Interval Spacing = " + str(calculated_intv_spacing))
        else:
            print("INCORRECT: Interval left=" + str(interval_left) + " Interval Right= " + str(interval_left+1) + " CSV Interval Spacing = " + str(csv_intv_spacing) + " Calculated Interval Spacing = " + str(calculated_intv_spacing))
            failed +=1
        numerator_row+=2
        col+=1
    print("*** test_interval_spacing() SUMMARY *** ")
    print("Failed: %d " % failed)

def eq(a, b, eps=0.01):
    return abs(a - b) <= eps


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False