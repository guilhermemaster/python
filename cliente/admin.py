from django.contrib import admin
from cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
	model = Cliente
	date_hierarchy = 'data_nascimento'
	#fields = ('nome', 'data_nascimento')
	#exclude = ('data_nascimento',)


admin.site.register(Cliente, ClienteAdmin)

