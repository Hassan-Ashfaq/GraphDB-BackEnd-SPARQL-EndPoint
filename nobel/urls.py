from django.urls import path
from . import views

urlpatterns = [
    #Dashboard, Etc.
    path('dashboard/', views.dashboard, name='board'),
    path('SelectedResult/<int:id>/', views.selectQueryResult, name='selectedresult'),
    
    path('sparql/', views.sparqlEndpoint, name='sparqlEnd'),
    path('result/', views.queryResult, name='result'),
    
    #logIn, logOut
    path('', views.logInUser, name='LogInUser'),
    path('logOut/', views.logOutUser, name='LogOutUser'),
]