from django.urls import path
from . import views

urlpatterns = [
    path("addsub/",views.addsub,name="addsub"),
    path("createsub/",views.createsub,name="createsub"),
    path("",views.login,name="login"), 
    path("listsub/",views.listsub,name="listsub"),
    path("listsub/supprimer/<str:sub_id>/",views.supprimer,name="supprimer"),
    path('editsub/<str:sub_id>',views.editsub,name='editsub'),
    path("updatesub/<str:sub_id>",views.updatesub,name="updatesub"),
    path('search/', views.search, name='search'),
]