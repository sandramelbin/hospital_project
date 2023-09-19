from django.urls import path
from . import views
urlpatterns  = [
    path('',views.base, name='base'),
    path('home',views.home, name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('adminview',views.adminview,name='adminview'),
    path('doctorview',views.doctorview,name='doctorview'),
    path('base2',views.base2,name='base2'),
    path('adminsignup',views.admin_signup_view,name='adminsignup'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('admindashboard',views.admin_dashboard,name='admindashboard'),
    path('admin_dash1',views.admin_dash1,name='admin_dash1'),
    path('doctor1',views.doctor1,name='doctor1'),
    path('patient1',views.patient1,name='patient1'),
    path('appointment1',views.appointment1,name='appointment1'),
    path('doctorsignup',views.doctor_signup,name='doctorsignup'),
    path('doctorlogin',views.doctor_login,name='doctorlogin'),
    path('approvedoctor',views.approvedoctor,name='approvedoctor'),
    path('approve_doc1',views.approve_doc1,name='approve_doc1'),

]