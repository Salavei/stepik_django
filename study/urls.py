from django.contrib import admin
from django.urls import path, include
from horoscope import views as views_horoscope
from week_days import views as views_week_days



urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', include('horoscope.urls')),
    path('todo/', include('week_days.urls')),
    path('calculate_geometry/', include('geometry.urls')),
]
