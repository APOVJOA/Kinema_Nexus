FASE 15 – RoboDK Communication (Versión inicial)
Objetivo

Establecer la primera comunicación entre el sistema de visión artificial desarrollado en Python y el simulador RoboDK.

En esta primera versión no se realiza todavía el seguimiento del brazo humano, sino la transmisión de la posición detectada de un objeto mediante un archivo JSON que posteriormente será leído por RoboDK.

Esta arquitectura permite mantener ambos sistemas independientes:

Sistema de visión artificial.
Sistema de control del robot.
15.1 Exportación de datos

Se añade al sistema de visión la exportación continua de la información obtenida durante la detección.

Cada iteración genera un archivo:

robot_data.json

que contiene la información necesaria para el robot.

Ejemplo:

{
    "x": 32.81,
    "y": -169.79,
    "area": 79.5,
    "direccion": "Izquierda",
    "velocidad": 0.0,
    "velocidad_media": 60.06,
    "distancia": 6006.10,
    "estado": "Dentro del espacio"
}
Información exportada

Actualmente se almacenan:

Coordenada X del robot.
Coordenada Y del robot.
Área detectada.
Dirección del movimiento.
Velocidad instantánea.
Velocidad media.
Distancia recorrida.
Estado respecto al espacio de trabajo.

Esta información será utilizada posteriormente por RoboDK para calcular los movimientos del robot.

15.2 Lectura desde RoboDK

Se desarrolla un segundo programa completamente independiente encargado únicamente del control del robot.

Su funcionamiento consiste en:

Leer continuamente el archivo JSON.
Obtener las coordenadas exportadas por el sistema de visión.
Preparar dichas coordenadas para generar futuros movimientos del robot.

Esquema de funcionamiento:

Sistema de visión
        │
        │
 robot_data.json
        │
        ▼
Programa RoboDK
        │
        ▼
Robot
15.3 Primeros movimientos del robot

Antes de utilizar la información procedente de la cámara se realizan varios movimientos programados manualmente mediante MoveJ.

Esto permite comprobar:

Conexión correcta con RoboDK.
Control mediante Python.
Funcionamiento de la API.
Configuración de velocidades.
Ejecución de trayectorias.

Ejemplo:

robot.MoveJ(home)

robot.MoveJ([0, -90, 90, 0, 90, 0])

robot.MoveJ([30, -70, 80, 0, 90, 30])

robot.MoveJ(home)

Estos movimientos verifican que el entorno de simulación funciona correctamente antes de introducir datos provenientes del sistema de visión.

15.4 Primera integración

Finalmente se consigue la primera integración funcional entre ambos sistemas.

El programa de RoboDK es capaz de leer en tiempo real la información generada por el sistema de visión artificial, obteniendo continuamente las coordenadas detectadas del objeto.

Aunque en esta fase dichas coordenadas todavía no se utilizan para mover el robot automáticamente, ya existe un canal de comunicación funcional entre ambos programas.

Esto supone el primer paso hacia el control del robot basado en información visual.

Resultado de la fase

Al finalizar esta fase se dispone de:

✔ Sistema de visión independiente.
✔ Exportación automática mediante JSON.
✔ Programa independiente de RoboDK.
✔ Lectura continua del archivo JSON.
✔ Comunicación entre ambos programas.
✔ Primeros movimientos del robot mediante Python.
Nota

Creo que esta fase marca un cambio importante en tu proyecto. Hasta ahora todo estaba centrado en visión artificial; con la fase 15 aparece por primera vez la arquitectura de un sistema robótico real:

Cámara
      ↓
Visión Artificial (Python)
      ↓
Archivo JSON
      ↓
Control RoboDK
      ↓
Robot

A partir de aquí, las mejoras en visión (detectar hombro, codo, muñeca, etc.) y las mejoras en comunicación podrán evolucionar prácticamente de forma independiente. Esa separación es muy similar a la que se utiliza en aplicaciones industriales, donde el sistema de percepción y el controlador del robot suelen estar desacoplados.