from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('order', views.Order.as_view(), name='order'),
    path('addOrder/', views.createOrder.as_view(), name='addOrder'),
    path('client', views.Client.as_view(), name='client'),
    path('addClient/', views.createClient.as_view(), name='addClient'),

    path('ajax/getClient/', views.GetClient.as_view()),
    path('ajax/updateClient/', views.UpdateClient.as_view()),

    path('ajax/getOrder/', views.GetOrder.as_view()),
]