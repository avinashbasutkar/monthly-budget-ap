from django.urls import path

from . import views
from .views import updateExpenseView

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addTransaction, name='addTransaction'),
    path('detail/<transaction_id>', views.transDetail, name='transDetail'),
    path('detail-update/<pk>', updateExpenseView.as_view(), name='updateExpense'),
    path('detail-delete/<transaction_id>', views.deleteExpense, name='deleteExpense'),
    path('login/', views.login, name='login'),

]
