# Human Pose Detection Module (`human_pose_detection.py`) - Fase 16: Estimación de Poses con YOLO

> ⚠️ **DOCUMENTO EVOLUTIVO / EN DESARROLLO CONTINUO**
> 
> Este documento representa el **script principal y orquestador (*Pipeline Main*)** de la **Fase 16**. A diferencia de los módulos auxiliares de estructura de datos (`landmark.py` y `pose.py`), este módulo actuará como la columna vertebral del proyecto e irá **actualizándose y extendiéndose dinámicamente** en las siguientes iteraciones.
> 
> **Próxima fase planificada:** Una vez aislados los puntos anatómicos de interés (hombros, codos y muñecas) mediante `pose_drawer.py`, el siguiente paso integrará algoritmos de **cálculo trigonométrico e invariantes cinemáticas** para determinar los **ángulos de flexión/extensión articular en tiempo real**. Conforme se incorporen nuevas librerías, modelos o capas de análisis biomecánico, este documento actualizará su arquitectura, dependencias y explicaciones técnicas.

---

## 1. Visión General

El módulo `human_pose_detection.py` es el **script principal y orquestador (Pipeline Main)** de la **Fase 16**. Integra todos los componentes del sistema de visión artificial:

1. **Captura de Video:** Stream en tiempo real vía Webcam (`cv2.VideoCapture`).
2. **Inferencia con Red Neuronal:** Procesamiento de fotogramas utilizando la arquitectura de redes neuronales ultraligeras **YOLO11 Pose (`yolo11n-pose.pt`)** de Ultralytics.
3. **Mapeo Anatómico:** Extracción y desempaquetado de tensores multidimensionales de coordenadas y niveles de confianza hacia el objeto estructurado `HumanPose`.
4. **Visualización en Tiempo Real:** Invocación del renderizado personalizado definido en `pose_drawer.py`.

---

## 2. Código Fuente (Versión Actual - Fase Base)

```python
import cv2
from ultralytics import YOLO

from pose import HumanPose
from pose_drawer import draw_pose

# -----------------------------
# Cargar modelo
# -----------------------------

model = YOLO("yolo11n-pose.pt")

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # -----------------------------
    # Inferencia
    # -----------------------------

    results = model(frame)

    # -----------------------------
    # Crear objeto Pose
    # -----------------------------

    pose = HumanPose()

    keypoints = results[0].keypoints

    if keypoints is not None and len(keypoints.xy) > 0:

        puntos = keypoints.xy[0]
        conf = keypoints.conf[0]

        # Nariz
        pose.nose.x = float(puntos[0][0])
        pose.nose.y = float(puntos[0][1])
        pose.nose.confidence = float(conf[0])

        # Ojos
        pose.left_eye.x = float(puntos[1][0])
        pose.left_eye.y = float(puntos[1][1])
        pose.left_eye.confidence = float(conf[1])

        pose.right_eye.x = float(puntos[2][0])
        pose.right_eye.y = float(puntos[2][1])
        pose.right_eye.confidence = float(conf[2])

        # Orejas
        pose.left_ear.x = float(puntos[3][0])
        pose.left_ear.y = float(puntos[3][1])
        pose.left_ear.confidence = float(conf[3])

        pose.right_ear.x = float(puntos[4][0])
        pose.right_ear.y = float(puntos[4][1])
        pose.right_ear.confidence = float(conf[4])

        # Hombros
        pose.left_shoulder.x = float(puntos[5][0])
        pose.left_shoulder.y = float(puntos[5][1])
        pose.left_shoulder.confidence = float(conf[5])

        pose.right_shoulder.x = float(puntos[6][0])
        pose.right_shoulder.y = float(puntos[6][1])
        pose.right_shoulder.confidence = float(conf[6])

        # Codos
        pose.left_elbow.x = float(puntos[7][0])
        pose.left_elbow.y = float(puntos[7][1])
        pose.left_elbow.confidence = float(conf[7])

        pose.right_elbow.x = float(puntos[8][0])
        pose.right_elbow.y = float(puntos[8][1])
        pose.right_elbow.confidence = float(conf[8])

        # Muñecas
        pose.left_wrist.x = float(puntos[9][0])
        pose.left_wrist.y = float(puntos[9][1])
        pose.left_wrist.confidence = float(conf[9])

        pose.right_wrist.x = float(puntos[10][0])
        pose.right_wrist.y = float(puntos[10][1])
        pose.right_wrist.confidence = float(conf[10])

        # Caderas
        pose.left_hip.x = float(puntos[11][0])
        pose.left_hip.y = float(puntos[11][1])
        pose.left_hip.confidence = float(conf[11])

        pose.right_hip.x = float(puntos[12][0])
        pose.right_hip.y = float(puntos[12][1])
        pose.right_hip.confidence = float(conf[12])

        # Rodillas
        pose.left_knee.x = float(puntos[13][0])
        pose.left_knee.y = float(puntos[13][1])
        pose.left_knee.confidence = float(conf[13])

        pose.right_knee.x = float(puntos[14][0])
        pose.right_knee.y = float(puntos[14][1])
        pose.right_knee.confidence = float(conf[14])

        # Tobillos
        pose.left_ankle.x = float(puntos[15][0])
        pose.left_ankle.y = float(puntos[15][1])
        pose.left_ankle.confidence = float(conf[15])

        pose.right_ankle.x = float(puntos[16][0])
        pose.right_ankle.y = float(puntos[16][1])
        pose.right_ankle.confidence = float(conf[16])

        pose.print_pose()

        draw_pose(frame, pose)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 3. Desglose Detallado de Bloques Técnicos y Algoritmos

A diferencia de los scripts puramente estructurales, este script constituye el núcleo de ejecución. A continuación, se desglosa técnicamente cada fase del algoritmo de procesamiento en tiempo real:

---

### A. Inicialización del Modelo e Captura de Video

* **Carga del Modelo YOLO11 (`model = YOLO("yolo11n-pose.pt")`):**
  Se instancia la variante **Nano (`n`)** de YOLO11 optimizada para estimación de postura (*pose estimation*). Esta red neuronal liviana está diseñada para ejecutarse con altísimas tasas de FPS en dispositivos de cómputo local o Edge sin requerir GPUs masivas.
* **Stream de Video (`cv2.VideoCapture(0)`):**
  Inicializa el dispositivo de captura predeterminado (cámara web en el índice `0`).

---

### B. Bucle Principal de Inferencia y Validación de Tensores

```python
results = model(frame)
keypoints = results[0].keypoints
```

1. **Inferencia Directa:** El fotograma `frame` extraído en la iteración actual se pasa a través de la red neuronal `model(frame)`.
2. **Estructura del Objeto `Results`:** YOLO devuelve una lista de resultados por imagen. Al procesar un único stream, accedemos al primer índice `results[0]`.
3. **Validación Antifallos (`Safety Check`):**
   ```python
   if keypoints is not None and len(keypoints.xy) > 0:
   ```
   Esta condición previene que el programa colapse (*crashee*) por excepciones de puntero nulo o tensores vacíos en situaciones donde:
   * No hay ninguna persona frente a la cámara.
   * La persona está completamente ocluida o fuera del campo de visión.

---

### C. Mapeo de Índices Estándar COCO Keypoints

El modelo de estimación de pose devuelve los puntos clave siguiendo el formato estándar del dataset **COCO (Common Objects in Context)** de 17 marcas anatómicas. 

Las matrices extraídas `keypoints.xy[0]` (coordenadas bidimensionales $X, Y$) y `keypoints.conf[0]` (vector de confianzas $C$) se mapean ordenadamente a los atributos del objeto `HumanPose`:

| Índice COCO | Nombre de Keypoint | Atributo en `HumanPose` | Asignación de Datos |
| :---: | :--- | :--- | :--- |
| **0** | Nose (Nariz) | `pose.nose` | `x = float(puntos[0][0])`, `y = float(puntos[0][1])`, `conf = float(conf[0])` |
| **1** | Left Eye (Ojo Izquierdo) | `pose.left_eye` | `x = float(puntos[1][0])`, `y = float(puntos[1][1])`, `conf = float(conf[1])` |
| **2** | Right Eye (Ojo Derecho) | `pose.right_eye` | `x = float(puntos[2][0])`, `y = float(puntos[2][1])`, `conf = float(conf[2])` |
| **3** | Left Ear (Oreja Izquierda) | `pose.left_ear` | `x = float(puntos[3][0])`, `y = float(puntos[3][1])`, `conf = float(conf[3])` |
| **4** | Right Ear (Oreja Derecha) | `pose.right_ear` | `x = float(puntos[4][0])`, `y = float(puntos[4][1])`, `conf = float(conf[4])` |
| **5** | Left Shoulder (Hombro Izq.) | `pose.left_shoulder` | `x = float(puntos[5][0])`, `y = float(puntos[5][1])`, `conf = float(conf[5])` |
| **6** | Right Shoulder (Hombro Der.)| `pose.right_shoulder`| `x = float(puntos[6][0])`, `y = float(puntos[6][1])`, `conf = float(conf[6])` |
| **7** | Left Elbow (Codo Izquierdo) | `pose.left_elbow` | `x = float(puntos[7][0])`, `y = float(puntos[7][1])`, `conf = float(conf[7])` |
| **8** | Right Elbow (Codo Derecho) | `pose.right_elbow` | `x = float(puntos[8][0])`, `y = float(puntos[8][1])`, `conf = float(conf[8])` |
| **9** | Left Wrist (Muñeca Izquierda)| `pose.left_wrist` | `x = float(puntos[9][0])`, `y = float(puntos[9][1])`, `conf = float(conf[9])` |
| **10**| Right Wrist (Muñeca Derecha) | `pose.right_wrist` | `x = float(puntos[10][0])`, `y = float(puntos[10][1])`, `conf = float(conf[10])` |
| **11**| Left Hip (Cadera Izquierda) | `pose.left_hip` | `x = float(puntos[11][0])`, `y = float(puntos[11][1])`, `conf = float(conf[11])` |
| **12**| Right Hip (Cadera Derecha) | `pose.right_hip` | `x = float(puntos[12][0])`, `y = float(puntos[12][1])`, `conf = float(conf[12])` |
| **13**| Left Knee (Rodilla Izquierda)| `pose.left_knee` | `x = float(puntos[13][0])`, `y = float(puntos[13][1])`, `conf = float(conf[13])` |
| **14**| Right Knee (Rodilla Derecha)| `pose.right_knee` | `x = float(puntos[14][0])`, `y = float(puntos[14][1])`, `conf = float(conf[14])` |
| **15**| Left Ankle (Tobillo Izquierdo)| `pose.left_ankle` | `x = float(puntos[15][0])`, `y = float(puntos[15][1])`, `conf = float(conf[15])` |
| **16**| Right Ankle (Tobillo Derecho)| `pose.right_ankle` | `x = float(puntos[16][0])`, `y = float(puntos[16][1])`, `conf = float(conf[16])` |

> **Conversión de Tipos (`float(...)`):** Los valores nativos devueltos por PyTorch/Ultralytics son tensores (`torch.Tensor`). Es indispensable aislarlos mediante el casting explícito a `float` nativo de Python para garantizar la interoperabilidad con las funciones de OpenCV y evitar consumo excesivo de memoria.

---

### D. Depuración y Control de Eventos

1. **Monitoreo en Consola (`pose.print_pose()`):** Imprime continuamente los valores numéricos actualizados de las extremidades superiores en cada fotograma procesado.
2. **Visualización Gráfica (`draw_pose(frame, pose)`):** Envía el marco y la estructura de pose rellenada al módulo visualizador.
3. **Cierre Controlado del Bucle:**
   ```python
   if cv2.waitKey(1) & 0xFF == ord("q"):
       break
   ```
   Captura eventos de teclado con una latencia de $1	ext{ ms}$. Si el usuario presiona la tecla `'q'`, interrumpe el bucle `while`.

4. **Liberación de Recursos:**
   `cap.release()` destruye el objeto de captura liberando el hardware de la cámara web y `cv2.destroyAllWindows()` cierra la ventana gráfica.

---

## 4. Diagrama de Arquitectura de Ejecución

```
       [ Cámara Web (Index 0) ]
                  |
                  v  (cv2.VideoCapture)
             [ Frame ]
                  |
                  v
      [ YOLO11 Pose Inferencia ]
                  |
                  v
       ¿Detecta Keypoints > 0?
             /        \
       (Sí) /          \ (No)
           v            v
  Extracción COCO    Saltar Frame
  [0..16] Tensores
           |
           v
 Casting float() -> Objeto HumanPose
           |
           +---> pose.print_pose() (Logs Consola)
           |
           +---> draw_pose() -------> [ Ventana KINEMA NEXUS ]