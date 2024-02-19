from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from course_app.models import Course


# Create your views here.

def course_list(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(Course.objects.all(), 4)
    page_obj = paginator.get_page(page_number)

    return render(request, 'course_app/course_list.html', {'courses': page_obj})


def search(request):
    q = request.GET.get("q")
    if q:
        courses = Course.objects.filter(title__icontains=q)
        return render(request, "course_app/course_list.html", context={"courses": courses})
    else:
        return redirect("home_app:main")


def autocomplete(request):
    if 'term' in request.GET:
        courses = Course.objects.filter(title__istartswith=request.GET.get('term'))
        titles = []
        for course in courses:
            titles.append(course.title)
        return JsonResponse(titles, safe=False)
    return render(request, "home_app/index.html")


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
