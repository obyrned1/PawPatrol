from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^signed_in/$', views.signed_in, name="signed_in")
]
