from django.shortcuts import render
from todo.models import Task

def home(request):
    # Fetch all tasks that are not completed, ordered by updated_at in ascending order
    tasks = Task.objects.filter(is_completed=False).order_by('updated_at') # -updated_at for descending order
    completed_tasks = Task.objects.filter(is_completed=True).order_by('updated_at')
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'home.html', context)