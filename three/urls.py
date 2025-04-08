from three.views import (UserRegistrationView,LoginView)
from django.urls import path
from . import views

urlpatterns =[
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
]

good one