from django.shortcuts import render
from users.models import Registro
from .processing import get_average
import requests

# -- DASHBOARD
def index(request):
    all_logs = Registro.objects.filter(difficulty = 1)
    context = get_average(all_logs, 1)
    return render(request, 'zoonicWebsite/average.html', context)

def general(request, difficulty):
    all_logs = Registro.objects.filter(difficulty = difficulty)
    context = get_average(all_logs, difficulty)
    return render(request, 'zoonicWebsite/average.html', context)

def classroomA(request, difficulty):
    all_logs = Registro.objects.filter(difficulty = difficulty, classroom = 'A')
    context = get_average(all_logs, difficulty, 'A')
    return render(request, 'zoonicWebsite/average.html', context)

def classroomB(request, difficulty):
    all_logs = Registro.objects.filter(difficulty = difficulty, classroom = 'B')
    context = get_average(all_logs, difficulty, 'B')
    return render(request, 'zoonicWebsite/average.html', context)

def dashboard(request, difficulty, classroom, role_number):
    # from django.db.models import Max
    # Usar Object.objects.all().agregate(Max('column_name'))
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

def notfound(request):
    return render(request, 'zoonicWebsite/notfound.html')