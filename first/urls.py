from django.urls import path
from django.views.generic import TemplateView

from first.views import homepage

urlpatterns = [
    path('', homepage),
]
