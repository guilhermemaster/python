from django.shortcuts import render,redirect
from django.http import HttpResponse
from cliente.models import Cliente
from django import template
from cliente.forms import ClienteForm


# Create your views here.
def home(request):
	return HttpResponse('Hello word')

def cliente(request):
	data = {}
	data['list_clientes']=Cliente.objects.all() #equivalente a select * from cliente
	data['djangomoc'] = 'gui'
	return render(request, 'cliente.html', data) 


def cliente_update(request, pk):
	cliente = Cliente.objects.get(pk=pk)
	#return HttpResponse('Cliente'+str(pk))
	return render(request, 'cliente_listagem.html',{'objets': cliente})

def create(request):
	form = ClienteForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('cliente_principal')
	return render(request, 'cliente_novo.html', {'form':form})
