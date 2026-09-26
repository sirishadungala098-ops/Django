from django.http import HttpResponse
from . models import Student

# Create your views here.




def Student(request):
    students= Student.objects.all()
    return HttpResponse(students)
