# FASE 17 — MATEMÁTICAS DE LA POSE

**Proyecto:** Kinema Nexus
**Fase:** 17
**Bloque:** Análisis de la Pose Humana
**Estado:** Completada

---

## 1. Descripción general

El objetivo de la Fase 17 es introducir las herramientas matemáticas necesarias para analizar la pose humana detectada por Kinema Nexus.

Una vez obtenidos los puntos clave del cuerpo mediante el sistema de detección de pose, el proyecto dispone de una capa matemática independiente capaz de trabajar con:

* Vectores.
* Ángulos.
* Distancias.
* Vectores normalizados.

Estas operaciones se mantienen separadas del programa principal de detección para poder reutilizarlas posteriormente en otros componentes del sistema.

---

# 2. Fase 17.1 — Análisis de vectores del brazo

**Estado:** Completada

## Objetivo

Representar matemáticamente los segmentos relevantes del brazo utilizando los landmarks detectados.

Para cada brazo se utilizan principalmente:

* Hombro.
* Codo.
* Muñeca.

A partir de estos puntos se obtienen dos vectores:

```text
Hombro → Codo
Codo → Muñeca
```

Estos vectores permiten representar matemáticamente la configuración de cada brazo.

## Implementación

El cálculo de vectores se encuentra en `pose_math.py`:

```python
def calculate_vector(origin, destination):

    dx = destination.x - origin.x
    dy = destination.y - origin.y

    return dx, dy
```

La función recibe dos landmarks y devuelve su desplazamiento relativo en las coordenadas de la imagen:

```text
(dx, dy)
```

De esta forma, el cálculo queda independiente del sistema de detección y puede reutilizarse posteriormente.

## Resultado

El brazo izquierdo y el derecho pueden representarse mediante vectores independientes.

---

# 3. Fase 17.2 — Análisis de ángulos articulares

**Estado:** Completada

## Objetivo

Calcular los ángulos de las articulaciones relevantes utilizando los vectores obtenidos a partir de la pose.

La primera articulación analizada es el codo.

Para cada brazo se calcula el ángulo entre:

```text
Hombro ← Codo → Muñeca
```

Esto permite representar numéricamente la configuración del codo.

## Método matemático

El ángulo entre dos vectores se obtiene mediante el producto escalar:

```text
A · B = |A| |B| cos(θ)
```

El cálculo realizado por el sistema consiste en:

1. Calcular el producto escalar de ambos vectores.
2. Calcular el módulo de cada vector.
3. Obtener el coseno del ángulo.
4. Convertir el resultado a grados.

La función implementada en `pose_math.py` es:

```python
def calculate_angle(vector_A, vector_B):

    producto_escalar = (
        vector_A[0] * vector_B[0] +
        vector_A[1] * vector_B[1]
    )

    modulo_vector_A = math.sqrt(
        vector_A[0]**2 +
        vector_A[1]**2
    )

    modulo_vector_B = math.sqrt(
        vector_B[0]**2 +
        vector_B[1]**2
    )

    if modulo_vector_A == 0 or modulo_vector_B == 0:
        return 0

    coseno_angulo = (
        producto_escalar /
        (modulo_vector_A * modulo_vector_B)
    )

    coseno_angulo = max(-1.0, min(1.0, coseno_angulo))

    angulo = math.degrees(math.acos(coseno_angulo))

    return angulo
```

La limitación del valor del coseno entre `-1` y `1` evita problemas provocados por pequeños errores numéricos al utilizar `acos()`.

## Visualización

Los ángulos calculados se muestran en tiempo real mediante `pose_drawer.py`.

Actualmente se muestran:

* Ángulo del codo izquierdo.
* Ángulo del codo derecho.

Los valores aparecen junto al correspondiente landmark del codo.

## Validación

Los cálculos fueron comprobados mediante movimientos reales de los brazos.

Los valores observados resultaron coherentes con la configuración física de los brazos, proporcionando una primera validación del funcionamiento matemático implementado.

---

# 4. Cálculo de distancias

**Estado:** Completada

## Objetivo

Disponer de una función reutilizable para calcular la distancia entre dos landmarks detectados.

La función implementada en `pose_math.py` es:

```python
def calculate_distance(origin, destination):

    dx = destination.x - origin.x
    dy = destination.y - origin.y

    distancia = math.sqrt(
        dx**2 +
        dy**2
    )

    return distancia
```

El resultado representa la distancia euclídea entre ambos puntos dentro de las coordenadas de la imagen.

Actualmente las distancias se expresan en **píxeles**.

## Aplicaciones actuales

El sistema puede calcular:

* Longitud del brazo.
* Longitud del antebrazo.
* Distancias de los segmentos del brazo izquierdo.
* Distancias de los segmentos del brazo derecho.

Estos valores se muestran actualmente mediante `pose_drawer.py` para facilitar la validación y depuración.

La conversión de píxeles a unidades físicas todavía no se realiza.

---

# 5. Normalización de vectores

**Estado:** Completada

## Objetivo

Disponer de una representación normalizada de un vector que mantenga su dirección independientemente de su magnitud.

La función implementada es:

```python
def normalize_vector(vector):

    modulo = math.sqrt(
        vector[0]**2 +
        vector[1]**2
    )

    if modulo == 0:
        return (0, 0)

    vector_normalizado = (
        vector[0] / modulo,
        vector[1] / modulo
    )

    return vector_normalizado
```

La función transforma el vector en un vector unitario manteniendo su dirección.

Esta funcionalidad será útil posteriormente para el cálculo de poses relativas y el análisis del movimiento.

---

# 6. Arquitectura del proyecto

La Fase 17 introduce una separación más clara entre el procesamiento matemático y la visualización.

La estructura actual puede representarse de la siguiente manera:

```text
human_pose_detection.py
        │
        ▼
    HumanPose
        │
        ├───────────────┐
        ▼               ▼
 pose_math.py      pose_drawer.py
        │               │
        │               └── Representación visual
        │
        ├── Vectores
        ├── Ángulos
        ├── Distancias
        └── Normalización
```

Esta separación permite reutilizar las funciones matemáticas sin acoplarlas directamente a la cámara, a OpenCV o al modelo YOLO.

---

# 7. Fase 17.3 — Restricciones de la pose

**Estado:** Preparada / Pendiente de implementación

## Objetivo

Preparar el sistema para poder validar en el futuro si las configuraciones detectadas son compatibles con el sistema robótico.

Para ello se ha creado el archivo:

```text
limits.py
```

En esta fase los límites son deliberadamente provisionales.

Por ejemplo:

```python
ELBOW_MIN_ANGLE = 0
ELBOW_MAX_ANGLE = 360
```

Estos valores **no representan los límites físicos definitivos** del operador ni del robot.

Actualmente funcionan como valores de referencia para dejar preparada la arquitectura del futuro sistema de restricciones.

## Motivo de los límites provisionales

Todavía no se ha definido el modelo concreto del robot ni sus limitaciones físicas.

Por ello, establecer ahora límites específicos podría introducir restricciones incorrectas que posteriormente habría que modificar.

Los límites definitivos se establecerán cuando se conozcan las características del robot y los requisitos del sistema de mapeo.

## Flujo futuro de validación

La arquitectura prevista será:

```text
Detección de pose humana
        ↓
Matemáticas de la pose
        ↓
Cálculo de ángulos / distancias
        ↓
Restricciones de la pose
        ↓
Validación
        ↓
Generación del JSON
        ↓
Comunicación con el robot
```

La capa de validación será la encargada de detectar configuraciones que se encuentren fuera de los límites permitidos antes de enviar los datos al sistema robótico.

---

# 8. Archivos implicados

## `pose_math.py`

Contiene las funciones matemáticas utilizadas para analizar la pose detectada.

Funciones actuales:

```text
calculate_vector()
normalize_vector()
calculate_angle()
calculate_distance()
```

## `pose_drawer.py`

Se encarga de representar visualmente la información obtenida de la pose.

Actualmente muestra:

* Landmarks de hombros.
* Landmarks de codos.
* Landmarks de muñecas.
* Conexiones de los brazos.
* Ángulos de los codos.
* Distancias de los segmentos del brazo.

## `limits.py`

Contiene la configuración provisional de las futuras restricciones de movimiento.

## `pose.py`

Contiene la estructura `HumanPose`, utilizada para almacenar los landmarks detectados.

## `landmark.py`

Define la estructura individual de cada landmark, incluyendo:

* Coordenada X.
* Coordenada Y.
* Confianza.

---

# 9. Capacidades actuales

Tras completar la Fase 17, Kinema Nexus es capaz de:

* Detectar landmarks de la pose humana.
* Representar segmentos del brazo mediante vectores.
* Calcular ángulos de los codos.
* Calcular distancias entre landmarks.
* Normalizar vectores.
* Mostrar los ángulos calculados en tiempo real.
* Mostrar las distancias calculadas en tiempo real.
* Separar el procesamiento matemático de la visualización.
* Mantener preparada una estructura para futuras restricciones de movimiento.

---

# 10. Limitaciones actuales

Las siguientes funcionalidades **no forman parte todavía de la implementación de esta fase**:

* Estimación de la distancia física del operador respecto a la cámara.
* Conversión de píxeles a milímetros.
* Estimación de pose en 3D.
* Reconstrucción mediante varias cámaras.
* Límites específicos del robot.
* Mapeo definitivo entre el movimiento humano y el robot.
* Generación del JSON a partir de una pose validada.

Estas funcionalidades corresponden a fases posteriores del roadmap.

---

# 11. Mejoras futuras relacionadas

Durante el desarrollo se identificaron posibles mejoras que deliberadamente quedan fuera del roadmap actual.

Entre ellas:

* Entrenamiento o ajuste personalizado del modelo YOLO.
* Mejora de la detección mediante modelos específicos.
* Uso de múltiples cámaras.
* Reconstrucción tridimensional de la pose.
* Mejora de la robustez frente a oclusiones y posiciones complejas.

Estas mejoras se mantendrán fuera del desarrollo principal hasta completar el roadmap establecido.

---

# 12. Conclusión de la fase

La Fase 17 establece la base matemática necesaria para que Kinema Nexus pueda pasar de **detectar landmarks humanos a interpretar las relaciones geométricas existentes entre ellos**.

El sistema dispone ahora de herramientas para trabajar con vectores, ángulos, distancias y normalización, además de una estructura preparada para introducir restricciones de movimiento en fases posteriores.

Con esta base completada, el proyecto puede avanzar hacia la siguiente etapa:

**Fase 18 — Operator Calibration**

**Estado de la Fase 17: COMPLETADA**
-----------------------------------------------------------------------------
# PHASE 17 — POSE MATHEMATICS

**Project:** Kinema Nexus
**Phase:** 17
**Block:** Human Pose Analysis
**Status:** Completed

---

## 1. Overview

The objective of Phase 17 was to introduce the mathematical tools required to analyse the human pose detected by Kinema Nexus.

After obtaining the relevant body landmarks through the pose detection system, the project now has a dedicated mathematical layer capable of working with:

* Vectors.
* Angles.
* Distances.
* Normalized vectors.

These calculations are kept separate from the main detection program so that the mathematical operations can be reused by other components of the system.

---

# 2. Phase 17.1 — Arm Vector Analysis

**Status:** Completed

## Objective

Represent the relevant arm segments mathematically using the detected landmarks.

The system focuses on the following landmarks:

* Shoulder.
* Elbow.
* Wrist.

For each arm, two vectors are obtained:

```text
Shoulder → Elbow
Elbow → Wrist
```

These vectors provide the basis for analysing the orientation and configuration of each arm.

## Implementation

The vector calculation is implemented in `pose_math.py` through:

```python
def calculate_vector(origin, destination):

    dx = destination.x - origin.x
    dy = destination.y - origin.y

    return dx, dy
```

The function receives two landmarks and returns their relative displacement in the image:

```text
(dx, dy)
```

This keeps the calculation independent from the rest of the pose detection system.

## Result

The left and right arms can now be represented mathematically using independent vectors.

---

# 3. Phase 17.2 — Joint Angle Analysis

**Status:** Completed

## Objective

Calculate the angles of the relevant joints using the vectors obtained from the pose.

The first joint analysed is the elbow.

For each arm, the system calculates the angle between:

```text
Shoulder ← Elbow → Wrist
```

This allows the elbow configuration to be represented numerically.

## Mathematical Method

The angle between two vectors is calculated using the dot product:

```text
A · B = |A| |B| cos(θ)
```

The implementation calculates:

1. The scalar product of both vectors.
2. The magnitude of each vector.
3. The cosine of the angle.
4. The angle in degrees.

The function implemented in `pose_math.py` is:

```python
def calculate_angle(vector_A, vector_B):

    producto_escalar = (
        vector_A[0] * vector_B[0] +
        vector_A[1] * vector_B[1]
    )

    modulo_vector_A = math.sqrt(
        vector_A[0]**2 +
        vector_A[1]**2
    )

    modulo_vector_B = math.sqrt(
        vector_B[0]**2 +
        vector_B[1]**2
    )

    if modulo_vector_A == 0 or modulo_vector_B == 0:
        return 0

    coseno_angulo = (
        producto_escalar /
        (modulo_vector_A * modulo_vector_B)
    )

    coseno_angulo = max(-1.0, min(1.0, coseno_angulo))

    angulo = math.degrees(math.acos(coseno_angulo))

    return angulo
```

The numerical limitation of the cosine value between `-1` and `1` prevents small floating-point errors from causing problems when using `acos()`.

## Visualization

The calculated angles are displayed in real time through `pose_drawer.py`.

The system currently displays:

* Left elbow angle.
* Right elbow angle.

The values are shown next to the corresponding elbow landmark.

## Validation

The calculated angles were tested through real-time movement.

The observed values were consistent with the physical configuration of the arms, providing an initial validation of the implemented mathematical calculations.

---

# 4. Distance Calculation

**Status:** Completed

## Objective

Provide a reusable method for measuring the distance between two detected landmarks.

The function implemented in `pose_math.py` is:

```python
def calculate_distance(origin, destination):

    dx = destination.x - origin.x
    dy = destination.y - origin.y

    distancia = math.sqrt(
        dx**2 +
        dy**2
    )

    return distancia
```

The result represents the Euclidean distance between the two landmarks in image coordinates.

At the current stage, distances are expressed in **pixels**.

## Current Applications

The system can calculate:

* Upper-arm length.
* Forearm length.
* Left arm segment distances.
* Right arm segment distances.

These values are currently displayed through `pose_drawer.py` for validation and debugging.

The measurements are intentionally kept in pixels at this stage.

Physical conversions such as pixels → millimetres are not implemented yet.

---

# 5. Vector Normalization

**Status:** Completed

## Objective

Provide a normalized representation of a vector independent of its magnitude.

The implemented function is:

```python
def normalize_vector(vector):

    modulo = math.sqrt(
        vector[0]**2 +
        vector[1]**2
    )

    if modulo == 0:
        return (0, 0)

    vector_normalizado = (
        vector[0] / modulo,
        vector[1] / modulo
    )

    return vector_normalizado
```

The function converts a vector into a unit vector while preserving its direction.

This functionality will be useful for future relative-pose calculations and movement analysis.

---

# 6. Project Architecture

Phase 17 introduced a clearer separation between mathematical processing and visualization.

The current structure is approximately:

```text
human_pose_detection.py
        │
        ▼
    HumanPose
        │
        ├───────────────┐
        ▼               ▼
  pose_math.py    pose_drawer.py
        │               │
        │               └── Visual representation
        │
        ├── Vectors
        ├── Angles
        ├── Distances
        └── Normalization
```

This separation allows mathematical functions to be reused without coupling them directly to the camera or YOLO inference process.

---

# 7. Phase 17.3 — Pose Constraints

**Status:** Prepared / Pending implementation

## Objective

Prepare the system for future validation of whether detected human configurations are compatible with the robotic system.

A new configuration file has been introduced:

```text
limits.py
```

At this stage, the limits are intentionally provisional.

Example:

```python
ELBOW_MIN_ANGLE = 0
ELBOW_MAX_ANGLE = 360
```

These values do **not** represent the final physical limitations of the human operator or the robot.

They currently act as placeholders so that the project architecture is prepared for the future constraint system.

## Why the limits are provisional

The final robotic platform and its physical limitations have not yet been defined.

Therefore, defining specific robotic limits at this stage would introduce assumptions that could later become incorrect.

The actual limits will be established when the robot configuration and mapping requirements are defined.

## Future validation flow

The intended future architecture is:

```text
Human Pose Detection
        ↓
Pose Mathematics
        ↓
Angle / Distance Calculation
        ↓
Pose Constraints
        ↓
Validation
        ↓
JSON Generation
        ↓
Robot Communication
```

The validation layer will eventually be responsible for detecting configurations that fall outside the allowed limits before the data is sent to the robotic system.

---

# 8. Files Involved

### `pose_math.py`

Contains the mathematical functions used to analyse the detected pose.

Current functions:

```text
calculate_vector()
normalize_vector()
calculate_angle()
calculate_distance()
```

### `pose_drawer.py`

Responsible for visualizing the relevant pose information.

Currently displays:

* Shoulder landmarks.
* Elbow landmarks.
* Wrist landmarks.
* Arm connections.
* Elbow angles.
* Arm segment distances.

### `limits.py`

Contains the provisional configuration for future movement constraints.

### `pose.py`

Contains the `HumanPose` structure used to store the detected landmarks.

### `landmark.py`

Defines the individual landmark structure containing:

* X coordinate.
* Y coordinate.
* Confidence.

---

# 9. Current Capabilities

After completing Phase 17, Kinema Nexus can:

* Detect human pose landmarks.
* Represent arm segments as vectors.
* Calculate elbow angles.
* Calculate distances between landmarks.
* Normalize vectors.
* Display calculated angles in real time.
* Display calculated distances in real time.
* Maintain mathematical processing independently from visualization.
* Prepare a future constraint system.

---

# 10. Limitations

The following features are intentionally **not implemented yet**:

* Physical distance estimation from the camera.
* Pixel-to-millimetre conversion.
* 3D pose estimation.
* Multi-camera reconstruction.
* Robot-specific movement limits.
* Final human-to-robot coordinate mapping.
* JSON generation based on validated pose data.

These features belong to later stages of the roadmap.

---

# 11. Phase Completion

Phase 17 establishes the mathematical foundation required for the next stage of Kinema Nexus.

The system has moved from simply detecting human landmarks to being able to **interpret their geometric relationships**.

The next development stage will focus on operator calibration and relative pose representation.

**Phase 17 — Pose Mathematics: COMPLETED**
