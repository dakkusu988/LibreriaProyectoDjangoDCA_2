from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .forms import LibreriaForm
from .models import Libreria
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

"""
class Listado(View):
    libreria_template = 'libreria/listado.html'

    def get(self,request):
        libros = Libreria.objects.all()
        return render(request, self.libreria_template, {'libros': libros})
"""
class Listado(ListView):
    model = Libreria
    template_name = 'libreria/listado.html'
    
class Añadir(View):
    books = Libreria.objects.all()
    bookForm_template = 'libreria/añadir.html'

    def actualizarBook(self):
        self.books = Libreria.objects.all()
        return self.books
    
    def get(self, request):
        books = Libreria.objects.all()
        form = LibreriaForm()
        return render(request, self.bookForm_template , {'books': self.actualizarBook, 'form': form})

    def post(self, request):
        form = LibreriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado')
        books = Libreria.objects.all()
        return render(request, self.bookForm_template , {'books': self.actualizarBook, 'form': form})

class Detalles(DetailView):
    model = Libreria
    template_name = 'libreria/detalles.html'

"""
class Editar(View):
    bookEdit_template = 'libreria/editar.html'
    
    def get(self, request, pk):
        book = get_object_or_404(Libreria, pk=pk)
        form = LibreriaForm(instance=book)
        return render(request, self.bookEdit_template , {'book': book, 'form': form})
    
    def post(self, request, pk):
        book = get_object_or_404(Libreria, pk=pk)
        form = LibreriaForm(request.POST, instance = book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('listado')
        return render(request, self.bookEdit_template , {'book': book, 'form': form})
"""    

class Editar(UpdateView):
    model = Libreria
    fields = ['title', 'author', 'rating']
    template_name = "libreria/editar.html"

    # Puedes redirigir a una vista específica usando reverse
    def get_success_url(self):
        return reverse('listado')
    
class Borrar(DeleteView):
    model = Libreria
    template_name = "libreria/borrar.html"
    success_url = reverse_lazy("listado")

    # Mensaje de éxito al borrar
    def get_success_message(self):
        return "El libro ha sido eliminado exitosamente"