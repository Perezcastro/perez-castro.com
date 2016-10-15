from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^aboutme',views.aboutMe,name='about_me'),
    url(r'^cv',views.cv,name='curriculum'),
]


"""

    url(r'^creations/$', views.creations),
    url(r'^creations/(?P<num>[0-9]{4})/$', views.creations,name='creations'),

"""