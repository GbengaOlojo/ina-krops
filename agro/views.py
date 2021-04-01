from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse('index')
    return render(request, 'index.html')

def sesame_seed(request):
    return render(request, 'sesame_seed.html')

def cashew_nut(request):
    return render(request, 'cashew_nuts.html')

def new_crop(request):
    return render(request, 'new_crop.html')