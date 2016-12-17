from django.conf.urls import url
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'upload$', UploadView.as_view()),
    url(r'^([-\w]+)$', ImageView.as_view()),
]
