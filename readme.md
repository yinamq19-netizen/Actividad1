Instrucciones de ejecucion e instalacion:

1. Se crea el proyecto o carpeta de nombre "mi_proyecto".
2. Instalar librerias o dependencias las cuales se encuentran en el archivo requirements.txt
3. Ejecutar los comandos de django-admin startproject "nombre del proyecto" (Esto es requerido solo si se va a crear una app django desde cero, si no omitir este paso)
4. Ejecutar el run o build del proyecto con el comando 
   python manage.py runserver 

Nota: Es de aclarar que este proyecto se puede ejecutar en un .env o tambien de manera local con el launcher
de python ( no importa la version pero es recomendable version 13), de igual forma si se presenta un error
de compilacion o ejecucion del proyecto porfavor usar este comando(cambiamos el puerto ya que puede estar siendo
utilizado por otra aplicacion)

  python manage.py runserver 8001