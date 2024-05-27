from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/',login_page, name='login' ),
    path('register/',register, name='register' ),
    path('activate/<emailtoken>',activate_email, name='activate_email' ),
]