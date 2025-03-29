from django.urls import path
from . import views

urlpatterns = [
  
    path("",views.login,name="login"), 
    path("listsub/",views.listsub,name="listsub"),
    path("listsub/supprimer/<str:name>/",views.supprimer,name="supprimer"),
]