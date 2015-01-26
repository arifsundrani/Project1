from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect


from List.models import Task
# Create your views here.
def list(request):
	todo_list = Task.objects.all()
	template = loader.get_template('List/list.html')
	context = RequestContext(request, {
		'todo_list': todo_list,
	})
	#output = '\n '.join([t.task_text for t in todo_list])
	return HttpResponse(template.render(context))
def index(request):
	todo_list = Task.objects.all()
	context = {'ToDo_List':todo_list}
	return render(request, 'List/index.html', context)


