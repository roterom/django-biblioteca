from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor

# Create your views here.
def Home(request):
    return render(request, 'index.html')


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
        
    else: 
        autor_form = AutorForm()
        return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})    

    
def listarAutor(request):
    # autores = Autor.objects.all()
    autores = Autor.objects.filter(estado=True) # sustituimos este all por filter poruqe ahora usamos el campo 'estado' para hacer elminaciones llamadas 'lógicas' 
    return render(request,'libro/listar_autor.html', {'autores': autores})


def editarAutor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})
        

def eliminarAutor(request, identif):
    autor = Autor.objects.get(id=identif)
    if request.method == 'POST':
        # autor.delete() # esto para una elimnacion directa en bd
        # si quisieramos una eliminación lógica donde usemos el nuevo atributo estado de la clase autor...
        autor.estado = False
        autor.save()
        
        return redirect('libro:listar_autor')
        
    return render(request, 'libro/eliminar_autor.html', {'autor': autor})    