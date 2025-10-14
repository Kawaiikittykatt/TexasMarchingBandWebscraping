import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome() 
URL = "https://www.texasmusicforms.com/areamarchrptuilpublic.asp"
years = ["14-15", "15-16", "16-17", "17-18", "18-19",
         "19-20", "20-21", "21-22", "22-23"]

with open("RegionalsUpdated.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Conference", "School"])

    for year in years:
        driver.get(URL)
        time.sleep(3)

        Select(driver.find_element(By.NAME, "yr")).select_by_value(year)
        Select(driver.find_element(By.ID, "reg")).select_by_value("ALL")
        time.sleep(4)

        #year_dropdown = Select(driver.find_element(By.NAME, "yr"))
        #year_dropdown.select_by_value(year)
        #time.sleep(2)

        #dropdown name is reg
        #By.ID becayse 

        driver.execute_script("$('.dynamicTable_two').DataTable().page.len(-1).draw();")
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')



        table = soup.find("table", class_ = "dynamicTable_two")
        if not table:
            continue

        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all('td')
            #cols = [ele.get_text(strip=True) for ele in cols]

            if len(cols) == 5:
                school = cols[0].text.strip()
                conference = cols[4].text.strip()
                #temp = []
                temp = year.split("-")
                writer.writerow([temp[1], conference, school])
        
        #tables = driver.find_element(By.TAG_NAME, "table")
        #for table in tables:
            #if "Conference" in table.text and "School" in table.text:
               # rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # skip header
                
                #for row in rows:
                 #   cols = row.find_elements(By.TAG_NAME, "td")
                  #  if len(cols) == 5:
                    #    conference = cols[4].text.strip()
                      #  school = cols[0].text.strip()
                       # writer.writerow([year, conference, school])
              #  break

                
            
print(f"Done! records saved to 'Regionals.csv'")
driver.quit()




