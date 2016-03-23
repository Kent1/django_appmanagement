from django.conf.urls import url
from django.conf import settings

from .views import ApplicationListView, ApplicationDetailView, ApplicationCreateView, ApplicationEditView

urlpatterns = [
    # /app
    url(r'^$', ApplicationListView.as_view(), name='list'),
    # /app/add/
    url(r'^add/$', ApplicationCreateView.as_view(), name='add'),
    # /app/app_name/
    url(r'^(?P<slug>\w+)/$', ApplicationDetailView.as_view(), name='detail'),
    # /app/app_name/edit
    url(r'^(?P<slug>\w+)/edit/$', ApplicationEditView.as_view(), name='edit'),
    # /uploaded_apps/file
    url(r'^uploaded_apps/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
]
