from django.forms import forms
from django.core.exceptions import ValidationError
from Boletin import settings


class Formulario(forms.Form):
    fecha_inicio = forms.DateTimeField(label='fecha de inicio', input_formats=settings.DATE_INPUT_FORMATS,
                                       help_text='la fecha inicio no debe ser superior a la fecha fin')
    fecha_fin = forms.DateTimeField(label='fecha fin', input_formats=settings.DATE_INPUT_FORMATS,
                                    help_text='la fecha fin no debe ser inferior a la fecha inicio')
    dias_semana = forms.MultipleChoiceField(
        choices=[('lunes', 'Lunes'),
                 ('martes', 'Martes'),
                 ('miercoles', 'Miércoles'),
                 ('jueves', 'Jueves'),
                 ('viernes', 'Viernes'),
                 ('sabado', 'Sábado'),
                 ('domingo', 'Domingo'),
                 ],
        widget=forms.CheckboxSelectMultiple,
        label='Dias de la semana',
        help_text='el numero maximo de dias debe ser 10')

    correo_electronico = forms.EmailField(
        help_text='Por favor introduzca una direccion de email de este formato (ejemplo@iesmartinezm.es)', )

    if fecha_inicio > fecha_fin:
        raise ValidationError('la fecha inicio no debe ser superior a la fecha fin')
    elif not dias_semana:
        raise ValidationError('debes seleccionar por lo menos un día de la semana')
    elif len(dias_semana) >= 3:
        raise ValidationError('puedes seleccionar un máximo de 3 días a la semana')
    elif correo_electronico.endswith('iesmartinezm.es'):
        raise ValidationError('El correo electrónico tiene que acabar con iesmartinezm.es')

