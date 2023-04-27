from django.urls import path
from store2 import views

urlpatterns = [
    path('hello/', views.hello),
    path('bye/', views.goodbye),
    path('welcome/',views.welcome),
    path('thankyou/', views.thankyou )
    
]