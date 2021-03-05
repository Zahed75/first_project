from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album,Text,Planguage

# Create your views here.
def index(request):
    letter=Text.objects.order_by('-id')
    musician_list=Musician.objects.order_by('first_name')
    language=Planguage.objects.order_by('name')
    diction ={'musician':musician_list,'letter':letter,'data':language} 
    # for music in musician_list:
    #     print(music.first_name,music.last_name,music.instrument)
    # print(musician_list)
    return render(request,'first_app/index.html',context=diction)
