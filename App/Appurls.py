from django.urls import path
from . import views

urlpatterns = [
    path("addsub/",views.createsub,name="addsub"),
    path("",views.login,name="login"), 
    path("listsub/",views.listsub,name="listsub"),
    path("listsub/supprimer/<str:sub_id>/",views.supprimer,name="supprimer"),
]