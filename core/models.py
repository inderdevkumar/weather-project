from django.db import models

# Create your models here.

class city(models.Model):
    name= models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='cities'  #To show cities in admin page in place of citys
