"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import job.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', job.views.index, name="index"),
    path('admin_login', job.views.admin_login, name="admin_login"),
    path('user_login', job.views.user_login, name="user_login"),
    path('company_login', job.views.company_login, name="company_login"),
    path('user_signup', job.views.user_signup, name="user_signup"),
    path('user_home', job.views.user_home, name="user_home"),
    path('Logout', job.views.Logout, name="Logout"),
    path('company_signup', job.views.company_signup, name="company_signup"),
    path('admin_home', job.views.admin_home, name="admin_home"),
    path('company_home', job.views.company_home, name="company_home"),
    path('view_users', job.views.view_users, name="view_users"),
    path('company_pending', job.views.company_pending, name="company_pending"),
    path('candidate_pending', job.views.candidate_pending, name="candidate_pending"),
    path('company_accepted', job.views.company_accepted, name="company_accepted"),
    path('candidate_accepted', job.views.candidate_accepted, name="candidate_accepted"),
    path('candidate_rejected', job.views.candidate_rejected, name="candidate_rejected"),
    path('company_rejected', job.views.company_rejected, name="company_rejected"),
    path('company_all', job.views.company_all, name="company_all"),
    path('change_passwordadmin', job.views.change_passwordadmin, name="change_passwordadmin"),
    path('change_passworduser', job.views.change_passworduser, name="change_passworduser"),
    path('change_passwordcompany', job.views.change_passwordcompany, name="change_passwordcompany"),
    path('delete_user/<int:pid>', job.views.delete_user, name="delete_user"),
    path('add_job', job.views.add_job, name="add_job"),
    path('job_list', job.views.job_list, name="job_list"),
    path('applied_candidatelist', job.views.applied_candidatelist, name="applied_candidatelist"),
    path('delete_company/<int:pid>', job.views.delete_company, name="delete_company"),
    path('edit_jobdetail/<int:pid>', job.views.edit_jobdetail, name="edit_jobdetail"),
    path('job_detail/<int:pid>', job.views.job_detail, name="job_detail"),
    path('applyforjob/<int:pid>', job.views.applyforjob, name="applyforjob"),
    path('contact', job.views.contact, name="contact"),
    path('latest_jobs', job.views.latest_jobs, name="latest_jobs"),
    path('user_latestjobs', job.views.user_latestjobs, name="user_latestjobs"),
    path('change_status/<int:pid>', job.views.change_status, name="change_status"),
    path('change_statuscandidate/<int:pid>', job.views.change_statuscandidate, name="change_statuscandidate")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
