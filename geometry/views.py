from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


# get_rectangle_area (площадь прямоугольника) принимает длину и ширину фигуры
# get_square_area (площадь квадрата) принимает размер стороны квадрата
# get_circle_area (площадь круга) принимает радиус круга

def get_rectangle_area(request, width, height):
    if 'get' in request.get_full_path():
        return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width * height}')

def get_square_area(request, width):
    if 'get' in request.get_full_path():
        return HttpResponseRedirect(f'/calculate_geometry/square/{width}')
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {width * width} {request}')

def get_circle_area(request, radius):
    if 'get' in request.get_full_path():
        return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {3.14 * radius ** 2}')