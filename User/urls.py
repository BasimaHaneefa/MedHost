from django.urls import path
from User import views
app_name='user'

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    
    path('upprofile/<int:uid>',views.upprofile,name='Up_Profile'),
    path('changepwd/<int:uid>',views.changepwd,name="Change_pwd"),

    path('searchdoctor/',views.searchdoctor,name="Searchdoctor"),

    path('appoinment/<int:did>',views.appoinmet,name="Appoinment"),
    path('Bookappoinment/<int:did>',views.Bookappoinmet,name="BookAppoinment"),
    path('getdoc/',views.getdoctor,name="GetDoctor"),
    path('viewprescription/',views.viewprescription,name="viewprescription"),

    path('complaint/',views.complaint,name="Complaint"),
    path('description/',views.description,name="description"),
    path('myappoinment/',views.myappoinment,name="myappoinment"),
    path('paynow/<int:aid>',views.paynow,name="paynow"),

    path('logout/',views.logout,name="logout"),
]