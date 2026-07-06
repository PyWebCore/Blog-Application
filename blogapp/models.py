from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cat_name=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=200)
    content=models.TextField()

    def __str__(self):
        return self.title 
    

class Comment(models.Model):
    blog_comment=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()

    def __str__(self):
        return self.comment
    

class Reply(models.Model):
    comt_reply=models.ForeignKey(Comment, on_delete=models.CASCADE,related_name="replies")
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    reply=models.TextField()

    def __str__(self):
        return self.reply
    
