from django.urls import path
from .views import home, about, contacts, test, article_detail
urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('about/', about, name="about"),
    path('article/<slug:slug>', article_detail, name="article-detail"),
    path('test/', test, name="test"),
    
    ]
