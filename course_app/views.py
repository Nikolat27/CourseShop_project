from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from course_app.models import Course


# Create your views here.


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_app/course_list.html", context={"courses": courses})


@login_required
def course_buy(request, pk):
    if request.method == "POST":
        course = Course.objects.get(id=pk)
        user = request.user

        course.buyers.add(user)
        return redirect("course_app:course_detail", course.id)
    else:
        return redirect("home_app:main")


@login_required
def user_courses(request):
    user = request.user
    courses = Course.objects.filter(buyers=user)
    return render(request, "course_app/your_courses.html", context={"courses": courses})


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, "course_app/course_detail.html", context={"course": course})
