from django.contrib import admin
from django.urls import path
from fkip.views import indexfkip
from fk.views import indexfk
from faperta.views import indexfaperta
from feb.views import indexfeb
from fh.views import indexfh
from fisip.views import indexfisip
from ft.views import indexft
from pascasarjana.views import indexpascasarjana
from profil.views import indexprofil
from about.views import indexabout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', indexfkip),
    path('fk/', indexfk),
    path('faperta/', indexfaperta),
    path('feb/', indexfeb),
    path('fh/', indexfh),
    path('fisip/', indexfisip),
    path('ft/', indexft),
    path('pascasarjana/', indexpascasarjana),
    path('profil/', indexprofil),
    path('about/', indexabout),
    
]
