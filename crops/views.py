from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'agro/index.html')

def sesame_seeds(request):
    return render(request, 'agro/sasame_seeds.html')

def cashew_nuts(request):
    return render(request, 'agro/cashew_nuts.html')

def cashew_nuts(request):
    return render(request, 'agro/new_crop.html')