from django.db import models


class countries_covid(models.Model):

    KOREA= 'K'
    CHINA = 'C'
    UK = 'UK'
    US = 'US'
    FRANCE = 'F'
    PORT_CHOICES = (
        (KOREA, 'Korea, South'),
        (CHINA, 'China'),
        (UK, 'United Kingdom'),
        (US, 'US'),
        (FRANCE, 'France'),
    )

    date= models.DateField()
    country=models.CharField(max_length=100,choices=PORT_CHOICES)
    confirmed=models.FloatField()
    recovered=models.FloatField()
    deaths=models.FloatField()

    def __str__(self):
        return self.country
