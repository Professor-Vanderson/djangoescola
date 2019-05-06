from django.contrib import admin
from .models import categoria
from .models import usuario
from .models import professor
from .models import aluno

admin.site.register(categoria)
admin.site.register(usuario)
admin.site.register(professor)
admin.site.register(aluno)
