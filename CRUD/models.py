from django.db import models

class Employee (models.Model):
    ename= models.CharField( max_length=100)
    eemail =models.EmailField( max_length=254)
    econtact = models.CharField(max_length=50)
    

    class Meta:
        verbose_name =("Employee")
        verbose_name_plural =("Employees")

    def __str__(self):
        return self.ename

    

