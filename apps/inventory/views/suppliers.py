from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from core.htmx import BlockObject, Response

from ..forms import SupplierForm
from ..models import Supplier
from . import AuthMixin


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
