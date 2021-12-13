from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('deliver', views.deliver, name='deliver'),
    path('manufacture', views.manufacture, name='manufacture'),
    path('payment', views.payment, name='payment'),
    path('refund', views.refund, name='refund'),
]