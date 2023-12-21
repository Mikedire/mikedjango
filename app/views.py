from django.shortcuts import render
from app.forms import EmployeeForm
from app.models import Employee


# Create your views here.
def home(request):
    return render(request, template_name='index.html')


def gallery(request):
    return render(request, template_name='gallery.html')


def aboutus(request):
    return render(request, template_name='about.html')


def contactus(request):
    return render(request, template_name='contact.html')


def join(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name='join.html')

    else:
        return render(request, template_name='join.html')


def details(request):
    members = Employee.objects.all()
    return render(request, template_name='details.html', context={'all': members})
