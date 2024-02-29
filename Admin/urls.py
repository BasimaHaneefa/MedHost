from django.urls import path
from Admin import views
app_name='webadmin'
urlpatterns=[
    path('district/',views.district,name="district"),
    path('dltdis/<int:did>',views.dltdis,name='Dlt_Dis'),
    path('updis/<int:uid>',views.updis,name="Up_Dis"),

    path('place/',views.place,name="place"),
    path('dltplace/<int:did>',views.dltplace,name='Dlt_Place'),
    path('upplace/<int:uid>',views.upplace,name='Up_Place'),
   
    path('testtype/',views.testtype,name="testtype"),
    path('dlttst/<int:did>',views.dlttst,name='Dlt_Tst'),
    path('uptest/<int:uid>',views.uptest,name='Up_Tst'),

    path('department/',views.department,name="department"),
    path('dltdep/<int:did>',views.dltdep,name='Dlt_Dep'),
    path('updep/<int:uid>',views.updep,name='Up_Dep'),

    path('newdoctor/',views.newdoctor,name="newdoctor"),
    path('dltdoctor/<int:did>',views.dltdoctor,name='Dlt_doctor'), 

    path('newlab/',views.newlab,name="newlab"),
    path('dltlab/<int:did>',views.dltlab,name='Dlt_lab'),

    path('viewuser/',views.viewuser,name="viewuser"),
    path('acceptuser/<int:aid>',views.acceptuser,name='Accept_User'),
    path('rejectuser/<int:rid>',views.rejectuser,name='Reject_User'),

    path('accepteduser/',views.accepteduser,name="AcceptedUser"),
    path('rejecteduser/',views.rejecteduser,name="RejectedUser"),

    path('home/',views.home,name="home"),
    path('viewappoinment/',views.viewappoinment,name="viewappoinment"),
    path('acceptappoinment/<int:app>',views.acceptappoinment,name='Accept_Appoinment'),
    path('rejectappoinment/<int:rpp>',views.rejectappoinment,name="Reject_appoinment"),
    

    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('reply/<int:did>',views.reply,name="reply"),

    path('slots/<int:dcid>',views.slots,name="Slots"),
    path('report/',views.report,name="Report"),
    path('lbreport/',views.lbreport,name="Lb_Report"),
    
    path('logout/',views.logout,name="logout"),
    
]