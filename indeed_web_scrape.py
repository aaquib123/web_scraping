# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup 
import requests

page = requests.get('https://www.indeed.fr/Paris-Emplois').text
soup = BeautifulSoup(page, "lxml")

##for jobs in soup.find_all('div',class_='jobsearch-SerpJobCard unifiedRow row result clickcard'):

##detail = soup.find('td',attrs={"id":"resultsCol"})    

for job_detail in soup.find_all('div',class_='jobsearch-SerpJobCard unifiedRow row result'):
    
        
    try:
        company_name = job_detail.find('span',class_='company').text
    except Exception as e:
        company_name = None
        
    print (company_name)
    
    job_type = job_detail.h2.text
    print (job_type)
    
    job_location = job_detail.find('span',class_='location accessible-contrast-color-location').text
    print(job_location)
    
    job_desc = job_detail.find('div',class_='summary').text
    print(job_desc)
    
    job_url_src = job_detail.h2.a['href']
    job_url = job_url_src.split('/')[2]
    job_url = job_url.split('?')[1]
    job_url_indeed = f'https://www.indeed.fr/viewjob?{job_url}'
    print(job_url_indeed)
    
    source = requests.get(job_url_indeed)
    soup_1 = BeautifulSoup(source.content, "html.parser")
    
    try:   
        desc = soup_1.find('div',class_='jobsearch-DesktopStickyContainer').text
        print (desc)
    except Exception as e:
        desc = None
    
    

print ()
print ()
##    try:
##        company_name = jobs.h2.a.text
##    except Exception as e:
##        company_name = None
    
##    print(company_name)


##    try:   
##        desc = soup.find('div',class_='description__text description__text--rich').text
##        print (desc)
##        print ()
##    except Exception as e:
##        desc = None
    
##    data.append(desc)
##print(desc)

##print(soup.prettify())