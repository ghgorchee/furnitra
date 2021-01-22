from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blueprint', views.blueprint, name="blueprint"),
    path('calc', views.calc, name="calc"),
    path('calc_en', views.calc_en, name="calc_en"),
    path('mystyle', views.mystyle, name="mystyle"),
]	