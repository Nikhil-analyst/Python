#Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30 respectively and print out

from pprint import pprint

d = {}

a = []
b= []
c = []

for value in range (1,11):
    a.append(value)
for value in range (11,21):
    b.append(value)
for value in range (21,31):
    c.append(value)

d['a'] = a
d['b'] = b
d['c'] = c

pprint(d)

# Check the one liner code below

# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# pprint(d)