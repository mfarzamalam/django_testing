from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('', home_view, name='home'),
    path('author/<int:pk>/', author_detail, name='author-detail'),
]
