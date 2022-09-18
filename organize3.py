from pickletools import stackslice
from bs4 import BeautifulSoup

#OGE-TransmissionLines-20220427.kml

file = input('Enter file: ')
fhand = open(file)

soup = BeautifulSoup(fhand, 'xml')

line = soup.findAll('Placemark/ExtendedData')


ls = list()

for values in line:
    names = values.get('SimpleData').text
    ls.append(names)


name = input('Enter txt name: ')
st = str(ls)
with open(name, 'w') as tx:
    tx.write(st)
