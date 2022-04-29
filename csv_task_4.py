# Store the Dict Value in Json file with the column Name

import csv
import json

with open("Student_list.csv","r") as js:
    csv1 = csv.reader(js)

    data = []
    for row in csv1:
        data.append({'Roll No': row[0], 'Student Name': row[1], 'Marks': row[2], 'Grade': row[3], 'Result': row[4]})
        print(data)

with open("New_jsn.json","w") as nsj:
    json.dump(data,nsj, indent=4)
