from django.urls import path

from . import views

app_name = 'products'

urlpatterns =[
    path('', views.browse, name='browse'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.info, name='info'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]