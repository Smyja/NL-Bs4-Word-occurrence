import pandas as pd
import requests 
from bs4 import BeautifulSoup as bs
z = []
y=  []
for i in range(18):
    r = requests.get('https://www.nairaland.com/search/afonja/0/0/0/{}'.format(i))
    soup = bs(r.content, 'lxml')
    occurrences = len(soup.select('.highlight'))
    z.append(occurrences)
for w in range(18):
    r = requests.get('https://www.nairaland.com/search/pigs/0/0/0/{}'.format(w))
    soup = bs(r.content, 'lxml')
    occurrence = len(soup.select('.highlight'))
 
    y.append(occurrence)
df = pd.DataFrame(list(zip(*[z,y])))
df.columns =['Afonja', 'pigs'] 

df.to_csv('fitle.csv', index=False)

print(df)