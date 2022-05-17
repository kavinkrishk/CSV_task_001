import xml.etree.ElementTree as ET
import os
x = os.getcwd()
print(x)
root = ET.parse("D:\KAVIN\IT\Projects\Pycharm_Projects\Task_1\T1\Food_Menu.xml")
print(root)
print(dir(root))
root_node = root.getroot()
print(root_node)
print(root_node.attrib)
print(root_node[2][2].text)
print(root_node[3][0].text)
print(root_node[4][3].text)
print(root_node[4].attrib)
