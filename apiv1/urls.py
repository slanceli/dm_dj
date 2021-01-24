from django.urls import path
from apiv1 import views

urlpatterns = [
    path('login/', views.Login.as_view()),
]
