from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about' ),
    path('cats/', views.cats_index, name='cat_index'),
    path('cats/<int:cat_id>/', views.cats_show, name='cats_show')
]

# When thinking about making a webpage inside of django- first step would be:
# 1. create a view function
# 2. create your html page
# 3. Create a path inside of urls.py (maim_app)