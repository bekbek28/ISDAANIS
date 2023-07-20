from django.db import models

class Species(models.Model):
    species_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.species_name

class Origin(models.Model):
    origin = models.CharField(max_length=30)
    date = models.DateTimeField()
    class Meta:
        unique_together = ('origin', 'date')

    def __str__(self):
        return self.origin
    
    
class Vessel(models.Model):
    vessel_name = models.CharField(max_length=30)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)

    def __str__(self):
        return self.vessel_name

class DailyTransaction(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, null=True)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.species}'
