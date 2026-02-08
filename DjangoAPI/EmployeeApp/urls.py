from django.urls import path
from django.urls import re_path # Изменено здесь
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('ai-report/', views.ai_inventory_analysis), # Самым первым!
    re_path(r'^goods$', views.goodApi),
    re_path(r'^goods/([0-9]+)$', views.goodApi),

    re_path(r'^stocks$', views.stockApi),
    re_path(r'^stocks/([0-9]+)$', views.stockApi),

    re_path(r'^goodmoves$', views.goodmoveApi),
    re_path(r'^goodmoves/([0-9]+)$', views.goodmoveApi),

    #re_path(r'^goodrests$', views.goodrestApi),
    #re_path(r'^goodrests/([0-9]+)$', views.goodrestApi),
 #   re_path(r'goodrest/<str:wnameStock>/<str:wnameGood>/', views.goodrestApi),
     # Важно: str позволяет принимать кириллицу "Все"
    # Обязательно добавьте слэши в конце, если браузер их присылает
    path('goodrests/<str:wnameStock>/<str:wnameGood>/', views.goodrestApi),
    re_path(r'^goodincomes$', views.goodincomeApi),
    re_path(r'^goodincomes/([0-9]+)$', views.goodincomeApi)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


##Commit