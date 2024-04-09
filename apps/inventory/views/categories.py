from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from core.htmx import BlockObject, Response

from ..forms import CategoryForm
from ..models import Category
from . import AuthMixin


class CategoriesDashboardView(AuthMixin, View):
    template_name = "pages/inventory/categories/index.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={"categories": request.user.business.categories.all()},
        )


class CategoriesActionView(AuthMixin, View):
    template_name = "pages/inventory/categories/action.html"

    def get(self, request, category_id: int):
        category = get_object_or_404(
            Category, id=category_id, business=request.user.business
        )
        return render(
            request,
            self.template_name,
            context={"category": category},
        )


class CategorySearchView(AuthMixin, View):
    template_name = "pages/inventory/categories/index.html"

    def post(self, request):
        query = request.POST["query"]
        if query:
            categories = Category.objects.filter(
                title__icontains=query, business=request.user.business
            )
        else:
            categories = request.user.business.categories.all()

        user_partial = BlockObject(
            template_name=self.template_name,
            context={"categories": categories},
            block_name="categories-list-container",
        )

        return Response(request, htmx_objects=[user_partial])


class CategoryCreateView(AuthMixin, View):
    template_name = "pages/inventory/categories/create.html"
    form = CategoryForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.business = request.user.business
            category.created_by = request.user
            category.save()

            messages.success(request, message="Category Created Successfully")
            return redirect("categories")
        else:
            messages.error(request, message=form.get_first_error())

        return render(request, self.template_name, {"form": form})


class CategoryEditView(AuthMixin, View):
    template_name = "pages/inventory/categories/edit.html"
    form = CategoryForm

    def get(self, request, category_id):
        category = get_object_or_404(
            Category, id=category_id, business=request.user.business
        )
        form = self.form(instance=category)
        return render(request, self.template_name, {"form": form})

    def post(self, request, category_id):
        category = get_object_or_404(
            Category, id=category_id, business=request.user.business
        )
        form = self.form(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, message="Category Edited Successfully")
            return redirect("categories")
        else:
            messages.error(request, message=form.get_first_error())

        return render(request, self.template_name, {"form": form})
