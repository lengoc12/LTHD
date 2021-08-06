from . import views
from django.contrib import admin
from django.urls import path, re_path
#from .admin import admin_site
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('welcome/<int:year>/', views.welcome, name="welcome"), #c1
    path('test/', views.TestView.as_view()),
    re_path(r'welcome2/(?P<year>[0-9]{4})/$', views.welcome2, name="welcome2"), #c2
    #path('admin/', admin_site.urls)
]