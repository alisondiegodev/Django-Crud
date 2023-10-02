from django.shortcuts import render, redirect
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


def edit(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        return render(request, 'root/edit.html', {'produto': produto})
    except Produto.DoesNotExist:
        return render(request, 'root/404.html', status=404)


def store_edit(request, pk):
    if request.method == 'POST':
        try:
            produto = Produto.objects.get(pk=pk)
            form = ProdutoForm(request.POST, instance=produto)
            if form.is_valid():
                form.save()
                return redirect('home')
        except:
            return render(request, 'root/404.html', status=404)
    else:
        return render(request, 'root/404.html', status=405)


def delete(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
        return redirect('home')
    except:
        return redirect('home')
