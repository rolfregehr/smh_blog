from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente

class ProdutoAdmin(admin.ModelAdmin): # Lista, no gerenciador (/admin) os campos definidos abaixo 
    list_display = ('nome', 'preco', 'estoque')

admin.site.register(Produto, ProdutoAdmin) # tem que incluir a class criada para visualização
admin.site.register(Cliente)
