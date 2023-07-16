from django import forms
from App.models import *
class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
        help_texts={'topic':'Enter a valid Topic'}
        labels={'topic':'Topic Name'}
        
class PageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        # fields=['name','url']
        # exclude=['url']
        help_texts={'topic':'Enter a valid Topic','name':'Enter a valid Name','url': 'Enter a valid URL'}
        labels={'topic':'Topic Name', 'name':'Name','url':'URL'}

class RecordForm(forms.ModelForm): 
    class Meta():
        model=AccessRecord
        fields='__all__'
        # fields=['name','author']
        # exclude=['date']
        help_texts={'name':'Enter a valid Name','date':'Enter a valid Date','author':'Enter a valid Author name'}
        labels={'name':'Name','date':'Date','author':'Author'}
