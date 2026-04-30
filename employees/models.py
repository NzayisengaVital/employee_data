from django.db import models

# Create your models here.
class Abakozi(models.Model):
   
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    akazi = models.CharField(max_length=100)
    arakora = models.BooleanField(default=True)
    itariki = models.DateTimeField()

    def __str__(self):
        return f" {self.first_name} {self.last_name}"

class Umushahara(models.Model):
    
    umukozi = models.ForeignKey(Abakozi, on_delete=models.CASCADE)
    umushahara = models.IntegerField()
    igihe = models.DateField()
    

    def __str__(self):
        return f" {self.umukozi.first_name}: {self.umushahara} {self.igihe}"