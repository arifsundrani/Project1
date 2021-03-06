from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader


#from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from List.forms import UserForm
from List.models import Task
# Create your views here.
def list(request):
	todo_list = Task.objects.all()
	if(request.POST.get('Add')):
		titem = Task(task_text=request.POST.get('Task'))
		titem.save()
	elif(request.POST.get('complete') and todo_list and request.POST.get('listid')):
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
	
# for user authentication

def user_login(request):
	if (request.method == 'POST'):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/list/')
			else:
				return HttpResponse("Your account has been disabled.")
		else:
			return HttpResponseRedirect('/login_fail/')
	else:
		return render(request, 'List/login.html', {})

def login_fail(request):
	return render(request, 'List/login_fail.html', {})
	
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

		
def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print (user_form.errors)
	else:
		user_form = UserForm()
	return render(request, 'List/register.html', {'user_form': user_form,'registered': registered,})#HttpResponse(template.render(context))		

