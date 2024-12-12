from django.shortcuts import render, redirect
from .models import Autor, Genero, Libro
from .forms import AutorForm, GeneroForm, LibroForm
from django.shortcuts import render, redirect

def agregar_datos(request):
    # Instanciar los formularios
    form_autor = AutorForm(prefix='autor')
    form_genero = GeneroForm(prefix='genero')
    form_libro = LibroForm(prefix='libro')

    if request.method == 'POST':
        if 'submit_autor' in request.POST:  # Botón de agregar autor
            form_autor = AutorForm(request.POST, prefix='autor')
            if form_autor.is_valid():
                form_autor.save()
                return redirect('agregar_datos')

        elif 'submit_genero' in request.POST:  # Botón de agregar género
            form_genero = GeneroForm(request.POST, prefix='genero')
            if form_genero.is_valid():
                form_genero.save()
                return redirect('agregar_datos')

        elif 'submit_libro' in request.POST:  # Botón de agregar libro
            form_libro = LibroForm(request.POST, prefix='libro')
            if form_libro.is_valid():
                form_libro.save()
                return redirect('agregar_datos')

    return render(request, 'libros/agregar.html', {
        'form_autor': form_autor,
        'form_genero': form_genero,
        'form_libro': form_libro,
    })

def buscar_libro(request):
    query = request.GET.get('query', '')
    resultados = Libro.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'libros/buscar.html', {'resultados': resultados})

def inicio(request):
    return redirect('agregar_datos')