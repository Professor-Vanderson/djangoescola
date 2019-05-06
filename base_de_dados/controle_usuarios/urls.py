"""controle_usuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('arduino/', views.arduino, name ='arduino'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cobol/', views.cobol, name='cobol'),
    path('cursos/', views.cursos, name='cursos'),
    path('descontos/', views.descontos, name='descontos'),
    path('designgrafico/', views.designgrafico, name='deseigngrafico'),
    path('java/', views.java, name='java'),
    path('logica/', views.logica, name='logica'),
    path('manutencao/', views.manutencao, name='manutencao'),
    path('noticias/', views.noticias, name='noticias'),
    path('python/', views.python, name='python'),
    path('ruby/', views.ruby, name='ruby'),
    path('aluno/', views.aluno, name='aluno'),
    path('cadastro/professor/', views.professor, name='professor'),
    path('cadastro/usuario/', views.usuario, name='usuario'),
    path('cadastro/disciplina/', views.disciplina, name='disciplina'),

]
