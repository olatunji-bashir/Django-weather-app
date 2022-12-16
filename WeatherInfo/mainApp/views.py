from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm




def index(request):
    cities = City.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=52f4c9ffb8d304414b86bde4c6c5c9ba'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []
    global temperature_data, average, median
    temperature_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        temperature_data.append(city_weather['main']['temp'])

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'humidity': city_weather['main']['humidity'],
            'pressure': city_weather['main']['pressure'],
            'country': city_weather['sys']['country'],
            'sunrise': city_weather['sys']['sunrise'],
            'sunset': city_weather['sys']['sunset'],
            'windspeed': city_weather['wind']['speed']
        }

        weather_data.append(weather)

        def median(lst):
            lst.sort()
            half = len(lst) // 2
            b = lst[half]
            c = lst[-half - 1]
            return (b + c) / 2

        result = {
            'maximum': max(temperature_data),
            'minimum': min(temperature_data),
            'average': sum(temperature_data) / len(temperature_data),
            'median': median(temperature_data)
        }

    context = {'weather_data': weather_data, 'form': form, 'result': result}

    return render(request, 'index.html', context)
