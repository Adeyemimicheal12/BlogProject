from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name
    
    
class BlogPost(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,related_name='caterory_blogs')
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,related_name='user_posts')
    title = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    
    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields = ["-created"]),
        ]
    
    def __str__(self):
        return self.title
    
    