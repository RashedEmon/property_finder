from django.contrib import admin



from .models import Image,Location,Property
# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image','type','property')
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title','description','price','location')
    



