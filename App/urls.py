
from django.urls import path,include
from App import views
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views
from App.views import *



urlpatterns = [
    
    path('',EbookCreate.as_view(),name='ebookcreate'),
    path('<int:pk>',EbookDetails.as_view(),name='ebookdetail'),
    path('all/',AllEbook.as_view(),name='allebook'),
    # path('user/',UserCreate.as_view(),name='usercreate'),
    path('user/<int:pk>',UserDetails.as_view(),name='userdetail'),
    path('list/',Alluser.as_view(),name='alluser'),
    path('login/',obtain_auth_token,name='login'),
    path('api-token-auth/',views.obtain_auth_token),
    path('register/',Registeruser.as_view(),name='registeruser'),
]
