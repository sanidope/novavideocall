from . import views
from django.urls import path, re_path


app_name = 'publishapp'

urlpatterns = [

    re_path(r'^posts/$', views.post_list, name='post_list'),
    re_path(r'^posts/detail/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^posts/tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_slug'),

]
