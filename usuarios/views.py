from django.shortcuts import render, request

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
