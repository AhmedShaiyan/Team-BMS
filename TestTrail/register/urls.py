from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line to map the index view to the root URL
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('signup/', views.register, name='signup'),
]