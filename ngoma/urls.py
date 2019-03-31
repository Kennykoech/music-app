from django.conf.urls import url
from ngoma import views


app_name ='ngoma'

urlpatterns = [
    #display user menu
    # url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    #display user songs
    url(r'^$', views.IndexView.as_view(), name='index'),
    #display admin menu
    url(r'^kenny/$', views.KennyIndexView.as_view(), name='kenny_index'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    # Kenny_admin functionalities 
    url(r'^(?P<pk>[0-9]+)$', views.Songupdate.as_view(), name='song-update'),
    url(r'song/add/$', views.Songcreate.as_view(), name='song-add'),
    url(r'song/(?P<pk>[0-9]+)/delete/$', views.Songdelete.as_view(), name='song-delete'),
    

        ]
