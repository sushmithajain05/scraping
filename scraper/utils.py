import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Company,City

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

def scrape_latlong():
    url = 'https://www.latlong.net/category/cities-102-15.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'wide'})
        cities_data = []

        if table:
            rows = table.find_all('tr')
            for row in rows[1:]:  # Skipping the header row
                columns = row.find_all('td')
                if len(columns) >= 4:
                    city = columns[0].get_text(strip=True)
                    country = columns[1].get_text(strip=True)
                    lat = columns[2].get_text(strip=True)
                    lng = columns[3].get_text(strip=True)

                    cities_data.append({
                        'city': city,
                        'country': country,
                        'latitude': lat,
                        'longitude': lng,
                    })
        return cities_data
    else:
        return None