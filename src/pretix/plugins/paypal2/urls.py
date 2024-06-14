from django.urls import include, re_path

from .views import (
    PayView, XHRView, abort, isu_disconnect, isu_return, redirect_view,
    success, webhook,
)

event_patterns = [
    re_path(r'^paypal2/', include([
        re_path(r'^abort/$', abort, name='abort'),
        re_path(r'^return/$', success, name='return'),
        re_path(r'^redirect/$', redirect_view, name='redirect'),
        re_path(r'^xhr/$', XHRView.as_view(), name='xhr'),
        re_path(r'^pay/(?P<order>[^/]+)/(?P<hash>[^/]+)/(?P<payment>[^/]+)/$', PayView.as_view(), name='pay'),
        re_path(r'^(?P<order>[^/][^w]+)/(?P<secret>[A-Za-z0-9]+)/xhr/$', XHRView.as_view(), name='xhr'),

        re_path(r'w/(?P<cart_namespace>[a-zA-Z0-9]{16})/abort/', abort, name='abort'),
        re_path(r'w/(?P<cart_namespace>[a-zA-Z0-9]{16})/return/', success, name='return'),
        re_path(r'w/(?P<cart_namespace>[a-zA-Z0-9]{16})/xhr/', XHRView.as_view(), name='xhr'),
    ])),
]

urlpatterns = [
    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/paypal2/disconnect/', isu_disconnect,
            name='isu.disconnect'),
    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/paypal/return/$', isu_return, name='isu.return'),
    re_path(r'^_paypal/webhook/$', webhook, name='webhook'),
]
