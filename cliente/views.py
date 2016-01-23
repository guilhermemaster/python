from django.shortcuts import render
from django.http import HttpResponse
from cliente.models import Cliente

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
	return render(request, 'cliente_detalhe.html',{'objets': cliente})
