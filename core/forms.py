class FormFirstErrorTrackingMixin:
    """Mixin to track first error in form."""

    def get_first_error(self):
        return next(iter(self.errors.items()))[1][0]  # type: ignore
