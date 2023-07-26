from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . views import *
urlpatterns = [
    path('',view=welcome,name='welcome'),
    path('index/',view=index,name='index'),
    path('index/table/',view=table,name='table'),
    path('index/insertdevice/',view=insert,name='insert'),
    path('index/deletedevice/<int:id>/',view=deletedevice,name='deletedevice'),
     path('index/edit/<int:id>/',view=edit,name='edit'),
     path('index/update/<int:id>/',view=updatedevice,name='updatedevice'),

    path('indexpa/',view=indexpa,name='indexpa'),
    path('indexpa/tablepa/',view=tablepa,name='tablepa'),
    path('indexemp/',view=indexemp,name='indexemp'),
    path('indexemp/tableemp/',view=tableemp,name='tableemp'),
    path('indexemp/insertemp/',view=insertemp,name='insertemp'),
    path('indexemp/deleteemp/<int:id>/',view=deleteemp,name='deleteemp'),
    path('indexemp/edit/<int:id>/',view=editemp,name='editemp'),
    path('indexemp/update/<int:id>/',view=updateemp,name='updateemp'),
    
    path('indexpa/insertpa/',view=insertpa,name='insertpa'),
    path('indexpa/deletepa/<int:id>/',view=deletepa,name='deletepa'),
    path('indexpa/edit/<int:id>/',view=editpa,name='editpa'),
    path('indexpa/update/<int:id>/',view=updatepa,name='updatepa'),
    path('index/details/<int:id>/<str:name>/',view=details,name='details'),
    path('index/maintaince/<int:id>/<str:name>/',view=maintiance,name='maintaince'),
    path('index/maintaince/<int:id>/<str:name>/tablemain/',view=tablemain,name='tablemain'),
    path('index/maintaince/<int:id>/<str:name>/insertmain/',view=insertmain,name='insertmain'),
     


     path('accounts/login/',view=login_user,name='login'),

    path('logout/',LogoutView.as_view(next_page='login'),name='logout')



]
