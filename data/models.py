from django.db import models

# Create your models here.


class UDI(models.Model):
    """
    modelo para datos UDI
    """
    udi = models.FloatField()
    udi_date = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.udi_date)


class PesoDolar(models.Model):
    """
    modelo para datos del precio peso-dolar
    """
    peso_dolar = models.FloatField()
    peso_dolar_date = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.peso_dolar_date)


class TIE(models.Model):
    """
    modelo para datos tie
    """
    tie = models.FloatField()
    tie_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return str(self.tie_date)


    
    

   


   