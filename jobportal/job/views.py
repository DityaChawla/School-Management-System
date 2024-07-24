from django.shortcuts import render,redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_login(request):
    return render(request,'admin_login.html')

def user_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request,'user_login.html',d)

def admin_login(request):
    error = ""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'admin_login.html',d)
def company_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['company'];
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Company.objects.get(user=user)
                if user1.type == "company" and user1.status!="pending":
                    login(request,user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request,'company_login.html',d)

def company_signup(request):
    error = ""
    if request.method =='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        company = request.POST['company']
        con = request.POST['contact']
        e = request.POST['email']
        p = request.POST['pwd']
        i = request.FILES['image']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Company.objects.create(user=user, mobile=con, image=i, gender=gen, company=company, type="company", status="pending")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'company_signup.html', d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']

        gen = request.POST['gender']

        student.user.first_name = f
        student.user.last_name = l
        student.mobile = con
        student.gender = gen

        try:
            student.save()
            student.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error = "no"
        except:
            pass
    d = {'student': student, 'error': error}
    return render(request, "user_home.html", d)

def company_home(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    return render(request, "company_home.html")

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rcount=Company.objects.all().count()
    scount=StudentUser.objects.all().count()
    d={'rcount':rcount, 'scount':scount}
    return render(request, "admin_home.html",d )

def Logout(request):
    logout(request)
    return redirect('index')
def user_signup(request):
    error = ""
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        e = request.POST['email']
        p = request.POST['pwd']
        i = request.FILES['image']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            StudentUser.objects.create(user=user, mobile=con, image=i, gender=gen, type="student")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'user_signup.html', d)

def company_home(request):

    if not request.user.is_authenticated:
        return redirect('company_login')
    user = request.user
    recruiter = Company.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']

        gen = request.POST['gender']

        recruiter.user.first_name = f
        recruiter.user.last_name = l
        recruiter.contact = con
        recruiter.gender = gen

        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            recruiter.image = i
            recruiter.save()
            error = "no"
        except:
            pass
    d = {'recruiter': recruiter, 'error': error}
    return render(request, 'company_home.html', d)

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data':data}
    return render(request, "view_users.html",d)

def latest_jobs(request):

    job = Job.objects.all().order_by('-start_date')
    d = {'job':job}
    return render(request, "latest_jobs.html",d)

def user_latestjobs(request):

    job = Job.objects.all().order_by('-start_date')
    d = {'job':job}
    user = request.user
    student = StudentUser.objects.get(user=user)
    data = Apply.objects.filter()
    li = []
    for i in data:
        li.append(i.job.id)
    d = {'job':job, 'li':li}
    return render(request, "user_latestjobs.html",d)

def job_detail(request, pid):

    job = Job.objects.get(id=pid)
    d = {'job' : job}
    return render(request, "job_detail.html",d)


def company_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Company.objects.filter(status='pending')
    d = {'data':data}
    return render(request, "company_pending.html",d)

def candidate_pending(request):
    if not request.user.is_authenticated:
        return redirect('applied_candidates')
    data = Company.objects.filter(status='Pending')
    d = {'data':data}
    return render(request, "candidate_pending.html",d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    error = ""
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        user = request.user
        recruiter = Company.objects.get(user=user)
        try:
          Job.objects.create(recruiter = recruiter, start_date=sd, end_date=ed, title=jt, salary=sal,image=l,description=des, experience=exp, location=loc, skills=skills, creationdate=date.today())

          error="no"
        except:
            error = "yes"
    d = {'error': error}

    return render(request, "add_job.html",d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    user = request.user
    recruiter =  Company.objects.get(user=user)
    job = Job.objects.filter(recruiter = recruiter)
    d = {'job':job}

    return render(request, "job_list.html",d)



def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    company = Company.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        company.status=s
        try:
            company.save()
            error="no"
        except:
            error="yes"

    d = {'company':company, 'error':error}
    return render(request, "change_status.html",d)

def change_statuscandidate(request,pid):
    if not request.user.is_authenticated:
        return redirect('applied_candidates')
    error=""
    student = StudentUser.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        student.status=s
        try:
            student.save()
            error="no"
        except:
            error="yes"

    d = {'student':student, 'error':error}
    return render(request, "change_status.html",d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""

    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"

    d = {'error':error}
    return render(request, "change_passwordadmin.html",d)

def change_passwordcompany(request):
    if not request.user.is_authenticated:
        return redirect('company_login')
    error=""

    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"

    d = {'error':error}
    return render(request, "change_passwordcompany.html",d)

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""

    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"

    d = {'error':error}
    return render(request, "change_passworduser.html",d)


def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')

def delete_company(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    company = User.objects.get(id=pid)
    company.delete()
    return redirect('company_all')


def company_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Company.objects.filter(status='Accept')
    d = {'data':data}
    return render(request, "company_accepted.html",d)

def company_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Company.objects.filter(status='Reject')
    d = {'data':data}
    return render(request, "company_rejected.html",d)
def candidate_accepted(request):
    accepted_applications = Application.objects.filter(status='Accepted')
    context = {'accepted_applications': accepted_applications}
    return render(request, 'candidate_accepted.html', context)


def candidate_rejected(request):
    if request.method == 'POST':
        applicant_id = request.POST.get('applicant_id')
        # Update the status of the applicant to 'Rejected' in the database
        applicant = Company.objects.get(pk=applicant_id)  # Replace YourModel with the actual model name
        applicant.status = 'Rejected'
        applicant.save()
        # Redirect back to the same page after rejecting the candidate
        return redirect('applied_candidatelist.html')
    else:
        return redirect('applied_candidatelist.html')
def company_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Company.objects.all()
    d = {'data':data}
    return render(request, "company_all.html",d)

def edit_jobdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('company_login')
    error = ""
    job = Job.objects.get(id = pid)
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']

        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = skills
        job.description = des
        try:
            job.save()
            error="no"
        except:
            error = "yes"
        if sd:
            try:
                job.start_date = sd
                job.save()

            except:
                pass
        else:
            pass

        if ed:
            try:
                job.end_date = ed
                job.save()

            except:
                pass
        else:
            pass
    d = {'error': error, 'job':job}

    return render(request, "edit_jobdetail.html",d)

def applyforjob(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user = request.user
    student = StudentUser.objects.get(user=user)
    job = Job.objects.get(id=pid)
    date1 = date.today()
    if job.end_date< date1:
        error = "close"
    elif job.start_date > date1:
        error = "notopen"
    else:
        if request.method == 'POST':
            r = request.FILES['resume']
            Apply.objects.create(job = job, student= student, resume=r,applydate=date.today())
            error="done"
    d = {'error':error}

    return render(request, 'applyforjob.html', d)

def contact(request):

    return render(request,'contact.html')






def applied_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect('company_login')

    if request.method == 'POST':
        applicant_id = request.POST.get('applicant_id')
        applicant = Apply.objects.get(pk=applicant_id)
        job = applicant.job

        if request.POST.get('action') == 'Accept':
            # Accept the candidate
            applicant.status = 'Accepted'
            applicant.save()
            # Decrease vacancies


        elif request.POST.get('action') == 'Reject':
            # Reject the candidate
            applicant.status = 'Rejected'
            applicant.save()

    data = Apply.objects.all()
    d = {'data': data}
    return render(request, 'applied_candidatelist.html', d)
