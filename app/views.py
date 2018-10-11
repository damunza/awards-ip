from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    '''
    function that returns the index page
    '''
    project = Project.objects.all
    return render(request,'index.html',{'content': project})