from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Produto

def listar_produtos_completo(request):
    nome_busca = request.GET.get('busca', '')
    if nome_busca:
        produtos_lista = Produto.objects.filter(nome__icontains=nome_busca)
    else:
        produtos_lista = Produto.objects.all()

    paginador = Paginator(produtos_lista, 5)
    numero_pagina = request.GET.get('page')
    produtos_paginados = paginador.get_page(numero_pagina)

    return render(request, 'produtos/lista.html', {'produtos': produtos_paginados, 'busca': nome_busca})
