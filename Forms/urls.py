from django.urls import path
from . import views

urlpatterns = [
       
       path('form1/', views.controlerform1, name='controlerform1'),
       path('form2/', views.controleform2, name='controleform2'),
       path('form3/', views.controleform3, name='controleform3'),
       path('contact/', views.contactView, name='contact'),  # URL for the contact form
       path('success/', views.successView, name='success'),  # URL for success page
    ]