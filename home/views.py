from django.shortcuts import render
from .models import *



def index(request):
    allData = Index.objects.all()
    #filterdData = Index.objects.filter(sold=False)
    context = {'cars':allData}
    return render(request,'home\index.html',context)

def about(request):
    return render(request,'home\iabout.html')
