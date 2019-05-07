from django.urls import path
from . import views
from app_blog.views import *

urlpatterns=[
    path('',views.HomePageView.as_view(), name='home'),

]