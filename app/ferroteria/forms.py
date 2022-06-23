
from django import  forms

from .models import herramienta
from .models import Pinturas

class FormularioHerramientas(forms.ModelForm):
    class Meta():
        model = herramienta
        fields = '__all__'
class FormularioPinturas(forms.ModelForm):
    class Meta():
        model = Pinturas
        fields = '__all__'