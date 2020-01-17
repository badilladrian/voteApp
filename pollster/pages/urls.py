from django.urls import path
from . import views

#Always import the views to the URL area

urlpatterns = [
    path('', views.index, name='index')
]