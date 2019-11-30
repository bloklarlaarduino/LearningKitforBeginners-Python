from django.urls import path
from django.conf.urls import url
from news import views

app_name = 'news'

urlpatterns = [
    path('news/<int:pk>', views.news_detail, name='news_detail'),
]
