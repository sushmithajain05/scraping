import requests
from bs4 import BeautifulSoup
from .models import Company
 #companies scraping logic
def scrape_companies():
    #URL and Request
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
    response = requests.get(url)
    #Parsing the HTML Content
    soup = BeautifulSoup(response.content, 'html.parser')
   
    #Finding the Table
    table = soup.find('table', {'class': 'wikitable sortable'})
    #Extracting Table Rows
    rows = table.find_all('tr')[1:]  
    #Clearing Existing Records
    Company.objects.all().delete()  
    #Looping Through Rows and Extracting Data
    for row in rows:
        cols = row.find_all('td')
        rank = int(cols[0].text.strip())
        name = cols[1].text.strip()
        revenue = cols[2].text.strip()
        employees = cols[3].text.strip()
        industry = cols[4].text.strip()
        #Saving Data to the Database
        Company.objects.create(
            rank=rank,
            name=name,
            revenue=revenue,
            employees=employees,
            industry=industry
        )
