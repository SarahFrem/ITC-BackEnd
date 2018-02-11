from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'), #path /
    url(r'^login$', views.login_page, name='login'),
    url(r'^registration$', views.register_page, name='registration'),
    url(r'^board$', views.board_page, name='board'),
    url(r'^board/datas$', views.add_message_DB, name='datas')
]