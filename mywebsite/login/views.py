from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from .models import MyUser


def turn_to_login(request):
    """ 跳转到登陆 """
    return render(request, 'login/login.html', {'next': request.GET.get('next')})


def turn_to_register(request):
    """ 跳转到注册 """
    return render(request, 'login/register.html')


def login(request):
    """ 登录 """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            next_action = request.POST.get('next')
            if next_action == 'None':
                return render(request, 'index/index.html')
            return redirect(next_action)
    return render(request, 'login/login.html')


def logout(request):
    """ 退出登录 """
    auth.logout(request)
    return render(request, 'index/index.html')


def register(request):
    """ 注册 """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = MyUser.objects.filter(username=username)
        if user:
            return JsonResponse({'status': 'exist', 'msg': '用户已存在！'})
        else:
            MyUser.objects.create_user(username=username, password=password)
            return JsonResponse({'status': 'ok', 'msg': '注册成功！'})
    else:
        render(request, 'login/register.html')
