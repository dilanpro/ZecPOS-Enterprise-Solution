from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from apps.user.forms import UserCreateForm
from apps.user.models import Business, User


class TeamIndexView(View):
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


class UserCreateView(View):
    template_name: str = "pages/team/user-create.html"
    form = UserCreateForm

    def get(self, request):
        form = self.form()
        return render(request, template_name=self.template_name, context={"form": form})

    def post(self, request):
        business = request.user.business
        if business.available_license_count() <= 0:
            messages.error(request, "No available license to add new user")
            return redirect(reverse("team-users"))

        form = self.form(request.POST)
        if form.is_valid():
            user: User = form.save()
            user.password = make_password(user.password)
            user.business = business
            user.save()
            messages.success(request, "User created successfully")
            return redirect(reverse("team-users"))

        else:
            error = form.get_first_error()
            messages.error(request, error)

        return render(request, template_name=self.template_name, context={"form": form})


class UserEditView(View):
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
            return redirect(reverse("team-users"))

        else:
            error = form.get_first_error()
            messages.error(request, error)

        return render(request, template_name=self.template_name, context={"form": form})


class UserDeleteView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id, business=request.user.business)
        if user == request.user:
            messages.error(request, "You can't delete yourself")
            return redirect(reverse("team-users"))

        user.delete()
        messages.success(request, "User deleted successfully")
        return redirect(reverse("team-users"))
