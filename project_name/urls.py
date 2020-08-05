from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('members.urls')),
    path('employee/',include('employee.urls')),
    path('news/', include('news.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
]
