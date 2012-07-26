from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('django_books.views',
    url(r'^$', 'test')
)
