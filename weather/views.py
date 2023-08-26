from django.shortcuts import render

import urllib.request
import json
def index(request):
    if request.method=='POST':

        city=request.POST['city']
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +city + '&units=metric&appid=3e7cfb003f0f578c181603a18da1d832').read()
        list_of_data=json.loads(source)
        data={

            "country_code":str(list_of_data['sys']['country']),
            "temp":str(list_of_data['main']['temp'])+'C',
            "humidity":str(list_of_data['main']['humidity']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon":str(list_of_data['weather'][0]['icon']),
        }
        print(data)
    else:
        data={}

    return render(request,'index.html', data)