from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from List.models import Task
# Create your views here.
def index(request):
	todo_list = Task.objects.all()
	context = {'ToDo_List':todo_list}
	return render(request, 'List/index.html', context)