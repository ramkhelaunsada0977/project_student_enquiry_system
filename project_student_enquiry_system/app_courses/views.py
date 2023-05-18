from django.shortcuts import render

# Create your views here.
def course_index(request):
    context ={
        "title": "SES |Courses"
        "body_title": "Here are the courses details."
    }
    return render(request, 'courses/index.html')

def course_edit(request):
    context= {"title":"SES | Courses","body_title":"Here are the Courses Details"}
    return render(request, 'courses/edit.html')

def course_show(request):
    return render(request, 'courses/show.html')

def course_create(request):
    return render(request, 'courses/create.html')