
import csv
import io
import re
from django.shortcuts import render
from .forms import CSVUploadForm
from django.contrib import messages

def validar_csv(f):
	errores = []
	contenido = f.read().decode('utf-8')
	reader = csv.reader(io.StringIO(contenido))
	filas = list(reader)
	for i, fila in enumerate(filas, start=1):
		if len(fila) != 5:
			errores.append({'fila': i, 'columna': 'Todas', 'mensaje': 'El archivo debe tener exactamente 5 columnas.'})
			continue
		# Columna 1: Enteros de 3 a 10 dígitos
		if not re.fullmatch(r'\d{3,10}', fila[0]):
			errores.append({'fila': i, 'columna': 1, 'mensaje': 'Debe ser un número entero de 3 a 10 dígitos.'})
		# Columna 2: Email
		if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", fila[1]):
			errores.append({'fila': i, 'columna': 2, 'mensaje': 'Debe ser un correo electrónico válido.'})
		# Columna 3: CC o TI
		if fila[2] not in ["CC", "TI"]:
			errores.append({'fila': i, 'columna': 3, 'mensaje': "Debe ser 'CC' o 'TI'."})
		# Columna 4: Entre 500000 y 1500000
		try:
			valor = int(fila[3])
			if not (500000 <= valor <= 1500000):
				errores.append({'fila': i, 'columna': 4, 'mensaje': 'Debe estar entre 500000 y 1500000.'})
		except ValueError:
			errores.append({'fila': i, 'columna': 4, 'mensaje': 'Debe ser un número entero.'})
		# Columna 5: cualquier valor (no se valida)
	return errores

def cargar_csv(request):
	errores = []
	exito = False
	if request.method == 'POST':
		form = CSVUploadForm(request.POST, request.FILES)
		if form.is_valid():
			archivo = form.cleaned_data['archivo']
			errores = validar_csv(archivo)
			if not errores:
				exito = True
	else:
		form = CSVUploadForm()
	return render(request, 'validador_csv/cargar_csv.html', {'form': form, 'errores': errores, 'exito': exito})
