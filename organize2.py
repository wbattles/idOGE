#organize updated circuit IDs for OGE transmission lines
#find the udapted IDs, Names
fhand = input('Enter file: ')
fhand = open(fhand)


#list1: all circuit_ids and line_names
ls = list()

import re
for line in fhand:
    if 'CIRCUIT_ID' in line:
        words = re.split('>|<',line)
        ls.append(words[2])

    if "LINE_NAME" in line:
        words = re.split('>|<', line)
        ls.append(words[2])


#list2: find '66' values, find names next to them
ls2 = list()

for words in ls:
    if words.startswith('66') or words.startswith('066'):
        num = ls.index(words)
        name = num + 1
        ls2.append(words)
        ls2.append(ls[name])
        ls2.append('\n')


#output list2 to file
name = input('Enter txt name: ')
with open(name, 'w') as tx:
    tx.writelines('\t')
    for x in ls2:
        tx.writelines(x)
        tx.writelines('\t')
