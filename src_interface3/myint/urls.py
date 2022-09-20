from django.urls import path
from . import views

urlpatterns = [
    path('interfaces',      views.int_index,         name='index'),
    path('update-database', views.database_index,    name='database'),
    path('reserve',         views.add,               name='add'),
    path('add/addrecord/',  views.addrecord,         name='addrecord'),
    path('testing/',        views.testing,           name='testing'),
    path('searchint/',      views.search_int,        name='search-int'),
    path('searchID/',       views.search_ID,         name='searchID'),
    path('searchID/index/', views.searchidindex,     name='searchindex'),
    path('about/',          views.about,             name='about'),
]
