from django.urls import path

from . import views
from myapp.views import register

urlpatterns = [
    path('', views.index, name='index'),
]
