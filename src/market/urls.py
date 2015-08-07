from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from profiles.views import *
from market.views import my_custom_404_view

admin.autodiscover()
handler404 = my_custom_404_view
urlpatterns = [
    url(r'^accounts/signup/$', 'profiles.views.register', name='register') ,
    url (r'^accounts/signin/$', 'profiles.views.signin', name='signin'),
    url (r'^accounts/signout/$', 'profiles.views.signout', name='signout') ,
    url (r'^accounts/signup_confirm/(?P<confirm_code>\w{1,40})/$', 'profiles.views.signup_confirm', name='signup_confirm') ,
    #url(r'^auth/', include('allauth.urls')),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', 'market.views.home', name="home"),
    #url(r'^lib/', 'profiles.views.register', name='register'),
    url(r'^products/', include('products.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)