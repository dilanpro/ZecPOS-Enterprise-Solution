from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import View

from core.htmx import BlockObject, Response

from ..forms import ChangeMarkPriceForm, ProductForm
from ..models import Product
from . import AuthMixin


class ProductsDashboardView(AuthMixin, View):
    template_name = "pages/inventory/products/index.html"

    def get(self, request):
        products = request.user.business.products.all()
        category_query = request.GET.get("category", False)
        if category_query:
            products = products.filter(category=category_query)

        return render(
            request,
            self.template_name,
            context={"products": products, "category_query": category_query},
        )


class ProductsActionView(AuthMixin, View):
    template_name = "pages/inventory/products/action.html"

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
    template_name = "pages/inventory/products/index.html"

    def post(self, request):
        query = request.POST["query"]
        if query:
            products = Product.objects.filter(
                title__icontains=query, business=request.user.business
            )
        else:
            products = request.user.business.products.all()

        category_query = request.GET.get("category", False)
        if category_query:
            products = products.filter(category=category_query)

        user_partial = BlockObject(
            template_name=self.template_name,
            context={"products": products},
            block_name="products-list-container",
        )

        return Response(request, htmx_objects=[user_partial])


class ProductCreateView(AuthMixin, View):
    template_name = "pages/inventory/products/create.html"
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
    template_name = "pages/inventory/products/edit.html"
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


class ProductsRelatedGRNItemsView(AuthMixin, View):
    template_name = "pages/inventory/products/related-grns.html"

    def get(self, request, product_id: int):
        product = get_object_or_404(
            Product, id=product_id, business=request.user.business
        )

        grn_items = product.items.filter(quantity__gt=0, is_finalized=True)  # type: ignore

        return render(
            request,
            self.template_name,
            context={"grn_items": grn_items},
        )


class ChangeMarkPriceView(AuthMixin, View):
    template_name = "pages/inventory/products/mark-price-change.html"
    form = ChangeMarkPriceForm

    def get(self, request, product_id: int):

        form = self.form()

        product = get_object_or_404(
            Product, id=product_id, business=request.user.business
        )

        return render(
            request,
            self.template_name,
            context={"form": form, "product": product},
        )

    def post(self, request, product_id: int):
        product = get_object_or_404(
            Product, id=product_id, business=request.user.business
        )

        form = self.form(request.POST)
        if form.is_valid():
            new_price = form.cleaned_data["new_price"]
            product.items.filter(quantity__gt=0, is_finalized=True).update(price=new_price)  # type: ignore

            messages.success(request, message="Price Changed Successfully")
            return redirect(reverse("products-related-grns", args=[product_id]))
        else:
            messages.error(request, message=form.get_first_error())

        return render(
            request, self.template_name, context={"form": form, "product": product}
        )


class ProductsRelatedSRsView(AuthMixin, View):
    template_name = "pages/inventory/products/related-srs.html"

    def get(self, request, product_id: int):
        product = get_object_or_404(
            Product, id=product_id, business=request.user.business
        )

        grn_items = product.items.all()  # type: ignore

        related_srs = []
        for _grn_item in grn_items:
            if _grn_item.srs.exists():
                related_srs.extend(_grn_item.srs.all())
        related_srs = sorted(related_srs, key=lambda x: int(x.id), reverse=True)
        return render(
            request,
            self.template_name,
            context={"srs": related_srs},
        )
