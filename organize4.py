
#API, sort xml data
import xml.etree.ElementTree as ET


xml = 'OGE-TransmissionLines-20220427.kml'
tree = ET.fromstring(xml)

#search structure for groups
# 'comments' is only 1 catagory above
cmts = tree.findall('Placemark/ExendedData')

#search groups for tags
lst = list()
for tags in cmts:
    nums = tags.find('SimpleData name="CIRCUIT_ID"').text
    lst.append(int(nums))

print(lst)
