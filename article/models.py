from django.db import models
from ckeditor.fields import RichTextField
from django import forms
# Create your models here.


class Article(models.Model):
   
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = models.CharField(verbose_name="Yorumunuz.. (En fazla 1000 karakter)",null=True,max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Soru Fotoğrafı Ekleyin")
    article_image_c = models.FileField(blank = True,null = True,verbose_name="Cevap Fotoğrafı Ekleyin")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
    
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']

