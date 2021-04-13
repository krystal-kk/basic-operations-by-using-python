import csv

output=open('xyz.txt','w')

with open('abc.csv',"rt", encoding='ascii') as f:
  for row in f:
    output.write(row)
