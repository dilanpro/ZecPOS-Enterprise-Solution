from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class ProductsDashboardView(View):
    def get(self, request):
        return render(request, "pages/inventory/products.html")


class CategoriesDashboardView(View):
    def get(self, request):
        return render(request, "pages/inventory/categories.html")


class SuppliersDashboardView(View):
    def get(self, request):
        return render(request, "pages/inventory/suppliers.html")
