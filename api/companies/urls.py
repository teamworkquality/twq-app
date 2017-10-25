from django.conf.urls import url

from .views import TeamView

urlpatterns = [
    url(r'^$', TeamView.as_view(), name="teams"),
    url(r'^(?P<team_id>\w+)$', TeamView.as_view(), name="get_team"),
]