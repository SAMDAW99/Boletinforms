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
            if fecha_inicio > fecha_fin:
                show_alert_1 = True
                return render(request, 'Ejercicio1/pagina_formulario.html', {'show_alert_1': show_alert_1})
            elif not dias_semana:
                show_alert_2 = True
                return render(request, 'Ejercicio1/pagina_formulario.html', {'show_alert_2': show_alert_2})
            elif len(dias_semana) <= 3:
                show_alert_3 = True
                return render(request, 'Ejercicio1/pagina_formulario.html', {'show_alert_3': show_alert_3})

            elif correo_electronico.endswith('iesmartinezm.es'):
                show_alert_4 = True
                return render(request, 'Ejercicio1/pagina_formulario.html', {'show_alert_4': show_alert_4})
            return render(request, 'Ejercicio1/pagina_detalles.html', {'fecha_inicio': fecha_inicio,
                                                                       'fecha_fin': fecha_fin,
                                                                       'dias_semana': dias_semana,
                                                                       'correo_electronico': correo_electronico})
