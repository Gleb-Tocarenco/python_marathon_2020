import csv
import json
import urllib.request
import requests
from bs4 import BeautifulSoup

url = 'https://www.rabota.md/ru/jobs-chisinau-Python'

# with urllib.request.urlopen(url) as r:
#     f = open('text.html', 'w')
#     f.write(r.read().decode('utf-8'))
#     f.close()

page = requests.get(url)
content = page.content.decode('utf-8')
# print(content)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main')
# print(results.prettify())
jobs = results.find_all('div', class_='preview')
print(len(jobs))

data = []

for job in jobs:
    title = job.find('h3').find('a', class_='vacancy').text.strip()
    company_data = job.find('div', class_='vacancy-meta').text
    company_data = company_data.replace('\n', '').split('•')
    print(company_data)
    salary, location = company_data[-3], company_data[-2]

    try:
        company_name = company_data[-4]
    except IndexError:
        company_name = ''

    data.append({
        'title': title,
        'company_name': company_name.strip(),
        'salary': salary.strip(),
        'location': location.strip()
    })


with open('jobs.csv', 'w') as f:
    keys = data[0].keys()
    dict_writer = csv.DictWriter(f, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)


with open('jobs.json', 'w', ensure_ascii=True) as json_file:
    json.dump(data, json_file)