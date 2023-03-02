from django.urls import path
from Employee import views

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('base/', views.Base, name='basic page'),
    path('name/',views.Name, name='name page'),
    path('vivek/',views.Vivek,name='vivek page'),
    path('main/', views.Main, name='main page'),
    path('save/', views.Save, name='save employee details'),
    path('details/', views.AllEmp, name='all employee details'),
    path('update/<id>/', views.Update, name='employee details update'),
    path('home/<id>/', views.Home1, name = 'employee details with id'),
    path('delete/<id>/', views.Delete, name='delete employee details'),
    path('new/', views.New, name='new template'),
]