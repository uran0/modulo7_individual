from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task, Comments
from forms import TaskForm, CommentForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bienvenida')
        else:
            return render(request, 'login-html', {'error': 'Su usuario/contraseña no corresponden'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def bienvenida(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'bienvenida.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    comments = Comments.objects.filter(task=task).order_by('-publishing_date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect('task_detail, task_id=task.id')
    else:
        form = CommentForm()

    return render(request, 'task_detail.html', {'task': task})

@login_required
def add_comment(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = CommentForm()
    
    return render(request, 'add_comment.html', {'form': form})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('bienvenida')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'task_edit.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('bienvenida')
    
    return render(request, 'task_delete.html', {'task': task})