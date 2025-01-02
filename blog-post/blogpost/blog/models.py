from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200) # for title max length 200
    content = models.TextField() # for content with text field 
    create_date = models.DateField() # for date 
    author = models.ForeignKey( User , on_delete= models.CASCADE , related_name="posts")

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateField()
    blog = models.ForeignKey(BlogPost , on_delete = models.CASCADE , related_name="comments" )
    author = models.ForeignKey(User , on_delete= models.CASCADE , related_name = "comments")

    def __str__(self):
        return f"{self.text} is created at {self.blog}"

class Tag(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    blog_posts = models.ManyToManyField(BlogPost , related_name="tags")

    def __str__(self):
        return self.name