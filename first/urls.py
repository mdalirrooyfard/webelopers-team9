from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from first.views import homepage, signup

urlpatterns = [
    path('', homepage,name='home'),
    path('signup/', signup, name='signup'),
]
