from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    #url(r'^login$',views.login_back_log,name='login_back_log'),
    url(r'^register',views.register_candidat,name='bla'),
    #url(r'^register_agent',views.register_agent,name='blo'),
    url(r'^login/',auth_view.login,{
            'template_name': 'dgi/back_log/login.html'},name= "login"),
    url(r'^logout/',auth_view.logout,{
            'template_name': 'dgi/index.html'},name= "logout"),
]