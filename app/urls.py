from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('members/', views.index, name='index'),
    path('members/add/', views.edit, name='add'),
    path('members/edit/<int:id>/', views.edit, name='edit'),
    path('members/delete/<int:id>/', views.delete, name='delete'),
    path('members/detail/<int:id>/', views.detail, name='detail'),
]