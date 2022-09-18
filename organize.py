#organize updated circuit IDs for OGE transmission lines
#find all IDs, Names
fhand = input('Enter file: ')
fhand = open(fhand)

ls = list()
import re

for line in fhand:
    if 'CIRCUIT_ID' in line:
        words = re.split('>|<', line)
        ls.append(words[2])

    if "LINE_NAME" in line:
        words = re.split('>|<', line)
        ls.append(words[2])
        ls.append('\n')

name = input('Enter txt name: ')
with open(name, 'w') as tx:
    for x in ls:
        tx.writelines(x)
        tx.writelines('\t')
