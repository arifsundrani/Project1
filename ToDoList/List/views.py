from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

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
<<<<<<< HEAD
	
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
=======


<<<<<<< HEAD
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')
	

def loggedin(request):
	return render_to_response('loggedin.html', {'full_name' : request.user.username})


def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
	
	
	
	
	
	
	
=======
>>>>>>> FETCH_HEAD
>>>>>>> FETCH_HEAD
