from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('mallesh/',views.mallesh,name="mallesh"),
    path('mallesh/details/<int:id>',views.details,name='details')
    
]
