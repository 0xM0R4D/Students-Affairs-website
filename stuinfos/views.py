from msilib import datasizemask
from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
# Create your views here.
from.models import stu
from.models import coursestudent
from.models import course
from django.shortcuts import render
from django.http import HttpResponse

from.forms import *

from.forms import courseForm
from.forms import coursestudent
from.forms import coursestudentForm

def stu_detector(new_old):
    
    alls = stu.objects.all()
    
    for i in alls:
        if i.GPA > 4 or i.GPA < 0:
            print(i)
            if new_old == "new":
                i.delete()
            return 'gpaerror'
            
            
    for i in alls:
        if i.level > 4 or i.level < 1:
            print(i)
            if new_old == "new":
                i.delete()
            return 'level'
            
    for i in alls:
        if i.stu_dep is not 'gen' and i.level == 1 or i.level == 2:
            print(i)
            if new_old == "new":
                i.delete()
            return 'dep'
            
    deps = ['cs','is','it','ai','gen']
    for i in alls:
        if i.stu_dep not in deps:
            print(i)
            if new_old == "new":
                i.delete()
            return 'dep'
        
    return ""
            


def home(request):
    return render(request,"../templates/home.html")

def news(request):
    return render(request,"../templates/news.html")

def search(request):
    return render(request,"../templates/search.html")

def active_inactive(request):
    data = {
        'student':stu.objects.all()
    }
    #return JsonResponse({'stus':list(data.stu_name())})
    return render(request,"../templates/active_inactive.html",data)
    

def add(request):
    form = stuForm()
    if request.method == 'POST':
        form = stuForm(request.POST)
        if form.is_valid():
            form.save()
            error_message = stu_detector("new")
            if error_message:
                return redirect(f'http://127.0.0.1:8000/{error_message}/')#link could change
            else:
                return redirect('http://127.0.0.1:8000/fine/')#link could change

        
    formII = courseForm()
    if request.method == 'POST':
        formII = courseForm(request.POST)
        if formII.is_valid():
            formII.save()
            return redirect('http://127.0.0.1:8000/fine/')
        
        
    formIII = coursestudent()
    if request.method == 'POST':
        formIII = coursestudentForm(request.POST)
        if formIII.is_valid():
            formIII.save()
            return redirect('http://127.0.0.1:8000/fine/')
        
    
    
    
    data = {
        'form':form,
        'formII':formII,
        'formIII':formIII
    }
    
    return render(request,"../templates/add_stu.html",data)





def contact(request):
    return render(request,"../templates/contact.html")

def edit(request,stu_id):
    
    
    context = {
        'stu':get_object_or_404(stu,pk=stu_id),
    }
    return render(request,"../templates/edit.html",context)


def show(request):
    allstu = stu.objects.all()
    total = len(allstu)
    stu_courses = coursestudent.objects.all()
    course_db = course.objects.all();
    stu_name = None
    stu_id = None
    stu_dep = None
    
    if 'searchname' in request.GET:
        stu_name = request.GET['searchname']
        if stu_name:
            allstu = allstu.filter(stu_name__icontains=stu_name)


    if 'searchid' in request.GET:
        stu_id = request.GET['searchid']
        if stu_id:
            allstu = allstu.filter(stu_id__icontains=stu_id)
            
    if 'Depart' in request.GET:
        stu_dep = request.GET['Depart']
        if stu_dep:
            allstu = allstu.filter(stu_dep__icontains=stu_dep)
            
            
    filterd_data = {
        'stus':allstu,
        'stu_courses':stu_courses,
        'searched':len(allstu),
        'total':total
    }
    
    return render(request,"../templates/show.html",filterd_data)




    
def delete(request,stu_id):
    order = stu.objects.get(stu_id=stu_id)
    deleted_courses = coursestudent.objects.filter(stuID=stu_id)
    
    if request.method == 'POST':
        deleted_courses.delete()
        order.delete()
        return redirect('/')
        
    
    context = {
    'stu':get_object_or_404(stu,pk=stu_id),
    }
    
    return render(request,"../templates/delete.html",context)


def _edit(request,stu_id):
    order = stu.objects.get(stu_id=stu_id)
    
    form = stuForm(instance=order)
    
    

    
    if request.method == 'POST':
        form = stuForm(request.POST,instance=order)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/fine/')
            

    
    context = {
        'form':form,
        'current_id':stu_id
    }
    return render(request,"../templates/_edit.html",context)


def onecourse(request,course_name):
    course_infos = coursestudent.objects.all()
    course_infos = course_infos.filter(courseNAME__icontains=course_name)
    context = {
        'course':get_object_or_404(course,course_name=course_name),
        'course_infos':course_infos,
        'stu_num':len(course_infos)
    }
    return render(request,"../templates/onecourse.html",context)


def gpaerror(request):
    return render(request,"../templates/error_handlle/GPA_error.html")

def level(request):
    return render(request,"../templates/error_handlle/level.html")

def dep(request):
    return render(request,"../templates/error_handlle/dep.html")

def fine(request):
    return render(request,"../templates/error_handlle/fine.html")


