from django.conf.urls import url

from users.views import UserView

urlpatterns = [
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'^users/(?P<user_id>\w+)/$', UserView.as_view(), name="get_users"),
]