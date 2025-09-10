from django import forms


class CSVUploadForm(forms.Form):
    archivo = forms.FileField(label='Seleccione un archivo CSV')
