from django.shortcuts import render , redirect
from .models import Person
from django.contrib import messages
from .forms import TodoCreateForm , TodoUpdateForm
# Create your views here.

def say_hello(request):
    person = {"name" : "ozhan"}
    return render(request,'hello.html',context=person)

def Home(request):

    all = Person.objects.all()
    # person = {"name" : "ozhan! "}
    return render(request,'home.html',context={"all":all})

def detail(request,person_id):
    todo = Person.objects.get(id=person_id)
    return render(request,'detail.html',{'todo':todo})

def delete(request,person_id):
    Person.objects.get(id=person_id).delete()
    messages.success(request,'Delete shd','success')
    return redirect('home')

def create(request) :
    if request.method == 'POST' :
        form = TodoCreateForm(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            Person.objects.create(name=cd['name'],last_name=cd['last_name'],number=cd['number'],birthday=cd['birthday'])
            messages.success(request, 'Person Created successfully ', 'success')
            return redirect('home')

    else :
        form = TodoCreateForm()
    return render(request,'create.html',context={'form':form})

def update(request,person_id) :
    todo = Person.objects.get(id=person_id)

    if request.method == 'POST' :
        form = TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated','success')
            return redirect('details',person_id)

    else :
        form = TodoUpdateForm(instance=todo)
    return render(request , 'update.html',{'form':form})