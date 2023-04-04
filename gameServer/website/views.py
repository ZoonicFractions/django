from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.request import HttpRequest
import requests

# -- DASHBOARD
@csrf_exempt
def index(request):
    return render(request, 'website/index.html')

@csrf_exempt
def dashboard(request, classroom, role_number):
    # Calling the Api
    response = requests.get(f'http://localhost:8000/api/view-logs-student/{classroom}/{role_number}')
    response = response.json()  
    logs = response['logs']
    context = {'total_logs':0, 'last_level':0, 'best_grade':0, 'best_time':0,
               'classroom': classroom, 'role_number': role_number,
               'level_logs': {'1':[], '2':[], '3':[]}}
    
    # Getting all the logs
    context['total_logs'] = len(logs)

    # Getting the best_grade, best_time, , last_level and level_logs
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

    return render(request, 'website/studentDashbard.html', context)

@csrf_exempt
def forget_password(request):
    return render(request, 'website/forget-password.html')

@csrf_exempt
def recover(request: HttpRequest):
    if request.method == 'POST':
        return render(request, 'website/recover.html')
