from django.db import models
from django.urls import reverse # new

# Create your models here.
class Post(models.Model):
   # blog_image = models.ImageField(upload_to = 'blog/')
   title = models.CharField(max_length=200)
author = models.ForeignKey(
'auth.User',
on_delete=models.CASCADE,
)
body = models.TextField()
def __str__(self):
  return self.title

def get_absolute_url(self): # new
   return reverse('post_detail', args=[str(self.id)])
