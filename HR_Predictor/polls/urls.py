from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    url('form/', views.form),
    url('output/', views.form),
    # url('output/', views.tabs),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)