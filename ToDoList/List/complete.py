from List.models import Task

def complete(task_id): # return Fibonacci series up to n
	t = get_Object_or_404(Task,task_id)
	t.completed=True
	return t
	
def add(task_id):
	return 0