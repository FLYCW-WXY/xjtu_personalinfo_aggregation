"""xjtu_personalinfo_aggregation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from mainapp import views as mainapp_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',mainapp_views.index),
    url(r'^perinfo/$',mainapp_views.perinfo),
    url(r'^edunews/$',mainapp_views.edunews),
    url(r'^notice/$',mainapp_views.notice),
    url(r'^activity/$',mainapp_views.activity)

]
