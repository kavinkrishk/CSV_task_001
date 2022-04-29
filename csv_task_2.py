#print particular  column in a csv file

import csv

with open("Student_list.csv",encoding="utf-8-sig") as new:
    Filter = csv.DictReader(new)
    list = []


    for i in Filter:
        print(i["Grade"])
        list.append(i["Student Name"])

print(list)




