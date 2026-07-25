# Pose Module (`pose.py`) - Fase 16: Estimación de Poses con YOLO

## 1. Visión General

El módulo `pose.py` define la clase `HumanPose`, encargada de modelar y agrupar la estructura anatómica completa del cuerpo humano (los 17 *keypoints* estándar del dataset COCO utilizados por YOLO Pose).

A partir de las instancias individuales de la clase `Landmark` (importada de `landmark.py`), `HumanPose` mapea cada articulación y punto facial relevante, ofreciendo además métodos auxiliares para la depuración en consola y la extracción de subconjuntos de puntos específicos (como las extremidades superiores).

---

## 2. Estructura de la Clase `HumanPose`

```python
from landmark import Landmark


class HumanPose:

    def __init__(self):
        # Rostro
        self.nose = Landmark()
        self.left_eye = Landmark()
        self.right_eye = Landmark()
        self.left_ear = Landmark()
        self.right_ear = Landmark()

        # Extremidades superiores
        self.left_shoulder = Landmark()
        self.right_shoulder = Landmark()
        self.left_elbow = Landmark()
        self.right_elbow = Landmark()
        self.left_wrist = Landmark()
        self.right_wrist = Landmark()

        # Tronco / Cadera
        self.left_hip = Landmark()
        self.right_hip = Landmark()

        # Extremidades inferiores
        self.left_knee = Landmark()
        self.right_knee = Landmark()
        self.left_ankle = Landmark()
        self.right_ankle = Landmark()
```

---

## 3. Estructura de Atributos (*Keypoints*)

La clase inicializa por defecto 17 objetos `Landmark` neutros (coordenadas $(0, 0)$ y confianza $0.0$), categorizados según la zona anatómica:

| Zona Anatómica | Atributos Representados | Tipo |
| :--- | :--- | :--- |
| **Cabeza / Rostro** | `nose`, `left_eye`, `right_eye`, `left_ear`, `right_ear` | `Landmark` |
| **Brazos / Torso Superior** | `left_shoulder`, `right_shoulder`, `left_elbow`, `right_elbow`, `left_wrist`, `right_wrist` | `Landmark` |
| **Cadera / Torso Inferior** | `left_hip`, `right_hip` | `Landmark` |
| **Piernas / Extremidades Inferiores** | `left_knee`, `right_knee`, `left_ankle`, `right_ankle` | `Landmark` |

---

## 4. Métodos de la Clase

### `print_pose(self)`
Muestra en consola las coordenadas y niveles de confianza de las articulaciones principales de los brazos (hombros, codos y muñecas). Es útil para inspecciones rápidas en vivo de las extremidades superiores durante la ejecución.

### `print_all(self)`
Itera de forma dinámica sobre todos los atributos del objeto (`self.__dict__`) e imprime cada *keypoint* alineado con su nombre. Excelente para la depuración (*debugging*) global del esqueleto completo.

### `get_arm_landmarks(self)`
Devuelve un diccionario Python que contiene únicamente las instancias de `Landmark` asociadas a los brazos y hombros:

```python
{
    "left_shoulder": self.left_shoulder,
    "right_shoulder": self.right_shoulder,
    "left_elbow": self.left_elbow,
    "right_elbow": self.right_elbow,
    "left_wrist": self.left_wrist,
    "right_wrist": self.right_wrist,
}
```
> **Nota:** Este método facilita la integración directa con filtradores o renderizadores específicos (como `post_drawer.py`) cuando solo interesa analizar o dibujar el tren superior.

---

## 5. Integración dentro de la Fase 16

1. **Recepción de Datos:** `human_pose_detection.py` asigna a cada atributo de `HumanPose` las coordenadas calculadas por la inferencia de YOLO.
2. **Filtrado / Selección:** Módulos de procesamiento o renderizado como `post_drawer.py` invocan métodos como `get_arm_landmarks()` para trabajar únicamente con los datos necesarios sin sobrecargar la visualización.

```
 [ YOLO Keypoints ] ---> [ Instancia HumanPose ]
                                 |
                                 +---> print_all() / print_pose()  (Depuración)
                                 |
                                 +---> get_arm_landmarks() -------> [ post_drawer.py ]
```

---

## 6. Ejemplo de Uso

```python
from pose import HumanPose

# Instanciar el esqueleto
pose = HumanPose()

# Asignar detecciones (por ejemplo, desde el detector YOLO)
pose.left_shoulder.x = 240.5
pose.left_shoulder.y = 150.0
pose.left_shoulder.confidence = 0.89

# Imprimir solo articulaciones clave del brazo
pose.print_pose()

# Obtener diccionario de brazos para el dibujador
arm_points = pose.get_arm_landmarks()
print(arm_points["left_shoulder"])