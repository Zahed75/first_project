from django.contrib import admin
from first_app.models import Musician,Album,Text,Planguage


# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Text)
admin.site.register(Planguage)
