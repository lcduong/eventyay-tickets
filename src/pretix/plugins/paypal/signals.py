from django.dispatch import receiver

from pretix.base.signals import logentry_display, register_payment_providers


@receiver(register_payment_providers, dispatch_uid="payment_paypal")
def register_payment_provider(sender, **kwargs):
    from .payment import Paypal
    return Paypal


@receiver(signal=logentry_display, dispatch_uid="paypal_logentry_display")
def pretixcontrol_logentry_display(sender, logentry, **kwargs):
    from pretix.plugins.paypal2.signals import pretixcontrol_logentry_display

    return pretixcontrol_logentry_display(sender, logentry, **kwargs)
