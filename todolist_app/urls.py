from todolist_app import views
from django.urls import path
urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('contactus/', views.contactus, name="contactus"),
    path('aboutus/', views.aboutus, name="aboutus"),
]