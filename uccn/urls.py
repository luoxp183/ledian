from django.conf.urls import url
from uccn import views

urlpatterns = [
    url(r'^base/',views.base),
    url(r'^info/',views.info),
    url(r'^show/',views.show),
    url(r'^goods/',views.goods),
    url(r'^contact/',views.contact),
    url(r'^manage/',views.manage),
    url(r'^service/',views.service),


]
