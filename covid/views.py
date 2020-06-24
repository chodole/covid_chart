import arrow as arrow
from django.shortcuts import render
from .models import countries_covid
from django.db.models import Count, Q, FloatField, Sum
import json
from datetime import timedelta

def covid(request):
    dataset = countries_covid.objects \
        .values('date') \
        .annotate(Korea=(Sum('confirmed',filter=Q(country='Korea, South'))/51269185*1000000),
                  China=(Sum('confirmed', filter=Q(country='China'))/1439323776*1000000),
                  UK=(Sum('confirmed', filter=Q(country='United Kingdom'))/67886011*1000000),
                  US=(Sum('confirmed', filter=Q(country='US'))/331002651*1000000),
                  France=(Sum('confirmed', filter=Q(country='France'))/65273511*1000000),
                  )\
        .order_by('date') \


    categories = list()
    korea=list()
    china = list()
    uk = list()
    us = list()
    france = list()

    for entry in dataset:
        categories.append('%s' % entry['date'])
        korea.append(entry['Korea'])
        china.append(entry['China'])
        uk.append(entry['UK'])
        us.append(entry['US'])
        france.append(entry['France'])


    return render(request, 'covid/covid.html', {
        'categories': json.dumps(categories),
        'korea': json.dumps(korea),
        'china': json.dumps(china),
        'uk': json.dumps(uk),
        'us': json.dumps(us),
        'france': json.dumps(france),
    })

def covid_2(request):

    dataset2 = countries_covid.objects \
        .values('date') \
        .annotate(Korea=(Sum('confirmed',filter=Q(country='Korea, South'))),
                  China=(Sum('confirmed', filter=Q(country='China'))),
                  UK=(Sum('confirmed', filter=Q(country='United Kingdom'))),
                  US=(Sum('confirmed', filter=Q(country='US'))),
                  France=(Sum('confirmed', filter=Q(country='France'))),
                  )\
        .order_by('date')\


    categories = list()
    korea=list()
    china = list()
    uk = list()
    us = list()
    france = list()

    for entry in dataset2:
        categories.append('%s' % entry['date'])
        korea.append(entry['Korea'])
        china.append(entry['China'])
        uk.append(entry['UK'])
        us.append(entry['US'])
        france.append(entry['France'])


    return render(request, 'covid/covid2.html', {
        'categories': json.dumps(categories),
        'korea': json.dumps(korea),
        'china': json.dumps(china),
        'uk': json.dumps(uk),
        'us': json.dumps(us),
        'france': json.dumps(france),
    })
