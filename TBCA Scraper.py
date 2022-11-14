#TBCA-USP Scraper for database

import requests
from bs4 import BeautifulSoup
import csv

url_main = "http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina="
foods = []

#Gets all the links from the food pages

for pages in range(1,70,1):
    page = requests.get(url_main+str(pages))
    soup = BeautifulSoup(page.content, "html.parser")
    for tr in soup.findAll('tr')[1:]:
        foods.append(str(tr.find('a'))[9:-12])
        #(str(soup.findAll('td')[1].text),str(soup.findAll('td')[4].text), [name and food group]
    print("Got page {}...".format(pages))

# with open('output.csv', 'w', newline='') as out_file:
#     for food in foods:
#         spamwriter = csv.writer(out_file, quotechar='|', quoting=csv.QUOTE_NONE)
#         spamwriter.writerow([food])

#-----------------------------------------------

#Gets the data we want from the pages

url_foods = "http://www.tbca.net.br/base-dados/" #**
table_row_data = []
header = []
data = []

with open('foods.csv','w', newline='') as file:
    writer = csv.writer(file)

#Get data from the table
    for link in foods:
        page = requests.get(url_foods+str(link))
        soup = BeautifulSoup(page.content, "html.parser")

        header.append(soup.find('h5'))
        for h in soup.findAll('th'):
            header.append(h.text)
        writer.writerow([header])
        header=[]

        for tr in soup.findAll('tr')[1:]:
            for td in tr.findAll('td'):
                table_row_data.append(td.text)
            writer.writerow([table_row_data])
            table_row_data=[]
        print(("Done {}").format(soup.find('h5').text))
