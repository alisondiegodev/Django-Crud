from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from .models import Produto
from .forms import ProdutoForm


def home(request):
    produtos = Produto.objects.all()
    return render(request, 'root/home.html', {'produtos': produtos})


def create(request):
    return render(request, 'root/create.html')


def store(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'root/home.html')


def edit(request):
    return render(request, 'root/home.html')


def delete(request):
    return render(request, 'root/home.html')
