from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    """Render the index page."""
    api_key = '9750ce5bd3642197183bf37924b84db9'
    city = request.GET.get('city', 'Nairobi')

    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    data = response.json()

    context = {
        'location': data['location']['name'],
        'temperature': data['current']['temp_c'],
        'condition': data['current']['condition']['text'],
    }

    return render(request, 'weather/index.html', context)