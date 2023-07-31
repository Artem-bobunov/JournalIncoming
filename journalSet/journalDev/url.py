from django.urls import path
from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', views.listJournal, name ='list'),
    path('create/', views.Create, name ='create'),
    path('update/<int:id>', views.Update, name ='update'),
    path('filter/', views.FilterList, name ='filter'),
    path('search/', views.searchList, name='search'),
    path('exportcsv/', views.exportcsv, name='exportcsv'),
    path('подробная информация/<int:id>', views.Detail, name='detail'),

    #path('Список вопросов/', views.listObjects, name ='list'),

]