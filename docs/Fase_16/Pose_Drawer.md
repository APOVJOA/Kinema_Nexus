# Pose Drawer Module (`pose_drawer.py`) - Fase 16: Estimación de Poses con YOLO

## 1. Visión General

El módulo `pose_drawer.py` es la capa de **renderizado y visualización gráfica** del pipeline en la Fase 16. Utiliza la librería **OpenCV** para proyectar visualmente las articulaciones (puntos clave) y los segmentos anatómicos (conexiones) detectados por el modelo YOLO sobre el fotograma de imagen.

A diferencia del renderizado por defecto de YOLO (que dibuja todo el esqueleto y cajas delimitadoras), este módulo implementa un **dibuja personalizado centrado exclusivamente en el tren superior (brazos y hombros)**, discriminando además los falsos positivos mediante un umbral de confianza mínimo.

---

## 2. Código Fuente

```python
import cv2


def draw_landmark(img, landmark, color):

    if landmark.confidence > 0.3:

        cv2.circle(
            img,
            (int(landmark.x), int(landmark.y)),
            6,
            color,
            -1
        )


def draw_connection(img, p1, p2, color=(255, 255, 255)):

    if p1.confidence > 0.3 and p2.confidence > 0.3:

        cv2.line(
            img,
            (int(p1.x), int(p1.y)),
            (int(p2.x), int(p2.y)),
            color,
            2
        )


def draw_pose(frame, pose):

    frame_draw = frame.copy()

    # -----------------------------
    # Hombros
    # -----------------------------

    draw_landmark(frame_draw, pose.left_shoulder, (0, 0, 255))
    draw_landmark(frame_draw, pose.right_shoulder, (0, 0, 255))

    # -----------------------------
    # Codos
    # -----------------------------

    draw_landmark(frame_draw, pose.left_elbow, (0, 255, 0))
    draw_landmark(frame_draw, pose.right_elbow, (0, 255, 0))

    # -----------------------------
    # Muñecas
    # -----------------------------

    draw_landmark(frame_draw, pose.left_wrist, (255, 0, 0))
    draw_landmark(frame_draw, pose.right_wrist, (255, 0, 0))

    # -----------------------------
    # Brazo izquierdo
    # -----------------------------

    draw_connection(
        frame_draw,
        pose.left_shoulder,
        pose.left_elbow
    )

    draw_connection(
        frame_draw,
        pose.left_elbow,
        pose.left_wrist
    )

    # -----------------------------
    # Brazo derecho
    # -----------------------------

    draw_connection(
        frame_draw,
        pose.right_shoulder,
        pose.right_elbow
    )

    draw_connection(
        frame_draw,
        pose.right_elbow,
        pose.right_wrist
    )

    cv2.imshow("KINEMA NEXUS", frame_draw)
```

---

## 3. Desglose Detallado de Funciones y Lógica Algorítmica

En este módulo se introduce la primera capa lógica de filtrado numérico y representación espacial en OpenCV. A continuación, se analiza detalladamente el comportamiento de cada función:

---

### A. `draw_landmark(img, landmark, color)`

Esta función dibuja un círculo sólido en la posición exacta del *keypoint* si cumple con las condiciones de calidad requeridas.

* **Filtrado por Umbral de Confianza (`confidence > 0.3`):**
  Evita dibujar marcas erróneas o "fantasmas". Si la confianza asignada por el detector es igual o inferior al $30\%$, la función ignora el punto.
* **Casting a Enteros (`int(landmark.x), int(landmark.y)`):**
  Las coordenadas generadas por YOLO vienen en formato de coma flotante (`float`). Como las funciones de dibujado de OpenCV operan sobre la matriz discreta de píxeles, es imprescindible castear estas coordenadas a enteros (`int`).
* **Parámetros de OpenCV (`cv2.circle`):**
  * `radio = 6`: Define un tamaño visible pero no restrictivo para el punto.
  * `thickness = -1`: Indicar un grosor negativo ordena a OpenCV rellenar completamente el círculo.

---

### B. `draw_connection(img, p1, p2, color=(255, 255, 255))`

Renderiza un segmento rectilíneo que conecta dos puntos anatómicos consecutivamente.

* **Evaluación de Confianza Doble (`p1.confidence > 0.3 and p2.confidence > 0.3`):**
  Lógica crítica: la línea que une dos articulaciones **solo se dibuja si ambos extremos son fiables**. Si uno de los dos puntos no supera el umbral ($30\%$), la línea completa se omite para evitar conexiones flotantes o distorsionadas.
* **Trazado (`cv2.line`):**
  Une las coordenadas enteras de `p1` y `p2` con un color predeterminado blanco (o el configurado) y un grosor de línea de $2$ píxeles.

---

### C. `draw_pose(frame, pose)`

Es la función principal de orquestación visual. Procesa el objeto `HumanPose` completo e imparte el esquema de color y la topología de los brazos.

#### 1. Inmutabilidad de la Imagen Original (`frame.copy()`)
```python
frame_draw = frame.copy()
```
* **¿Por qué se hace esto?** En OpenCV, pasar la imagen de entrada directamente modificaría los datos por referencia. Al realizar una copia con `.copy()`, preservamos el *frame* original intacto en memoria. Esto es crucial si más adelante en la aplicación se necesita procesar el fotograma limpio o pasarlo a otros algoritmos sin "contaminar" las matrices con trazos directos.

#### 2. Esquema de Codificación por Color (Formato BGR de OpenCV)
OpenCV utiliza nativamente la codificación de canales **BGR** (Azul, Verde, Rojo) en lugar de RGB. El código asigna estratégicamente un color distinto para cada par de articulaciones:

| Articulación | Tupla BGR | Color Resultante | Propósito Visual |
| :--- | :--- | :--- | :--- |
| **Hombros** (`left_shoulder`, `right_shoulder`) | `(0, 0, 255)` | **Rojo** | Identificar la base del torso superior. |
| **Codos** (`left_elbow`, `right_elbow`) | `(0, 255, 0)` | **Verde** | Identificar la articulación intermedia del brazo. |
| **Muñecas** (`left_wrist`, `right_wrist`) | `(255, 0, 0)` | **Azul** | Identificar los puntos extremidad / efectores finales. |
| **Conexiones** | `(255, 255, 255)` | **Blanco** | Trazado continuo del esqueleto (por defecto). |

#### 3. Topología de Conexiones Dibujadas
El algoritmo conecta explícitamente la cadena cinemática de los brazos:
* **Brazo Izquierdo:** `Hombro Izquierdo` $
ightarrow$ `Codo Izquierdo` $
ightarrow$ `Muñeca Izquierda`.
* **Brazo Derecho:** `Hombro Derecho` $
ightarrow$ `Codo Derecho` $
ightarrow$ `Muñeca Derecha`.

#### 4. Renderizado Final (`cv2.imshow`)
Llama a la interfaz gráfica de usuario (GUI) de OpenCV para desplegar en tiempo real la ventana titulada `"KINEMA NEXUS"`.

---

## 4. Diagrama del Flujo de Detección e Inferencia Visual

```
  [ Fotograma Entrada ]
            |
            v
   frame.copy() (Inmutabilidad)
            |
            +---> draw_landmark() ---> ¿confidence > 0.3? ---> Dibuja Círculo BGR
            |
            +---> draw_connection() -> ¿ambos conf > 0.3? ----> Dibuja Línea Blanca
            |
            v
   cv2.imshow("KINEMA NEXUS")