from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import todo
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class tasklistview(ListView):
    model=todo
    template_name = 'home.html'
    context_object_name = 'view'
class taskdetailview(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = 'view'
class taskupdateview(UpdateView):
    model = todo
    template_name = 'update.html'
    context_object_name = 'view'
    fields = ('task','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model = todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# Create your views here.
def index(request):
    view=todo.objects.all()
    if request.method=='POST':
        task=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=todo(task=task,priority=priority,date=date)
        task.save()

    return render(request,'home.html',{'view':view})

def delete(request,taskid):
    task=todo.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=todo.objects.get(id=id)
    form=todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})

