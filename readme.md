Instrucciones de ejecucion e instalacion:

Prueba Técnica – Desarrollador Junior (Django)

Este proyecto consiste en una aplicación en **Django** que permite a los usuarios **cargar y validar archivos TXT**.  
El sistema revisa que el archivo cumpla con una serie de reglas de validación y muestra mensajes claros con los errores encontrados.

---

## Requisitos de Validación

El archivo TXT que se suba debe cumplir con las siguientes condiciones:

1. **Número de columnas:** El archivo debe tener exactamente **5 columnas**.  
   - Si tiene más o menos, se genera una alerta.
2. **Columna 1:** Debe contener únicamente **números enteros** con una longitud entre **3 y 10 caracteres**.  
3. **Columna 2:** Debe contener únicamente **correos electrónicos válidos**.  
4. **Columna 3:** Solo se aceptan los valores:  
   - `CC`  
   - `TI`  
5. **Columna 4:** Solo se aceptan valores numéricos en el rango de **500.000 a 1.500.000**.  
6. **Columna 5:** Se permite **cualquier valor**.

---

## Funcionalidades

- **Carga de Archivos:** A través de un formulario web.  
- **Validación Automática:** Cada fila y columna es verificada según las reglas anteriores.  
-**Mensajes de Resultado:** El sistema indica si la validación fue exitosa o detalla los errores (con fila y columna).  
**Interfaz Intuitiva:** Fácil de usar para el usuario final.  

---

## 🔧 Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- **Python** (>= 3.12.9)  
- **pip** (gestor de paquetes de Python)  
- **Virtualenv** (opcional, recomendado para aislar dependencias)  

---

##  Instalación y Ejecución

### 1️. Clonar el Repositorio
```bash
git clone https://github.com/yinamq19-netizen/Actividad1.git
```

### 2️. Crear y Activar un Entorno Virtual (opcional pero recomendado)

#### En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### En Linux / MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4️. Ingresar a la carpeta del proyecto
```bash
cd validate_file
```

### 5️. Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

Luego abre tu navegador y accede a:  
`http://127.0.0.1:8000`

---

##  Ejemplos de Uso

- **Página inicial**

![Inicio](Actividad1/im1.png)


- **Archivo válido (con errores encontrados)**

![Validación 2](Actividad1/im2.png)

- **Archivo válido corregido (sin errores)**

![Validación 3](Actividad1/im3.png)

---

## Importante

- El sistema valida que **únicamente se acepten archivos `.txt`**.  
- En caso de errores, se detalla la **fila y columna exacta**.  
- El archivo de ejemplo **`valido.txt`** contiene datos correctos que cumplen con todas las validaciones.  

---

Autor: Yina Millan 
