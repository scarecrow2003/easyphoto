from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import login as lg, authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.settings import api_settings
import json
from .models import EPAccount, EPCompany

@csrf_exempt
def signup(request):
    data = json.loads(request.body.decode('utf-8'))
    user_name = data.get('user_name')
    email = data.get('email')
    password = data.get('confirmed_password')
    nick_name = data.get('nick_name')
    is_company = data.get('is_company')
    company_name = data.get('company_name')
    try:
        user = User.objects.get(email=email)
        return JsonResponse({'error': 'The email address you entered has already been used'})
    except User.DoesNotExist:
        if is_company:
            try:
                EPCompany.objects.get(company_name=company_name)
                return JsonResponse({'error': 'The company name you entered has already been used'})
            except EPCompany.DoesNotExist:
                group = Group.objects.create(name=user_name)
                group.save()
                company = EPCompany.objects.create(group=group, company_name=company_name)
        user = User.objects.create_user(user_name, email, password, first_name=nick_name, last_name='')
        user.is_active = True
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        account = EPAccount.objects.create(user=user, nick_name=nick_name)
        user.groups.add(group)
        lg(request, user)
        return JsonResponse({'token': generate_token(user)})


@csrf_exempt
def login(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data.get('email')
    password = data.get('password')
    user = authenticate(email=email, password=password)
    if user and user.is_active:
        lg(request, user)
        return JsonResponse({'token': generate_token(user)})
    return JsonResponse({'error': 'Invalid Credentials'}, status=401)


def logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def generate_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token
