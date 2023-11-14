# Remesalclic Functions

## Descripción
Este proyecto contiene funciones que se ejecutan en el backend de Firebase para hacer el envio de notificaciones push
en el momento en el que se envia un mensaje en el chat de la App o se inicia un nuevo trato.

Estas funciones estan escritas en python.

## Instalacion de Firebase tools
Para poder ejecutar las funciones de firebase en tu computadora y desplegarlas, debes instalar las firebase tools, para ello debes ejecutar el siguiente comando en tu terminal:

```bash
npm install -g firebase-tools
```

Ahora inicia sesion en firebase con el siguiente comando:

```bash
firebase login
```

Este comando conecta tu máquina local a Firebase y te otorga acceso a los proyectos de Firebase.

Enumera tus proyectos de Firebase para probar que se instaló correctamente la CLI y que accediste a tu cuenta. Ejecuta el siguiente comando:

```bash
firebase projects:list
```

Deberas ver los proyectos de firebase que tienes en tu consola asociados a tu cuenta.
Debes de ver el proyecto de remesalclic en la lista con el id _**remesaalclic**_, si no es asi
deberas pedir acceso a este proyecto a algun administrador.

## Clonar el repositorio
Para clonar el repositorio por ssh, ejecuta el siguiente comando en tu terminal:

```bash
git clone git@github.com:<username>/remesalclic-functions.git
```

ahora entra a la carpeta de las funciones con el siguiente comando:

```bash
cd remesalclic-functions/functions
```

## Requisitos
- `python` 3.11 o superior
- `pip` 22.0.2 o superior
- `firebase-tools` 12.8.1 o superior

## Instalación de dependencias

Abre tu terminal y ejecuta los siguientes comando (debes estar en la carpeta _**functions**_ del proyecto):

Primero debemos activar el entorno virtual con el siguiente comando:
```bash
source venv/bin/activate
```

Despues instalamos las dependencias con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Despliegue de las funciones
Para desplegar las funciones en Firebase, debes ejecutar el siguiente comando en tu terminal (debes estar en la carpeta raiz del proyecto):

```bash
firebase deploy --only functions
```

