from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    """Render the index page."""
    api_key = '9750ce5bd3642197183bf37924b84db9'
    city = request.GET.get('city')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = {
        'location': city,
        'temperature': data['main']['temp'],
        'condition': data['weather'][0]['description'],
    }
    return render(request, 'weather/index.html', {'weather': weather})