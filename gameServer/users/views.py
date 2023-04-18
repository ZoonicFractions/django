from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Usuario, Registro
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import re, json, hashlib
from datetime import datetime

# Creación de usuario (Administrador o Profesor)
class CreateUser(View):
    # Allowing everyone to use this POST request.
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        # Decoding the payload
        body = request.body.decode('utf-8')
        body = json.loads(body)

        # Checking that the input data is correct 
        try:
            # Getting the keys of the dictionary / JSON
            keys = list(body.keys())

            # Checking the number of parameters
            if(len(keys) != 4):
                raise Exception('Invalid number of parameters')

            # Naming the variables.
            mail = body[keys[0]]
            user_name = body[keys[1]]
            password = body[keys[2]]
            role = body[keys[3]]

            # Checking that all the variables are string type.
            if(not(isinstance(mail, str) and isinstance(user_name, str) and isinstance(password, str) and isinstance(role, str))):
                raise Exception('Invalid type in some arguments.')

            # Checking the mail is valid.
            # Regex for mail validation.
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(not re.fullmatch(regex, mail)):
                raise Exception('Invalid e-mail.')
            
            # Encrypting the password.
            password = hashlib.sha256(password.encode('ascii')).hexdigest()
            
            # Checking that the role is valid
            roles = ['Administrador', 'Profesor']
            if(role not in roles):
                raise Exception('Invalid role.')

            # Storing the new user in the database.
            new_user = Usuario(
                mail = mail,
                role = role,
                user_name = user_name,
                password = password
            )
            new_user.save()

            return JsonResponse({'status':"success"}) 

        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]}) 

# Validate User (log-in)
class ValidateUser(View):
    def get(self, request, mail, password):
        # Checking that the input data is correct 
        try:
            # Checking the mail is valid.
            # Regex for mail validation.
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(not re.fullmatch(regex, mail)):
                raise Exception('Invalid e-mail.')

            # Checking that mail and password are valid.
            # Looking for the User.
            foundUser = Usuario.objects.get(mail = mail)

            if(foundUser.password != password):
                raise Exception('Either the mail or the password are not correct.')
            
            return JsonResponse({'status':"success"}) 

        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]}) 

# View User (Administrador or Profesor)
class ViewUser(View):
    # Allowing everyone to use this POST request.
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, mail):
        # Checking that the input data is correct 
        try:
            # Checking the mail is valid.
            # Regex for mail validation.
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if(not re.fullmatch(regex, mail)):
                raise Exception('Invalid e-mail.')
 
            # Looking for the User.
            foundUser = Usuario.objects.get(mail = mail)

            if(not foundUser):
                raise Exception('E-mail not linked to any account.')

            (mail, role, user_name) = (foundUser.mail, foundUser.role, foundUser.user_name)
            
            return JsonResponse({'status':"success", "information" : {"mail" : mail, "user_name" : user_name, "role" : role}}) 
            
        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]})

# Update User
class UpdateUser(View):
    # Allowing everyone to use this POST request.
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #{pk, username, email, first_name, last_name, is_staff}
    def put(self, request):
        # Decoding the payload
        body = request.body.decode('utf-8')
        body = json.loads(body)
 
        # Checking that the input data is correct 
        try:
            # Getting the keys of the dictionary / JSON
            keys = list(body.keys())
 
            # Checking the number of parameters
            if(len(keys) != 6):
                raise Exception('Invalid number of parameters.')
            
            # Looking for the User.
            foundUser = User.objects.get(username = body[keys[0]])
            
            # Changing parameters
            foundUser.username = body[keys[1]]
            foundUser.email = body[keys[2]]
            foundUser.first_name = body[keys[3]]
            foundUser.last_name = body[keys[4]]
            foundUser.is_staff = body[keys[5]]

            # Saving changes.
            foundUser.save()
    
            return JsonResponse({'status':"success"}) 
        
        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]})

# Delete User
class DeleteUser(View):
    # Allowing everyone to use this POST request.
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def delete(self, request, username): 
        # Checking that the input data is correct 
        try:
            # Looking for the User.
            foundUser = User.objects.get(username = username)
 
            # Deleting the user.
            foundUser.delete()
            return JsonResponse({'status':"success"}) 
 
        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]})

# Game Log Register
class GameLogRegister(View):
    # Allowing everyone to use this POST request.
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
 
    def put(self, request):
        # Decoding the payload
        body = request.body.decode('utf-8')
        body = json.loads(body)
 
        # Checking that the input data is correct 
        try:
            # Getting the keys of the dictionary / JSON
            keys = list(body.keys())
 
            # Checking the number of parameters
            if(len(keys) != 6):
                raise Exception('Invalid number of parameters.')
            classroom = body[keys[0]]
            role_number = int(body[keys[1]])
            difficulty = int(body[keys[2]])
            level = int(body[keys[3]])
            grade = float(body[keys[4]])
            time = float(body[keys[5]])

            # Checking that all the values are the data type they should.
            if(not(isinstance(classroom, str) and isinstance(role_number, int) and 
                   isinstance(difficulty, int) and isinstance(level, int) and 
                   isinstance(grade, float) and isinstance(time, float))):
                raise Exception('Invalid type in some arguments.')
 
            # Creating ans saving the Log.
            new_log = Registro(
                classroom = classroom,
                role_number = role_number,
                difficulty = difficulty,
                level = level,
                date = datetime.now(),
                grade = grade,
                time = time
            )
            new_log.save()
            return JsonResponse({'status':"success"}) 
 
        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]})

# View Student Logs
class ViewStudentLogs(View):
    def get(self, request, difficulty, classroom, role_number):
        # Checking that the input data is correct 
        try:
            # Filtering students.
            foundStudents = list(Registro.objects.filter(
                classroom = classroom,
                role_number = role_number,
                difficulty = difficulty
            ))

            if (not foundStudents):
                raise Exception ('Student not found')
            # Pasing and storing the logs of the user
            logs = []
            for log in foundStudents:
                log = {'classroom': log.classroom, 'role_number': log.role_number,
                       'difficulty': log.difficulty, 'level': log.level,
                       'date': log.date.strftime("%d/%m/%Y : %H:%M:%S"), 
                       'grade': round(log.grade, 2), 'time': round(log.time, 2), }
                logs.append(log)
            
            return JsonResponse({'status':"success", 'logs': logs}) 
        
        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]})

# View Student Logs of a certain level 
class ViewStudentLogsChart(View):
    def get(self, request, difficulty, classroom, role_number, level):
        # Checking that the input data is correct 
        try:
            # Filtering students.
            foundStudents = list(Registro.objects.filter(
                classroom = classroom,
                role_number = role_number,
                difficulty = difficulty,
                level = level
            ))

            if (not foundStudents):
                raise Exception ('Student not found')

            # Pasing and storing the logs of the user
            logs = {'date_list': [], 'grade_list':[]}
            for log in foundStudents:
                logs['date_list'].append(log.date.strftime("%d/%m/%Y : %H:%M:%S"))
                logs['grade_list'].append(round(log.grade, 2))
            
            return JsonResponse({'status':"success", 'logs': logs}) 
        
        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]})