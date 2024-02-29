from django.urls import path
from Doctor import views

app_name='doctor'

urlpatterns=[
    path('homedoctor/',views.homedoctor,name="Home_Doctor"),
    path('doctorprofile/',views.doctorprofile,name="Doctor_Profile"),
    path('updocprofile/<int:drid>',views.updocprofile,name="Up_Profile"),
    path('changepwd/<int:uid>',views.changepwd,name="Change_pwd"),

    path('accepted_appoinment/',views.accepted_appoinment,name="Accepted_appoinment"),
    path('checkupdetails/<int:cid>',views.checkupdetails,name="checkupdetails"),
    path('ajax_checkup/',views.ajaxcheckup,name="Ajax_checkup"),

    path('view_checkup/<int:vid>',views.view_checkup,name="view_checkup"),
    path('reference/<int:vid>',views.reference,name="reference"),
    path('sendreference/<int:vid>',views.sendrefer,name="sendrefer"),
    path('search_history/',views.search_history,name="Search_History"),

    path('prescription/<int:pid>',views.prescription,name="prescription"),
    path('checkprescription/<int:pid>',views.checkprescription,name="checkprescription"),
    path('complaintdoc/',views.complaintdoc,name="Complaint_Doc"),
    path('description/',views.descriptiondoc,name="Description_doc"),
     path('viewrefer/',views.viewrefer,name="viewrefer"),

     path('logout/',views.logout,name="logout"),
]