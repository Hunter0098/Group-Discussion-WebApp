from django.urls import path
from . import views     #To access functions in views file
#Here . represents current working directory means that from current working directory import views.py

urlpatterns=[
    path('', views.showHome, name='showHome')   #When pattern is '' access showHome function from views.py file
]
