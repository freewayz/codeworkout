__author__ = 'pitaside'



from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns(
    '',
     url(r'^$', view=index_page, name="index"),
    url(r'^payment/$', view=checkout_payment, name="payment")
)