from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('post/<int:pk>', PostDetail.as_view(), name='detail'),
]
