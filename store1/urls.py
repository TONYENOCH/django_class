from django.urls import path, include
from store1 import views

urlpatterns = [
    path('test',views.testpage,)
    path('hello/', views.hello),
    path('bye/', views.goodbye),
    # path('welcome/', views.welcome ),
    path('createpost/', views.createpost)
]