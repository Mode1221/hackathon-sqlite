from django.shortcuts import render, redirect
from django.contrib.auth.models import User, update_last_login
from django.contrib import auth
from django.utils import timezone
from .models import Member

# Create your views here.
def signup(request):
    if request.method == "POST":
        id = request.POST['id']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        if User.objects.filter(username = id).exists():
            return render(request, 'signup.html', {'error': "이미 존재하는 사용자입니다."})
        if password == request.POST['passwordCheck']:
            member = Member()
            member.member_id = id
            member.password = password
            member.name = name
            member.email = email
            member.save()
            user = User.objects.create_user(
                id, password = password, email = email
            )
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'error': "비밀번호 확인이 일치하지 않습니다."})
    else:
        return render(request, 'signup.html')