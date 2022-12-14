from django.urls import path

from .views import BlacklistTokenUpdateView, RegisterView, UserView

app_name = 'accounts'

urlpatterns = [
       path('register', RegisterView.as_view(), name="create_user"),
       path('user', UserView.as_view(), name="get_user"),
]
