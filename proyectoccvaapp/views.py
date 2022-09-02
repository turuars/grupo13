from django.shortcuts import render, HttpResponse

from noticias.models import Post

#from cursos.models import Curso



# Create your views here.




def home(request):

    post = Post.objects.last ()
    #curso = Curso.objects.last ()
    post1 = { 'Post': post }
    #curso1 = { 'Curso': curso }
    return render(request, "proyectoccvaapp/home.html", post1) #curso1)


def quienessomos(request):

    return render(request, "proyectoccvaapp/quienessomos.html") 



#def cursosycapacitaciones(request):

   # return render(request, "proyectoccvaapp/cursosycapacitaciones.html")   
   

#def descargas(request):

   # return render(request, "proyectoccvaapp/descargas.html")

