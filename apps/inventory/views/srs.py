import django.contrib
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from core.htmx import BlockObject, Response

from ..forms import SRCreateEditForm
from ..models import SR, Supplier
from . import AuthMixin


class SRDashboardView(AuthMixin, View):
    template_name = "pages/inventory/srs/index.html"

    def get(self, request, supplier_id: int):
        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )
        return render(
            request,
            self.template_name,
            context={"srs": supplier.srs.all(), "supplier": supplier},  # type: ignore
        )


class SRCreateView(AuthMixin, View):
    template_name = "pages/inventory/srs/create.html"
    form = SRCreateEditForm

    def get(self, request, supplier_id: int):
        form = self.form()

        return render(request, template_name=self.template_name, context={"form": form})

    def post(self, request, supplier_id: int):
        form = self.form(request.POST)

        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )

        if form.is_valid():
            sr = form.save(commit=False)
            sr.supplier = supplier
            sr.business = request.user.business
            sr.created_by = request.user
            sr.save()

            messages.success(request, "SR Created Successfully")
            return redirect("sr-action", sr_id=sr.id)

        return render(request, template_name=self.template_name, context={"form": form})


class SRActionView(AuthMixin, View):
    template_name = "pages/inventory/srs/action.html"

    def get(self, request, sr_id: int):
        sr = get_object_or_404(SR, id=sr_id, business=request.user.business)
        return render(
            request,
            self.template_name,
            context={"sr": sr},
        )


class SRDeleteView(AuthMixin, View):
    def get(self, request, sr_id: int):
        sr = get_object_or_404(
            SR, id=sr_id, business=request.user.business, is_finalized=False
        )
        sr.delete()

        return redirect("srs", supplier_id=sr.supplier.id)  # type: ignore


class SRSearchView(AuthMixin, View):
    template_name = "pages/inventory/srs/index.html"

    def post(self, request, supplier_id: int):
        query = request.POST["query"]
        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )
        if query:
            srs = supplier.srs.all().filter(  # type: ignore
                title__icontains=query, business=request.user.business
            )
        else:
            srs = supplier.srs.all()  # type: ignore

        user_partial = BlockObject(
            template_name=self.template_name,
            context={"srs": srs, "supplier": supplier},
            block_name="sr-list-container",
        )

        return Response(request, htmx_objects=[user_partial])
