import pandas as pd
import os
 
 
data = pd.read_csv('/home/jaran/Documents/ISIC2017/Reocrd/Train.csv', encoding='utf-8')
with open('/home/jaran/Documents/ISIC2017/Reocrd/Train1.txt','a+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[0])+' '+str(line[1])+'\n'))

        
# the first row may miss
