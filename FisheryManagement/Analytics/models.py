from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    

class Species(models.Model):
    species_name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='species')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.species_name


class unloadType(models.Model):
    unloadTypeName = models.CharField(max_length=30)


class Origin(models.Model):
    origin = models.CharField(max_length=30)

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
    date = models.DateField()
    unloadType = models.ForeignKey(unloadType,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f'{self.species}'