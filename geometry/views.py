from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} рана {width*height}")
def get_square_area(request, width: int):
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width * width}")
def get_circle_area(request, radius: int):
    return HttpResponse(f"Площадь круга радиусом {radius} равна {radius * 3.14}")

# get_rectangle_area (площадь прямоугольника) принимает длину и ширину фигуры
# get_square_area (площадь квадрата) принимает размер стороны квадрата
# get_circle_area (площадь круга) принимает радиус круга
