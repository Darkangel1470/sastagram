from django.urls import path
from signup import views

urlpatterns = [
    path('', views.index, name='blah'),
    path('user_register/', views.user_register, name='register')
]