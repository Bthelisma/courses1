from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "course/index.html", context)

def courses(request):

    # using ORM
    Course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
    #insert into Course(name, description, creates_at) values (name, description, now())
    print request.POST['description']
    return redirect('/')
#
def remove(request, id):
    course = Course.objects.filter(id=id)
    course.delete()

    return redirect('/')
