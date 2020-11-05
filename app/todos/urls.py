from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.home_page, name='index'),
    path('new', views.new_list, name='new_list'),
    path('<int:list_id>/', views.view_list, name='view_list'),
]
