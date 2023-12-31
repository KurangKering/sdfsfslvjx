from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.

class Airports(models.Model):
    airport = models.TextField(primary_key=True)
    airport_name = models.TextField(null=True, blank=True)

    objects = DataFrameManager()

    class Meta:
        db_table = "airports"
    
    def __str__(self):
        return '{}, {}'.format(self.airport, self.airport_name)
    
    
class Carriers(models.Model):
    carrier = models.TextField(primary_key=True)
    carrier_name = models.TextField(null=True, blank=True)

    objects = DataFrameManager()

    class Meta:
        db_table = "carriers"
    
    def __str__(self):
        return '{}'.format(self.carrier)
    
class DatasetRaw(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    carrier = models.ForeignKey(Carriers, on_delete=models.CASCADE, blank=True, null=True, db_column='carrier')
    airport = models.ForeignKey(Airports, on_delete=models.CASCADE, null=True, blank=True, db_column='airport')
    arr_flights = models.FloatField(null=True, blank=True)
    arr_del15 = models.FloatField(null=True, blank=True)
    carrier_ct = models.FloatField(null=True, blank=True)
    weather_ct = models.FloatField(null=True, blank=True)
    nas_ct = models.FloatField(null=True, blank=True)
    security_ct = models.FloatField(null=True, blank=True)
    late_aircraft_ct = models.FloatField(null=True, blank=True)
    arr_cancelled = models.FloatField(null=True, blank=True)
    arr_diverted = models.FloatField(null=True, blank=True)
    arr_delay = models.FloatField(null=True, blank=True)
    carrier_delay = models.FloatField(null=True, blank=True)
    weather_delay = models.FloatField(null=True, blank=True)
    nas_delay = models.FloatField(null=True, blank=True)
    security_delay = models.FloatField(null=True, blank=True)
    late_aircraft_delay = models.FloatField(null=True, blank=True)
    
    objects = DataFrameManager()

    class Meta:
        db_table = "dataset_raw"
    
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.year, self.month, self.carrier.carrier, self.airport.airport)
    
    
class DatasetNull(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    carrier = models.TextField(null=True, blank=True)
    airport = models.TextField(null=True, blank=True)
    arr_flights = models.FloatField(null=True, blank=True)
    arr_del15 = models.FloatField(null=True, blank=True)
    carrier_ct = models.FloatField(null=True, blank=True)
    weather_ct = models.FloatField(null=True, blank=True)
    nas_ct = models.FloatField(null=True, blank=True)
    security_ct = models.FloatField(null=True, blank=True)
    late_aircraft_ct = models.FloatField(null=True, blank=True)
    arr_cancelled = models.FloatField(null=True, blank=True)
    arr_diverted = models.FloatField(null=True, blank=True)
    arr_delay = models.FloatField(null=True, blank=True)
    carrier_delay = models.FloatField(null=True, blank=True)
    weather_delay = models.FloatField(null=True, blank=True)
    nas_delay = models.FloatField(null=True, blank=True)
    security_delay = models.FloatField(null=True, blank=True)
    late_aircraft_delay = models.FloatField(null=True, blank=True)
    
    objects = DataFrameManager()

    class Meta:
        db_table = "dataset_null"
    
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.year, self.month, self.carrier, self.airport)
    
    
class DatasetClean(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    carrier = models.ForeignKey(Carriers, on_delete=models.CASCADE, blank=True, null=True, db_column='carrier')
    airport = models.ForeignKey(Airports, on_delete=models.CASCADE, null=True, blank=True, db_column='airport')
    arr_flights = models.FloatField(null=True, blank=True)
    arr_del15 = models.FloatField(null=True, blank=True)
    carrier_ct = models.FloatField(null=True, blank=True)
    weather_ct = models.FloatField(null=True, blank=True)
    nas_ct = models.FloatField(null=True, blank=True)
    security_ct = models.FloatField(null=True, blank=True)
    late_aircraft_ct = models.FloatField(null=True, blank=True)
    arr_cancelled = models.FloatField(null=True, blank=True)
    arr_diverted = models.FloatField(null=True, blank=True)
    arr_delay = models.FloatField(null=True, blank=True)
    carrier_delay = models.FloatField(null=True, blank=True)
    weather_delay = models.FloatField(null=True, blank=True)
    nas_delay = models.FloatField(null=True, blank=True)
    security_delay = models.FloatField(null=True, blank=True)
    late_aircraft_delay = models.FloatField(null=True, blank=True)
    
    objects = DataFrameManager()

    class Meta:
        db_table = "dataset_clean"
    
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.year, self.month, self.carrier.carrier_name, self.airport.airport_name)
    