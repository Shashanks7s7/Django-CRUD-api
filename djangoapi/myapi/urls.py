from django.urls import path
from . import views
urlpatterns = [
   path('',views.getdatas),
   path('create/',views.createdata),
   path('<str:pk>/update/',views.updatedata),
   path('<str:pk>/delete/',views.deletedata),
   path('<str:pk>/',views.getdata),
   

] 