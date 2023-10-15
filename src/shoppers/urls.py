from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . forms import LoginForm

app_name = 'shoppers'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('follow_us/', views.follow_us, name='follow_us'),
    path('terms/', views.terms, name='terms'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='shoppers/login.html', authentication_form=LoginForm), name='login'),
]