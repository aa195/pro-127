from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/Users/Dell/Desktop/pro 12/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    soup = BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table",attrs={'class','wikitable'})   
    table_body = bright_star_table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows :
        cols = row.find_all('td')
        temp_list = []

        for col in cols :
            data = col.text.strip()
            temp_list.append(data)

    scraped_data.append(temp_list)

  

        
# Calling Method    
scrape()
stars_data = []

for i in range (0,len(scraped_data)):
    stars_data.append([scraped_data[i][1],scraped_data[i][3],scraped_data[i][5],scraped_data[i][6],scraped_data[i][7]])

# Define Header
headers = ['Star_name','Distance','Mass','Radius','Luminosity']
df = pd.DataFrame(stars_data,columns=headers)
df.to_csv('scraped_data.csv',index=True,index_label='id')