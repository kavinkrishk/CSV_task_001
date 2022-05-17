import xml.etree.ElementTree as ET
college_tag = ET.Element("college")
rollno_tag = ET.SubElement(college_tag, "Rollno")
rollno_tag.text = "731714114035"
name_tag = ET.SubElement(college_tag, "Name")
name_tag.text = "KAVINKK"
Dept_tag = ET.SubElement(college_tag, "Department")
Dept_tag.text = "Mechanical"
clas_tag = ET.SubElement(college_tag, "Class")
clas_tag.text = "A"
Place_tag = ET.SubElement(college_tag, "Place")
Place_tag.text = "Erode"
pin_tag = ET.SubElement(college_tag, "Pincode")
pin_tag.text = "638009"

print(college_tag)
Result = ET.tostring(college_tag)
print(Result)