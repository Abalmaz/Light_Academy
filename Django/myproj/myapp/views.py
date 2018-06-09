from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/index.html', {'tasks': tasks})


def create_task(request):

    if request.method == 'POST':
        task = Task(text=request.POST.get('text'), checked=bool(request.POST.get('checked', False)))
        task.save()

    return redirect('/tasks')

def detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        print('Exception')

    return render(request, 'myapp/detail.html', {'task': task})

