# FASE 18 — CALIBRACIÓN DEL OPERADOR Y MAPEO HUMANO-ROBOT

**Proyecto:** Kinema Nexus

**Fase:** 18

**Bloque:** Calibración y Preparación del Mapeo Robótico

**Estado:** Completada

---

# 1. Descripción general

El objetivo de la Fase 18 es introducir una fase de calibración inicial que permita obtener y almacenar las dimensiones relativas del operador antes de comenzar el procesamiento continuo del movimiento.

En las fases anteriores, Kinema Nexus era capaz de calcular las distancias entre landmarks en cada frame.

Sin embargo, algunas de estas medidas representan características físicas del operador que permanecen prácticamente constantes durante una sesión.

Por ejemplo:

* Longitud del brazo.
* Longitud del antebrazo.

Por este motivo, estas medidas no necesitan ser recalculadas continuamente.

La Fase 18 introduce una separación entre:

```text
CALIBRACIÓN INICIAL

Medidas físicas relativas del operador
              ↓
       calibration.json
```

y:

```text
PROCESAMIENTO CONTINUO

Landmarks dinámicos
       ↓
Ángulos
       ↓
Movimiento
```

Esta separación permite reducir cálculos innecesarios durante el procesamiento continuo y establece una base para el posterior mapeo del movimiento humano al robot.

---

# 2. Fase 18.1 — Calibración del operador

**Estado:** Completada

## Objetivo

Obtener las medidas necesarias del operador mediante una postura de referencia y almacenarlas para utilizarlas durante el resto de la sesión.

Las medidas se obtienen utilizando los landmarks detectados por el sistema de pose.

Actualmente se utilizan principalmente:

* Hombro.
* Codo.
* Muñeca.

A partir de estos puntos se calculan:

```text
Hombro → Codo
Codo → Muñeca
```

correspondientes a:

* Longitud del brazo.
* Longitud del antebrazo.

Las medidas se expresan inicialmente en píxeles.

---

# 3. Proceso de calibración

La calibración se realiza antes de iniciar el procesamiento principal del movimiento.

El operador adopta una postura de referencia.

Durante esta fase, Kinema Nexus obtiene varias mediciones de los segmentos corporales relevantes.

El proceso puede representarse como:

```text
Postura de referencia
        ↓
Detección de landmarks
        ↓
Cálculo de distancias
        ↓
Varias mediciones
        ↓
Cálculo de la media
        ↓
Valores de calibración
```

El uso de varias mediciones permite reducir el efecto de pequeñas variaciones producidas por la detección de landmarks.

En lugar de utilizar una única medición:

```text
Medición 1
```

se obtiene un conjunto de valores:

```text
Medición 1
Medición 2
Medición 3
...
Medición N
```

y posteriormente se calcula una media.

De esta forma, el valor almacenado representa una estimación más estable de la longitud del segmento durante la sesión.

---

# 4. Almacenamiento de la calibración

**Estado:** Completada

Una vez finalizado el proceso de calibración, los valores obtenidos se almacenan en:

```text
data/calibration.json
```

El archivo contiene las medidas obtenidas durante la sesión.

La estructura permite que otros componentes del sistema puedan acceder a estos valores sin tener que repetir el proceso de medición.

Conceptualmente:

```text
calibration.json

{
    "left_arm_length": ...,
    "right_arm_length": ...,
    "left_forearm_length": ...,
    "right_forearm_length": ...
}
```

Los valores almacenados representan las dimensiones relativas del operador obtenidas mediante la cámara.

---

# 5. Separación entre calibración y procesamiento

Uno de los principales objetivos arquitectónicos de esta fase es evitar que el programa principal tenga que recalcular continuamente parámetros que permanecen prácticamente constantes.

Antes de la calibración:

```text
FRAME
  ↓
Landmarks
  ↓
Distancias corporales
  ↓
Ángulos
  ↓
Procesamiento
```

Las distancias se calculaban continuamente.

Después de introducir la calibración:

```text
                    ┌──────────────────────┐
                    │      CALIBRACIÓN     │
                    │                      │
                    │ Landmarks            │
                    │      ↓               │
                    │ Distancias           │
                    │      ↓               │
                    │ Media                │
                    │      ↓               │
                    │ calibration.json     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ PROCESAMIENTO         │
                    │ CONTINUO              │
                    │                      │
                    │ Landmarks dinámicos  │
                    │      ↓               │
                    │ Ángulos / movimiento │
                    └──────────────────────┘
```

Esta arquitectura permite distinguir entre parámetros de configuración de la sesión y datos dinámicos del movimiento.

---

# 6. Fase 18.2 — Robot Mapping

**Estado:** Completada

## Objetivo

Crear una primera capa de relación entre las dimensiones del operador y las dimensiones del robot.

Para ello se ha creado:

```text
robot_mapping.py
```

Este módulo utiliza los valores obtenidos durante la calibración humana y los compara con las dimensiones correspondientes del robot.

Actualmente las dimensiones del robot son provisionales y se utilizan únicamente para realizar pruebas.

---

# 7. Medidas provisionales del robot

Mientras no se haya definido el robot definitivo, `robot_mapping.py` utiliza valores de prueba:

```python
ROBOT_LEFT_ARM_LENGTH = 300.0
ROBOT_RIGHT_ARM_LENGTH = 300.0

ROBOT_LEFT_FOREARM_LENGTH = 280.0
ROBOT_RIGHT_FOREARM_LENGTH = 280.0
```

Estos valores **no representan todavía las dimensiones físicas definitivas del robot**.

Su objetivo es permitir desarrollar y validar la arquitectura del sistema de mapeo antes de disponer de las dimensiones finales.

Una vez definido el robot, estos valores podrán ser sustituidos por las medidas reales.

---

# 8. Cálculo de las escalas humano-robot

El sistema calcula una relación de escala entre cada segmento corporal humano y su correspondiente segmento robótico.

La relación utilizada es:

```text
Escala = Longitud del segmento del robot
         ─────────────────────────────────
         Longitud del segmento humano
```

Por ejemplo:

```text
left_arm_scale =
ROBOT_LEFT_ARM_LENGTH /
human_left_arm_length
```

Este cálculo se realiza independientemente para:

* Brazo izquierdo.
* Brazo derecho.
* Antebrazo izquierdo.
* Antebrazo derecho.

La función utilizada para obtener la escala es:

```python
def calculate_scale(
    robot_length,
    human_length
):

    if human_length <= 0:

        raise ValueError(
            "La longitud humana debe ser mayor que cero."
        )

    return robot_length / human_length
```

La comprobación evita realizar una división utilizando una longitud humana igual o inferior a cero.

---

# 9. Creación del mapeo

El módulo `robot_mapping.py` obtiene primero los valores almacenados en:

```text
calibration.json
```

Posteriormente utiliza estas medidas para calcular las relaciones de escala.

El flujo es:

```text
calibration.json
        ↓
Medidas del operador
        ↓
Robot Mapping
        ↓
Medidas provisionales del robot
        ↓
Cálculo de escalas
        ↓
Configuración de mapeo
```

El resultado contiene actualmente:

```text
left_arm_scale
right_arm_scale
left_forearm_scale
right_forearm_scale
```

Estos valores representan la relación dimensional entre el operador calibrado y el modelo de robot utilizado durante las pruebas.

---

# 10. Arquitectura actual

La Fase 18 amplía la arquitectura introducida durante la Fase 17.

La estructura puede representarse de la siguiente manera:

```text
human_pose_detection.py
          │
          ▼
      HumanPose
          │
          ▼
     pose_math.py
          │
          ├── Vectores
          ├── Ángulos
          └── Distancias
                  │
                  ▼
          ┌───────────────┐
          │ CALIBRACIÓN   │
          │               │
          │ calibration.py│
          └───────┬───────┘
                  │
                  ▼
        calibration.json
                  │
                  ▼
         robot_mapping.py
                  │
                  ▼
        Escalas humano-robot
```

La arquitectura permite mantener separadas tres responsabilidades:

```text
Detección
    ↓
Matemáticas de la pose
    ↓
Calibración
    ↓
Mapeo
```

Cada componente puede ser desarrollado y validado de forma independiente.

---

# 11. Archivos implicados

## `calibration.py`

Gestiona el proceso de calibración inicial del operador.

Sus responsabilidades principales son:

* Obtener los landmarks necesarios.
* Calcular las distancias corporales.
* Recoger varias mediciones.
* Calcular la media.
* Almacenar los resultados de calibración.

---

## `calibration.json`

Contiene las medidas obtenidas durante la calibración.

Actualmente almacena:

```text
left_arm_length
right_arm_length
left_forearm_length
right_forearm_length
```

Estos valores se utilizan posteriormente por otros módulos del sistema.

---

## `robot_mapping.py`

Gestiona la primera relación dimensional entre el operador y el robot.

Sus responsabilidades actuales son:

* Cargar la calibración.
* Obtener las dimensiones humanas.
* Definir las dimensiones provisionales del robot.
* Calcular las relaciones de escala.
* Crear la configuración de mapeo.

---

## `pose_math.py`

Continúa proporcionando las funciones matemáticas utilizadas durante la calibración:

```text
calculate_vector()

normalize_vector()

calculate_angle()

calculate_distance()
```

La función `calculate_distance()` es especialmente relevante durante esta fase, ya que permite obtener las longitudes de los segmentos corporales a partir de los landmarks.

---

# 12. Capacidades actuales

Tras completar la Fase 18, Kinema Nexus es capaz de:

* Detectar los landmarks necesarios para la calibración.
* Medir las longitudes relativas de los brazos y antebrazos.
* Realizar múltiples mediciones.
* Calcular una media de las mediciones obtenidas.
* Almacenar las medidas del operador en `calibration.json`.
* Separar los parámetros de calibración del procesamiento continuo.
* Cargar las medidas calibradas desde otros módulos.
* Definir medidas provisionales del robot.
* Calcular factores de escala humano-robot.
* Mantener una primera capa independiente de `Robot Mapping`.

---

# 13. Limitaciones actuales

Las siguientes funcionalidades todavía no forman parte de la implementación definitiva:

* Conversión de píxeles a unidades físicas.
* Definición de las dimensiones definitivas del robot.
* Mapeo completo de coordenadas humanas a coordenadas robóticas.
* Conversión directa de posiciones humanas en posiciones articulares del robot.
* Cinemática inversa.
* Comunicación final con el robot.
* Generación del movimiento robótico definitivo.

Los valores utilizados actualmente para el robot son provisionales y únicamente permiten validar la arquitectura inicial del sistema.

---

# 14. Consideraciones de diseño

La introducción de la calibración responde a una decisión de arquitectura:

> No todo lo que puede calcularse en cada frame necesita calcularse en cada frame.

Las dimensiones corporales del operador permanecen prácticamente constantes durante una sesión.

Por tanto, resulta más adecuado obtenerlas durante una fase inicial y reutilizarlas posteriormente.

Esta decisión permite que el procesamiento continuo se concentre en los datos que realmente cambian con el movimiento.

La separación también facilita futuras modificaciones, ya que la calibración puede evolucionar independientemente del procesamiento de la pose.

---

# 15. Relación con el sistema de teleoperación

La Fase 18 representa el primer paso explícito hacia la relación entre el operador humano y el sistema robótico.

Hasta la Fase 17, el sistema disponía principalmente de:

```text
Pose humana
    ↓
Geometría
    ↓
Ángulos
    ↓
Distancias
```

Con la Fase 18 se introduce:

```text
Pose humana
    ↓
Geometría
    ↓
Calibración
    ↓
Características del operador
    ↓
Robot Mapping
    ↓
Relación humano-robot
```

Esto no constituye todavía el movimiento del robot.

El objetivo de esta fase es establecer las bases necesarias para que las dimensiones del operador puedan relacionarse posteriormente con las del sistema robótico.

---

# 16. Mejoras futuras relacionadas

Durante el desarrollo se han identificado posibles mejoras que deliberadamente quedan fuera de la implementación actual.

Entre ellas:

* Calibraciones más avanzadas.
* Conversión de coordenadas de imagen a unidades físicas.
* Modelos tridimensionales del operador.
* Uso de múltiples cámaras.
* Estimación de profundidad.
* Mapeo espacial completo.
* Adaptación automática a diferentes robots.

Estas funcionalidades se mantendrán fuera del desarrollo principal hasta completar el roadmap establecido.

---

# 17. Conclusión de la fase

La Fase 18 introduce una nueva capa arquitectónica en Kinema Nexus.

El sistema ya no necesita recalcular continuamente las dimensiones corporales del operador, sino que puede obtenerlas durante una fase inicial de calibración y almacenarlas para su utilización durante la sesión.

Además, la creación de `robot_mapping.py` establece la primera relación entre las dimensiones humanas y las dimensiones del robot mediante factores de escala.

La arquitectura resultante queda preparada para evolucionar progresivamente desde:

**Detección de pose**

↓

**Análisis matemático**

↓

**Calibración del operador**

↓

**Mapeo humano-robot**

↓

**Interpretación del movimiento robótico**

La Fase 18 establece, por tanto, la base necesaria para comenzar a trasladar las características del movimiento humano hacia el espacio del sistema robótico.

**Fase 18 — Operator Calibration & Human-Robot Mapping: COMPLETADA**
