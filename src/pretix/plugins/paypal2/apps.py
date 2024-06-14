from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from pretix import __version__ as version


class Paypal2App(AppConfig):
    name = 'pretix.plugins.paypal2'
    verbose_name = "PayPal"

    class PretixPluginMeta:
        name = "PayPal"
        author = _("the pretix team")
        version = version
        category = 'PAYMENT'
        featured = True
        picture = 'pretixplugins/paypal2/paypal_logo.svg'
        description = _("Accept payments with your PayPal account. In addition to regular PayPal payments, you can now "
                        "also offer payments in a variety of local payment methods such as giropay, SOFORT, iDEAL and "
                        "many more to your customers - they don't even need a PayPal account. PayPal is one of the "
                        "most popular payment methods world-wide.")

    def ready(self):
        from . import signals  # NOQA

    def is_available(self, event):
        return 'pretix.plugins.paypal' not in event.plugins.split(',')
