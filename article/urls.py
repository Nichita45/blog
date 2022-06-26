from django.urls import path
from .views import home, about, contacts, test
urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('about/', about, name="about"),
    path('test/', test, name="test")
]
