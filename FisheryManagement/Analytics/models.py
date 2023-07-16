from django.db import models


class Species(models.Model):
    species_id = models.CharField(max_length=30, primary_key=True)
    species_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()


class Origin(models.Model):
    origin = models.CharField(max_length=30, primary_key=True)
    date = models.DateTimeField()


class Vessel(models.Model):
    vessel_id = models.CharField(max_length=30,)
    vessel_name = models.CharField(max_length=30)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)




class DailyTransaction(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField()
