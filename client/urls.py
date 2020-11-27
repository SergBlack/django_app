from django.urls import path
from .views import main_page, about_page

urlpatterns = [
    path('', main_page),
    path('about/', about_page),
]