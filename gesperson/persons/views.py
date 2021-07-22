from django.shortcuts import render, redirect
from persons.forms import PersonsForm
from persons.models import Persons

# Create your views here.
def std(request):
    if request.method == "POST":
        form = PersonsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/liste')
            except:
                pass
    else:
        form = PersonsForm()
    return render(request, 'index.html' , {'form':form}) 

def liste(request):
    persons = Persons.objects.all()
    return render(request, "liste.html", {'persons':persons})  

def delete(request, id):
    persons = Persons.objects.get(id=id)
    persons.delete()
    return redirect("/liste")

def edit(request, id):
    persons = Persons.objects.get(id=id)
    return render(request, 'edit.html', {'persons':persons}) 

def update(request, id):  
    persons = Persons.objects.get(id=id)  
    form = PersonsForm(request.POST, instance = persons)  
    if form.is_valid():  
        form.save()  
        return redirect("/liste")  
    return render(request, 'edit.html', {'persons': persons})        


