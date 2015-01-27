from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib import auth
from django.core.context_processors import csrf



from List.models import Task
from List.complete import complete, add
# Create your views here.
def list(request):
	#if(request.POST):
	#	if "Add" in request.POST:
	if(request.GET.get('Add')):
  		titem = Task(task_text=request.GET.get('Task'))
  		titem.save()
  	elif(request.GET.get('complete')):
  		litem = Task.objects.get(id = request.GET.get('listid'))
  		litem.completed = True
  		litem.save()
	todo_list = Task.objects.filter(completed=False)		
	template = loader.get_template('List/list.html')
	context = RequestContext(request, {
		'todo_list': todo_list,
	})
 
	return HttpResponse(template.render(context))	
	
def index(request):
	todo_list = Task.objects.all()
	context = {'ToDo_List':todo_list}
	return render(request, 'List/index.html', context)
	
def item(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	return render(request, 'List/item.html', {'task': task})
	
def complete(request,todo_id):
	items = Task.objects.all()
	if request.method =="POST":
		try:
			litem = Task.objects.get(id = request.POST['todo_id'])
			litem.completed = not litem.completed
			litem.save()
		except Task.DoesNotExist:
			pass
	return render_to_response("list.html", {'items':items})
    #return HttpResponseRedirect(reverse("admin:todo_list"))
    #return render_to_response('List/list.html')
	
def request_page(request):
  if(request.POST.get('btn')):
  	    Todo.objects.get(id=todo_id).completed = True    
  return render('List/list.html')





# for user authentication

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username})

def invalid_login(reqeust):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')


