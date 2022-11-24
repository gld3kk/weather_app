from django.shortcuts import render, redirect
from weather_app.models import City_Weather
from django.http import HttpResponse, JsonResponse
import requests


# Create your views here.

def home(request):
	return render(request, 'home.html')

def getWeather(request):  

    City_State = request.POST["city, state"]


    # .get() solves for multidicterror if cel/faren not checked- will return None
    units = request.POST.get("temp_unit")
    
    
    if units == 'celsius':
            units = 'metric'
    else:
            units = 'imperial'
    
    
    api_key = '7922845de80bcaaef3c83c6b09e69ea4'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=%s' %(City_State, api_key,units)
    output = requests.get(url).json()
        
    try:
        output['message'] == 'city not found'
            
        return render(request, 'home_2.html')
    except KeyError:
     
            current_temp = output['main']['temp']
            min_temp = output['main']['temp_min']
            max_temp = output['main']['temp_max']
            weather_description = output['weather'][0]['description']
            icon = output['weather'][0]['icon']
        
        
            return render(request,'weather_page.html',
                          {'current_temp': current_temp,
                           'min_temp': min_temp,
                           'max_temp': max_temp,
                           'icon': icon,
                           'City_State': City_State,
                           'weather_description': weather_description})
    