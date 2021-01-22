from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blueprint', views.blueprint, name="blueprint"),
    path('calc', views.calc, name="calc"),
    path('mystyle', views.mystyle, name="mystyle"),
]	