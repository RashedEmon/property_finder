from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return str(self.name)


class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(name='description')
    price = models.FloatField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.title)
    class Meta:
        verbose_name_plural = "Properties"


class Label(models.Model):
    title = models.CharField(max_length=100,unique=True)
    

    def __str__(self) -> str:
        return str(self.title)

class Image(models.Model):
    image = models.ImageField(upload_to="img/property/")
    type = models.ForeignKey(Label,on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.image)

