from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Usuario, Registro
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import re, json, hashlib

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

            # Chcking that all the variables are string type.
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
            if(len(keys) != 2):
                raise Exception('Invalid number of parameters')

            # Naming the variables.
            mail = body[keys[0]]
            password = body[keys[1]]
            password = hashlib.sha256(password.encode('ascii')).hexdigest()

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

    def post(self, request):
        # Decoding the payload
        body = request.body.decode('utf-8')
        body = json.loads(body)

        # Checking that the input data is correct 
        try:
            # Getting the keys of the dictionary / JSON
            keys = list(body.keys())

            # Checking the number of parameters
            if(len(keys) != 1):
                raise Exception('Invalid number of parameters')
            
            # Naming the variables.
            mail = body[keys[0]]
        
            # Looking for the User.
            foundUser = Usuario.objects.get(mail = mail)
            (mail, role, user_name) = (foundUser.mail, foundUser.role, foundUser.user_name)
            
            return JsonResponse({'status':"success", "information" : {"mail" : mail, "user_name" : user_name, "role" : role}}) 
            
        except Exception as inst:
            return JsonResponse({'status':"failure", "message" : inst.args[0]})

# Update User (Román Mauricio Elias Valencia)
# Your code goes here...

# Delete User (Ernesto Miranda Solís)
# Your code goes here...

# Game Log Register (David Gonzalez Alanís)
# Your code goes here...

# View Student Logs (Fernando García Tejeda)
# Your code goes here...