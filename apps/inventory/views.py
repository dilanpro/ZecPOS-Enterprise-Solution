from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import View

from core.htmx import BlockObject, Response

from .forms import CategoryForm, GRNForm, GRNItemsForm, ProductForm, SupplierForm
from .models import GRN, Category, Product, Supplier


class AuthMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_stock_access()  # type: ignore


class ProductsDashboardView(AuthMixin, View):
    template_name = "pages/inventory/products.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={"products": request.user.business.products.all()},
        )


class ProductsActionView(AuthMixin, View):
    template_name = "pages/inventory/product-action.html"

    def get(self, request, product_id: int):
        product = get_object_or_404(
            Product, id=product_id, business=request.user.business
        )
        return render(
            request,
            self.template_name,
            context={"product": product},
        )


class ProductSearchView(AuthMixin, View):
    template_name = "pages/inventory/products.html"

    def post(self, request):
        query = request.POST["query"]
        if query:
            products = Product.objects.filter(
                title__icontains=query, business=request.user.business
            )
        else:
            products = request.user.business.products.all()

        user_partial = BlockObject(
            template_name=self.template_name,
            context={"products": products},
            block_name="products-list-container",
        )

        return Response(request, htmx_objects=[user_partial])


class ProductCreateView(AuthMixin, View):
    template_name = "pages/inventory/product-create.html"
    form = ProductForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.business = request.user.business
            product.created_by = request.user
            product.save()

            messages.success(request, message="Product Created Successfully")
            return redirect("products")
        else:
            messages.error(request, message=form.get_first_error())

        return render(request, self.template_name, {"form": form})


class ProductEditView(AuthMixin, View):
    template_name = "pages/inventory/product-edit.html"
    form = ProductForm

    def get(self, request, product_id):
        product = get_object_or_404(
            Product, id=product_id, business=request.user.business
        )
        form = self.form(instance=product)
        return render(request, self.template_name, {"form": form})

    def post(self, request, product_id):
        product = get_object_or_404(
            Product, id=product_id, business=request.user.business
        )
        form = self.form(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, message="Product Edited Successfully")
            return redirect("products")
        else:
            messages.error(request, message=form.get_first_error())

        return render(request, self.template_name, {"form": form})


class CategoriesDashboardView(AuthMixin, View):
    template_name = "pages/inventory/categories.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={"categories": request.user.business.categories.all()},
        )


class CategoriesActionView(AuthMixin, View):
    template_name = "pages/inventory/category-action.html"

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


class SuppliersActionView(AuthMixin, View):
    template_name = "pages/inventory/supplier-action.html"

    def get(self, request, supplier_id: int):
        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )
        return render(
            request,
            self.template_name,
            context={"supplier": supplier},
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


class GRNDashboardView(AuthMixin, View):
    template_name = "pages/inventory/grns.html"

    def get(self, request, supplier_id: int):
        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )
        return render(
            request,
            self.template_name,
            context={"grns": supplier.grns.all(), "supplier": supplier},  # type: ignore
        )


class GRNActionView(AuthMixin, View):
    template_name = "pages/inventory/grn-action.html"

    def get(self, request, grn_id: int):
        grn = get_object_or_404(GRN, id=grn_id, business=request.user.business)
        return render(
            request,
            self.template_name,
            context={"grn": grn},
        )


class GRNSearchView(AuthMixin, View):
    template_name = "pages/inventory/grns.html"

    def post(self, request, supplier_id: int):
        query = request.POST["query"]
        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )
        if query:
            grns = supplier.grns.all().filter(  # type: ignore
                title__icontains=query, business=request.user.business
            )
        else:
            grns = supplier.grns.all()  # type: ignore

        user_partial = BlockObject(
            template_name=self.template_name,
            context={"grns": grns, "supplier": supplier},
            block_name="grn-list-container",
        )

        return Response(request, htmx_objects=[user_partial])


class GRNCreateView(AuthMixin, View):
    template_name = "pages/inventory/grn-create.html"
    form = GRNForm

    def get(self, request, supplier_id: int):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, supplier_id: int):
        form = self.form(request.POST)
        if form.is_valid():
            grn = form.save(commit=False)
            grn.supplier = get_object_or_404(
                Supplier, id=supplier_id, business=request.user.business
            )
            grn.business = request.user.business
            grn.created_by = request.user
            grn.save()

            messages.success(request, message="GRN Created Successfully")
            return redirect(reverse("grn-action", args=[grn.id]))
        else:
            messages.error(request, message=form.get_first_error())

        return render(request, self.template_name, {"form": form})


class GRNItemCreateView(AuthMixin, View):
    template_name = "pages/inventory/grn-items-create.html"
    form = GRNItemsForm

    def get(self, request, grn_id: int):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, grn_id: int):
        form = self.form(request.POST)
        if form.is_valid():
            grn_item = form.save(commit=False)
            grn_item.grn = get_object_or_404(
                GRN, id=grn_id, business=request.user.business
            )
            grn_item.business = request.user.business
            grn_item.created_by = request.user
            grn_item.calculate_cost()
            grn_item.save()

            messages.success(request, message="GRN Item Created Successfully")
            return redirect(reverse("grn-action", args=[grn_id]))
        else:
            messages.error(request, message=form.get_first_error())

        return render(request, self.template_name, {"form": form})
