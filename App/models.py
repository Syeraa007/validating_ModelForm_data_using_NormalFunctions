from django.db import models
from django import forms
# Create your models here.
def valid_name(peru):
    if peru[0].lower()=='n':
        raise forms.ValidationError('Name error at starting only')
    
def valid_size(size):
    if len(size)<=3:
        raise forms.ValidationError('Length error in name')
    
class Topic(models.Model):
    topic=models.CharField(max_length=100,primary_key=True,validators=[valid_name  ])
    
    def __str__(self) -> str:
        return self.topic
    
class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[valid_size])
    url=models.URLField()

    def __str__(self) -> str:
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100,validators=[valid_name,valid_size])

    def __str__(self) -> str:
        return self.author