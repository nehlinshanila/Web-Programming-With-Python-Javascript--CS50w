from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.getentry, name="entry" ),
    path("search/", views.getsearch, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("editpage/", views.editpage, name="editpage"),
    path("savepage/", views.savepage, name="savepage"),
    path("randompage/", views.randompage, name="randompage")
    
]
# views.getentry links to function we created in views.py