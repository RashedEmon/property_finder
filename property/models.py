from django.db import models

# Create your models here.

class Location(models.Model):
    name= models.CharField(max_length=500)

    def __str__(self) -> str:
        return str(self.name)

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(name='description')
    price = models.FloatField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.title)


class Image(models.Model):
    CHOICES = [
        ('br', 'Bedroom'),
        ('lr', 'Living room')
    ]
    image=models.ImageField(upload_to = "img/property/")
    type = models.CharField(max_length=50, choices=CHOICES)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.type)