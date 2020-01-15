from django.db import models
import datetime

def year_choices(current):
    return [(year, year) for year in range(current, 1920, -1)]

# Create your models here.
class Bottle(models.Model):
    current_year = datetime.date.today().year
    YEAR_CHOICES = year_choices(current_year)
    CAB = 'Cabernet Sauvignon'
    CHA = 'Chardonnay'
    MAL = 'Malbec'
    MER = 'Merlot'
    GRI = 'Pinot Gris'
    PIN = 'Pinot Noir'
    RIE = 'Riesling'
    SAV = 'Sauvingnon Blanc'
    SHI = 'Shiraz/Syrah'
    ZIN = 'Zinfandel'
    GRAPE_CHOICES = [
        (CAB, 'Cabernet Sauvignon'),
        (CHA, 'Chardonnay'),
        (MAL, 'Malbec'),
        (MER, 'Merlot'),
        (GRI, 'Pinot Gris'),
        (PIN, 'Pinot Noir'),
        (RIE, 'Riesling'),
        (SAV, 'Sauvingnon Blanc'),
        (SHI, 'Shiraz/Syrah'),
        (ZIN, 'Zinfandel'),
    ]
    User = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Winery = models.CharField(max_length=128)
    Grape = models.CharField(choices=GRAPE_CHOICES, default=CAB, max_length=20)
    Year = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
    Description = models.TextField()
    Image = models.ImageField(upload_to='static/img', blank=True)

    def __str__(self):
        return self.Winery