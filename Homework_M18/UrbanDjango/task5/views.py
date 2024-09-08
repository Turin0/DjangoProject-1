from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.


def sign_up_by_html(request):
    users = ['Ronin', 'Lincoln', 'Krusty']
    info = {}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            return HttpResponse('Вы должны быть старше 18 лет')
        for user in users:
            if username == user:
                return HttpResponse('Пользователь уже существует')
        return HttpResponse(f'Приветствуем {username}!')
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    users = ['Ronin', 'Lincoln', 'Krusty']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                return HttpResponse('Пароли не совпадают')
            elif int(age) < 18:
                return HttpResponse('Вы должны быть старше 18 лет')
            for user in users:
                if username == user:
                    return HttpResponse('Пользователь уже существует')
            return HttpResponse(f'Приветствуем {username}!')
        else:
            form = UserRegister()
        return render(request, 'fifth_task/registration_page.html', context=info)
