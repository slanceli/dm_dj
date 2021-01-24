from django.contrib import admin
from django.urls import path, include
from apiv1 import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('admin/', admin.site.urls),
    path('apiv1/', include('apiv1.urls'))
]
