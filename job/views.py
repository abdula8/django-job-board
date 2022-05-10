from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.

def job_list(request):
    job_list = Job.objects.all() #get all jobs from database

    # filters
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs

    paginator = Paginator(job_list, 2) # Show 1
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs' : page_obj, 'myfilter' : myfilter} # its name template
    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)

    if request.method=='POST':
        form = ApplyForm(request.POST, request.FILES)
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        if form.is_valid():
            # print("DDDDDOOOOOOOOOOONNNNNNNNNNNNEEEEEEEEEEE")
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm()
    context = {'job' : job_detail, 'form':form}
    return render(request,'job/job_detail.html',context)


@login_required
def add_job(request):
    # # print('\n\n\n')
    # # print(type(JobForm(request.POST, request.FILES)))
    # # <class 'job.forms.JobForm'>
    # # print('\n\n\n')
    # print('\n\n\n')
    # print(type(request.user))
    # print(request.user)
    # print(len(str(request.user)))
    # print('\n\n\n')
    if request.method=='POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid() and ((str(request.user) =='abdallah') or str(request.user) =='admin'):
            myform = form.save(commit=False)
            myform.owner = request.user # the currently logged in user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()
    
    #return render(request, 'folder/fileNAme', {})
    return render(request, 'job/add_job.html', {'form':form})

