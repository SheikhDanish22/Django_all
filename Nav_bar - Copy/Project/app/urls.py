from django.urls import path
from . import views
urlpatterns=[
    path('',views.landingpage,name='landingpage'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.ragister,name='ragister')
]