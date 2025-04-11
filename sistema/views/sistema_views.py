from django.shortcuts import render




# A função index informa o que vai acontecer quando ela for chamada
def index(request):
    return render(
        request,
        'sistema/sistema.html',
    )

def apresentacao(request):
    return render(
        request,
        'sistema/apresentacao.html',
    )


# REQUEST
# RESPONSE   