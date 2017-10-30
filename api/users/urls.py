from django.conf.urls import url

from users.views import UserView
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^$', UserView.as_view(), name="admins"),
    url(r'^(?P<user_id>\w+)$', UserView.as_view(), name="get_admins"),
    url(r'^api-token-auth/', views.obtain_auth_token)
]