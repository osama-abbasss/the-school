from django.shortcuts import render
from django.core.paginator import Paginator

import json
import requests


def all_counties(request):

    try:
        api_json = requests.get("https://api.covid19api.com/summary").json()
        paginator = Paginator(api_json['Countries'], 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except:
        api_json = 'error'
        page_obj = 'error'

    template_name = 'covid_19/all_countries.html'
    context = {
        'page_obj': page_obj,
        'api_json': api_json
    }

    return render(request, template_name, context)


def single_country(request, slug):

    try:
        api_json = requests.get("https://api.covid19api.com/summary").json()
        coutries = api_json['Countries']
        for c in coutries:

            if c['Slug'] == slug:
                the_country = c
                break
            else:
                the_country = 'not founed'

    except:
        the_country = 'not founed'

    template_name = 'covid_19/single_country.html'
    context = {'country': the_country}

    return render(request, template_name, context)
