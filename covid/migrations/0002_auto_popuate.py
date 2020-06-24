
import csv
import os
from django.db import migrations
from django.conf import settings
from django.db import transaction

DATE = 0
COUNTRY = 1
CONFIRMED = 2
RECOVERED = 3
DEATHS = 4

@transaction.atomic
def country_add(apps, schema_editor):
    counties_covid = apps.get_model('covid', 'countries_covid')
    csv_file = os.path.join(settings.BASE_DIR, 'countries-covid.csv')
    with open(csv_file) as dataset:
        reader = csv.reader(dataset)
        next(reader)
        for entry in reader:
            counties_covid.objects.create(
                date=entry[DATE],
                country=entry[COUNTRY],
                confirmed=int(entry[CONFIRMED]),
                recovered=int(entry[RECOVERED]),
                deaths=int(entry[DEATHS]),
            )

class Migration(migrations.Migration):
    dependencies = [
        ('covid', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(country_add),
    ]