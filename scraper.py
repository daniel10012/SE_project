import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='SearchResults')



job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    try:
        # print(title_elem.text.strip())
        # print(company_elem.text.strip())
        # print(location_elem.text.strip())
        print()
    except AttributeError:
        pass

python_jobs = results.find_all('h2',
                               string=lambda text: 'java' in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")


#(ref https://github.com/realpython/materials/blob/master/web-scraping-bs4/job_search.py)
#check streeteasy next