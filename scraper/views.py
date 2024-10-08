from django.shortcuts import render
from django.http import HttpResponse
from .models import Company
from .utils import scrape_companies,scrape_latlong
#example

def scrape1(request):
    scrape_companies()
    return HttpResponse("Scraping completed and data saved.")

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'scraper/company_list.html', {'companies': companies})


def scrape_view(request):
    data = scrape_latlong()
    return render(request, 'scraper/city_list.html', {'data': data})