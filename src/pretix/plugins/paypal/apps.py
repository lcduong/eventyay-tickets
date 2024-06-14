from django.apps import AppConfig
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from pretix import __version__ as version


class PaypalApp(AppConfig):
    name = 'pretix.plugins.paypal'
    verbose_name = _("PayPal")

    class PretixPluginMeta:
        name = _("PayPal")
        author = _("the pretix team")
        version = version
        category = 'PAYMENT'
        featured = True
        picture = 'pretixplugins/paypal/paypal_logo.svg'
        description = _("Accept payments with your PayPal account. PayPal is one of the most popular payment methods "
                        "world-wide.")

    def ready(self):
        from . import signals  # NOQA

    def is_available(self, event):
        return 'pretix.plugins.paypal' in event.plugins.split(',')

    @cached_property
    def compatibility_errors(self):
        errs = []
        try:
            import paypalrestsdk  # NOQA
        except ImportError:
            errs.append("Python package 'paypalrestsdk' is not installed.")
        return errs
