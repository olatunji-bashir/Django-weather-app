# yoyoweather

A Django weather app that allows api users get 
the minimum, maximum, average and median temperature for a given city and period of time.
It also showcases a view of various cities and their temperature.

set up process as follows:

$ python3 -m venv env
$ pip install django
$ pip install requests
$ django-admin startproject WeatherInfo
$ cd WeatherInfo
$ python manage.py startapp mainApp



USER STORY
A post request is being sent to server side that contains the reqired result:

context = {'weather_data': weather_data, 'form': form, 'result': result}

where result is an object of the following structure:

{
 "maximum": value,
 "minimum": value,
 "average": value,
 "median": value
 }
 this can be found in views.py





