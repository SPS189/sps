from django.shortcuts import redirect, render
from . models import *
from random import randint
# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")

def SignupPage(request):
    return render(request,"app/signup.html")

def RegisterUser(request):
    
    if request.POST['role']=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email = email)

        if user:
            message = "This email is already exist!"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
    else:
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email = email)

        if user:
            message = "This email is already exist!"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcomp = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})

def OTPPage(request):
    return render(request,"app/otpverify.html")

def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)
    if user:
        if user.otp == otp:
            message = "OTP Verified Successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "OTP is incorrect"
            return render(request,"app/otpverify.html",{'msg':message,'email':email})
    else:
        return render(request,"app/signup.html")


def Loginpage(request):
    return render(request,"app/login.html")



def LoginUser(request):
    if request.POST['role']=="Candidate":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserMaster.objects.get(email=email)
        except UserMaster.DoesNotExist:
            user=None

        if user:
            if user.password == password and user.role == "Candidate":
                cand = Candidate.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.role
                request.session['email']=user.email
                request.session['firstname']=cand.firstname
                request.session['lastname']=cand.lastname

                return redirect("index")
            else:
                message = "Password doesnot match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User doesnot exist"
            return render(request,"app/login.html",{'msg':message})
    else:
        if request.POST['role']=="Company":
            email = request.POST['email']
            password = request.POST['password']

            try:
                user = UserMaster.objects.get(email=email)
            except UserMaster.DoesNotExist:
                user=None

            if user:
                if user.password == password and user.role == "Company":
                    comp = Company.objects.get(user_id=user)
                    request.session['id']=user.id
                    request.session['role']=user.role
                    request.session['email']=user.email
                    request.session['firstname']=comp.firstname
                    request.session['lastname']=comp.lastname

                    return redirect("companyindex")
                else:
                    message = "Password doesnot match"
                    return render(request,"app/login.html",{'msg':message})
            else:
                message = "User doesnot exist"
                return render(request,"app/login.html",{'msg':message})

        

def ProfilePage(request,pk):
    user = UserMaster.objects.get (pk=pk)
    cand = Candidate.objects.get(user_id=user)
    dict_gender = {'Gender':'Gender', '1':'Male', '2':'Female'} 
    dict_job_type = {'Job Type':'Job Type', '1':'Full Time', '2':'Part Time'}
    dict_jobcategory = {'Category':'Category', '1':'Web Developer', '2':'PHP Developer', '3':'Web Designer', '4':'Graphic Designer'}
    dict_level = {'Level':'Level', '1':'Level-1', '2':'Level-2', '3':'Level-3', '4':'Level-4'}
    dict_experience = {'Experience':'Experience', '1':'1 Year', '2':'2 Year', '3':'3 Year', '4':'4 Year'}
    dict_shift = {'Shift':'Shift', '1':'Morning', '2':'Evening'}
    return render(request,"app/profile.html",{'user':user,'cand':cand,
                                                        'dict_gender':dict_gender,
                                                        'dict_job_type':dict_job_type,
                                                        'dict_jobcategory':dict_jobcategory,
                                                        'dict_level':dict_level,
                                                        'dict_experience':dict_experience,
                                                        'dict_shift':dict_shift,})
                                                        


def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        cand = Candidate.objects.get(user_id = user)
        cand.job_type=request.POST['job_type']
        cand.jobcategory=request.POST['jobcategory']
        cand.city=request.POST['city']
        cand.state=request.POST['state']
        cand.min_salary=int(request.POST['min_salary'])
        cand.max_salary=int(request.POST['max_salary'])
        cand.highestedu=request.POST['highestedu']
        cand.experience=request.POST['experience']
        cand.website=request.POST['website']
        # email
        cand.contact=request.POST['contact']
        cand.gender=request.POST['gender']
        cand.shift=request.POST['shift']
        cand.jobdescription=request.POST['jobdescription']
        cand.profile_pic=request.FILES['profile_pic']
        cand.save()
        url = f'/profile/{pk}'  #Formating URL
        return redirect(url)

def candidatelogout(request):
    del request.session['id']
    del request.session['role']
    del request.session['email']
    del request.session['firstname']
    del request.session['lastname']

    return redirect('index')
    

#################### Company Side Views ####################

def CompanyIndexPage(request):
    return render(request,"app/company/index.html")

def CompanyProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)
    return render(request,"app/company/profile.html",{'user':user, 'comp':comp})

def UpdateCompanyProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)   
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        comp.firstname=request.POST['firstname']
        comp.lastname=request.POST['lastname']
        comp.company_name=request.POST['company_name']
        comp.state=request.POST['state']
        comp.city=request.POST['city']
        comp.contact=request.POST['contact']
        comp.address=request.POST['address']
        comp.website=request.POST['website']
        comp.description=request.POST['description']
        comp.logo_pic=request.FILES['logo_pic']
       
        comp.save()
        url = f'/companyprofile/{pk}'  #Formating URL
        return redirect(url)

def JobPostPage(request):
    return render(request,"app/company/jobpost.html")

def JobDetailSubmit(request):
    user = UserMaster.objects.get(id=request.session['id'])
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        jobdescription =request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibilies = request.POST['responsibilies']
        location = request.POST['location']
        companywebsite = request.POST['companywebsite']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        salarypackage = request.POST['salarypackage']
        experience = int(request.POST['experience'])

        newjob = JobDetails.objects.create(company_id=comp,
                                            jobname=jobname,
                                            companyname=companyname,
                                            companyaddress=companyaddress,
                                            jobdescription=jobdescription,
                                            qualification=qualification,
                                            responsibilies=responsibilies,
                                            location=location,
                                            companywebsite=companywebsite,
                                            companyemail=companyemail,
                                            companycontact=companycontact,
                                            salarypackage=salarypackage,
                                            experience=experience)
        
        message = "Job posted successfully"
        return render(request,"app/company/jobpost.html",{'msg':message})

def JobListPage(request):
    # user = UserMaster.objects.get(id=request.session['id'])
    # comp = Company.objects.get(user_id=user)
    # joblist = JobDetails.objects.get
    all_job = JobDetails.objects.all()
    return render(request,"app/company/jobpostlist.html",{'all_job':all_job})


def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/job-list.html",{'all_job':all_job})


def companylogout(request):
    del request.session['id']
    del request.session['role']
    del request.session['email']
    del request.session['firstname']
    del request.session['lastname']

    return redirect('index')

