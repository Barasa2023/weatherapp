from django.shortcuts import render
from datetime import datetime
import requests

# Create your views here.
def index(request):
    """Render the index page."""
    api_key = '9750ce5bd3642197183bf37924b84db9'
    city = request.GET.get('city', 'Mombasa')
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather, forecast = {}, []

    if lat and lon:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    else:
        city = city or "Nairobi"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    if data.get('main'):
        weather = {
            'location': city,
            'temperature': data['main']['temp'],
            'condition': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
        }

    
    #Weather forecast for the next 5 days
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    if forecast_data.get('list'):
        for entry in forecast_data['list']:
            dt = datetime.fromtimestamp(entry['dt'])
            if dt.hour == 12:  # Get forecast for noon
                forecast.append({
                    'date': dt.strftime('%Y-%m-%d'),
                    'temperature': entry['main']['temp'],
                    'desc': entry['weather'][0]['description'],
                    'icon': entry['weather'][0]['icon'],
                })

    return render(request, 'weather/index.html', {'weather': weather, 'forecast': forecast})