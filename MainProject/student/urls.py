from django.urls import path
from student import views

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('new/', views.New, name='new student details'),
    path('details/',views.AllStd, name='all students details'),
    path('update/<id>/', views.Update, name='students details update'),
    path('home/<id>/', views.Home1, name = 'student details with id'),
    path('delete/<id>/', views.Delete, name='delete student details'),
]