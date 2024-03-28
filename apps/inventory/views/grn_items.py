from django.shortcuts import get_object_or_404
from django.views.generic import View

from core.htmx import BlockObject, Response

from ..forms import GRNItemsForm
from ..models import GRN, GRNItem
from . import AuthMixin


class GRNItemCreateView(AuthMixin, View):
    template_name = "pages/inventory/grn-action.html"
    form = GRNItemsForm

    def get(self, request, grn_id: int):
        form = self.form()
        grn = get_object_or_404(GRN, id=grn_id, business=request.user.business)

        modal_block = BlockObject(
            template_name=self.template_name,
            context={"grn_item_form": form, "grn": grn, "grn_item_create_modal": True},
            block_name="grn-item-create-modal",
        )
        return Response(request, htmx_objects=[modal_block])

    def post(self, request, grn_id: int):
        form = self.form(request.POST)
        grn = get_object_or_404(
            GRN, id=grn_id, business=request.user.business, is_finalized=False
        )
        if form.is_valid():
            grn_item = form.save(commit=False)
            grn_item.grn = grn
            grn_item.business = request.user.business
            grn_item.created_by = request.user
            grn_item.calculate_cost()
            grn_item.save()

            grn_action_block = BlockObject(
                template_name=self.template_name,
                context={"grn": grn},
                block_name="content",
            )
            return Response(
                request,
                htmx_objects=[grn_action_block],
                success_message="GRN Item Created Successfully",
            )

        modal_block = BlockObject(
            template_name=self.template_name,
            context={"grn_item_form": form, "grn_item_create_modal": True},
            block_name="grn-item-create-modal",
        )
        return Response(
            request, htmx_objects=[modal_block], error_message=form.get_first_error()
        )


class GRNItemCloneView(AuthMixin, View):
    template_name = "pages/inventory/grn-action.html"
    form = GRNItemsForm

    def get(self, request, grn_id: int, grn_item_id: int):
        grn = get_object_or_404(
            GRN, id=grn_id, business=request.user.business, is_finalized=False
        )
        grn_item = get_object_or_404(
            GRNItem, id=grn_item_id, grn=grn, business=request.user.business
        )
        form = self.form(instance=grn_item)

        modal_block = BlockObject(
            template_name=self.template_name,
            context={"grn_item_form": form, "grn": grn, "grn_item_create_modal": True},
            block_name="grn-item-create-modal",
        )
        return Response(request, htmx_objects=[modal_block])


class GRNItemEditView(AuthMixin, View):
    template_name = "pages/inventory/grn-action.html"
    form = GRNItemsForm

    def get(self, request, grn_id: int, grn_item_id: int):
        grn = get_object_or_404(GRN, id=grn_id, business=request.user.business)
        grn_item = get_object_or_404(
            GRNItem, id=grn_item_id, grn=grn, business=request.user.business
        )

        form = self.form(instance=grn_item)

        modal_block = BlockObject(
            template_name=self.template_name,
            context={
                "grn_item_form": form,
                "grn": grn,
                "grn_item_create_modal": True,
                "edit": True,
                "grn_item": grn_item,
            },
            block_name="grn-item-create-modal",
        )
        return Response(request, htmx_objects=[modal_block])

    def post(self, request, grn_id: int, grn_item_id: int):
        grn = get_object_or_404(
            GRN, id=grn_id, business=request.user.business, is_finalized=False
        )
        grn_item = get_object_or_404(
            GRNItem, id=grn_item_id, grn=grn, business=request.user.business
        )
        form = self.form(request.POST, instance=grn_item)

        if form.is_valid():
            grn_item = form.save(commit=False)
            grn_item.calculate_cost()
            grn_item.save()

            grn_action_block = BlockObject(
                template_name=self.template_name,
                context={"grn": grn},
                block_name="content",
            )
            return Response(
                request,
                htmx_objects=[grn_action_block],
                success_message="GRN Item Modified Successfully",
            )

        modal_block = BlockObject(
            template_name=self.template_name,
            context={
                "grn_item_form": form,
                "grn_item_create_modal": True,
                "edit": True,
                "grn_item": grn_item,
            },
            block_name="grn-item-create-modal",
        )
        return Response(
            request, htmx_objects=[modal_block], error_message=form.get_first_error()
        )


class GRNItemDeleteView(AuthMixin, View):
    template_name = "pages/inventory/grn-action.html"
    form = GRNItemsForm

    def get(self, request, grn_id: int, grn_item_id: int):
        grn = get_object_or_404(
            GRN, id=grn_id, business=request.user.business, is_finalized=False
        )
        grn_item = get_object_or_404(
            GRNItem, id=grn_item_id, grn=grn, business=request.user.business
        )
        grn_item.delete()

        grn_action_block = BlockObject(
            template_name=self.template_name,
            context={"grn": grn},
            block_name="content",
        )
        return Response(
            request,
            htmx_objects=[grn_action_block],
            success_message="GRN Item Deleted Successfully",
        )
