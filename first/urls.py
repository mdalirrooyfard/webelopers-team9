from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from first.views import homepage, signup, contact

urlpatterns = [
    path('', homepage,name='home'),
    path('signup/', signup, name='signup'),
    path('contact/',contact,name='contact'),
    path('done/',TemplateView.as_view(template_name="done_request.html"),name='done')
]
