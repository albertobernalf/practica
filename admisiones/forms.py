from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import django.core.validators
import django.core.exceptions
from django.core.exceptions import ValidationError



class ingresosForm(forms.ModelForm):

    class Meta:
        model = Ingresos

        tipoDoc = forms.ModelChoiceField(queryset=TiposDocumento.objects.all())
        documento = forms.IntegerField(label='No Documento')



        fields = '__all__'

        widgets = {
            'tipoDoc':    forms.TextInput(attrs={'readonly': 'readonly'})
            'documento':  forms.TextInput(attrs={'readonly': 'readonly'})

        }


    def clean_documento(self):
        print("entre a validar Documento Historia1 Form")

        return documento

