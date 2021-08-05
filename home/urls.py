from django.urls import *
from . import views

urlpatterns=[

         path('',views.homeview,name="homeview"),
         path('signup/', views.signup, name="signup"),
         path('login/', views.login, name="login"),
         path('logout/', views.logout, name='logout'),
         path('order/', views.order, name='order'),
         path('suggestion/', views.suggestion, name="suggestion"),
         path('upload/', views.upworks, name="upload"),


 ]
