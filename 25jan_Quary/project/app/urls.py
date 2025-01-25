from django.urls import path
from .import views


urlpatterns = [
    path('alldata/',views.alldata),
    path('fillterdata/',views.fillterdata),
    path('values/',views.value),
    path('valuelist/',views.vlist),
    path('ex/',views.ex)
]