from django.urls import path

from . import views

urlpatterns = [
    # Business
    path("", views.SuperAdminIndexView.as_view(), name="sa-businesses"),
    path(
        "business/create", views.BusinessCreateView.as_view(), name="sa-business-create"
    ),
    path(
        "business/<int:business_id>",
        views.BusinessEditView.as_view(),
        name="sa-business-edit",
    ),
    # Users
    path(
        "business/<int:business_id>/users",
        views.UsersListView.as_view(),
        name="sa-users",
    ),
    path(
        "business/<int:business_id>/users/<int:user_id>",
        views.UserEditView.as_view(),
        name="sa-user-edit",
    ),
    path(
        "business/<int:business_id>/users/<int:user_id>/delete",
        views.UserDeleteView.as_view(),
        name="sa-user-delete",
    ),
    path(
        "business/<int:business_id>/users/create",
        views.UserCreateView.as_view(),
        name="sa-user-create",
    ),
]
