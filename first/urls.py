from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from first.views import homepage, signup, contact, Login, Logout, profile, setting

urlpatterns = [
    path('', homepage,name='home'),
    path('signup/', signup, name='signup'),
    path('contact/',contact,name='contact'),
    path('done/',TemplateView.as_view(template_name="done_request.html"),name='done'),
    path('login/',Login,name='login'),
    path('logout/',Logout, name='logout'),
    path('profile/',profile,name='profile'),
    path('settings/', setting,name='settings'),
    path('panel/', TemplateView.as_view(template_name="panel.html"), name = 'panel')
]
