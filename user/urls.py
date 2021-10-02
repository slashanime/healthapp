
from django.urls import path 
from .views import login

urlpatterns = [
    # user/
    path('login/', login)
]