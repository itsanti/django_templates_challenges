from django.http import HttpResponse
from django.shortcuts import render


"""
Эта вьюха показывает телефонный номер простой стройкой, а браузер дорисовывает остальные HTML тэги.
Но у нас есть свой темплэйт, где все эти тэги мы уже проставили и заполнен номер телефона.

Задания:
    1. Откройте страницу http://127.0.0.1:8000/phone-number/ и посмотрите на результат вывода.
    2. Используйте функцию render, чтобы вьюха вовращала ответ с темплэйтом level_1/phone_number.html
    3. Снова откройте страницу http://127.0.0.1:8000/phone-number/ , вывод результат должен быть таким же, что и изначально.
"""


def get_phone_number_view(request):
    phone_number = '+79848522383'

    return render(request, 'level_1/phone_number.html', context={'phone_number': phone_number})
