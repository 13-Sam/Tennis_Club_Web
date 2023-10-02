from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('member_list', views.members, name='members'),
    path('details/<int:pk>', views.member_details, name='member_details'),
    path('testing', views.testing, name='testing'),
]

