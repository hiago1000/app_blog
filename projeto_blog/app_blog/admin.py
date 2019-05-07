from django.contrib import admin
from .models import Pessoa,Postagem

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    pass