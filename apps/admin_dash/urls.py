from django.urls import path, include

from . import views

team_urlpatterns = [
    path("", views.TeamIndexView.as_view(), name="team"),
    path("users/create", views.UserCreateView.as_view(), name="team-users-create"),
    path(
        "users/<int:user_id>/action",
        views.UserActionView.as_view(),
        name="team-users-action",
    ),
    path("users/search", views.UserSearchView.as_view(), name="team-users-search"),
    path(
        "users/<int:user_id>/edit",
        views.UserEditView.as_view(),
        name="team-users-edit",
    ),
    path(
        "users/<int:user_id>/password-reset",
        views.UserPasswordResetView.as_view(),
        name="team-users-password-reset",
    ),
    path(
        "users/<int:user_id>/delete",
        views.UserDeleteView.as_view(),
        name="team-user-delete",
    ),
]


urlpatterns = [
    path("team/", include(team_urlpatterns)),
]
