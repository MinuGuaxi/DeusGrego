from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

def treinos(request):
    return render(request, 'paginas/treinos.html')

def desafios(request):
    return render(request, 'paginas/desafios.html')

def receitas(request):
    return render(request, 'paginas/receitas.html')
