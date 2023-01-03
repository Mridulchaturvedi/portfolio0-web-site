from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('certificates',views.certifi),
    path('blogs',views.blogslink),
    path('<int:id>/',views.view_blog,name='view_blog'),
    
    
]
