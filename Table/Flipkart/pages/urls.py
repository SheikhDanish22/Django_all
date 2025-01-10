from django.urls import path
from . import views
urlpatterns = [
    path('form/',views.home,name='form'),
    path('data/',views.data,name='data')
     
]