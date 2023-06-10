"""django_kbbi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from kbbi import views as kbbi
from django.conf.urls import handler403, handler404, handler500

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', kbbi.main_page, name='main_index'),
    url(r'^api/v1/$', kbbi.search_api, name='search_api'),
    url(r'^404', kbbi.not_found, name='not_found'),
    url(r'^500', kbbi.server_error, name='server_error'),
]

handler404 = 'kbbi.views.not_found'
handler500 = 'kbbi.views.server_error'
handler403 = 'kbbi.views.server_error'