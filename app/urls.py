from django.conf.urls import url
from app.views import *

urlpatterns = [
    url(r'^$', HomeView.as_view()),

    # testing
    url(r'subscribe$', SubscribeView.as_view()),
    url(r'api/imgboard$', APIBoardView.as_view()),

    # working
    url(r'upload$', UploadView.as_view()),
    url(r'^([\w]+.[\w]+)$', ImageView.as_view()),

]