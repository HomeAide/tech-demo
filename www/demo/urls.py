from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_device', views.add_device, name='add_device'),
    path('create_user', views.create_user, name='create_user'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('get_devices/<str:type>/<int:location>', views.get_devices),
]
