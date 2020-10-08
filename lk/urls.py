from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list3'),
    path('post/<int:pk>/', views.post_detail3, name='post_detail3'),
]
