from django.urls import path

from .views import home, test_view

urlpatterns = [
    path('home/', home, name='home'),
    path('test_view/', test_view, name='test_view'),
]