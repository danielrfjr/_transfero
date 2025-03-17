from django.shortcuts import render

# Aqui irão ficar todas as viwes (controladores) ref ao sistema.


def index(request):
    return render(
        request,
        'sistema/index.html',
    )



# REQUEST
# RESPONSE   