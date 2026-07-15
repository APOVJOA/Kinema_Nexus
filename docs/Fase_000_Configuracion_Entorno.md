Configuración del entorno de desarrollo
Objetivo

Antes de continuar con el desarrollo del sistema de visión artificial y la integración con RoboDK, se ha preparado un entorno virtual de Python independiente para garantizar que todas las librerías utilizadas por el proyecto sean compatibles y puedan reproducirse en cualquier equipo.

El uso de un entorno virtual evita conflictos entre versiones de Python y dependencias instaladas globalmente en el sistema operativo.

Nota: Los pasos posteriores describen cómo se configuró originalmente el entorno de desarrollo. Para un nuevo colaborador basta con seguir el apartado "Más rápido", utilizando el archivo requirements.txt generado al finalizar esta configuración.Lo encontraras casi al final del documento.

1. Instalación de Python

Se recomienda utilizar Python 3.12, ya que proporciona una mayor compatibilidad con las librerías empleadas en el proyecto.

Puede comprobarse la versión instalada mediante:

python --version
2. Creación del entorno virtual

Desde la carpeta raíz del proyecto se crea un entorno virtual denominado .venv.

python -m venv .venv

Una vez ejecutado aparecerá la siguiente estructura:

KINEMA_NEXUS/
│
├── .venv/
├── src/
├── data/
├── docs/
└── ...
3. Activación del entorno virtual
En Windows (CMD)
.venv\Scripts\activate.bat
En PowerShell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1

Una vez activado el entorno aparecerá:

(.venv)

al inicio de la línea de comandos.

4. Comprobación del intérprete

Es recomendable verificar que realmente se está utilizando el intérprete del entorno virtual.

where python

Debe aparecer como primera ruta:

C:\...\KINEMA_NEXUS\.venv\Scripts\python.exe

También puede comprobarse la versión:

python --version
5. Instalación de dependencias

Las principales librerías utilizadas durante esta etapa del proyecto son:

pip install numpy
pip install opencv-python
pip install ultralytics
pip install robodk

Las versiones instaladas pueden comprobarse mediante:

pip list

o bien:

pip show nombre_paquete

Por ejemplo:

pip show opencv-python
6. Verificación de OpenCV

Antes de comenzar el desarrollo se verifica que OpenCV se ha instalado correctamente.

import cv2

print(cv2.__version__)

Si la instalación es correcta se mostrará la versión instalada.

7. Selección del intérprete en Visual Studio Code

Para evitar errores de importación mostrados por Pylance, Visual Studio Code debe utilizar el intérprete correspondiente al entorno virtual.

Abrir:

Ctrl + Shift + P

Seleccionar:

Python: Select Interpreter

Y elegir:

...\KINEMA_NEXUS\.venv\Scripts\python.exe

Posteriormente puede recargarse la ventana mediante:

Developer: Reload Window
8. Organización del proyecto

Durante esta etapa se establece la siguiente estructura de directorios:

KINEMA_NEXUS
│
├── src/
│   ├── robodk_communication.py
│   ├── human_pose_detection.py
│   └── ...
│
├── data/
│   └── robot_data.json
│
├── docs/
│
├── .venv/
│
└── README.md
Resultado
9. Instalación de YOLO (Ultralytics)

Una vez configurado el entorno virtual, se instala la librería Ultralytics, que proporciona la implementación oficial de los modelos YOLO utilizados durante el desarrollo del sistema de visión artificial.

La instalación se realiza mediante:

pip install ultralytics
10. Verificación de la instalación

Para comprobar que la instalación se ha realizado correctamente, puede abrirse el intérprete de Python y ejecutar:

from ultralytics import YOLO

print("YOLO instalado correctamente")

Si no aparece ningún error, la instalación ha finalizado correctamente.

11. Descarga automática de modelos

Los modelos de YOLO no necesitan descargarse manualmente.

La primera vez que se carga un modelo:

from ultralytics import YOLO

model = YOLO("yolo11n-pose.pt")

Ultralytics descarga automáticamente los pesos necesarios desde su repositorio oficial y los almacena en caché para futuras ejecuciones.

12. Comprobación del funcionamiento

Puede realizarse una prueba rápida ejecutando el script de detección de pose humana desarrollado durante la Fase 16:

python src/human_pose_detection.py

Si el entorno está correctamente configurado, el programa abrirá la cámara y comenzará a detectar personas utilizando el modelo YOLO Pose.


13. Dependencias del proyecto

Una vez finalizada la instalación de todas las librerías utilizadas, es recomendable generar el archivo requirements.txt para facilitar la reproducción del entorno en otros equipos.

Desde la raíz del proyecto:

pip freeze > requirements.txt



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MAS RÁPIDO

Preparación del entorno de desarrollo
1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/KINEMA_NEXUS.git

Entrar en el proyecto:

cd KINEMA_NEXUS
2. Crear el entorno virtual

Crear un entorno virtual de Python:

python -m venv .venv
3. Activar el entorno virtual
Windows (CMD)
.venv\Scripts\activate.bat
Windows (PowerShell)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1

Tras la activación deberá aparecer:

(.venv)

al comienzo de la línea de comandos.

4. Instalar todas las dependencias

Con el entorno virtual ya activado:

pip install -r requirements.txt

Este comando instalará automáticamente todas las librerías necesarias para ejecutar el proyecto, incluyendo OpenCV, RoboDK, Ultralytics (YOLO), NumPy y el resto de dependencias.

5. Comprobar la instalación
python --version
pip list

Si todo ha sido correcto, el proyecto estará listo para ejecutarse.

Al finalizar esta configuración el proyecto dispone de un entorno de desarrollo completamente aislado, reproducible y preparado para continuar con las siguientes fases del sistema de visión artificial y su integración con RoboDK