from django.db import models

# Create your models here.



# Many_to_many
V_nm=[('Tata','Tata'),('Bmw','Bmw'),('Audi','Audi')]
F_nm=[('Petro','Petrol'),('Desail','Desail'),('Cng','Cng')]


class Vehical(models.Model):
    V_name=models.CharField(max_length=50,choices=V_nm)
    def __str__(self):
        return self.V_name


class Fuel(models.Model):
    V_fuel=models.CharField(max_length=50,choices=F_nm)
    V_name=models.ManyToManyField(Vehical)    
    def __str__(self):
      return self.V_fuel
