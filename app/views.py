from django.shortcuts import render,get_object_or_404
from .models import Restaurant

def rest_index(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'app/rest_index.html',{
        'restaurant':restaurant
    })

def rest_new(request):
    return render(request, 'app/rest_new.html')
