from unicodedata import category
from django.db import models
from soupsieve import select_one

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50,null=False,blank=False)

    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category
         
    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length=50,null=False,blank=False)
    
    @classmethod
    def get_location_id(cls, id):
        location = Location.objects.get(pk = id)
        return location

    def __str__(self):
        return self.location_name

class Image(models.Model):
    image = models.ImageField(null=False,blank=False)
    image_name= models.CharField(max_length=100,null=False,blank=False)
    image_description= models.TextField()
    image_category= models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    image_location= models.ForeignKey('Location',on_delete=models.CASCADE,null=True,blank=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_image_id(cls, id):
        image = Image.objects.get(pk = id)
        return image

    @classmethod
    def search_by_category(cls,image_category):
        images = Image.objects.filter(image_category__category_name__icontains=image_category)
        return images

    @classmethod
    def search_by_location(cls,image_location):
        images = Image.objects.filter(image_location__location_name__icontains=image_location)
        return images

    def __str__(self):
        return self.image_description

        
