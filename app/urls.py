from django.urls import path, include
from . import views

urlpatterns = [
   path("",views.IndexPage,name="index"), 
   path("signup/",views.SignupPage,name="signup"), 
   path("register/",views.RegisterUser,name="register"),
   path("otppage/",views.OTPPage,name="otppage"),
   path("otp/",views.Otpverify,name="otp"),
   path("loginpage/",views.Loginpage,name="loginpage"),
   path("loginuser/",views.LoginUser,name="login"),
   path("profile/<int:pk>",views.ProfilePage,name="profile"),
   path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
   path("joblist",views.CandidateJobListPage,name="joblist"),
   path("candidatelogout/",views.candidatelogout,name="candidatelogout"),


   #################### Company Side Views ####################


   path("companyindex/",views.CompanyIndexPage,name="companyindex"),
   path("companyprofile/<int:pk>",views.CompanyProfilePage,name="companyprofile"),
   path("updatecompanyprofile/<int:pk>",views.UpdateCompanyProfile,name="updatecompanyprofile"),
   path("jobpostpage/",views.JobPostPage,name="jobpostpage"),
   path("jobpost/",views.JobDetailSubmit,name="jobpost"),
   path("jobpostlistpage/",views.JobListPage,name="jobpostlist"),
   path("companylogout/",views.companylogout,name="companylogout"),

]





