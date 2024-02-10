from django import template
from course_app.models import Course

register = template.Library()


@register.filter
def check_user(pk, request):
    course = Course.objects.get(id=pk)
    user = request.user

    if course.buyers.filter(username=user.username).exists():
        return True
    else:
        return False
