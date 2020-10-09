from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_events, name='recommend_events'),
]