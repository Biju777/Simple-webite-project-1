from django.urls import path
from . import views
app_name = "tech"
urlpatterns = [
    path("", views.index,name="index"),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("about", views.about, name='about'),
]
