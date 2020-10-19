from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('user/<str:pk_test>/', views.user, name="user"),
    path('create_note/', views.createNote, name="create_note"),
    path('update_note/<str:pk>/', views.updateNote, name="update_note"),
    path('delete_note/<str:pk>/', views.deleteNote, name="delete_note"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]