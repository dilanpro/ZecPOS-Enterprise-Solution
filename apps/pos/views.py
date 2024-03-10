from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views import View


class AuthMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_pos_access()


class PosDashboardView(AuthMixin, View):

    def get(self, request):
        return render(request, "pages/pos/pos.html")
