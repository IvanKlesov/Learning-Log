from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Страница входа
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name = 'login'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    # Страница входа
    url(r'^register/$', views.register, name = 'register'),
]
