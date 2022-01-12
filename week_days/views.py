from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

todo_dict = {

}
# Create your views here.
# def todo_views_all(request, todo_name):
#     if todo_name == 'monday':
#         return HttpResponse('В понедельник нужно убраться в квартире')
#     elif todo_name == 'tuesday':
#         return HttpResponse('Вторник: много поесть, сходить на курсы, купить много еды')
#     return HttpResponseNotFound('Days not corrected')
#
# def todo_day(request, todo_day: int):
#     if 0 < todo_day < 8:
#         return HttpResponse(f'Today day number {todo_day}')
#     return HttpResponseNotFound('Days not corrected')


day_dict = {
    'monday': 'Понедельник - день тяжелый.',
    'tuesday': 'Вторник - полегчало',
    'wednesday': 'Среда - неделя почти закончилась',
    'thursday': 'Среда - неделя почти закончилась',
    'friday': 'Пятница -развратница.',
    'saturday': 'Суббота -таки Да',
    'sunday': 'Воскресенье - выходной'
}

def get_about_day_week(request, day_week:str):
    description = day_dict.get(day_week, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Нам ещё не известен такой знак - {day_week}.')


def get_about_day_week_by_number(request, day_week:int):
    days = list(day_dict)
    if day_week > len(days):
        return HttpResponseNotFound(f'Неправильный номер дня недели {day_week}')
    name_day = days[day_week - 1]
    return HttpResponseRedirect(f'/week_days/{name_day}')
