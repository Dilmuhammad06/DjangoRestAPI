from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('students/', views.Students.as_view()),
    path('students/<int:pk>', views.Students.as_view()),
    path('homework/',views.Homeworks.as_view()),
    path('homework/<int:pk>', views.Homeworks.as_view())

]
