from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.FormsView.as_view(), name="forms"),
    url(r'^(?P<form_id>\w+)$', views.FormsView.as_view(), name="get_form"),
    url(r'^(?P<form_id>\w+)/answers/$', views.AnswersView.as_view(), name="send_answers")
]
