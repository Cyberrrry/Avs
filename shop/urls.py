from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name = 'shophome'),
path('About', views.about, name = 'About'),
path('contact', views.contact, name = 'ContactUs'),
path('tracker', views.track, name = 'TrackingStatus'),
path('search', views.search, name = 'search'),
path('products/<int:myid>', views.productview, name = 'productview'),
path('checkout', views.checkout, name = 'checkout'),

]