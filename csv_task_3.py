# Store list of value in csv file with column name

import csv

with open("Student_list.csv") as name:
    Store = csv.reader(name)
    Store_list = []

    for i in Store:
        #print(i[0])
        #str1.append(i[2])
        Store_list.append(i[3])

print(Store_list)
