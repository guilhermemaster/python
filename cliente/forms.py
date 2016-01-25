from django.forms import ModelForm
from cliente.models import Cliente

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		#fields=['nome','data_nascimento', 'salario','email','filhos','ativo']
		
		exclude = [''] 