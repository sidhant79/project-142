from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

url = "https://en.wikipedia.org/wiki/Lists_of_stars"
page = requests.get(url)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

table_rows=star_table[7].find_all('tr')

print(len(star_table))

temp_list= []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)


name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

    data = pd.DataFrame(list(zip(name,distance,mass,radius,)),columns=['Name','Distance','Mass','Radius'])
print(data)

data.to_csv('dwarf_stars.csv')

    