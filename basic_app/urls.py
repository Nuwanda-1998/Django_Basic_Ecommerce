from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^registring/', views.registration, name='register_page'),
]
