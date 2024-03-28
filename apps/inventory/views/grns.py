from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import View

from core.htmx import BlockObject, Response

from ..forms import GRNCreateEditForm, GRNDiscountsForm
from ..models import GRN, Supplier
from . import AuthMixin


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


class GRNDeleteView(AuthMixin, View):

    def get(self, request, grn_id: int):
        grn = get_object_or_404(
            GRN, id=grn_id, business=request.user.business, is_finalized=False
        )
        grn.delete()

        return redirect("grns", supplier_id=grn.supplier.id)  # type: ignore


class GRNEditView(AuthMixin, View):
    template_name = "pages/inventory/grn-action.html"
    form = GRNCreateEditForm

    def get(self, request, grn_id: int):
        grn = get_object_or_404(GRN, id=grn_id, business=request.user.business)
        form = self.form(instance=grn)

        modal_block = BlockObject(
            template_name=self.template_name,
            context={
                "grn_edit_form": form,
                "grn": grn,
                "grn_edit_modal": True,
            },
            block_name="grn-edit-modal",
        )
        return Response(request, htmx_objects=[modal_block])

    def post(self, request, grn_id: int):
        grn = get_object_or_404(
            GRN, id=grn_id, business=request.user.business, is_finalized=False
        )
        form = self.form(request.POST, instance=grn)

        if form.is_valid():
            grn = form.save()

            grn_action_block = BlockObject(
                template_name=self.template_name,
                context={"grn": grn},
                block_name="content",
            )
            return Response(
                request,
                htmx_objects=[grn_action_block],
                success_message="GRN Modified Successfully",
            )

        modal_block = BlockObject(
            template_name=self.template_name,
            context={
                "grn_edit_form": form,
                "grn_edit_modal": True,
            },
            block_name="grn-edit-modal",
        )
        return Response(
            request, htmx_objects=[modal_block], error_message=form.get_first_error()
        )


class GRNDiscountsView(AuthMixin, View):
    template_name = "pages/inventory/grn-action.html"
    form = GRNDiscountsForm

    def get(self, request, grn_id: int):
        grn = get_object_or_404(GRN, id=grn_id, business=request.user.business)
        form = self.form(instance=grn)

        modal_block = BlockObject(
            template_name=self.template_name,
            context={
                "grn_discounts_form": form,
                "grn": grn,
                "grn_discounts_modal": True,
            },
            block_name="grn-discounts-modal",
        )
        return Response(request, htmx_objects=[modal_block])

    def post(self, request, grn_id: int):
        grn = get_object_or_404(
            GRN, id=grn_id, business=request.user.business, is_finalized=False
        )
        form = self.form(request.POST, instance=grn)

        if form.is_valid():
            grn = form.save()

            grn_action_block = BlockObject(
                template_name=self.template_name,
                context={"grn": grn},
                block_name="content",
            )
            return Response(
                request,
                htmx_objects=[grn_action_block],
                success_message="Discounts Added Successfully",
            )

        modal_block = BlockObject(
            template_name=self.template_name,
            context={
                "grn_discounts_form": form,
                "grn_discounts_modal": True,
            },
            block_name="grn-discounts-modal",
        )
        return Response(
            request, htmx_objects=[modal_block], error_message=form.get_first_error()
        )


class GRNFinalizeView(AuthMixin, View):

    def get(self, request, grn_id: int):
        grn = get_object_or_404(GRN, id=grn_id, business=request.user.business)
        grn.finalize(finalized_by=request.user)
        return redirect("grn-action", grn_id=grn.id)  # type: ignore


class GRNCreateView(AuthMixin, View):
    template_name = "pages/inventory/grns.html"
    form = GRNCreateEditForm

    def get(self, request, supplier_id: int):
        form = self.form()
        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )
        modal_block = BlockObject(
            template_name=self.template_name,
            context={
                "grn_create_form": form,
                "grn_create_modal": True,
                "supplier": supplier,
            },
            block_name="grn-create-modal",
        )
        return Response(request, htmx_objects=[modal_block])

    def post(self, request, supplier_id: int):
        form = self.form(request.POST)

        supplier = get_object_or_404(
            Supplier, id=supplier_id, business=request.user.business
        )

        if form.is_valid():
            grn = form.save(commit=False)
            grn.supplier = supplier
            grn.business = request.user.business
            grn.created_by = request.user
            grn.save()

            return Response(
                request,
                success_message="GRN Created Successfully",
                redirect_uri=reverse("grn-action", args=[grn.id]),  # type: ignore
            )

        modal_block = BlockObject(
            template_name=self.template_name,
            context={
                "grn_create_form": form,
                "grn_create_modal": True,
            },
            block_name="grn-create-modal",
        )
        return Response(
            request, htmx_objects=[modal_block], error_message=form.get_first_error()
        )
