from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class ArticleModel(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    content=RichTextField()
    created_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=["-created_date"]   


class Article(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    image_link=models.CharField(max_length=1000)
    content=RichTextField()
    created_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-created_date']    

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="article",related_name="comments")
    comment_author=models.CharField(max_length = 50 ,verbose_name="name")
    comment_content=models.CharField(max_length = 50 ,verbose_name="comment")
    comment_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta :
        ordering=  ['-comment_date']

    

 





