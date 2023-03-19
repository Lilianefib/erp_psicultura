from django import forms
from .models import Insumo

class InsumoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Insumo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InsumoForm, self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'