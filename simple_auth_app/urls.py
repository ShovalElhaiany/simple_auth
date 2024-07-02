from django.urls import path
from .views import *

app_name = "simple_auth_app"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("users-list/", UsersList.as_view(), name="users_list"),
]
