from django.shortcuts import render
from usuarios import views

from django.http import HttpResponse

def home(request):
    return render(request, 'usuarios/index.html')

def arduino(request):
    return render(request, 'usuarios/arduino.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def cobol(request):
    return render(request, 'usuarios/cobol.html')

def cursos(request):
    return render(request, 'usuarios/cursos.html')

def descontos(request):
    return render(request, 'usuarios/descontos.html')

def designgrafico(request):
    return render(request, 'usuarios/designgrafico.html')

def java(request):
    return render(request, 'usuarios/java.html')

def logica(request):
    return render(request, 'usuarios/logica.html')

def manutencao(request):
    return render(request, 'usuarios/manutencao.html')

def noticias(request):
    return render(request, 'usuarios/noticias.html')

def python(request):
    return render(request, 'usuarios/python.html')

def ruby(request):
    return render(request, 'usuarios/ruby.html')

def sobre(request):
    return render(request, 'usuarios/sobre.html')

def sql(request):
    return render(request, 'usuarios/sql.html')

def webdesign(request):
    return render(request, 'usuarios/webdesign.html')

def anima(request):
    return render(request, 'usuarios/anima.html')

def usuario(request):
    return render(request, 'usuarios/usuario.html')

def aluno(request):
    return render(request, 'usuarios/aluno.html')

def disciplina(request):
    return render(request, 'usuarios/disciplina.html')

def professor(request):
    return render(request, 'usuarios/professor.html')

