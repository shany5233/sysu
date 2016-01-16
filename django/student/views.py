#! /usr/bin/python
# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponseRedirect

def dashboard(request):
	userName = request.session.get('current_user', '')

	user = {'userName': userName}

	return render(request,'dashboard.html',{'user': user,})

def image_collocation(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('image_collocation.html',data)
def project(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('project.html',data)
def common_image_details(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('common_image_details.html',data)
def login(request):
	request.session['current_user'] = request.POST['userName']
	return HttpResponseRedirect('/project/')

def logout(request):
	del request.session['current_user']
	return HttpResponseRedirect('/dashboard/')

def register(request):
	return login(request)

def image_manage(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('image_manage.html',data)

def app_manage(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('app_manage.html',data)

def app_create(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('app_create.html',data)

#创建项目
def create_project(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('create_project.html',data)

#部署
def deploy(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('deploy.html',data)

#详细信息页
def app_detail(request):
	data = {'user': {'userName': request.session.get('current_user','')},}
	return render_to_response('app_detail.html',data)