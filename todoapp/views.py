from django.shortcuts import render,redirect
from todoapp.models import Task_db
from datetime import datetime
from django.contrib import messages
from django.template import loader
from .forms import Listform

# Create your views here.


def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        task = request.POST.get('task')
        # date=datetime.today()
        if (title and task)=="":
            messages.success(request,"Field Are empty! Add Somthing 😋")
        else:
            user_task = Task_db(title=title, task=task, date=datetime.today())
            user_task.save()
            messages.success(request,"New task added successfully!")
    return render(request,'index.html')

def task(request):
    mydata = Task_db.objects.all().values()
    template = loader.get_template('index.html')
    
    context = {
        'mymembers': mydata,
    }
    if(len(mydata)==0):
        messages.success(request,"There Is no task Added 😢")
    return render(request,'index.html', context)

def delete(request, list_id):
    item = Task_db.objects.get(pk=list_id)
    item.delete()
    messages.success(request,"Task deleted successfully!")
    return redirect('task')