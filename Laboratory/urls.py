from django.urls import path
from Laboratory import views
app_name='Laboratory'

urlpatterns=[
    path('homelaboratory/',views.homelaboratory,name="Home_Lab"),
    path('labmyprofile/',views.labmyprofile,name="Lab_myprofile"),
    path('uplabprofile/<int:lid>',views.uplabprofile,name="Up_Profile"),
    path('changelabpwd/<int:lid>',views.changelabpwd,name="Change_pwd"),
    path('testdetails/',views.testdetails,name="Test_Details"),
    path('viewcheckup/',views.viewcheckup,name="viewcheckup"),
    path('upcheckup/<int:uid>',views.upcheckup,name='Up_Checkup'),

    path('complaintlab/',views.complaintlab,name="Complaint_Lab"),
    path('description/',views.descriptionlab,name="Description_lab"),

    path('logout/',views.logout,name="logout"),

]