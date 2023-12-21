from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
import json

from .models import Contact, MyUser

@csrf_exempt
def register_user_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if MyUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        if MyUser.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        user = MyUser.objects.create_user(email=email, username=username, password=password)
        user.backend = 'joinbackend.myauth.EmailAuthBackend'
        login(request, user)
        return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)



@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def add_contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        contact = Contact.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            firstNameLetter=data.get('firstNameLetter'),
            lastNameLetter=data.get('lastNameLetter'),
        )
        return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)



def get_users(request):
    users = MyUser.objects.all().values('email', 'username')
    return JsonResponse(list(users), safe=False)


def get_contacts(request):
    contacts = Contact.objects.all().values('name', 'email', 'phone', 'firstNameLetter', 'lastNameLetter')
    return JsonResponse(list(contacts), safe=False)