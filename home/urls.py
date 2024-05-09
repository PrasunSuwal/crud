from django.urls import path
from .import views
from home.views import *

urlpatterns = [
    path('', index, name='index'),
   path('edit_staff/<int:staff_id>/', views.edit_staff,  name='edit_staff' ),
   path('delete_staff/<int:staff_id>/', views.delete_staff,  name='delete_staff'),

]
