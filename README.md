
# Documentación de Endpoints - Proyecto EPIC

## Descripción del Proyecto

Esta es una API RESTful desarrollada con FastAPI para gestionar una aplicación de reservas de habitaciones. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) tanto para habitaciones como para reservas. Las habitaciones pueden ser de tipo simple, doble o suite, y cada una tiene un precio por noche. Las reservas incluyen el nombre del huésped, la fecha de inicio y fin de la reserva, y están asociadas a una habitación específica.

## Características 
- **Gestión de Habitaciones** - Crear, leer, actualizar y eliminar habitaciones. - Cada habitación tiene un número, tipo (simple, doble, suite), precio por noche, y disponibilidad. 
- **Gestión de Reservas** - Crear, leer, actualizar y eliminar reservas. - Cada reserva incluye el nombre del huésped, la fecha de inicio y fin de la reserva, y la habitación asociada. - Validación de disponibilidad de la habitación antes de crear una reserva. - Validación para evitar conflictos de fechas en las reservas. 
## Requisitos 
- Python 3.8+ 
- FastAPI 
-  SQLAlchemy 
-  Pydantic 
-  SQLite 

## Instalación y Configuración

### Pasos para Usar Localmente

1. clonar el proyecto con el siguiente comando: `git clone https://github.com/guille1999utp/epic`

2. nos ubicamos dentro del proyecto: `cd epic`

3. Instalamos las dependencias del proyecto con el siguiente comando (se debe tener instalado python y pip):

```console
 pip install -r requirements.txt
```

4. Inicia el servidor con el siguiente comando en la misma ruta: 

```console
 uvicorn main:app --reload
```

si con el anterior comando no se ejecuto el programa tambien se encuentra esta otra opcion:

```console
 python -m uvicorn main:app --reload
```

### Swagger de FastApi

Si quieres ver más información sobre los endpoints disponibles, ingresa a la siguiente ruta: [http://localhost:8000/docs](http://localhost:8000/docs)

### Postman

si quieres utilizar los enpoints directamente en postman puedes exportar los enpoints del archivo llamado epic del siguiente link del repositorio publico de postman: 
[https://www.postman.com/guille2001/workspace/public/collection/17417694-fc913df3-7a22-4d29-8c31-b52388ec8db0](https://www.postman.com/guille2001/workspace/public/collection/17417694-fc913df3-7a22-4d29-8c31-b52388ec8db0)