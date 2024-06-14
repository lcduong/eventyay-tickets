from django.urls import include, re_path

from .views import abort, oauth_disconnect, redirect_view, success

event_patterns = [
    re_path(r'^paypal/', include([
        re_path(r'^abort/$', abort, name='abort'),
        re_path(r'^return/$', success, name='return'),
        re_path(r'^redirect/$', redirect_view, name='redirect'),

        re_path(r'w/(?P<cart_namespace>[a-zA-Z0-9]{16})/abort/', abort, name='abort'),
        re_path(r'w/(?P<cart_namespace>[a-zA-Z0-9]{16})/return/', success, name='return'),
    ])),
]

urlpatterns = [
    re_path(r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/paypal/disconnect/',
            oauth_disconnect, name='oauth.disconnect'),
]
