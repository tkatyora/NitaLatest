from django.shortcuts import render
from .models import advertisment,aboutUs

# Create your views here.
advertismentdata = advertisment.objects.all()
about_us = aboutUs.objects.all()


def home(request):
    content ={}
    content ={
        'advert' : advertismentdata
    }
    
    return render(request , 'main/index.html' , content)
def about(request):
    content ={}
    content ={
        
    }
    
    return render(request , 'main/about.html',content)


# testing code 
def hometest(request):
    content ={}
    content ={
        'advert' : advertismentdata
    }
    
    return render(request , 'Nitacagra/index.html' , content)