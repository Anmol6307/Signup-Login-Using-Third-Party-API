from django.urls import path
from . import views


urlpatterns = [
	path('', views.loginPage, name="login"),
	path('register/', views.registerPage, name="register"),  
	path('logout/', views.logoutUser, name="logout"),
	path('home/', views.home, name="home"),  
]