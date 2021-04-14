from django.urls import path
from .views import (item_list,
                    check_out,
                    Homeview,
                    ItemDetailView,
                    add_to_inprogress,
                    LoginPage,
                    RegisterPage,
                    dashboard,
                    Writer,
                    home)

from .views import *

app_name = 'core'
urlpatterns = [
    path('', Homeview.as_view(), name="home-page"),
    path('home/', home, name="home"),
    path('checkout/', check_out, name='checkout'),
    path('order/', item_list, name='order-page'),
    #path('order-page/<slug>', ItemDetailView.as_view(), name='order-page')
    #path('add-to-inprogress/<slug>',add_to_inprogress(), name='add-to-inprogress'),
    path('login/', LoginPage, name='login'),
    path('register/', RegisterPage, name='register'),
    path('dashboard/', dashboard, name="dashboard"),
    #path('customer/<str:pk_test>/', Writer, name="customer")


]