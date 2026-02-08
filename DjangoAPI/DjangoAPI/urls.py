from django.contrib import admin
from django.urls import path, include, re_path # добавили re_path и include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('EmployeeApp.urls')), # используем re_path вместо url
]