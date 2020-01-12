from django.shortcuts import render, redirect
import requests
from .models import city
from .forms import cityform

# Create your views here.
def index(request):
    api= 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3ecc3967073628475fe441f5063c83f4'
    #metric= for degree celcius
    #imperial= for degre F

    err_msg=''
    message=''
    message_class=''

    if request.method=='POST':
        form= cityform(request.POST)

        if form.is_valid():
            new_city= form.cleaned_data['name']  # models field name
            existing_city_count= city.objects.filter(name= new_city).count()

            if existing_city_count==0 :
                response= requests.get(api.format(new_city)).json()
                print(response)

                if response['cod']==200:
                    form.save()
                else:
                    err_msg='That city does not exist in the world as per my understanding'


                
            else:
                err_msg= 'City already exist in our database!'
        
        if err_msg:
            message= err_msg
            message_class='is-danger'
        
        else:
            message='succefully saved!'
            message_class='is-success'
        

                   
    form= cityform

    cities= city.objects.all()
    weather_data=[]

    for cityy in cities:
        response= requests.get(api.format(cityy)).json() # creating the request into jason onject
    #print(response.text) # To see dictionary details. remove .json than only it will work
#As per print below dictionary is written
        city_weather={
        
        'city': cityy.name,
        'country':response['sys']['country'],
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon':response['weather'][0]['icon'] 
        }

        weather_data.append(city_weather)

    
    #print(weather_data)
    context={'weather':weather_data, 
             'user_form':form,
             'message': message,
             'message_css': message_class
             }

    return render(request, 'weather.html', context)

def deleteCity(request, city_name):
    city_to_delete= city.objects.get(name= city_name)  # Name of model field,  id can also be used
    city_to_delete.delete()
    print('vity to be deleted: ', city_to_delete)

    return redirect('home')
