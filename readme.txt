Se debe ejecutar es mediante el comando: python main.py

En el archivo "mail.py", ubicado en la carpeta "modules", se puede cambiar la cuenta de correo electronico "emisor y Password", para generar el envio de email.

En el archivo "main.py", se puede modificar o mantener la ruta, donde se ejecutara, directamente se puede ir a la variable "my_dir" y cambiar si se desea.

La BD utilizada es sqlite, la cual se encuentra normalizada, asimismo, en la información entregada, sobre la composición del archivo CSV y JSON, se procedio agregar el siguiente dato:

	CSV = user_email, con el objetivo de envio del email.

En la carpeta "files" se deben guardar los archivos que deseen ser procesados, posterior al procesamiento, los archivos sera movidos de manera automatica a la carpeta "procesados".

El siguiente link señala lo que se debe activar (permitir acceso) para poder enviar email desde el aplicativo, sin embargo, la opción esta relacionada a "Acceso de aplicaciones poco seguras"
https://myaccount.google.com/lesssecureapps

Con respecto a los entregables:
	1. Se adjunta el codigo fuente en .zip y por otro lado, se encuentra en github el codigo bajo la cuenta de "AldAndrew"
	2. Se adjunta el readme.txt con las instrucciones para su ejecución.
	3. El codigo no valida los email al proceder con el envio de estos.
	4. El desarrollo se genero con Python.
	5. No se dockeniza la aplicación.

Consideraciones:
	1. Cuando se procese o ejecute los archivo .py, es necesario proceder a setear los coding correspondientes en la primera linea del codigo. Ver referencia https://www.python.org/dev/peps/pep-0263/
	2. Se debe considerar donde estara ubicado el codigo, dado que se deberan setear las rutas para importar los codigos y proceder con la ejecución, de lo contrario tendran problemas por no encontrar la ruta. Ejemplo de las modificaciones a considerar:
		Archivo main.py - linea n°6 - sys.path.append(root + "/modules") = Se debe especificar la ruta que corresponda.
		Archivo main.py - linea n°15 - my_dir = '/trabajo/files/' = Se debe especificar la ruta que corresponda.
