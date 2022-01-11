from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

todo_dict = {

}
# Create your views here.
def todo_views_all(request, todo_name):
    if todo_name == 'monday':
        return HttpResponse('В понедельник нужно убраться в квартире')
    elif todo_name == 'tuesday':
        return HttpResponse('Вторник: много поесть, сходить на курсы, купить много еды')
    return HttpResponseNotFound('Days not corrected')

def todo_day(request, todo_day: int):
    if 0 < todo_day < 8:
        return HttpResponse(f'Today day number {todo_day}')
    return HttpResponseNotFound('Days not corrected')