from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Саранск, Пятница, 26 мая, Время: 13:58, Температура +27, "
                        "Пасмурно, без осадков, по ощущению +27, "
                        "Ветер - 5 м/c, ЮЗ, "
                        "Давление - 744 мм рт. ст., "
                        "Влажность - 41 %, "
                        "Г/м активность 2 балла, "
                        "Температура воды +18.")
