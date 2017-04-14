from django.shortcuts import render,get_object_or_404
from .models import Restaurant
from django.core import serializers
json_serializer = serializers.get_serializer("json")()
companies = json_serializer.serialize(Restaurant.objects.all().order_by('id')[:5], ensure_ascii=False)

def rest_index(request):
    restaurant = Restaurant.objects.order_by('?')
    return render(request, 'app/rest_index.html',{
        'restaurant':restaurant
    })

def rest_new(request):
    return render(request, 'app/rest_new.html')
