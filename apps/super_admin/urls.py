from django.urls import path

from . import views

urlpatterns = [
    # Business
    path("", views.SuperAdminIndexView.as_view(), name="business"),
    path("business/create", views.BusinessCreateView.as_view(), name="business-create"),
    path("business/<int:business_id>", views.BusinessEditView.as_view(), name="business-edit"),

    # Users
    path("business/<int:business_id>/users", views.UsersListView.as_view(), name="users"),
    path("business/<int:business_id>/users/<int:user_id>", views.UserEditView.as_view(), name="user-edit"),
    path("business/<int:business_id>/users/create", views.UserCreateView.as_view(), name="user-create"),
]