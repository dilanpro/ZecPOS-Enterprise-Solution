from typing import List

from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from apps.user.forms import BusinessForm, UserCreateForm
from apps.user.models import Business, User


class SuperAdminIndexView(View):
    template_name: str = "pages/super-admin/dashboard.html"

    def get(self, request) -> HttpResponse:
        businesses = Business.objects.all()
        return render(
            request,
            template_name=self.template_name,
            context={"businesses": businesses},
        )


class BusinessCreateView(View):
    template_name: str = "pages/super-admin/business-create.html"
    form = BusinessForm

    def get(self, request) -> HttpResponse:
        form = self.form()
        return render(request, template_name=self.template_name, context={"form": form})

    def post(self, request) -> HttpResponse:
        form = self.form(request.POST)
        if form.is_valid():
            business: Business = form.save()
            messages.success(request, "Business created successfully")
            return redirect(
                reverse("sa-business-edit", kwargs={"business_id": business.id})
            )

        else:
            error = form.get_first_error()
            messages.error(request, error)

        return render(request, template_name=self.template_name, context={"form": form})


class BusinessEditView(View):
    template_name: str = "pages/super-admin/business-edit.html"
    form = BusinessForm

    def get(self, request, business_id) -> HttpResponse:
        business = get_object_or_404(Business, id=business_id)
        form = self.form(instance=business)
        return render(
            request,
            template_name=self.template_name,
            context={"business": business, "form": form},
        )

    def post(self, request, business_id) -> HttpResponse:
        business = get_object_or_404(Business, id=business_id)
        form = self.form(request.POST, instance=business)
        if form.is_valid():
            business: Business = form.save()
            messages.success(request, "Business edited successfully")

        else:
            error = form.get_first_error()
            messages.error(request, error)

        return render(
            request,
            template_name=self.template_name,
            context={"business": business, "form": form},
        )


class UsersListView(View):
    template_name: str = "pages/super-admin/users.html"
    form = UserCreateForm

    def get(self, request, business_id) -> HttpResponse:
        users = User.objects.filter(business_id=business_id)
        business = get_object_or_404(Business, id=business_id)
        return render(
            request,
            template_name=self.template_name,
            context={"business": business, "users": users},
        )


class UserCreateView(View):
    template_name: str = "pages/super-admin/user-create.html"
    form = UserCreateForm

    def get(self, request, business_id) -> HttpResponse:
        form = self.form()
        return render(request, template_name=self.template_name, context={"form": form})

    def post(self, request, business_id) -> HttpResponse:
        business = get_object_or_404(Business, id=business_id)
        if business.available_license_count() <= 0:
            messages.error(request, "No available license to add new user")
            return redirect(reverse("sa-users", kwargs={"business_id": business_id}))

        form = self.form(request.POST)
        if form.is_valid():
            user: User = form.save()
            user.password = make_password(user.password)
            user.business = business
            user.save()
            messages.success(request, "User created successfully")
            return redirect(reverse("sa-users", kwargs={"business_id": business_id}))

        else:
            error = form.get_first_error()
            messages.error(request, error)

        return render(request, template_name=self.template_name, context={"form": form})


class UserEditView(View):
    template_name: str = "pages/super-admin/user-edit.html"
    form = UserCreateForm

    def get(self, request, business_id, user_id) -> HttpResponse:
        user = get_object_or_404(User, id=user_id, business_id=business_id)
        form = self.form(instance=user)
        return render(
            request,
            template_name=self.template_name,
            context={"form": form, "selected_user": user},
        )

    def post(self, request, business_id, user_id) -> HttpResponse:
        user = get_object_or_404(User, id=user_id, business_id=business_id)
        form = self.form(request.POST, instance=user)
        if form.is_valid():
            user: User = form.save()
            user.password = make_password(user.password)
            user.business = Business.objects.get(id=business_id)
            user.save()
            messages.success(request, "User edited successfully")
            return redirect(reverse("sa-users", kwargs={"business_id": business_id}))

        else:
            error = form.get_first_error()
            messages.error(request, error)

        return render(request, template_name=self.template_name, context={"form": form})


class UserDeleteView(View):
    def get(self, request, business_id, user_id) -> HttpResponse:
        user = get_object_or_404(User, id=user_id, business_id=business_id)
        user.delete()
        messages.success(request, "User deleted successfully")
        return redirect(reverse("sa-users", kwargs={"business_id": business_id}))
