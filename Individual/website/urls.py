from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
     path('navbar/',views.navbar,name="register"),
    path('register/',views.Register,name="register"),
    path('login/',views.Login,name="login"),
    path('homepage/', views.home, name='home'),
    path('register/otplogin',views.otp_verification,name="otp"),
    path('transaction/', views.transaction, name='transaction'),
    path('finance/', views.finance, name='finance'),
    path('query/', views.query, name='query'),
    path('credit/',views.credit,name='credit'),
    path('login/',views.Login,name='viewrecord'),
    path('profile/',views.profile,name='viewrecord'),
    path('edit/',views.edit,name='editprofile'),
    path('editorder/',views.editorder,name='editprofile'),
    path('passbook/',views.passbook,name="passbook"),
    path('insert/',views.insert,name='editprofile'),
    path('querysubmit/',views.submit,name='submit'),
    path('insert/insertid/',views.insertData,name='editprofile1'),
    path('users1/',views.users1,name="user"),
    path('query1/',views.query1,name="user1"),
    path('trans/',views.trans,name="user2"),
    path('logout/',views.logout,name="logout"),
    path('', views.main, name='main'),
]