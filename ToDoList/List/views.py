from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView


from List.models import Task
from List.complete import complete, add
# Create your views here.
def list(request):
	todo_list = Task.objects.all()
	if(request.POST.get('Add')):
  		titem = Task(task_text=request.POST.get('Task'))
  		titem.save()
  	elif(request.POST.get('complete') and todo_list and request.POST.get('listid')>0):
  		pk = request.POST.get('listid')
  		litem = get_object_or_404(Task, id = pk)
  		litem.delete()
  	todo_list = Task.objects.all()
	template = loader.get_template('List/list.html')
	context = RequestContext(request, {
		'todo_list': todo_list,
	})
	return HttpResponse(template.render(context))	
	
def index(request):
	todo_list = Task.objects.all()
	context = {'ToDo_List':todo_list}
	return render(request, 'List/index.html', context)
	
#def item(request, task_id):
#	if(request.GET.get('complete')):
#		titem = get_object_or_404(Task, pk=task_id)
#		titem.delete()
#		return render(request, 'List/list.html', {'task': task})
#	task = get_object_or_404(Task, pk=task_id)
#	return render(request, 'List/item.html', {'task': task})
	

	
