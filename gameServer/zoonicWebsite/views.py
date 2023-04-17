from django.shortcuts import render, redirect
from users.models import Registro
from .processing import get_average
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


# -- DASHBOARD
def general(request, difficulty):
    if request.user.is_authenticated:
        all_logs = Registro.objects.filter(difficulty = difficulty)
        context = get_average(all_logs, difficulty)
        return render(request, 'zoonicWebsite/average.html', context)
    else:
        return redirect("zoonicWebsite:log_in")

def classroomA(request, difficulty):
    if request.user.is_authenticated:
        all_logs = Registro.objects.filter(difficulty = difficulty, classroom = 'A')
        context = get_average(all_logs, difficulty, 'A')
        return render(request, 'zoonicWebsite/average.html', context)
    else:
        return redirect("zoonicWebsite:log_in")

def classroomB(request, difficulty):
    if request.user.is_authenticated:
        all_logs = Registro.objects.filter(difficulty = difficulty, classroom = 'B')
        context = get_average(all_logs, difficulty, 'B')
        return render(request, 'zoonicWebsite/average.html', context)
    else:
        return redirect("zoonicWebsite:log_in")

def dashboard(request, difficulty, classroom, role_number):
    if request.user.is_authenticated:
        # Calling the Api
        
        response = requests.get(f'http://localhost:8000/api/view-logs-student/{difficulty}/{classroom}/{role_number}')
        response = response.json()  
        logs = response['logs']
        context = {'total_logs':0, 'last_level':0, 'best_grade':0, 'best_time':0,
                'classroom': classroom, 'role_number': role_number,
                'level_logs': {'1':[], '2':[], '3':[]}, 'difficulty': difficulty}
        
        # Getting all the logs
        context['total_logs'] = len(logs)

        # Getting the best_grade, best_time, last_level and level_logs
        best_grade = 0
        best_time = float('inf')
        last_level = 0

        for log in logs:
            grade = log['grade']
            time = log['time']
            level = log['level']

            if(grade > best_grade):
                best_grade = grade

            if(time < best_time):
                best_time = time

            if(level > last_level):
                last_level = level
            
            context['level_logs'][f'{level}'].append({
                'grade': grade,
                'time': time,
                'date': log['date'],
            })

        context['best_grade'] = best_grade
        context['best_time'] = best_time
        context['last_level'] = last_level

        return render(request, 'zoonicWebsite/studentDashboard.html', context)
    else:
        return redirect("zoonicWebsite:log_in")

def notfound(request):
    if request.user.is_authenticated:
        return render(request, 'zoonicWebsite/notfound.html')
    else:
        return redirect("zoonicWebsite:log_in")

def log_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('zoonicWebsite:general', 1)
        
        else:
            messages.error(request,("Usuario o password incorrectos."))
            return redirect("zoonicWebsite:log_in")
        
    return render(request, 'zoonicWebsite/login.html')

def crud(request):
    return render(request, 'zoonicWebsite/crud.html')