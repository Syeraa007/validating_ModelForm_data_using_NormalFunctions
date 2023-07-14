from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from App.models import *

# Create your views here.
def topic_valid(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic Data is Valid')
        else:
            return HttpResponse('Data is Invalid')
    return render(request,'topic_valid.html',d)

def page_valid(request):
    PFO=PageForm()
    d={'PFO':PFO}
    if request.method=='POST':
        PFD=PageForm(request.POST)
        if PFD.is_valid():
            PFD.save()
            return HttpResponse('Page Data is Valid')
        else:
            return HttpResponse('Data is Invalid')
    return render(request,'page_valid.html',d)

def record_valid(request):
    RFO=RecordForm()
    d={'RFO':RFO}
    if request.method=='POST':
        RFD=RecordForm(request.POST)
        if RFD.is_valid():
            RFD.save()
            return HttpResponse('Record Data is Valid')
        else:
            return HttpResponse('Data is Invalid')
    return render(request,'record_valid.html',d)