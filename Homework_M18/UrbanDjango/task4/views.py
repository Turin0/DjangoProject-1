from django.shortcuts import render

# Create your views here.


def main_task4(request):
    page_name = 'Главная страница'
    context = {
        'page_name': page_name
    }
    return render(request, 'fourth_task/main.html', context)


def shop_task4(request):
    page_name = 'Магазин игр'
    game_1 = 'Age of Empires'
    game_2 = 'Hearts of Iron 4'
    game_3 = 'Bloodborn'
    back = "Вернуться назад"
    context = {
        'page_name': page_name,
        'games': [game_1, game_2, game_3],
        'back': back
    }
    return render(request, 'fourth_task/shop.html', context)


def cart_task4(request):
    page_name = 'Корзина'
    text = 'Тут пока ничего нет.'
    back = "Вернуться назад"
    context = {
        'page_name': page_name,
        'text': text,
        'back': back
    }
    return render(request, 'fourth_task/cart.html', context)
