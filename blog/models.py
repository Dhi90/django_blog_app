from django.db import models
from django.utils.text import slugify


class categories(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self) :
        return self.name



# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(null=True)
    img_url=models.URLField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=100,unique=True)
    category=models.ForeignKey(categories,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):    
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)
        
    
    def __str__(self) :
        return self.title
    
class AboutUs(models.Model):
    content = models.TextField()
    
