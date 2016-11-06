"""school_saas URL Configuration

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
from school_saas import settings
from saas import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^main_login', views.main_login, name='main_login'),
    url(r'^forgot_password', views.forgot_password, name='forgot_password'),
    url(r'^register', views.register, name='register'),
    url(r'^intermid', views.intermid, name='intermid'),
    url(r'^parent_register', views.parent_register, name='parent_register'),
    url(r'^judges_register', views.judges_register, name='judges_register'),
    url(r'^chair_register', views.chair_register, name='chair_register'),
    url(r'^main', views.main, name='main'),
    url(r'^volunteers', views.volunteers, name='volunteers'),
    url(r'^pta_board', views.pta_board, name='pta_board'),
    url(r'^school', views.school, name='school'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
