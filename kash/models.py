from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Tag(models.Model):
    name_uz = models.CharField(max_length=100,null=True)
    name_ru = models.CharField(max_length=100,null=True)


   


class News(models.Model):

    tags = models.ManyToManyField(Tag)
    title_uz = models.CharField(max_length=250,null=True)
    title_ru = models.CharField(max_length=250,null=True)
    description_uz = models.CharField(max_length=100,null=True)
    description_ru = models.CharField(max_length=100,null=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title_uz)





    