from django.conf.urls import url

from users.views import TeamView

urlpatterns = [
    url(r'^$', TeamView.as_view(), name="teams"),
    url(r'^(?P<team_id>\w+)$', UserView.as_view(), name="get_team"),
]