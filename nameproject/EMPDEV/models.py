
from django.utils import timezone
from django.db import models


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TypeDevice(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PublicAd(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employe(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200,default='المشتل')
    PublicAd = models.ForeignKey(PublicAd, on_delete=models.CASCADE)
    phone = models.IntegerField()
    empnumber = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    


class TypeRamHard(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type




class RamDevice(models.Model):
     type = models.ForeignKey(TypeRamHard,on_delete=models.CASCADE)
    
     size = models.IntegerField()  
     def __str__(self):
        return f"type: {self.type} - size: {self.size}"
     


class StorgeDevice(models.Model):

    type = models.ForeignKey(TypeRamHard,on_delete=models.CASCADE)
    
    size = models.IntegerField()

    def __str__(self):
        return f"type: {self.type} - size: {self.size}"    


class TypeBreaks(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Device(models.Model):
    serialnumber = models.CharField(max_length=100, unique=True)
    modal = models.CharField(max_length=100)
    rate = models.CharField(max_length=10,default='1')
    cpu = models.CharField(max_length=100,default='Corei7-12th')
    date = models.DateField(null=True)
    TypeDevice = models.ForeignKey(TypeDevice, on_delete=models.CASCADE, default=1)
    RamDevice = models.ForeignKey(RamDevice, on_delete=models.CASCADE, default=1)
    Employe = models.ForeignKey(Employe, on_delete=models.CASCADE, default=1)
    StorgeDevice = models.ForeignKey(StorgeDevice, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.serialnumber

    

class Maintainaces(models.Model):
    stpes =  models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=20,decimal_places=3)
    datein = models.DateField(null=True)
    dateout = models.DateField(null=True)
    TypeBreak = models.ForeignKey(TypeBreaks,on_delete=models.CASCADE)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    def __str__(self):
        return self.stpes


  