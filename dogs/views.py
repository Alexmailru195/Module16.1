from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Dog
from .forms import DogForm

def dog_list(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/dog_list.html', {'dogs': dogs})

def dog_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'dogs/dog_detail.html', {'dog': dog})

def dog_create(request):
    if request.method == "POST":
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dog_list')
    else:
        form = DogForm()
    return render(request, 'dogs/dog_form.html', {'form': form})

def dog_update(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    if request.method == "POST":
        form = DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            form.save()
            return redirect('dog_detail', pk=dog.pk)
    else:
        form = DogForm(instance=dog)
    return render(request, 'dogs/dog_form.html', {'form': form})

def dog_delete(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    if request.method == "POST":
        dog.delete()
        return redirect('dog_list')
    return render(request, 'dogs/dog_confirm_delete.html', {'dog': dog})