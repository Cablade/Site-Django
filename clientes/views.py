from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Cliente, Carro
import re
from django.core import serializers

def clientes(request):

    if request.method == 'GET':
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list})
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placas')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return render(request, 'clientes.html', {
                'nome': nome, 
                'sobrenome': sobrenome, 
                'email': email, 
                'carros': zip(carros, placas, anos),
                'error': 'Cliente já existe.'
            })
        email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(email_regex, email):
            return render(request, 'clientes.html', {
                'nome': nome, 
                'sobrenome': sobrenome, 
                'cpf': cpf, 
                'carros': zip(carros, placas, anos),
                'error': 'Email inválido.'
            })
        
        cliente = Cliente(
            nome = nome, 
            sobrenome = sobrenome, 
            email = email, 
            cpf = cpf
        )
        cliente.save()

        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()

    return render(request, 'clientes.html', {'success': 'Cliente cadastrado com sucesso!'})

def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    cliente_json = serializers.serialize
    return JsonResponse({"teste": 1})