from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    todolist = Todo.objects.all()
    context = {
        "todos": todolist,
    }
    return render(request, "todo/todo_list.html", context)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    print(todo.id)
    context = {
        "todo" : todo,
    }
    return render(request, "todo/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        # create todo object
        form.save()
        """ print(form.cleaned_data)
        name = form.cleaned_data['name']
        due_date = form.cleaned_data['due_date']
        new_todo = Todo.objects.create(name=name,due_date=due_date)
        new_todo.save() """
        return redirect("/")
    context = {
        "form" : form,
    }
    return render(request, "todo/todo_create.html", context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=todo)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        "form" : form,
    }
    return render(request, "todo/todo_update.html", context)

def todo_delete(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")
