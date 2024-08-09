from django.urls import path
from . import views

urlpatterns = [
    
    #for companies
    path('scrape1/', views.scrape1, name='scrape1'),
    path('companies/', views.company_list, name='company_list'),
    path('scrape/', views.scrape_view, name='scrape'),
]
