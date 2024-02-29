from django.urls import path
from Guest import views
app_name='guest'
urlpatterns=[
    path('userregistration/',views.userregistration,name="userregistration"),
    path('ajax_place/',views.ajaxplc,name="Ajax_Place"),
    path('login/',views.login,name="Login"),
    path('',views.index,name="index"),
    
]