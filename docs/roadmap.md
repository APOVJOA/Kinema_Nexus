# Kinema Nexus — Roadmap de Desarrollo

## Objetivo Final

Desarrollar un sistema de teleoperación robótica basado en visión artificial capaz de interpretar los movimientos de un operador mediante una cámara, transformar dicha información a un sistema de coordenadas compatible con el robot y utilizarla para controlar un brazo robótico de forma segura y controlada.

El sistema deberá ser capaz de:

* Capturar información visual mediante una cámara.
* Detectar y seguir el cuerpo del operador.
* Obtener las articulaciones relevantes del brazo.
* Analizar posiciones, vectores, distancias y ángulos.
* Interpretar restricciones biomecánicas del movimiento humano.
* Detectar y seguir una herramienta manipulada por el operador.
* Transformar la posición de la herramienta al sistema de coordenadas del robot.
* Utilizar RoboDK como entorno de simulación y validación.
* Comunicarse posteriormente con el hardware real.
* Utilizar un sistema de control que impida movimientos robóticos inválidos o peligrosos.

---

# BLOQUE 1 — Fundamentos de Visión Artificial

## Fase 01 — Camera Test

**Estado:** Completada

### Objetivo

Verificar la conexión entre Python y la cámara.

### Resultados

* Captura de vídeo en tiempo real.
* Apertura correcta de la webcam.
* Gestión básica de errores.
* Liberación correcta de recursos.

---

## Fase 02 — Frame Analysis

**Estado:** Completada

### Objetivo

Comprender cómo OpenCV almacena una imagen.

### Resultados

* Comprensión del concepto de frame.
* Análisis de dimensiones.
* Comprensión de la estructura NumPy.
* Análisis de canales BGR.
* Lectura de píxeles individuales.

---

## Fase 03 — Pixel Navigation

**Estado:** Completada

### Objetivo

Comprender el sistema de coordenadas de una imagen.

### Resultados

* Sistema fila-columna.
* Localización de píxeles.
* Interpretación de posiciones dentro del frame.

---

# BLOQUE 2 — Geometría de Imagen

## Fase 04 — Dynamic Image Center

**Estado:** Completada

### Objetivo

Calcular dinámicamente el centro de una imagen.

---

## Fase 05 — Regions of Interest

**Estado:** Completada

### Objetivo

Trabajar únicamente sobre regiones determinadas de una imagen.

---

## Fase 06 — Pixel Area Analysis

**Estado:** Completada

### Objetivo

Analizar grupos de píxeles y preparar las bases para futuras detecciones.

---

# BLOQUE 3 — Manipulación de Imagen

## Fase 07 — Visual Markers

**Estado:** Completada

### Objetivo

Representar información visual sobre la imagen.

### Resultados

* Puntos.
* Líneas.
* Rectángulos.
* Coordenadas.

---

## Fase 08 — Coordinate Tracking

**Estado:** Completada

### Objetivo

Representar y validar posiciones detectadas visualmente.

---

# BLOQUE 4 — Procesamiento de Color

## Fase 09 — Color Spaces

**Estado:** Completada

### Objetivo

Comprender los principales espacios de color utilizados en visión artificial.

---

## Fase 10 — Color Detection

**Estado:** Completada

### Objetivo

Detectar información visual mediante características de color.

---

## Fase 11 — Object Localization

**Estado:** Completada

### Objetivo

Determinar la posición de objetos dentro de una imagen.

---

# BLOQUE 5 — Seguimiento y Movimiento

## Fase 12 — Object Tracking

**Estado:** Completada

### Objetivo

Comprender el seguimiento de elementos entre frames.

---

## Fase 13 — Motion Analysis

**Estado:** Completada

### Objetivo

Analizar desplazamientos y trayectorias.

---

# BLOQUE 6 — Integración con RoboDK

## Fase 14 — Coordinate Mapping

**Estado:** Completada / Base establecida

### Objetivo

Establecer la relación entre las coordenadas obtenidas mediante visión artificial y el sistema de referencia utilizado por RoboDK.

### Resultados

* Definición de sistemas de referencia.
* Preparación de la transformación cámara → robot.
* Bases para la futura calibración espacial.

---

## Fase 15 — RoboDK Communication

**Estado:** Completada

### Objetivo

Establecer la comunicación entre Python y RoboDK.

### Resultados

* Comunicación funcional con RoboDK.
* Envío de información desde Python.
* Movimiento del robot dentro del entorno de simulación.
* Primera validación del flujo visión → software robótico.

---

# BLOQUE 7 — Detección del Operador

## Fase 16 — Human Pose Detection

**Estado:** Completada

### Objetivo

Detectar la postura humana utilizando YOLO Pose.

### Resultados

* Integración de Ultralytics YOLO.
* Uso del modelo `yolo11n-pose`.
* Detección de personas mediante cámara.
* Obtención de los 17 keypoints corporales.
* Extracción de coordenadas y confianza de cada punto.

---

## Fase 16.1 — Human Pose Data Model

**Estado:** Completada

### Objetivo

Crear una estructura independiente para representar la información corporal detectada.

### Resultados

* Clase `Landmark`.
* Clase `HumanPose`.
* Almacenamiento de coordenadas X/Y.
* Almacenamiento de confianza.
* Separación entre detección y representación de datos.

---

## Fase 16.2 — Pose Visualization

**Estado:** Completada

### Objetivo

Separar la representación visual de la lógica de detección.

### Resultados

* Creación de `pose_drawer.py`.
* Representación de hombros, codos y muñecas.
* Representación de conexiones del brazo.
* Separación entre procesamiento y visualización.

---

# BLOQUE 8 — Análisis Geométrico del Movimiento

## Fase 17 — Pose Mathematics

**Estado:** En desarrollo

### Objetivo

Crear las herramientas matemáticas necesarias para analizar el movimiento humano.

### Funciones

* Cálculo de vectores.
* Cálculo de ángulos.
* Cálculo de distancias.
* Normalización de vectores.

---

## Fase 17.1 — Arm Vector Analysis

**Estado:** Pendiente

### Objetivo

Representar matemáticamente los segmentos del brazo humano.

### Resultados esperados

* Vector hombro → codo.
* Vector codo → muñeca.
* Representación independiente de cada brazo.
* Preparación para análisis biomecánico.

---

## Fase 17.2 — Joint Angle Analysis

**Estado:** Pendiente

### Objetivo

Calcular los ángulos de las articulaciones relevantes.

### Resultados esperados

* Ángulo del codo izquierdo.
* Ángulo del codo derecho.
* Visualización en tiempo real.
* Validación de los cálculos matemáticos.

---

## Fase 17.3 — Pose Constraints

**Estado:** Pendiente

### Objetivo

Determinar qué configuraciones del brazo humano son válidas para el sistema robótico.

### Resultados esperados

* Límites angulares.
* Rangos de movimiento.
* Detección de configuraciones inválidas.
* Preparación de restricciones para el robot.

---

# BLOQUE 9 — Referencia Humana y Calibración

## Fase 18 — Operator Calibration

**Estado:** Pendiente

### Objetivo

Adaptar el sistema a las características físicas del operador.

### Resultados esperados

* Calibración inicial.
* Estimación de longitudes de segmentos.
* Determinación de referencias corporales.
* Normalización de medidas.

---

## Fase 18.1 — Relative Pose Representation

**Estado:** Pendiente

### Objetivo

Evitar depender únicamente de coordenadas de imagen absolutas.

### Resultados esperados

* Referencias relativas al cuerpo.
* Posiciones relativas de hombro, codo y muñeca.
* Independencia parcial respecto a la posición del operador en la imagen.

---

## Fase 18.2 — Human-Robot Mapping

**Estado:** Pendiente

### Objetivo

Establecer cómo se relaciona el movimiento humano con el espacio de trabajo del robot.

### Resultados esperados

* Transformación de coordenadas.
* Escalado.
* Referencias espaciales.
* Correspondencia entre movimiento humano y movimiento robótico.

---

# BLOQUE 10 — Detección de Herramienta

## Fase 19 — Tool Detection

**Estado:** Pendiente

### Objetivo

Detectar la herramienta utilizada por el operador.

### Resultados esperados

* Detección de la herramienta.
* Localización espacial.
* Seguimiento frame a frame.
* Estimación de su posición.

---

## Fase 19.1 — Tool Tracking

**Estado:** Pendiente

### Objetivo

Mantener el seguimiento estable de la herramienta durante el movimiento.

### Resultados esperados

* Trayectoria.
* Filtrado de ruido.
* Estabilidad temporal.
* Gestión de pérdidas de detección.

---

## Fase 19.2 — Tool as Primary Reference

**Estado:** Pendiente

### Objetivo

Utilizar la herramienta como referencia principal de teleoperación.

### Concepto

Cuando la herramienta esté disponible, el sistema utilizará su posición y orientación como referencia principal.

En ausencia de herramienta, las manos del operador podrán utilizarse como referencia alternativa.

---

# BLOQUE 11 — Seguridad y Validación del Movimiento

## Fase 20 — Motion Validation

**Estado:** Pendiente

### Objetivo

Determinar si una posición solicitada por el operador es válida para el robot.

### Resultados esperados

* Comprobación de límites.
* Comprobación de restricciones articulares.
* Comprobación del espacio de trabajo.
* Detección de movimientos inválidos.

---

## Fase 20.1 — Biomechanical Constraints

**Estado:** Pendiente

### Objetivo

Utilizar la información del brazo humano para limitar movimientos peligrosos o físicamente incoherentes.

### Resultados esperados

* Límites del codo.
* Límites de orientación.
* Restricciones de movimiento.
* Validación combinada herramienta + brazo.

---

## Fase 20.2 — Safety Layer

**Estado:** Pendiente

### Objetivo

Crear una capa independiente encargada de validar cualquier movimiento antes de enviarlo al robot.

### Concepto

```text
Movimiento solicitado
        ↓
Análisis biomecánico
        ↓
Restricciones del robot
        ↓
Espacio de trabajo
        ↓
¿Movimiento válido?
      ↙     ↘
    NO       SÍ
    ↓         ↓
 BLOQUEAR   EJECUTAR
```

---

# BLOQUE 12 — Teleoperación en Simulación

## Fase 21 — Basic Visual Teleoperation

**Estado:** Pendiente

### Objetivo

Conseguir que el movimiento del operador controle el robot dentro de RoboDK.

### Resultados esperados

* Movimiento en tiempo real.
* Seguimiento de herramienta.
* Uso de referencias humanas.
* Aplicación de restricciones.

---

## Fase 21.1 — Smooth Motion

**Estado:** Pendiente

### Objetivo

Reducir movimientos bruscos y ruido procedente de la visión artificial.

### Resultados esperados

* Filtrado.
* Suavizado de trayectoria.
* Control de velocidad.
* Movimiento más natural del robot.

---

## Fase 21.2 — Teleoperation Validation

**Estado:** Pendiente

### Objetivo

Validar el comportamiento completo del sistema en simulación.

### Resultados esperados

* Repetibilidad.
* Precisión.
* Estabilidad.
* Respuesta ante pérdida de detección.
* Comportamiento ante movimientos inválidos.

---

# BLOQUE 13 — Comunicación con Hardware

## Fase 22 — ESP32 Communication

**Estado:** Pendiente

### Objetivo

Establecer comunicación entre Python y ESP32.

### Resultados esperados

* Envío de comandos.
* Recepción de información.
* Protocolo de comunicación.
* Gestión de errores.

---

## Fase 23 — Real Robot Integration

**Estado:** Pendiente

### Objetivo

Trasladar el sistema validado en RoboDK al brazo robótico físico.

### Resultados esperados

* Comunicación con el robot real.
* Ejecución de movimientos.
* Validación de límites.
* Sistema de parada segura.

---

# BLOQUE 14 — Sistema Final

## Fase 24 — Integrated Teleoperation System

**Estado:** Pendiente

### Objetivo

Integrar todos los módulos desarrollados durante el proyecto.

### Sistema final

```text
                    CÁMARA
                       ↓
                 YOLO POSE
                       ↓
                 HUMAN POSE
                       ↓
              POSE MATHEMATICS
                       ↓
          ┌────────────┴────────────┐
          ↓                         ↓
   BRAZO HUMANO                 HERRAMIENTA
          ↓                         ↓
          └────────────┬────────────┘
                       ↓
              MOTION VALIDATION
                       ↓
                COORDINATE MAP
                       ↓
                 ROBOT CONTROL
                       ↓
                  RoboDK / UR
```

### Resultado final esperado

Kinema Nexus será capaz de interpretar el movimiento del operador mediante visión artificial y utilizarlo para teleoperar un brazo robótico, utilizando la herramienta como referencia principal cuando esté disponible y empleando la información biomecánica del operador para validar y restringir los movimientos del robot.

---

# Estado Actual

**Última fase completada:** Fase 16.2 — Pose Visualization

**Fase actualmente en desarrollo:** Fase 17 — Pose Mathematics

El siguiente objetivo será completar el análisis geométrico del brazo mediante vectores, ángulos y distancias antes de comenzar con la calibración y el mapeo humano-robot.

---

# Filosofía de Desarrollo

Kinema Nexus se desarrolla de forma incremental y modular.

Cada fase debe producir una funcionalidad verificable antes de continuar con la siguiente. La arquitectura del proyecto busca mantener separadas:

* Detección.
* Representación de datos.
* Matemáticas.
* Visualización.
* Calibración.
* Validación.
* Control robótico.

De esta forma, los módulos desarrollados durante las primeras fases podrán reutilizarse posteriormente tanto en la simulación como en el control del robot físico.
