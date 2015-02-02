from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from List.forms import UserForm


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
		
def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save
			registered = True
		else:
			print user_form.errors
	else:
		user_form = UserForm()
	template = loader.get_template('List/register.html')
	context = RequestContext(request, {
		'user_form': user_form, 
		'registered': registered,
		})
	return HttpResponse(template.render(context))		
	#return render(request, 'List/register.html', {'user_form': user_form, 'registered': registered})