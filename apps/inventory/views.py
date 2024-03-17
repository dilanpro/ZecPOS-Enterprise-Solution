from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from core.htmx import BlockObject, Response

from .forms import CategoryForm, SupplierForm
from .models import Category, Supplier


class AuthMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_stock_access()  # type: ignore


class ProductsDashboardView(AuthMixin, View):
    def get(self, request):
        return render(request, "pages/inventory/products.html")


class CategoriesDashboardView(AuthMixin, View):
    template_name = "pages/inventory/categories.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={"categories": request.user.business.categories.all()},
        )


class CategorySearchView(AuthMixin, View):
    template_name = "pages/inventory/categories.html"

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
    template_name = "pages/inventory/category-create.html"
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
    template_name = "pages/inventory/category-edit.html"
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


class SuppliersDashboardView(AuthMixin, View):
    template_name = "pages/inventory/suppliers.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={"suppliers": request.user.business.suppliers.all()},
        )


class SupplerSearchView(AuthMixin, View):
    template_name = "pages/inventory/suppliers.html"

    def post(self, request):
        query = request.POST["query"]
        if query:
            suppliers = Supplier.objects.filter(
                name__icontains=query, business=request.user.business
            )
        else:
            suppliers = request.user.business.suppliers.all()

        user_partial = BlockObject(
            template_name=self.template_name,
            context={"suppliers": suppliers},
            block_name="supplier-list-container",
        )

        return Response(request, htmx_objects=[user_partial])


class SupplierCreateView(AuthMixin, View):
    template_name = "pages/inventory/supplier-create.html"
    form = SupplierForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.business = request.user.business
            supplier.created_by = request.user
            supplier.save()

            messages.success(request, message="Supplier Created Successfully")
            return redirect("suppliers")
        else:
            messages.error(request, message=form.get_first_error())

        return render(request, self.template_name, {"form": form})


class SupplierEditView(AuthMixin, View):
    template_name = "pages/inventory/supplier-edit.html"
    form = SupplierForm

    def get(self, request, supplier_id):
        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )
        form = self.form(instance=supplier)
        return render(request, self.template_name, {"form": form})

    def post(self, request, supplier_id):
        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )
        form = self.form(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, message="Supplier Edited Successfully")
            return redirect("suppliers")
        else:
            messages.error(request, message=form.get_first_error())

        return render(request, self.template_name, {"form": form})
