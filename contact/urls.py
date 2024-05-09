from django.urls import path
from contact.views import *

urlpatterns = [
    path('index', contact_index, name='contact_index'),

]
