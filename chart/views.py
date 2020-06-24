from django.shortcuts import render
from .models import Passenger
from django.db.models import Count, Q, FloatField
import json

def home(request):
    return render(request, 'list.html')

def titanic(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False)),
                  survived_rate=
                                (1.0 * Count('id', filter=Q(survived=True), output_field=FloatField()))
                                / (1.0 * Count('id', output_field=FloatField())) * 100.0,) \
        .order_by('ticket_class')

    categories = list()
    survived_series_data = list()
    not_survived_series_data = list()
    survived_rate=list()

    for entry in dataset:
        categories.append('%s Class' % entry['ticket_class'])
        survived_series_data.append(entry['survived_count'])
        not_survived_series_data.append(entry['not_survived_count'])
        survived_rate.append(entry['survived_rate'])


    return render(request, 'chart/titanic.html', {
        'categories': json.dumps(categories),
        'survived_series_data': json.dumps(survived_series_data),
        'not_survived_series_data': json.dumps(not_survived_series_data),
        'survived_rate':json.dumps(survived_rate)
    })




