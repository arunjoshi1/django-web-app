from django.db import models
from django.contrib.auth.models import  User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=30,blank=False)
    body=models.TextField(blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='featured',default='default.jpg',blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def slice_body(self):
        return (self.body[:250]+'....')
