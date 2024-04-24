from django.urls import path
from . import views

app_name = 'launches'
urlpatterns = [
    path('', views.index, name='launch'),
    path('api/common/', views.CommonDataRequest.as_view()),
    path('api/common/<int:pk>/', views.CommonDataRequest.as_view()),
    path('api/launch/<int:pk>/', views.LaunchDataRequest.as_view()),
]
