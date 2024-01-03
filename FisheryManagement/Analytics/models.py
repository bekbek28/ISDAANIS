from django.db import models

class Species(models.Model):
    species_name = models.CharField(max_length=30)
    quantity = models.IntegerField()

    def __str__(self):
        return self.species_name

class Province(models.Model):
    ProvinceName = models.CharField(max_length=30)

class City(models.Model):
    CityName = models.CharField(max_length=30)
    Province = models.ForeignKey(Province,on_delete=models.CASCADE)

class unloadType(models.Model):
    unloadTypeName = models.CharField(max_length=30)


class Origin(models.Model):
    origin = models.CharField(max_length=30)
    date = models.DateTimeField()
    City = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return self.origin
    

class Vessel(models.Model):
    vessel_name = models.CharField(max_length=30)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    unloadType = models.ForeignKey(unloadType,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.vessel_name

class DailyTransaction(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, null=True)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    percentage = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    date = models.DateField()
    unloadType = models.ForeignKey(unloadType,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.species}'



    


