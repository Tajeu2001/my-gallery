from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()    

class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save() 
        
class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/', blank=True, null=True)
    name = models.CharField(max_length =60)
    description = models.CharField(max_length =200)
    location = models.ForeignKey(Location,on_delete=models.PROTECT)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()       

    def delete_image(self):
        self.delete()
    
#     @classmethod
#     def update_image(cls, id, value):
#         cls.objects.filter(id=id).update(image=value)

#     @classmethod
#     def search_by_category(cls, category):
#         images = cls.objects.filter(category__name__icontains=category)
#         return images    

