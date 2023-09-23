from django.shortcuts import render, redirect
from .models import Produk

def index(request):
    produk_list = Produk.objects.filter(status_id=1)
    return render(request, 'index.html', {'produk_list': produk_list})
def add_product(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdukForm()
    return render(request, 'index.html', {'form': form})
def delete_product(request, id_produk):
    produk = Produk.objects.get(id_produk=id_produk)
    produk.delete()
    return redirect('index')