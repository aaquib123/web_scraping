# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 03:06:21 2020

@author: aaquib.neyaz
"""

from bs4 import BeautifulSoup
import requests
import csv

## array of URLs from where the data needs to be fetched
urls = ['https://www.linkedin.com/jobs/search?location=Bengaluru%2C%20Karnataka&redirect=false&position=1&pageNum=0']


##for pg in urls:
page = requests.get('https://www.linkedin.com/jobs/search?location=Bengaluru%2C%20Karnataka&redirect=false&position=1&pageNum=0')
soup = BeautifulSoup(page.content, "html.parser")
 
urls = []   
for job in soup.find_all("li",class_='result-card job-result-card result-card--with-hover-state'):
    
## for company's name    
    try:
        company_name = job.div.h4.a.text
    except Exception as e:
        company_name = None
        
    print (company_name)

## for company's image
    company_img = job.find('img')['src']
    print (company_img)    
    
    
## for job type         
    job_type = job.div.h3.text
    print (job_type)

## for job location    
    job_location = job.div.div.span.text
    print (job_location)

## for job post date    
    job_post_date = job.div.div.time.text
    print (job_post_date)
    
    job_url_src = job.find('a',class_='result-card__full-card-link')['href']   
    job_url = job_url_src.split('/')[5]
    job_url = job_url.split('?')[0]
    
    job_url_linkedin = f'https://in.linkedin.com/jobs/view/{job_url}' 
#    print (job_url_linkedin)
    
    source = requests.get(job_url_linkedin)
    soup_1 = BeautifulSoup(source.content, "html.parser")
        
    try:   
        desc = soup_1.find('div',class_='description__text description__text--rich').text
        print (desc)
    except Exception as e:
        desc = None
    
##    urls.append(job_url_linkedin)
    
      
    print ()
    print ()
##print(urls)