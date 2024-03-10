from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from apps.user.forms import UserCreateForm
from apps.user.models import Business, User
from core.htmx import BlockObject, Response


class AuthMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_admin_access()


class TeamIndexView(AuthMixin, View):
    template_name = "pages/team/users.html"

    def get(self, request):
        return render(
            request,
            template_name=self.template_name,
            context={
                "users": request.user.business.users.all(),
                "business": request.user.business,
            },
        )


class UserCreateView(AuthMixin, View):
    template_name: str = "pages/team/user-create.html"
    form = UserCreateForm

    def _has_available_licenses(self, business: Business):
        return business.seat_count > business.users.all().count()

    def get(self, request):
        form = self.form()
        return render(
            request,
            template_name=self.template_name,
            context={
                "form": form,
                "licenses": self._has_available_licenses(
                    business=request.user.business
                ),
            },
        )

    def post(self, request):
        business = request.user.business
        if business.available_license_count() <= 0:
            messages.error(request, "No available license to add new user")
            return redirect(reverse("team"))

        form = self.form(request.POST)
        if form.is_valid():
            user: User = form.save()
            user.password = make_password(user.password)
            user.business = business
            user.save()
            messages.success(request, "User created successfully")
            return redirect(reverse("team"))

        else:
            error = form.get_first_error()
            messages.error(request, error)

        return render(request, template_name=self.template_name, context={"form": form})


class UserEditView(AuthMixin, View):
    template_name: str = "pages/team/user-edit.html"
    form = UserCreateForm

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id, business_id=request.user.business.id)
        form = self.form(instance=user)
        return render(
            request,
            template_name=self.template_name,
            context={"form": form, "selected_user": user},
        )

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id, business_id=request.user.business.id)
        form = self.form(request.POST, instance=user)
        if form.is_valid():
            user: User = form.save()
            user.password = make_password(user.password)
            user.business = request.user.business
            user.save()
            messages.success(request, "User edited successfully")
            return redirect(reverse("team"))

        else:
            error = form.get_first_error()
            messages.error(request, error)

        return render(request, template_name=self.template_name, context={"form": form})


class UserDeleteView(AuthMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id, business=request.user.business)
        if user == request.user:
            messages.error(request, "You can't delete yourself")
            return redirect(reverse("team"))

        user.delete()
        messages.success(request, "User deleted successfully")
        return redirect(reverse("team"))


class UserSearchView(AuthMixin, View):
    template_name = "pages/team/users.html"

    def post(self, request):
        query = request.POST["query"]
        if query:
            user = User.objects.filter(
                name__icontains=query, business=request.user.business
            )
        else:
            user = User.objects.filter(business=request.user.business)

        user_partial = BlockObject(
            template_name=self.template_name,
            context={"users": user, "business": request.user.business},
            block_name="users-list-container",
        )

        return Response(request, htmx_objects=[user_partial])
