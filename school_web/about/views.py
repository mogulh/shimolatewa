from django.shortcuts import render

# Create your views here.

def school(request):
    return render(request, 'about/about_school.html')

def staff(request):
    return render(request, 'about/about_staff.html')

def students(request):
    return render(request, 'about/students.html')

def clubs(request):
    return render(request, 'about/clubs.html')


def classes(request):
    return render(request, 'about/class.html')


def games(request):
    return render(request, 'about/games.html')
