from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addTransaction, name='addTransaction'),
    path('detail/<transaction_id>', views.transDetail, name='transDetail'),

    path('login/', views.login, name='login'),

]
