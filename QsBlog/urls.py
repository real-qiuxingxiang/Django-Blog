from django.contrib import admin
from django.conf.urls import *
from blog.views import TagListView, BlogListView, TagDetailView, RSSFeed, BlogDetailView
import xadmin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = [
    # Admin
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),
    url(r'^simditor/', include('simditor.urls')),

    # Index BlogList
    url(r'^$', BlogListView.as_view(), name='index'),

    # Tag
    url(r'^tag/$', TagListView.as_view(), name='tag_list'),
    url(r'^tag/(?P<id>[a-zA-Z0-9])+/$', TagDetailView.as_view(), name='tag_detail'),

    # About
    url(r'^about/', BlogListView.as_view(), name='about'),

    # RSS
    url(r'^feed/$', RSSFeed(), name="RSS"),

    # Blog Detail Page
    url(r'^blog/(?P<pk>[0-9])+/$', BlogDetailView.as_view(), name="blog_detail"),

    # Haystack Search
    url(r'^search/', include('haystack.urls')),
    url(r'', include('comments.urls')),
]


# Simditor Markdown Upload
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
