from django.http import HttpResponse
from django.template import loader


 
def saludo(self):
    dato={'nom':'Sebastián','ap':'Pereyra'}
    planilla=loader.get_template('inicio.html')
    documento=planilla.render(dato)
    return HttpResponse(documento)


def datosFamilia(request):
    #-----De esta forma vinculo esta view con el html correspondiente.---------
    planilla=loader.get_template('cuerpo.html')
    documento=planilla.render()
    return HttpResponse(documento)

