from django.db import models

# Create your models here.
   
class NseStockQuote(models.Model):
    def __str__(self):
        return "{0}-{1}".format(self.symbol, self.scriptdate)
    
    symbol = models.CharField(max_length=30)
    scriptdate = models.DateTimeField()
    series = models.CharField(max_length=30)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    totaltradeqty = models.FloatField()
    totaltrades = models.FloatField()
    isin = models.CharField(max_length=30)
    last = models.FloatField()
    prevclose = models.FloatField()
    totaltradevalue = models.FloatField()
