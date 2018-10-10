from django.shortcuts import render

# Create your views here.
def home(request):
    '''
    function that returns the index page
    '''
    return render(request,'index.html')