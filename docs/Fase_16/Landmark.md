# Landmark Module (`landmark.py`) - Fase 16: Estimación de Poses con YOLO

## 1. Visión General

El módulo `landmark.py` define la estructura de datos fundamental utilizada en el sistema de visión artificial de la **Fase 16**. Su objetivo principal es abstraer y encapsular la información espacial y estadística correspondiente a una única marca anatómica (*keypoint* o *landmark*) detectada por el modelo **YOLO (You Only Look Once)** en una imagen o fotograma de video.

En el pipeline de estimación de poses humanas, este módulo actúa como la unidad atómica sobre la cual se construyen estructuras de datos de mayor nivel (como arreglos de puntos anatómicos y esqueletos completos).

---

## 2. Estructura de la Clase `Landmark`

La clase `Landmark` almacena tanto la posición geométrica bidimensional del punto clave como la métrica de fiabilidad emitida por la red neuronal.

```python
class Landmark:

    def __init__(self, x=0, y=0, confidence=0):
        self.x = x
        self.y = y
        self.confidence = confidence

    def __repr__(self):
        return f"({self.x:.1f}, {self.y:.1f}) conf={self.confidence:.2f}"
```

---

## 3. Descripción de Atributos

| Atributo | Tipo de Dato | Valor por Defecto | Descripción |
| :--- | :--- | :--- | :--- |
| `x` | `float` / `int` | `0` | Coordenada horizontal (píxel) del punto en el plano de la imagen. |
| `y` | `float` / `int` | `0` | Coordenada vertical (píxel) del punto en el plano de la imagen. |
| `confidence` | `float` | `0` | Puntuación de confianza (score) asignada por YOLO, típicamente en el rango $[0.0, 1.0]$. Indica la certidumbre de la detección. |

---

## 4. Métodos de la Clase

### `__init__(self, x=0, y=0, confidence=0)`
Constructor de la clase. Permite instanciar un landmark asignando valores iniciales a las coordenadas `x`, `y` y al nivel de confianza (`confidence`). Si no se proporcionan parámetros, inicializa el punto en el origen $(0, 0)$ con una confianza de $0$.

### `__repr__(self)`
Proporciona una representación en formato de cadena de texto (*string*) optimizada para tareas de *logging*, depuración (*debugging*) e inspección rápida en consola.

* **Formato de salida:** `(x.x, y.y) conf=0.xx`
* **Precisión:** Aplica formato de punto flotante limitado a **1 decimal** para las coordenadas de píxel y **2 decimales** para el valor de confianza.

---

## 5. Integración dentro de la Fase 16

Dentro de la arquitectura modular de la Fase 16, la clase `Landmark` interactúa en el flujo de procesamiento de la siguiente forma:

1. **Extracción (Inferencia YOLO):** El script de detección principal (`human_pose_detection.py`) procesa el fotograma y obtiene la salida cruda de YOLO.
2. **Encapsulamiento:** Cada coordenada detectada se transforma en un objeto `Landmark`.
3. **Agregación (`pose.py`):** Los objetos `Landmark` individuales se agrupan en una estructura `Pose` que representa el esqueleto completo o conjunto de articulaciones de una persona.
4. **Visualización (`post_drawer.py`):** Los dibujadores utilizan las coordenadas `x`, `y` y filtran por `confidence` para renderizar únicamente los puntos clave con alta precisión sobre la imagen original.

```
 [ YOLO Output ] ---> (Crea instancias) ---> [ Landmark(x, y, conf) ]
                                                       |
                                                       v
 [ Renderizado / Dibujado ] <--- (Agrupa) <--- [ Pose ]
```

---

## 6. Ejemplo de Uso

```python
from landmark import Landmark

# Crear un landmark detectado con alta confianza
codo_derecho = Landmark(x=324.56, y=180.12, confidence=0.945)

# Imprimir representación legible (invoca __repr__)
print(codo_derecho)
# Salida: (324.6, 180.1) conf=0.95

# Acceso directo a los atributos
if codo_derecho.confidence > 0.5:
    print(f"Punto válido en X: {codo_derecho.x}, Y: {codo_derecho.y}")