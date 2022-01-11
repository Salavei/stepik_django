from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodia_by_number),
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodia),
    # path('scorp/', views.scorpio),
]