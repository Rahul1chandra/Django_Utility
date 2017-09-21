# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from myapp.tasks import addvalues




def simpleview(request):
	response = addvalues.delay(2,3)
	celery_result ={
		"result" : response.result,
		"task_id" : response.id,
		"task_name": response.task_name,
		"state": response.state,
	}
	return HttpResponse("Simple Response")
