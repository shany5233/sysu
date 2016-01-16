"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from djangoProject import settings
from student.views import dashboard, image_collocation, project,login,logout,register,image_manage,app_manage,app_create,create_project,deploy,app_detail, \
    common_image_details

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/',dashboard, name='dashboard'),
    url(r'^image_collocation/$',image_collocation, name='image_coll'),
    url(r'^common_image_details/$', common_image_details,name='common_image_details'),
    url(r'^project/$',project,name='project'),
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^register/$',register,name='register'),
    url(r'^image_manage/$',image_manage,name='image_manage'),
    url(r'^app_manage/$',app_manage,name="app_manage"),
    url(r'^app_create/$',app_create,name="app_create"),
    #new
    url(r'^create_project/$',create_project, name="create_project"),
    url(r'^deploy/$', deploy, name="deploy"),
    url(r'^app_detail/$', app_detail, name="app_detail"),

    #url(r'/(?P<path>.*)','django.views.static.serve',{'document_root':settings.STATIC_DIR,'show_indexes':False}),
]
