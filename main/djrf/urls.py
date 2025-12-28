from django.urls import path
from . import views

# add paths for our CBVs.
urlpatterns = [
    path("", views.ListAPIUserModel.as_view(), name="get-user-model"),
    path("add/", views.CreateAPIUserModel.as_view(), name="post-user-model"),
]
