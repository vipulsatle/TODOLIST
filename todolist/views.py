from django.shortcuts import render,redirect
from .models import ToDolist

from .forms import TodoListForm

from django.views.decorators.http import require_POST

def index(request):
    todo_items = ToDolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items' : todo_items,'form' : form}
    return render(request,'todo/index.html',context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = ToDolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completedTodo(requset,todo_id):
    todo = ToDolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')






# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Description


# def index(request):
    
#     #return HttpResponse("Hello World i a mdjango ")
#     # all_todo_items = ToDolistitem.objects.all()

#     obj = Description()
#     obj.name = "ashihs"

#     obj1 = Description()
#     obj1.name = "ek "

#     obj2 = Description()
#     obj2.name = "number "

#     obj3 = Description()
#     obj3.name = "boka"

#     obj4 = Description()
#     obj4.name = "admina"

#     objs = [obj,obj1,obj2,obj3,obj4]

#     return render(request,'todo/index.html',{'ashish': objs})
    



# Create your views here.








