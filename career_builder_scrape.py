# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:49:53 2020

@author: aaquib.neyaz
"""

from bs4 import BeautifulSoup
import requests
import csv
import time
from time import sleep
from random import randint
import pandas as pd

columns = ["company_name", "company_img", "job_type", "job_post_date", "job_desc", "job_requirement"]
sample_df = pd.DataFrame(columns = columns)

page = requests.get('https://www.careerbuilder.com/jobs?utf8=%E2%9C%93&keywords=&location=europe')
soup = BeautifulSoup(page.content, "html.parser")

#jobs_details = []

for job in soup.find_all("a",class_='data-results-content block job-listing-item'):
    
    jobs_details = []
#specifying row num for index of job posting in dataframe
    num = (len(sample_df) + 1) 
    
## for company's name    
    try:
        company_name = job.find('div',class_='data-details').text
        
    except Exception as e:
        company_name = None
        
    jobs_details.append(company_name)

## for company's image
    company_img = job.find('img',class_='lazy intl-company-logo')['data-src']
    jobs_details.append(company_img)       
    
## for job type         
    job_type = job.find('div',class_='data-results-title dark-blue-text b').text
    jobs_details.append(job_type)

## for job location    
#    job_location = job.div.div.span.text
#    jobs_details.append(job_location)

## for job post date    
    job_post_date = job.find('div',class_='data-results-publish-time').text
    jobs_details.append(job_post_date)

## detailed description    
    job_url_src = job['href']   
    job_url = job_url_src.split('/')[2]
    job_url = job_url.split('?')[0]
        
    job_url_careerbuilder = f'https://careerbuilder.com/job/{job_url}' 
#    print (job_url_careerbuilder)
    
    source = requests.get(job_url_careerbuilder)
    soup_1 = BeautifulSoup(source.text, "lxml")
    
    u = []
    v = []
    for a in soup_1.find_all('div',class_='col big col-mobile-full'):
        text_tmp = [','.join(b.find_all(text=True))for b in a.find_all('p')]
        u.append(text_tmp)
        
        text1_tmp = [','.join(c.find_all(text=True))for c in a.find_all('li')]
        v.append(text1_tmp)
        
    text = [x for x in u if x != []]
    chain = []
    while text:
        chain.extend(text.pop(0))
    str1 = " "
    job_desc = str1.join(chain) 
    jobs_details.append(job_desc)
    
    text1 = [y for y in v if y != []]
    chain1 = []
    while text1:
        chain1.extend(text1.pop(0))
    str2 = " "
    job_requirement = str2.join(chain1)
    jobs_details.append(job_requirement)
     
#        text_tmp = [','.join(b.find_all(text=True))for b in a.find_all('p')]
#        text = [x for x in text_tmp if x != []]
#        str1 = " "
#        job_desc = str1.join(text)
#        jobs_details.append(job_desc)       

        
#        text1_tmp = [','.join(c.find_all(text=True))for c in a.find_all('li')]
#        text1 = [y for y in text1_tmp if y != []]
#        str2 = " "
#        job_requirement = str2.join(text1)         
#        jobs_details.append(job_requirement)
        
#    for a in soup_1.find_all('div',class_='col big col-mobile-full'):
#        for b in a.find_all('p'):
#            x = []
#            job_desc_tmp = b.get_text().split(',')
            
#            job_desc = ','.join(job_desc_tmp)
            
#            jobs_details.append(job_desc)
#            print (jobs_details)
#        for c in a.find_all('li'):
#            y = []
#            job_requirement_tmp = c.get_text().split(',')
#            job_requirement = '\n'.join(job_requirement_tmp)
#            print (job_requirement)
    sample_df.loc[num] = jobs_details
#    print ("------------------------------------------------")
print(sample_df.to_csv())
