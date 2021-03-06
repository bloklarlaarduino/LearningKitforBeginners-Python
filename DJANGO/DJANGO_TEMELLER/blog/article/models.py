from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    # verbose_name -> admin panelinde bu modellerin nasıl görüleceği
    # article modelimizin auth field'ı. auth tablosundaki user kolonunu foreign key ile eşleştirdik. ondelete=models.CASCADE ise user silinince ona ait makalelerde silinsin dedik
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    image = models.FileField(blank=True, null=True,verbose_name='Fotoğraf Ekle') # resim eklemek zorunda değil

    # autonowadd=True -> direk o anki tarihi alır
    # eğer herhangi bir primary key belirlemezsek django otomatik olarak primary olarak id oluşturur
    def __str__(self):
        # bu şekilde admin paneline title'ı döndürüyoruz
        return self.title
    class Meta:
        ordering = ['-created_date'] # içeri verilen field'a göre sıralama yapılır


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments") # foreignkey sayesinde article modeli ile bağladık. related_name ile bu tabloya erişmemizi kolaylaştırdık. (article.comments)
    comment_author = models.CharField(max_length=50,verbose_name="Ziyaretçi")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-comment_date']
