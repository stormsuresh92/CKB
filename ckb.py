from requests_html import HTMLSession
import pandas as pd

s = HTMLSession()

datalist = []
url = 'https://ckb.jax.org/gene/grid'
baseurl = 'https://ckb.jax.org'
r = s.get(url)
#tags = r.html.find('div.col-sm-12')
rowtags = r.html.find('body > div > div > div > div > div > a')
for tag in rowtags:
  gene = tag.find('a', first=True).text
  links = baseurl + tag.find('a', first=True).attrs['href']
  ID = tag.find('a', first=True).attrs['href'].split('=')[-1]
  dic = {
    'gene':gene,
    'ID':ID,
    'links':links
    
  }
  datalist.append(dic)

df = pd.DataFrame(datalist)
df.to_csv('output4.csv', index=False)
print('fin')