from django.urls import *
from . import views

urlpatterns=[

         path('',views.adminview,name="adminview"),

         path('adddata/', views.adddata, name="adddata"),
         path('update/<int:pid>/', views.update, name='update'),
         path('delete/',views.delete, name='delete')
 ]
