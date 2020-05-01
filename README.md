# CC30622020201-A4
Assignment 4 de Sistemas web.

## Inicialización:
1. Crear un venv con las dependencias en requirements.txt, o actualizar uno ya existente para que tenga estas dependencias.
2. Con el venv activado, `../CC30622020201-A4/babies_api/python manage.py runserver`.
3. Utilizar postman para las siguientes acciones

## Acciones posibles (usando postman):
### Obtener el un Auth Token
Con la opción POST, entrar a http://localhost:8000/api/v1/token-auth/ con una de las siguientes combinaciones Username/Password en el body:
```
Opcion 1:
Username: Diego
Password: diego_password
Opcion 2:
username: not_diego
password: not_diegopassword
```
Esto generara un token, puede ser util guardarlo en un notepad. El numero de opcion es el mismo numero de ID utilizado para algunas de las acciones siguientes

### Obtener la lista de todos los bebes posibles
Con la opción GET, entrar a http://localhost:8000/api/v1/babies . Aun no he podido generar la opcion para que esto no muestre si el usuario no esta loggeado, y que muestre solo los del usuario loggeado.

### Obtener la lista de Bebes asignados al usuario #ID.
Con la opción POST, entrar a http://localhost:8000/api/v1/parent/{ID}/babies, sustituyendo {ID} por el numero de opción. Incluir en el header la llave Authorization, con contenidos: `JWT {el token auth}` para poder entrar. Aun no logro implementar que el backend de error si se intenta ingresar a los bebes de un usuario distinto.

### Ver los eventos para cada bebe.
Con la opcion GET, entrar a http://localhost:8000/api/v1/babies/{ID}/events/, sustituyendo {ID} por el ID del bebe que se quiere ver. Se debe incluir la llave Authorization en el header de la misma manera que se incluye en el inciso anterior. En este caso, si se intenta entrar con el auth de otro padre, se dara un error.

### Crear un evento para un bebe.
Con la opcion POST, entrar a http://localhost:8000/api/v1/events/, con la llave Authorization en el header, y la siguiente informacion en el body:
```
event_type: Opcional, por default sera N/A
date: Opcional, por default es la hora a la que se realiza la accion
notes: Opcional, por default sera N/A
baby: el id del bebe a quien se le asignara el evento.
```
El bebe debe pertenecer al usuario loggeado, de lo contrario se dara un error.
