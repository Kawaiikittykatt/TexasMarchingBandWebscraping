import requests
from bs4 import BeautifulSoup
import csv

#HTTP request to fetch the webpage
URL = 'https://smbc.uiltexas.org/archives.htm'
r = requests.get(URL)

#r.content is raw html content, 'html.parser' specifies html parser
soup = BeautifulSoup(r.content, 'html.parser')

#extracts text from HTML, seperates with new lines
#text = soup.get_text(seperator='\n')

data = []

#finds all <tr> elements, used in html tables....you wouldn't know (never use them)
#<table> <tr> <td> ___ </td> <td> -- </td> </tr> </table>
# table row --- tr
# table data ---- td
rows = soup.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.get_text(strip=True) for ele in cols]

    if len(cols) >= 5 and 'prelims' in cols[2].lower()and int(cols[0])>2014:
        year = cols[0]
        conference = cols[1]
        school = cols[4]
        data.append((year, conference, school))


with open('AreaUpdated.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Year', 'Conference', 'School'])
    writer.writerows(data)

print(f"Saved {len(data)} rows to 'Area.csv'")
