from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#To configure webdriver to use Chrome browser, we set the path to chromedriver
driver = webdriver.Chrome("C:\\Users\\rincy\\Downloads\\chromedriver_win32\\chromedriver")

#to open the url to linkedin
#driver.get("https://www.linkedin.com/jobs/jobs-in-kurla?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0")
driver.get("https://www.linkedin.com/jobs/search?keywords=Architect&location=Kurla%2C%20Maharashtra%2C%20India&geoId=104418992&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

#to load the page content 
content = driver.page_source

#to extract data from the html or xml file
soup = BeautifulSoup(content, features="html.parser")

position=[]
company=[]
location=[]

b=soup.find('section',attrs={'class':'two-pane-serp-page__results-list'})
#for a in soup.findAll('a',href=True, attrs={'class':'base-card__full-link'}):
#for a in soup.findAll('div', attrs={'class':'base-card base-card--link base-search-card base-search-card--link job-search-card job-search-card--active'}):
for a in b.findAll('div',attrs={'class':'base-search-card__info'}):
       pos = a.find('h3',attrs={'class':'base-search-card__title'})
       
       com = a.find('h4',attrs={'class':'base-search-card__subtitle'})
       loc = a.find('span', attrs={'class':'job-search-card__location'})
   
       position.append(pos.text.strip())
       company.append(com.text.strip())
       location.append(loc.text.strip())
       
           
print("\nposition: ",position)
print("\ncompany: ",company)
print("\nlocation: ",location)

df=pd.DataFrame({'Position':position,'Company':company,'Location':location})
df.to_csv('jobs.csv', index=False, encoding='utf-8')





################### TASK 2 ###############################


import mysql.connector as connector

#connect to the database created as WebScrapingT2
con = connector.connect(host="localhost",user="root",database="WebScrapingT2")

#ensure connection
if con.is_connected():
    dbInfo = con.get_server_info()     
print("connected to db")

#create an object of type cursor to execute queries
cursor = con.cursor()

#insert the company details scraped from the site in previous task into Jobs table
for val in range(0,position.__len__()):
    cursor.execute("insert into Jobs values('{}','{}','{}')".format(company[val],position[val],location[val]))
    con.commit()
    
print("done jobs")

