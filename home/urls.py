from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('deliver', views.deliver, name='deliver'),
    path('manufacture', views.manufacture, name='manufacture'),
    path('payment', views.payment, name='payment'),
    path('refund', views.refund, name='refund'),
    path('ring_sizes', views.ring_sizes, name='ring_sizes'),
    path('ts_and_cs', views.ts_and_cs, name='ts_and_cs'),
]
