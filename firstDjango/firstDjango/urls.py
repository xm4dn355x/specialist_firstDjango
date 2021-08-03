"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # Вот тут у меня вопрос. Обычно я тут кидаю ссылку на urls конкретного application и там уже их обрабатываю, например include('MainApp.urls').
    path('about', views.about),
    path('item/', views.items),
    path('items/', views.items),
    path('item/<int:pk>', views.item_details),
]

# И основной urls.py проекта просто перекидывает обработку урлов конкретным application, например вот так:
# urlpatterns = [
#     path('he-man/', admin.site.urls),
#     path('', include('i_list.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('analytics/', include('analytics.urls')),
#     path('streamlog/', include('streamlog.urls')),
#     path('imonitor/', include('imonitor.urls')),
#     path('imap/', include('internet_map.urls')),
#     path('governor/', include('governor.urls')),
#     path('government/', include('government.urls')),
#     path('risk-management/', include('risks.urls')),
#     path('incident-management/', include('incident.urls')),
#     path('api-auth/', include('rest_framework.urls')),
# ]
# Я всё правильно делал? Или есть какой-то best practice, которому я не следую?