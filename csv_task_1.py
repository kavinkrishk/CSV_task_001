# open csv file & print all values

import csv

with open("Student_list.csv") as new:
    output_all = csv.reader(new)

    for i in output_all:
        print(i)
