from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from List.models import Task
from List.complete import complete
# Create your views here.
def list(request):
	todo_list = Task.objects.filter(completed=False)
	template = loader.get_template('List/list.html')
	context = RequestContext(request, {
		'todo_list': todo_list,
	})
  #	if(request.GET.get('Complete')):
  	#	complete.setTrue()
	#	todo_list = Task.objects.filter(completed=False)		
  	#	return HttpResponse(template.render(context))
	return HttpResponse(template.render(context))	
	
def index(request):
	todo_list = Task.objects.all()
	context = {'ToDo_List':todo_list}
	return render(request, 'List/index.html', context)
	
def add(request):
    if request.POST:
        form = AddExternalItemForm(request.POST)

        if form.is_valid():
            if(request.GET.get('Add')):
            # Don't commit the save until we've added in the fields we need to set
            	item = form.save(commit=False)
            	item.list_id = settings.DEFAULT_LIST_ID
            	item.save()
            	return HttpResponseRedirect(reverse('list.html'))