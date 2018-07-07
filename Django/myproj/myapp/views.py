from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Task
from myapp.forms import TaskForm, TaskModelForm
from django.views.generic import TemplateView, View, ListView, DetailView
from django.views.generic.edit import FormView
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/index.html', {'tasks': tasks, 'form': TaskModelForm()})


def create_task(request):

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/tasks')
    return render(request, 'myapp/index.html', {'tasks': tasks, 'form': form})


def detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        print('Exception')

    form = TaskModelForm(instance=task)

    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/{}'.format(task.pk))

    return render(request, 'myapp/detail.html', {'task': task, 'form': form})


class TaskView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, 'myapp/index.html', {'tasks': tasks, 'form': TaskModelForm()})

    def post(self, request, pk=None):
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/tasks')


class TaskListView(ListView):
    model = Task
    # paginate_by = 5
    template_name='myapp/index.html'
    context_object_name = 'tasks'

    def get_context_data(self):
        data = super().get_context_data()
        data['form'] = TaskForm()
        return data

class TaskDetailView(DetailView):
    model = Task

    def get_objects(self):
        task = super().get_queryset(self.request)


class TaskFormView(FormView):
    from_class = TaskForm

    def form_valid(self, form):
        pass

