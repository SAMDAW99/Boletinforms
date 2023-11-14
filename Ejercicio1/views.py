from django.shortcuts import render
from forms import Formulario


def pagina_bienvenida(request):
    render(request, 'Ejercicio1/pagina_bienvenida.html', {})


def pagina_formulario(request):
    Formulario()
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            dias_semana = form.cleaned_data['dias_semana']
            correo_electronico = form.cleaned_data['correo_electronico']
            render(request, 'Ejercicio1/pagina_formulario.html',
                   {'fecha_inicio': fecha_inicio,
                    'fecha_fin': fecha_fin,
                    'dias_semana': dias_semana,
                    'correo_electronico': correo_electronico})
            return render(request, 'Ejercicio1/pagina_detalles.html', {'fecha_inicio': fecha_inicio,
                                                                       'fecha_fin': fecha_fin,
                                                                       'dias_semana': dias_semana,
                                                                       'correo_electronico': correo_electronico})

        render(request, 'Ejercicio1/pagina_formulario.html', {'form': form})



