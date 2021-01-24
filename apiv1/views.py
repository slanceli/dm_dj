from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib import auth
import json


@login_required
def home(request):
    return render(request, 'home.html', {
        'email': User.objects.get(username=request.user.username).email
    })


def login(request):
    return render(request, 'login.html')


class Login(View):
    def post(self, request, *args, **kwargs):
        p_data = json.loads(request.body.decode())

        name = p_data['name']
        passwd = p_data['passwd']
        user = auth.authenticate(username=name, password=passwd)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponse(status=200)

        return HttpResponse(status=403)
