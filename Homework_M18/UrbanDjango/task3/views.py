from django.shortcuts import render

# Create your views here.


def main_task3(request):
    return render(request, 'third_task/main.html')


def shop_task3(request):
    title = 'Game shop'
    game_1 = 'Age of Empires'
    game_2 = 'Hearts of Iron 4'
    game_3 = 'Bloodborn'
    back = "Вернуться назад"
    context = {
        'title': title,
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
        'back': back
    }
    return render(request, 'third_task/shop.html', context)


def cart_task3(request):
    text = 'Тут пока ничего нет.'
    back = "Вернуться назад"
    context = {
        'text': text,
        'back': back
    }
    return render(request, 'third_task/cart.html', context)
