from django.urls import path
from . import views

app_name    = "payroll_app"
urlpatterns = [ 
    path('', views.home, name="home"),
    path('salary', views.salary, name="salary"),
]