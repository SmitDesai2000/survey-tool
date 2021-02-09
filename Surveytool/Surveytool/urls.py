
from django.contrib import admin
from django.urls import path,include
from api import views


urlpatterns = [                                       # Endpoint urls
    path('admin/', admin.site.urls),
    path('',views.welcome),
    path('questions', views.get_question),
  path('info', views.get_info),
   
]
