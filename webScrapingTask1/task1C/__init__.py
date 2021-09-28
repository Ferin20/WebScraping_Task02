from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#To configure webdriver to use Chrome browser, we set the path to chromedriver
driver = webdriver.Chrome("C:\\Users\\rincy\\Downloads\\chromedriver_win32\\chromedriver")

#to open the url to linkedin
#driver.get("https://www.linkedin.com/jobs/jobs-in-kurla?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0")
driver.get("https://in.linkedin.com/jobs/view/project-architect-at-a3-cube-architects-2719454202?refId=omAlyaoXlIMtuqQe3B4Jmw%3D%3D&trackingId=Qn3lBcynDrGJOJxDhCxeDw%3D%3D&position=1&pageNum=0&trk=public_jobs_jserp-result_search-card")

#to load the page content 
content = driver.page_source

#to extract data from the html or xml file
soup = BeautifulSoup(content, features="html.parser")

#lists to store the company description, location and job description for the selected company as well as any other desired company
description=[]
location=[]
jobDes=[]

#find the container that contains the required details
b=soup.find('div',attrs={'class':'top-card-layout__entity-info-container'})

#extract the company description within the container
des=b.find('span',attrs={'class':'topcard__flavor'})

#extract the company location within the container
loc=b.find('span',attrs={'class':'topcard__flavor topcard__flavor--bullet'})

#extract the job description from the page
c=soup.find('div',attrs={'class':'show-more-less-html__markup show-more-less-html__markup--clamp-after-5'})

#append the details acquired to the lists created before
#strip them to remove unnecessary spaces or tabs
description.append(des.text.strip())
location.append(loc.text.strip())
jobDes.append(c.text.strip())
subcat="Architect"

#print the extractted contents
print("Description: ",description)
print("Location: ",location)
print("Job Description: ",jobDes)




################### TASK 2 ###############################

import mysql.connector as connector

#connect to the database created as task2
con = connector.connect(host="localhost",user="root",database="WebScrapingT2")

if con.is_connected():
    dbInfo = con.get_server_info()
     
print("connected to db")
cursor = con.cursor()

#put the company details scraped from the site in previos task in CompanyDetails table 
for val in range(0,description.__len__()):
    
    #to extract the state from the locations scraped
    locs=location[val].split(',')
    state=locs[1]
    
    cursor.execute("insert into CompanyDetails values('{}','{}','{}','{}')".format(description[val],jobDes[val],state,subcat))
    con.commit()
    
#to extract the state from the locations scraped
locs=location[0].split(',')
state=locs[1]

#put the value of state of the particular company scraped in previous task into states table
cursor.execute("insert into States value('{}')".format(state))
con.commit()
    
print("done company details")






