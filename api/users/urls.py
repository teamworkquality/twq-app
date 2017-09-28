from django.conf.urls import url

from users.views import UserView

urlpatterns = [
    url(r'^$', UserView.as_view(), name="admins"),
    url(r'^(?P<user_id>\w+)$', UserView.as_view(), name="get_admins"),
]