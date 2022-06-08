from django.db import models
from django.forms import CharField
from sqlalchemy import ForeignKey
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


#let the article have author, date, title, body, image, 


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add= True)
    last_modified = models.DateTimeField(auto_now= True)
    body = models.TextField(default= 'This fellers tongue has failed', editable= True, 
    verbose_name= 'Article Bodies', unique= True )

    def __str__(self):
        return (self.title)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    related_name = 'comments'


    def __str__(self):
        return (self.comment) 

    def get_absolute_url(self):
        return reverse('ArticleListView')
       



