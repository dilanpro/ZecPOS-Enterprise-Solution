from django.contrib.auth.mixins import UserPassesTestMixin


class AuthMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.has_stock_access()  # type: ignore
