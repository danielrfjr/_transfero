from django.shortcuts import render

# Aqui irão ficar todas as viwes (controladores) ref ao APP sistema.

# A função index informa o que vai acontecer quando ela for chamada
def index(request):
    return render(
        request,
        'sistema/index.html',
    )



# REQUEST
# RESPONSE   